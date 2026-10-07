#!/usr/bin/env python3
import argparse
import json
from collections import deque
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OBJECTS = BASE / "NAV_OBJECT_REGISTRY_V0_2.json"
RELATIONS = BASE / "NAV_RELATION_REGISTRY_V0_1.json"

def main():
    parser = argparse.ArgumentParser(
        description="Build a bounded Elyxion Navigator context slice from confirmed relations."
    )
    parser.add_argument("start_id")
    parser.add_argument("--max-hops", type=int, default=1)
    parser.add_argument(
        "--include-unresolved-boundary",
        action="store_true",
        help="Include unresolved relation questions touching selected objects, never as traversable facts.",
    )
    args = parser.parse_args()

    objects_doc = json.loads(OBJECTS.read_text(encoding="utf-8"))
    relations_doc = json.loads(RELATIONS.read_text(encoding="utf-8"))
    objects = {x["id"]: x for x in objects_doc.get("objects", [])}

    if args.start_id not in objects:
        raise SystemExit(f"unknown start object: {args.start_id}")
    if args.max_hops < 0:
        raise SystemExit("--max-hops must be >= 0")

    outgoing = {}
    for rel in relations_doc.get("confirmed_relations", []):
        if rel.get("state") != "CONFIRMED" or rel.get("traversal") != "ALLOWED_AS_FACT":
            continue
        outgoing.setdefault(rel["source_id"], []).append(rel)

    selected = {args.start_id}
    selected_relations = []
    seen_rel_ids = set()
    q = deque([(args.start_id, 0)])

    while q:
        node, depth = q.popleft()
        if depth >= args.max_hops:
            continue
        for rel in outgoing.get(node, []):
            if rel["id"] not in seen_rel_ids:
                selected_relations.append(rel)
                seen_rel_ids.add(rel["id"])
            target = rel["target_id"]
            if target not in selected:
                selected.add(target)
                q.append((target, depth + 1))

    unresolved = []
    if args.include_unresolved_boundary:
        for rel in relations_doc.get("unresolved_relations", []):
            if rel.get("traversal") != "BLOCKED_UNRESOLVED":
                continue
            if rel.get("source_id") in selected or rel.get("target_id") in selected:
                unresolved.append(rel)

    result = {
        "slice_version": "0.1",
        "project_scope": "ELYXION",
        "start_id": args.start_id,
        "max_hops": args.max_hops,
        "objects": [objects[x] for x in sorted(selected)],
        "confirmed_relations": selected_relations,
        "unresolved_boundary": unresolved,
        "laws": {
            "unresolved_relations_not_traversed": True,
            "slice_is_not_global_completeness_claim": True,
            "evidence_descent_preserved": True,
        },
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
