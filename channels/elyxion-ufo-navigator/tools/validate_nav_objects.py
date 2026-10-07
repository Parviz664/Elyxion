#!/usr/bin/env python3
import copy
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

SCHEMA_PATH = BASE / "NAV_OBJECT_SCHEMA_V0_3.json"
REGISTRY_PATH = BASE / "NAV_OBJECT_REGISTRY_V0_3.json"
REL_SCHEMA_PATH = BASE / "NAV_RELATION_SCHEMA_V0_2.json"
REL_REGISTRY_PATH = BASE / "NAV_RELATION_REGISTRY_V0_2.json"
COLLISION_PATH = BASE / "NAV_COLLISION_REGISTRY_V0_1.json"
FRESHNESS_PATH = BASE / "NAV_FRESHNESS_POLICY_V0_2.json"
RECOVERY_PATH = BASE / "NAV_GLOBAL_C0_RECOVERY_LADDER_V0_1.json"

OBJECT_FIXTURE_PATH = BASE / "tests" / "NAV_OBJECT_FALSIFICATION_CASES_V0_2.json"
REL_FIXTURE_PATH = BASE / "tests" / "NAV_RELATION_FALSIFICATION_CASES_V0_1.json"
COLLISION_FIXTURE_PATH = BASE / "tests" / "NAV_COLLISION_FALSIFICATION_CASES_V0_1.json"
FRESHNESS_FIXTURE_PATH = BASE / "tests" / "NAV_FRESHNESS_FALSIFICATION_CASES_V0_2.json"


def set_path(root, dotted_path, value):
    parts = dotted_path.split(".")
    cur = root
    for part in parts[:-1]:
        cur = cur[part]
    cur[parts[-1]] = value


def validate_objects(schema, registry, recovery):
    errors = []
    required = set(schema["required"])
    object_types = set(schema["object_types"])
    semantic_values = set(schema["semantic_status_values"])
    origins = set(schema["classification_origin_values"])
    evidence_states = set(schema["evidence_state_values"])
    readiness_values = set(schema["readiness_values"])
    baseline_dims = set(schema["baseline_authority_dimensions"])
    authority_states = set(schema["authority_state_values"])

    if registry.get("project_scope") != "ELYXION":
        errors.append("object registry project_scope must be ELYXION")
    if registry.get("schema_ref") != SCHEMA_PATH.name:
        errors.append("object registry schema_ref mismatch")

    seen = set()
    for obj in registry.get("objects", []):
        oid = obj.get("id", "<missing-id>")
        missing = required - set(obj)
        if missing:
            errors.append(f"{oid}: missing required fields {sorted(missing)}")

        if oid in seen:
            errors.append(f"duplicate object id: {oid}")
        seen.add(oid)

        if obj.get("project_scope") != "ELYXION":
            errors.append(f"{oid}: project_scope must be ELYXION")
        if obj.get("object_type") not in object_types:
            errors.append(f"{oid}: invalid object_type {obj.get('object_type')}")
        if obj.get("evidence_state") not in evidence_states:
            errors.append(f"{oid}: invalid evidence_state {obj.get('evidence_state')}")

        sem = obj.get("semantic_status", {})
        if sem.get("value") not in semantic_values:
            errors.append(f"{oid}: invalid semantic_status value {sem.get('value')}")
        if sem.get("origin") not in origins:
            errors.append(f"{oid}: invalid semantic_status origin {sem.get('origin')}")
        if not isinstance(sem.get("evidence"), list):
            errors.append(f"{oid}: semantic_status evidence must be a list")
        elif sem.get("value") != "UNKNOWN" and not sem.get("evidence"):
            errors.append(f"{oid}: non-UNKNOWN semantic_status requires evidence")

        ready = obj.get("readiness", {})
        if ready.get("value") not in readiness_values:
            errors.append(f"{oid}: invalid readiness value {ready.get('value')}")
        if ready.get("origin") not in origins:
            errors.append(f"{oid}: invalid readiness origin {ready.get('origin')}")
        if not isinstance(ready.get("evidence"), list):
            errors.append(f"{oid}: readiness evidence must be a list")
        elif ready.get("value") != "UNKNOWN" and not ready.get("evidence"):
            errors.append(f"{oid}: non-UNKNOWN readiness requires evidence")

        auth = obj.get("authority", {})
        missing_auth = baseline_dims - set(auth)
        if missing_auth:
            errors.append(f"{oid}: missing baseline authority dimensions {sorted(missing_auth)}")

        for dim in baseline_dims:
            claim = auth.get(dim, {})
            state = claim.get("state")
            evidence = claim.get("evidence")
            if state not in authority_states:
                errors.append(f"{oid}: invalid authority state {dim}={state}")
            if not isinstance(evidence, list):
                errors.append(f"{oid}: authority.{dim}.evidence must be a list")
            elif state != "UNKNOWN" and not evidence:
                errors.append(f"{oid}: authority.{dim}={state} requires evidence")
            if state == "CONSTRAINED" and not claim.get("constraint"):
                errors.append(f"{oid}: constrained authority.{dim} requires constraint")

        extra = obj.get("additional_authority_claims")
        if not isinstance(extra, list):
            errors.append(f"{oid}: additional_authority_claims must be a list")
        else:
            seen_domains = set()
            for idx, claim in enumerate(extra):
                prefix = f"{oid}: additional_authority_claims[{idx}]"
                domain = str(claim.get("domain", "")).strip()
                state = claim.get("state")
                scope = str(claim.get("scope", "")).strip()
                evidence = claim.get("evidence")

                if not domain:
                    errors.append(f"{prefix}: domain required")
                elif domain in baseline_dims:
                    errors.append(f"{prefix}: baseline authority must not be duplicated as specialized domain")
                elif domain in seen_domains:
                    errors.append(f"{prefix}: duplicate specialized authority domain {domain}")
                seen_domains.add(domain)

                if state not in authority_states:
                    errors.append(f"{prefix}: invalid state {state}")
                if not scope:
                    errors.append(f"{prefix}: scope required")
                if not isinstance(evidence, list):
                    errors.append(f"{prefix}: evidence must be a list")
                elif state != "UNKNOWN" and not evidence:
                    errors.append(f"{prefix}: evidenced claim required for state {state}")

        if sem.get("value") == "CANON":
            canon = auth.get("canon", {})
            if canon.get("state") != "EXPLICIT" or not canon.get("evidence"):
                errors.append(f"{oid}: CANON requires evidenced EXPLICIT canon authority")

        if obj.get("evidence_state") == "DIRECTLY_OBSERVED" and not obj.get("evidence"):
            errors.append(f"{oid}: directly observed object has no evidence pointers")

        if not registry.get("cross_project_contract_refs"):
            for loc in obj.get("locations", []):
                repo_name = loc.get("repository")
                if repo_name and repo_name != "Parviz664/Elyxion":
                    errors.append(f"{oid}: cross-project repository without explicit contract: {repo_name}")

    for target in registry.get("discovery_targets", []):
        if target.get("evidence_state") == "NOT_OBSERVED" and target.get("existence_elsewhere") != "UNKNOWN":
            errors.append(
                f"{target.get('id')}: NOT_OBSERVED target must keep existence_elsewhere UNKNOWN"
            )
        if "referenced_in" in target and not isinstance(target["referenced_in"], list):
            errors.append(f"{target.get('id')}: referenced_in must be a list")

    if registry.get("recovery_profile_ref") != RECOVERY_PATH.name:
        errors.append("object registry recovery_profile_ref mismatch")

    levels = recovery.get("layers", [])
    if [x.get("level") for x in levels] != list(range(6)):
        errors.append("recovery ladder levels must be exactly 0..5")

    rules = recovery.get("context_assembly_rules", {})
    if rules.get("task_scoped") is not True:
        errors.append("recovery ladder must require task-scoped context")
    if rules.get("load_unrelated_history_by_default") is not False:
        errors.append("unrelated history must not load by default")

    compression = recovery.get("compression_rules", {})
    if compression.get("summaries_are_caches_not_authority") is not True:
        errors.append("summaries must remain caches, not authority")
    if compression.get("compressed_views_must_preserve_evidence_descent") is not True:
        errors.append("compressed views must preserve evidence descent")
    if compression.get("cross_project_state_must_not_be_implicitly_imported") is not True:
        errors.append("cross-project implicit import must be forbidden")

    return errors


def validate_relations(rel_schema, rel_registry, object_registry):
    errors = []
    object_ids = {x["id"] for x in object_registry.get("objects", [])}
    discovery_ids = {x["id"] for x in object_registry.get("discovery_targets", [])}
    kinds = set(rel_schema["relation_kinds"])
    states = set(rel_schema["states"])
    origins = set(rel_schema["origins"])
    traversals = set(rel_schema["traversal_states"])
    seen = set()

    if rel_registry.get("project_scope") != "ELYXION":
        errors.append("relation registry project_scope must be ELYXION")
    if rel_registry.get("object_registry_ref") != REGISTRY_PATH.name:
        errors.append("relation registry object_registry_ref mismatch")
    if rel_registry.get("schema_ref") != REL_SCHEMA_PATH.name:
        errors.append("relation registry schema_ref mismatch")

    for rel in rel_registry.get("confirmed_relations", []):
        rid = rel.get("id", "<missing-id>")
        missing = set(rel_schema["required_confirmed"]) - set(rel)
        if missing:
            errors.append(f"{rid}: missing confirmed relation fields {sorted(missing)}")
        if rid in seen:
            errors.append(f"duplicate relation id: {rid}")
        seen.add(rid)

        if rel.get("project_scope") != "ELYXION":
            errors.append(f"{rid}: project_scope must be ELYXION")
        if rel.get("source_id") not in object_ids:
            errors.append(f"{rid}: unknown source object {rel.get('source_id')}")
        if rel.get("target_id") not in object_ids:
            errors.append(f"{rid}: unknown target object {rel.get('target_id')}")
        if rel.get("kind") not in kinds:
            errors.append(f"{rid}: invalid kind {rel.get('kind')}")
        if rel.get("state") not in states or rel.get("state") != "CONFIRMED":
            errors.append(f"{rid}: confirmed collection must contain CONFIRMED relations")
        if rel.get("origin") not in origins:
            errors.append(f"{rid}: invalid origin {rel.get('origin')}")
        if rel.get("traversal") not in traversals or rel.get("traversal") != "ALLOWED_AS_FACT":
            errors.append(f"{rid}: confirmed relation must be ALLOWED_AS_FACT")
        if not rel.get("evidence"):
            errors.append(f"{rid}: confirmed relation requires evidence")

    for rel in rel_registry.get("unresolved_relations", []):
        rid = rel.get("id", "<missing-id>")
        missing = set(rel_schema["required_unresolved"]) - set(rel)
        if missing:
            errors.append(f"{rid}: missing unresolved relation fields {sorted(missing)}")
        if rid in seen:
            errors.append(f"duplicate relation id: {rid}")
        seen.add(rid)

        if rel.get("project_scope") != "ELYXION":
            errors.append(f"{rid}: project_scope must be ELYXION")
        if rel.get("source_id") not in object_ids:
            errors.append(f"{rid}: unknown source object {rel.get('source_id')}")
        if "target_id" in rel and rel.get("target_id") not in object_ids:
            errors.append(f"{rid}: unknown target object {rel.get('target_id')}")
        if "target_discovery_id" in rel and rel.get("target_discovery_id") not in discovery_ids:
            errors.append(f"{rid}: unknown discovery target {rel.get('target_discovery_id')}")
        if "target_id" not in rel and "target_discovery_id" not in rel:
            errors.append(f"{rid}: unresolved relation requires target_id or target_discovery_id")
        if rel.get("state") != "UNRESOLVED":
            errors.append(f"{rid}: unresolved collection must remain UNRESOLVED")
        if rel.get("origin") not in origins:
            errors.append(f"{rid}: invalid origin {rel.get('origin')}")
        if rel.get("traversal") != "BLOCKED_UNRESOLVED":
            errors.append(f"{rid}: unresolved relation must be BLOCKED_UNRESOLVED")
        if not str(rel.get("question", "")).strip():
            errors.append(f"{rid}: unresolved relation requires explicit question")
        if not rel.get("evidence"):
            errors.append(f"{rid}: unresolved relation requires evidence for why the question exists")

    return errors


def validate_collisions(collision_registry, object_registry):
    errors = []
    object_ids = {x["id"] for x in object_registry.get("objects", [])}
    seen = set()

    if collision_registry.get("project_scope") != "ELYXION":
        errors.append("collision registry project_scope must be ELYXION")

    for collision in collision_registry.get("collisions", []):
        cid = collision.get("id", "<missing-id>")
        if cid in seen:
            errors.append(f"duplicate collision id: {cid}")
        seen.add(cid)

        ids = collision.get("object_ids")
        if not isinstance(ids, list) or len(ids) < 2:
            errors.append(f"{cid}: collision requires at least two object_ids")
        else:
            for oid in ids:
                if oid not in object_ids:
                    errors.append(f"{cid}: unknown collision object {oid}")

        if not str(collision.get("state", "")).strip():
            errors.append(f"{cid}: state required")
        if not str(collision.get("classification", "")).strip():
            errors.append(f"{cid}: classification required")
        if not collision.get("evidence"):
            errors.append(f"{cid}: evidence required")
        if collision.get("auto_resolution_forbidden") is not True:
            errors.append(f"{cid}: auto_resolution_forbidden must be true")
        if not str(collision.get("effect", "")).strip():
            errors.append(f"{cid}: effect required")

    return errors


def validate_freshness(policy, object_registry, relation_registry, collision_registry):
    errors = []
    sources = policy.get("sources", [])
    source_ids = [x.get("id") for x in sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("freshness source ids must be unique")
    source_set = set(source_ids)

    object_ids = {x["id"] for x in object_registry.get("objects", [])}
    rel_ids = {x["id"] for x in relation_registry.get("confirmed_relations", [])}
    unresolved_ids = {x["id"] for x in relation_registry.get("unresolved_relations", [])}
    collision_ids = {x["id"] for x in collision_registry.get("collisions", [])}

    for src in sources:
        mode = src.get("tracking_mode")
        if mode == "PINNED_OBSERVED_HEAD" and not src.get("observed_head"):
            errors.append(f"{src.get('id')}: pinned source requires observed_head")
        if mode == "SELF_CURRENT_HEAD" and src.get("observed_head") is not None:
            errors.append(f"{src.get('id')}: self-current source must not pin observed_head")
        if mode not in {"PINNED_OBSERVED_HEAD", "SELF_CURRENT_HEAD"}:
            errors.append(f"{src.get('id')}: invalid tracking_mode {mode}")

    tracked = {"OBJECT": set(), "RELATION": set(), "UNRESOLVED_RELATION": set(), "COLLISION": set()}

    for dep in policy.get("dependencies", []):
        kind = dep.get("subject_kind")
        sid = dep.get("subject_id")
        srcs = dep.get("source_ids")

        if kind not in tracked:
            errors.append(f"freshness dependency {sid}: invalid subject_kind {kind}")
            continue
        tracked[kind].add(sid)

        if not isinstance(srcs, list) or not srcs:
            errors.append(f"freshness dependency {sid}: source_ids required")
        else:
            for source_id in srcs:
                if source_id not in source_set:
                    errors.append(f"freshness dependency {sid}: unknown source {source_id}")

        valid_ids = {
            "OBJECT": object_ids,
            "RELATION": rel_ids,
            "UNRESOLVED_RELATION": unresolved_ids,
            "COLLISION": collision_ids,
        }[kind]
        if sid not in valid_ids:
            errors.append(f"freshness dependency: unknown {kind} subject {sid}")

    missing = {
        "OBJECT": object_ids - tracked["OBJECT"],
        "RELATION": rel_ids - tracked["RELATION"],
        "UNRESOLVED_RELATION": unresolved_ids - tracked["UNRESOLVED_RELATION"],
        "COLLISION": collision_ids - tracked["COLLISION"],
    }
    for kind, ids in missing.items():
        if ids:
            errors.append(f"freshness policy missing {kind} dependencies for {sorted(ids)}")

    return errors


def apply_object_fixture(registry, fixture):
    mutated = copy.deepcopy(registry)
    mutation = fixture["mutation"]
    if "target_object" in mutation:
        target = next(x for x in mutated["objects"] if x["id"] == mutation["target_object"])
    else:
        target = next(x for x in mutated["discovery_targets"] if x["id"] == mutation["target_discovery"])
    set_path(target, mutation["path"], mutation["value"])
    return mutated


def apply_relation_fixture(registry, fixture):
    mutated = copy.deepcopy(registry)
    target = next(
        x for x in mutated[fixture["target_collection"]]
        if x["id"] == fixture["target_id"]
    )
    set_path(target, fixture["mutation"]["path"], fixture["mutation"]["value"])
    return mutated


def apply_collision_fixture(registry, fixture):
    mutated = copy.deepcopy(registry)
    target = next(x for x in mutated["collisions"] if x["id"] == fixture["target_id"])
    set_path(target, fixture["mutation"]["path"], fixture["mutation"]["value"])
    return mutated


def simulate_stale_subjects(policy, changed_sources):
    changed = set(changed_sources)
    stale = set()
    for dep in policy.get("dependencies", []):
        if changed.intersection(dep.get("source_ids", [])):
            stale.add(dep["subject_id"])
    return stale


def main():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    rel_schema = json.loads(REL_SCHEMA_PATH.read_text(encoding="utf-8"))
    rel_registry = json.loads(REL_REGISTRY_PATH.read_text(encoding="utf-8"))
    collision_registry = json.loads(COLLISION_PATH.read_text(encoding="utf-8"))
    freshness = json.loads(FRESHNESS_PATH.read_text(encoding="utf-8"))
    recovery = json.loads(RECOVERY_PATH.read_text(encoding="utf-8"))

    object_fixtures = json.loads(OBJECT_FIXTURE_PATH.read_text(encoding="utf-8"))
    relation_fixtures = json.loads(REL_FIXTURE_PATH.read_text(encoding="utf-8"))
    collision_fixtures = json.loads(COLLISION_FIXTURE_PATH.read_text(encoding="utf-8"))
    freshness_fixtures = json.loads(FRESHNESS_FIXTURE_PATH.read_text(encoding="utf-8"))

    errors = []
    errors += validate_objects(schema, registry, recovery)
    errors += validate_relations(rel_schema, rel_registry, registry)
    errors += validate_collisions(collision_registry, registry)
    errors += validate_freshness(freshness, registry, rel_registry, collision_registry)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    failures = []

    for case in object_fixtures.get("cases", []):
        mutated = apply_object_fixture(registry, case)
        case_errors = validate_objects(schema, mutated, recovery)
        if case.get("expected") == "FAIL" and not case_errors:
            failures.append(f"{case['id']}: invalid object mutation was not rejected")

    for case in relation_fixtures.get("cases", []):
        mutated = apply_relation_fixture(rel_registry, case)
        case_errors = validate_relations(rel_schema, mutated, registry)
        if case.get("expected") == "FAIL" and not case_errors:
            failures.append(f"{case['id']}: invalid relation mutation was not rejected")

    for case in collision_fixtures.get("cases", []):
        mutated = apply_collision_fixture(collision_registry, case)
        case_errors = validate_collisions(mutated, registry)
        if case.get("expected") == "FAIL" and not case_errors:
            failures.append(f"{case['id']}: invalid collision mutation was not rejected")

    for case in freshness_fixtures.get("cases", []):
        stale = simulate_stale_subjects(freshness, case.get("changed_sources", []))
        for expected in case.get("expected_stale_subjects", []):
            if expected not in stale:
                failures.append(f"{case['id']}: expected stale subject not invalidated: {expected}")
        for forbidden in case.get("forbidden_stale_subjects", []):
            if forbidden in stale:
                failures.append(f"{case['id']}: unrelated subject incorrectly invalidated: {forbidden}")
        if "expected_global_recovery_required" in case:
            global_required = False
            if global_required != case["expected_global_recovery_required"]:
                failures.append(f"{case['id']}: unexpected global recovery result")

    if failures:
        for error in failures:
            print(f"FAIL: {error}")
        return 1

    total_falsification = (
        len(object_fixtures.get("cases", []))
        + len(relation_fixtures.get("cases", []))
        + len(collision_fixtures.get("cases", []))
        + len(freshness_fixtures.get("cases", []))
    )

    print(
        f"PASS: {len(registry.get('objects', []))} objects; "
        f"{len(rel_registry.get('confirmed_relations', []))} confirmed relations; "
        f"{len(rel_registry.get('unresolved_relations', []))} unresolved relations; "
        f"{len(collision_registry.get('collisions', []))} open collisions; "
        f"{len(freshness.get('dependencies', []))} freshness dependencies; "
        f"{total_falsification} falsification cases passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
