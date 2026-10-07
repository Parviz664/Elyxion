#!/usr/bin/env python3
import argparse
import json
from collections import deque
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OBJECTS = BASE / "NAV_OBJECT_REGISTRY_V0_3.json"
RELATIONS = BASE / "NAV_RELATION_REGISTRY_V0_2.json"
COLLISIONS = BASE / "NAV_COLLISION_REGISTRY_V0_1.json"

def load_documents():
    return (
        json.loads(OBJECTS.read_text(encoding="utf-8")),
        json.loads(RELATIONS.read_text(encoding="utf-8")),
        json.loads(COLLISIONS.read_text(encoding="utf-8")),
    )

def build_slice(
    objects_doc,
    relations_doc,
    collisions_doc,
    start_id,
    max_hops=1,
    direction="both",
    include_unresolved_boundary=False,
):
    objects = {x["id"]: x for x in objects_doc.get("objects", [])}
    if start_id not in objects:
        raise ValueError(f"unknown start object: {start_id}")
    if max_hops < 0:
        raise ValueError("max_hops must be >= 0")
    if direction not in {"outgoing", "incoming", "both"}:
        raise ValueError(f"invalid direction: {direction}")

    confirmed = [
        r for r in relations_doc.get("confirmed_relations", [])
        if r.get("state") == "CONFIRMED" and r.get("traversal") == "ALLOWED_AS_FACT"
    ]

    selected = {start_id}
    selected_relations = []
    seen_rel_ids = set()
    q = deque([(start_id, 0)])

    while q:
        node, depth = q.popleft()
        if depth >= max_hops:
            continue

        for rel in confirmed:
            neighbors = []
            if direction in ("outgoing", "both") and rel["source_id"] == node:
                neighbors.append(rel["target_id"])
            if direction in ("incoming", "both") and rel["target_id"] == node:
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
    if include_unresolved_boundary:
        for rel in relations_doc.get("unresolved_relations", []):
            touching = rel.get("source_id") in selected or rel.get("target_id") in selected
            if touching and rel.get("traversal") == "BLOCKED_UNRESOLVED":
                unresolved.append(rel)

    collisions = [
        c for c in collisions_doc.get("collisions", [])
        if any(oid in selected for oid in c.get("object_ids", []))
    ]

    return {
        "slice_version": "0.3",
        "project_scope": "ELYXION",
        "start_id": start_id,
        "max_hops": max_hops,
        "direction": direction,
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

def main():
    parser = argparse.ArgumentParser(
        description="Build a bounded Elyxion Navigator context slice from confirmed relations."
    )
    parser.add_argument("start_id")
    parser.add_argument("--max-hops", type=int, default=1)
    parser.add_argument("--direction", choices=["outgoing", "incoming", "both"], default="both")
    parser.add_argument("--include-unresolved-boundary", action="store_true")
    args = parser.parse_args()

    docs = load_documents()
    try:
        result = build_slice(
            *docs,
            start_id=args.start_id,
            max_hops=args.max_hops,
            direction=args.direction,
            include_unresolved_boundary=args.include_unresolved_boundary,
        )
    except ValueError as exc:
        raise SystemExit(str(exc))

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
