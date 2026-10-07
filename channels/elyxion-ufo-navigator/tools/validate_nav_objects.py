#!/usr/bin/env python3
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SCHEMA_PATH = BASE / "NAV_OBJECT_SCHEMA_V0_1.json"
REGISTRY_PATH = BASE / "NAV_OBJECT_REGISTRY_V0_1.json"
RECOVERY_PATH = BASE / "NAV_GLOBAL_C0_RECOVERY_LADDER_V0_1.json"

def fail(msg):
    print(f"FAIL: {msg}")
    return False

def main():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    recovery = json.loads(RECOVERY_PATH.read_text(encoding="utf-8"))

    ok = True
    required = set(schema["required"])
    semantic = set(schema["semantic_status_values"])
    evidence_states = set(schema["evidence_state_values"])
    readiness = set(schema["readiness_values"])
    authority_dims = set(schema["authority_dimensions"])

    seen = set()
    for obj in registry.get("objects", []):
        oid = obj.get("id", "<missing-id>")
        missing = required - set(obj)
        if missing:
            ok = fail(f"{oid}: missing required fields {sorted(missing)}") and ok

        if oid in seen:
            ok = fail(f"duplicate object id: {oid}") and ok
        seen.add(oid)

        if obj.get("semantic_status") not in semantic:
            ok = fail(f"{oid}: invalid semantic_status {obj.get('semantic_status')}") and ok

        if obj.get("evidence_state") not in evidence_states:
            ok = fail(f"{oid}: invalid evidence_state {obj.get('evidence_state')}") and ok

        if obj.get("readiness") not in readiness:
            ok = fail(f"{oid}: invalid readiness {obj.get('readiness')}") and ok

        auth = obj.get("authority", {})
        missing_auth = authority_dims - set(auth)
        if missing_auth:
            ok = fail(f"{oid}: missing authority dimensions {sorted(missing_auth)}") and ok

        if obj.get("semantic_status") == "CANON":
            canon_auth = auth.get("canon")
            if canon_auth in (None, "NONE", "UNKNOWN"):
                ok = fail(f"{oid}: CANON without explicit canon authority") and ok

        if obj.get("evidence_state") == "DIRECTLY_OBSERVED" and not obj.get("evidence"):
            ok = fail(f"{oid}: directly observed object has no evidence pointers") and ok

        if obj.get("object_type") == "IMPLEMENTATION_SURFACE" and auth.get("implementation") == "EXPLICIT":
            explicit_support = any(
                "authority" in str(x).lower()
                for x in obj.get("evidence", [])
            )
            if not explicit_support:
                ok = fail(
                    f"{oid}: implementation presence cannot self-prove explicit implementation authority"
                ) and ok

    for target in registry.get("discovery_targets", []):
        if target.get("evidence_state") == "NOT_OBSERVED" and target.get("existence_elsewhere") != "UNKNOWN":
            ok = fail(
                f"{target.get('id')}: NOT_OBSERVED target must keep existence_elsewhere UNKNOWN"
            ) and ok

    if registry.get("recovery_profile_ref") != RECOVERY_PATH.name:
        ok = fail("registry recovery_profile_ref does not match recovery ladder file") and ok

    levels = recovery.get("layers", [])
    level_ids = [x.get("level") for x in levels]
    if level_ids != list(range(6)):
        ok = fail(f"recovery ladder levels must be exactly 0..5, got {level_ids}") and ok

    if not recovery.get("context_assembly_rules", {}).get("task_scoped"):
        ok = fail("recovery ladder must require task-scoped context") and ok

    if recovery.get("context_assembly_rules", {}).get("load_unrelated_history_by_default") is not False:
        ok = fail("unrelated history must not load by default") and ok

    compression = recovery.get("compression_rules", {})
    if not compression.get("summaries_are_caches_not_authority"):
        ok = fail("summaries must remain caches, not authority") and ok
    if not compression.get("compressed_views_must_preserve_evidence_descent"):
        ok = fail("compressed views must preserve evidence descent") and ok
    if not compression.get("cross_project_state_must_not_be_implicitly_imported"):
        ok = fail("cross-project implicit import must be forbidden") and ok

    prohibited = set(recovery.get("prohibited_patterns", []))
    required_prohibited = {
        "FULL_HISTORY_REPLAY_BY_DEFAULT",
        "SUMMARY_AS_CANON_AUTHORITY",
        "SILENT_CROSS_PROJECT_IMPORT",
        "UNKNOWN_AUTOFILL",
    }
    missing_prohibited = required_prohibited - prohibited
    if missing_prohibited:
        ok = fail(f"missing prohibited recovery patterns {sorted(missing_prohibited)}") and ok

    if not ok:
        return 1

    print(
        f"PASS: {len(registry.get('objects', []))} objects validated; "
        f"{len(registry.get('discovery_targets', []))} unresolved discovery targets preserved; "
        f"{len(levels)} recovery levels validated."
    )
    return 0

if __name__ == "__main__":
    sys.exit(main())
