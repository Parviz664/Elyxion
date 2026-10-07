#!/usr/bin/env python3
import argparse
import json
from collections import deque
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OBJECTS = BASE / "NAV_OBJECT_REGISTRY_V0_3.json"
RELATIONS = BASE / "NAV_RELATION_REGISTRY_V0_2.json"
COLLISIONS = BASE / "NAV_COLLISION_REGISTRY_V0_1.json"

def main():
    parser = argparse.ArgumentParser(
        description="Build a bounded Elyxion Navigator context slice from confirmed relations."
    )
    parser.add_argument("start_id")
    parser.add_argument("--max-hops", type=int, default=1)
    parser.add_argument(
        "--direction",
        choices=["outgoing", "incoming", "both"],
        default="both",
        help="Select neighbors without changing the semantic direction stored in relation records.",
    )
    parser.add_argument(
        "--include-unresolved-boundary",
        action="store_true",
        help="Include unresolved relation questions touching selected objects; never traverse them.",
    )
    args = parser.parse_args()

    objects_doc = json.loads(OBJECTS.read_text(encoding="utf-8"))
    relations_doc = json.loads(RELATIONS.read_text(encoding="utf-8"))
    collisions_doc = json.loads(COLLISIONS.read_text(encoding="utf-8"))

    objects = {x["id"]: x for x in objects_doc.get("objects", [])}
    if args.start_id not in objects:
        raise SystemExit(f"unknown start object: {args.start_id}")
    if args.max_hops < 0:
        raise SystemExit("--max-hops must be >= 0")

    confirmed = [
        r for r in relations_doc.get("confirmed_relations", [])
        if r.get("state") == "CONFIRMED" and r.get("traversal") == "ALLOWED_AS_FACT"
    ]

    selected = {args.start_id}
    selected_relations = []
    seen_rel_ids = set()
    q = deque([(args.start_id, 0)])

    while q:
        node, depth = q.popleft()
        if depth >= args.max_hops:
            continue

        for rel in confirmed:
            neighbors = []
            if args.direction in ("outgoing", "both") and rel["source_id"] == node:
                neighbors.append(rel["target_id"])
            if args.direction in ("incoming", "both") and rel["target_id"] == node:
                neighbors.append(rel["source_id"])

            if not neighbors:
                continue

            if rel["id"] not in seen_rel_ids:
                selected_relations.append(rel)
                seen_rel_ids.add(rel["id"])

            for neighbor in neighbors:
                if neighbor not in selected:
                    selected.add(neighbor)
                    q.append((neighbor, depth + 1))

    unresolved = []
    if args.include_unresolved_boundary:
        for rel in relations_doc.get("unresolved_relations", []):
            touching = rel.get("source_id") in selected or rel.get("target_id") in selected
            if touching and rel.get("traversal") == "BLOCKED_UNRESOLVED":
                unresolved.append(rel)

    collisions = [
        c for c in collisions_doc.get("collisions", [])
        if any(oid in selected for oid in c.get("object_ids", []))
    ]

    result = {
        "slice_version": "0.2",
        "project_scope": "ELYXION",
        "start_id": args.start_id,
        "max_hops": args.max_hops,
        "direction": args.direction,
        "objects": [objects[x] for x in sorted(selected)],
        "confirmed_relations": selected_relations,
        "unresolved_boundary": unresolved,
        "collisions": collisions,
        "laws": {
            "relation_direction_preserved": True,
            "unresolved_relations_not_traversed": True,
            "open_collisions_preserved": True,
            "slice_is_not_global_completeness_claim": True,
            "evidence_descent_preserved": True,
        },
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
