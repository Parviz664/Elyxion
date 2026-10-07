#!/usr/bin/env python3
import json
from pathlib import Path
from build_context_slice import build_slice, load_documents

BASE = Path(__file__).resolve().parents[1]
FIXTURES = BASE / "tests" / "NAV_CONTEXT_SLICE_EXPECTATIONS_V0_1.json"

def ids(items):
    return {x["id"] for x in items}

def main():
    objects_doc, relations_doc, collisions_doc = load_documents()
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    failures = []

    for case in fixtures.get("cases", []):
        result = build_slice(
            objects_doc,
            relations_doc,
            collisions_doc,
            start_id=case["start_id"],
            max_hops=case["max_hops"],
            direction=case["direction"],
            include_unresolved_boundary=case["include_unresolved_boundary"],
        )

        got_objects = ids(result["objects"])
        got_relations = ids(result["confirmed_relations"])
        got_unresolved = ids(result["unresolved_boundary"])
        got_collisions = ids(result["collisions"])

        for expected in case.get("expected_object_ids", []):
            if expected not in got_objects:
                failures.append(f"{case['id']}: missing object {expected}")
        for forbidden in case.get("forbidden_object_ids", []):
            if forbidden in got_objects:
                failures.append(f"{case['id']}: unrelated object leaked into slice {forbidden}")

        if got_relations != set(case.get("expected_confirmed_relation_ids", [])):
            failures.append(
                f"{case['id']}: confirmed relations mismatch: {sorted(got_relations)}"
            )
        if got_unresolved != set(case.get("expected_unresolved_relation_ids", [])):
            failures.append(
                f"{case['id']}: unresolved boundary mismatch: {sorted(got_unresolved)}"
            )
        if got_collisions != set(case.get("expected_collision_ids", [])):
            failures.append(
                f"{case['id']}: collision set mismatch: {sorted(got_collisions)}"
            )

        if not result["laws"]["unresolved_relations_not_traversed"]:
            failures.append(f"{case['id']}: unresolved traversal guard missing")
        if not result["laws"]["open_collisions_preserved"]:
            failures.append(f"{case['id']}: collision preservation guard missing")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"PASS: {len(fixtures.get('cases', []))} bounded context-slice cases.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
