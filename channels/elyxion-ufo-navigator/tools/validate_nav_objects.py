#!/usr/bin/env python3
import copy
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SCHEMA_PATH = BASE / "NAV_OBJECT_SCHEMA_V0_2.json"
REGISTRY_PATH = BASE / "NAV_OBJECT_REGISTRY_V0_2.json"
RECOVERY_PATH = BASE / "NAV_GLOBAL_C0_RECOVERY_LADDER_V0_1.json"
FIXTURE_PATH = BASE / "tests" / "NAV_OBJECT_FALSIFICATION_CASES_V0_1.json"

def validate(schema, registry, recovery):
    errors = []
    required = set(schema["required"])
    object_types = set(schema["object_types"])
    semantic_values = set(schema["semantic_status_values"])
    origins = set(schema["classification_origin_values"])
    evidence_states = set(schema["evidence_state_values"])
    readiness_values = set(schema["readiness_values"])
    authority_dims = set(schema["authority_dimensions"])
    authority_states = set(schema["authority_state_values"])

    if registry.get("project_scope") != "ELYXION":
        errors.append("registry project_scope must be ELYXION")

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
        missing_auth = authority_dims - set(auth)
        if missing_auth:
            errors.append(f"{oid}: missing authority dimensions {sorted(missing_auth)}")

        for dim in authority_dims:
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

        if sem.get("value") == "CANON":
            canon = auth.get("canon", {})
            if canon.get("state") != "EXPLICIT" or not canon.get("evidence"):
                errors.append(f"{oid}: CANON requires evidenced EXPLICIT canon authority")

        if obj.get("evidence_state") == "DIRECTLY_OBSERVED" and not obj.get("evidence"):
            errors.append(f"{oid}: directly observed object has no evidence pointers")

        if not registry.get("cross_project_contract_refs"):
            for loc in obj.get("locations", []):
                repo = loc.get("repository")
                if repo and repo != "Parviz664/Elyxion":
                    errors.append(f"{oid}: cross-project repository without explicit contract: {repo}")

    for target in registry.get("discovery_targets", []):
        if target.get("evidence_state") == "NOT_OBSERVED" and target.get("existence_elsewhere") != "UNKNOWN":
            errors.append(
                f"{target.get('id')}: NOT_OBSERVED target must keep existence_elsewhere UNKNOWN"
            )

    if registry.get("recovery_profile_ref") != RECOVERY_PATH.name:
        errors.append("registry recovery_profile_ref does not match recovery ladder file")

    levels = recovery.get("layers", [])
    level_ids = [x.get("level") for x in levels]
    if level_ids != list(range(6)):
        errors.append(f"recovery ladder levels must be exactly 0..5, got {level_ids}")

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

    prohibited = set(recovery.get("prohibited_patterns", []))
    required_prohibited = {
        "FULL_HISTORY_REPLAY_BY_DEFAULT",
        "SUMMARY_AS_CANON_AUTHORITY",
        "SILENT_CROSS_PROJECT_IMPORT",
        "UNKNOWN_AUTOFILL",
    }
    missing_prohibited = required_prohibited - prohibited
    if missing_prohibited:
        errors.append(f"missing prohibited recovery patterns {sorted(missing_prohibited)}")

    return errors

def set_path(root, dotted_path, value):
    parts = dotted_path.split(".")
    cur = root
    for part in parts[:-1]:
        cur = cur[part]
    cur[parts[-1]] = value

def apply_fixture(registry, fixture):
    mutated = copy.deepcopy(registry)
    mutation = fixture["mutation"]
    if "target_object" in mutation:
        target = next(x for x in mutated["objects"] if x["id"] == mutation["target_object"])
    else:
        target = next(
            x for x in mutated["discovery_targets"]
            if x["id"] == mutation["target_discovery"]
        )
    set_path(target, mutation["path"], mutation["value"])
    return mutated

def main():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    recovery = json.loads(RECOVERY_PATH.read_text(encoding="utf-8"))
    fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    errors = validate(schema, registry, recovery)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    falsification_failures = []
    for case in fixtures.get("cases", []):
        mutated = apply_fixture(registry, case)
        case_errors = validate(schema, mutated, recovery)
        if case.get("expected") == "FAIL" and not case_errors:
            falsification_failures.append(
                f"{case['id']}: invalid mutation was not rejected"
            )

    if falsification_failures:
        for error in falsification_failures:
            print(f"FAIL: {error}")
        return 1

    print(
        f"PASS: {len(registry.get('objects', []))} objects validated; "
        f"{len(registry.get('discovery_targets', []))} unresolved discovery targets preserved; "
        f"{len(recovery.get('layers', []))} recovery levels validated; "
        f"{len(fixtures.get('cases', []))} falsification cases rejected."
    )
    return 0

if __name__ == "__main__":
    sys.exit(main())
