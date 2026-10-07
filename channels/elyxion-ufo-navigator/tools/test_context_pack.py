#!/usr/bin/env python3
import json
from pathlib import Path
from build_context_pack import build_pack

BASE = Path(__file__).resolve().parents[1]
FIXTURES = BASE / "tests" / "NAV_CONTEXT_PACK_EXPECTATIONS_V0_1.json"

def ids(items):
    return {x["id"] for x in items}

def evidence_ids(items):
    return {x["evidence_id"] for x in items}

def main():
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    failures = []

    for case in fixtures.get("cases", []):
        pack = build_pack(
            case["start_id"],
            max_hops=case["max_hops"],
            direction=case["direction"],
            include_unresolved_boundary=True,
        )

        got_objects = ids(pack["slice"]["objects"])
        got_discovery = ids(pack["discovery_boundary"])
        got_evidence = evidence_ids(pack["evidence_manifest"])

        if got_objects != set(case["expected_object_ids"]):
            failures.append(f"{case['id']}: object set mismatch {sorted(got_objects)}")
        for forbidden in case.get("forbidden_object_ids", []):
            if forbidden in got_objects:
                failures.append(f"{case['id']}: leaked unrelated object {forbidden}")
        if got_discovery != set(case["expected_discovery_ids"]):
            failures.append(f"{case['id']}: discovery set mismatch {sorted(got_discovery)}")
        if got_evidence != set(case["expected_evidence_ids"]):
            failures.append(f"{case['id']}: evidence set mismatch {sorted(got_evidence)}")
        if len(pack["materialization_plan"]["default_loaded_file_bodies"]) != case["expected_default_loaded_file_bodies"]:
            failures.append(f"{case['id']}: file bodies loaded by default")
        if len(got_evidence) != len(pack["evidence_manifest"]):
            failures.append(f"{case['id']}: evidence manifest contains duplicates")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"PASS: {len(fixtures.get('cases', []))} bounded context-pack cases.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
