#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from build_context_slice import build_slice, load_documents

BASE = Path(__file__).resolve().parents[1]
OBJECT_REGISTRY = BASE / "NAV_OBJECT_REGISTRY_V0_4.json"
EVIDENCE_INDEX = BASE / "NAV_EVIDENCE_INDEX_V0_1.json"
FRESHNESS_POLICY = BASE / "NAV_FRESHNESS_POLICY_V0_3.json"

def collect_evidence_locators(value, out):
    if isinstance(value, list):
        for item in value:
            collect_evidence_locators(item, out)
        return
    if not isinstance(value, dict):
        return
    for key, item in value.items():
        if key == "evidence" and isinstance(item, list):
            for ref in item:
                if isinstance(ref, str) and ":" in ref:
                    out.add(ref)
        else:
            collect_evidence_locators(item, out)

def build_pack(start_id, max_hops=1, direction="both", include_unresolved_boundary=True):
    objects_doc, relations_doc, collisions_doc = load_documents()
    slice_doc = build_slice(
        objects_doc,
        relations_doc,
        collisions_doc,
        start_id=start_id,
        max_hops=max_hops,
        direction=direction,
        include_unresolved_boundary=include_unresolved_boundary,
    )

    object_registry = json.loads(OBJECT_REGISTRY.read_text(encoding="utf-8"))
    evidence_index = json.loads(EVIDENCE_INDEX.read_text(encoding="utf-8"))
    freshness = json.loads(FRESHNESS_POLICY.read_text(encoding="utf-8"))

    discovery_map = {
        item["id"]: item for item in object_registry.get("discovery_targets", [])
    }

    discovery_ids = set()
    for relation in slice_doc.get("unresolved_boundary", []):
        target = relation.get("target_discovery_id")
        if target:
            discovery_ids.add(target)

    discovery_boundary = [
        discovery_map[x] for x in sorted(discovery_ids) if x in discovery_map
    ]

    locators = set()
    collect_evidence_locators(slice_doc["objects"], locators)
    collect_evidence_locators(slice_doc["confirmed_relations"], locators)
    collect_evidence_locators(slice_doc["unresolved_boundary"], locators)
    collect_evidence_locators(slice_doc["collisions"], locators)

    declaration_ids = set()
    for relation in slice_doc.get("unresolved_boundary", []):
        ref = relation.get("author_declaration_ref")
        if ref:
            declaration_ids.add(ref)
    for target in discovery_boundary:
        ref = target.get("author_declaration_ref")
        if ref:
            declaration_ids.add(ref)

    by_locator = {
        entry["locator"]: entry for entry in evidence_index.get("entries", [])
        if entry.get("source_type") == "GITHUB_FILE"
    }
    by_declaration = {
        entry["declaration_id"]: entry for entry in evidence_index.get("entries", [])
        if entry.get("source_type") == "AUTHOR_DECLARATION"
    }

    missing = sorted(x for x in locators if x not in by_locator)
    missing_declarations = sorted(
        x for x in declaration_ids if x not in by_declaration
    )
    if missing or missing_declarations:
        raise ValueError(
            "evidence index gap: "
            + json.dumps({
                "missing_locators": missing,
                "missing_declarations": missing_declarations,
            })
        )

    evidence_ids = {by_locator[x]["evidence_id"] for x in locators}
    evidence_ids.update(by_declaration[x]["evidence_id"] for x in declaration_ids)
    evidence_by_id = {
        entry["evidence_id"]: entry for entry in evidence_index.get("entries", [])
    }
    evidence_manifest = [
        evidence_by_id[x] for x in sorted(evidence_ids)
    ]

    return {
        "pack_version": "0.1",
        "project_scope": "ELYXION",
        "request": {
            "start_id": start_id,
            "max_hops": max_hops,
            "direction": direction,
            "include_unresolved_boundary": include_unresolved_boundary,
        },
        "slice": {
            "objects": slice_doc["objects"],
            "confirmed_relations": slice_doc["confirmed_relations"],
        },
        "discovery_boundary": discovery_boundary,
        "unresolved_boundary": slice_doc["unresolved_boundary"],
        "collisions": slice_doc["collisions"],
        "evidence_manifest": evidence_manifest,
        "materialization_plan": {
            "default_loaded_file_bodies": [],
            "manifest_only_evidence_ids": [
                x["evidence_id"] for x in evidence_manifest
            ],
            "escalation_required_for_file_content": True,
        },
        "freshness_contract": {
            "policy_ref": FRESHNESS_POLICY.name,
            "must_check_before_high_confidence_use": True,
            "stale_means_recover_affected_slice_not_global_replay": True,
        },
        "budget": {
            "selected_object_count": len(slice_doc["objects"]),
            "total_known_object_count": len(object_registry.get("objects", [])),
            "selected_evidence_count": len(evidence_manifest),
            "total_indexed_evidence_count": len(evidence_index.get("entries", [])),
        },
        "laws": {
            "pack_is_bounded_not_complete_world": True,
            "evidence_manifest_is_deduplicated": True,
            "file_bodies_not_loaded_by_default": True,
            "unresolved_relations_not_traversed": True,
            "collisions_not_auto_resolved": True,
            "author_declaration_source_kind_preserved": True,
            "evidence_descent_preserved": True,
        },
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_id")
    parser.add_argument("--max-hops", type=int, default=1)
    parser.add_argument("--direction", choices=["outgoing", "incoming", "both"], default="both")
    parser.add_argument("--exclude-unresolved-boundary", action="store_true")
    args = parser.parse_args()

    try:
        result = build_pack(
            start_id=args.start_id,
            max_hops=args.max_hops,
            direction=args.direction,
            include_unresolved_boundary=not args.exclude_unresolved_boundary,
        )
    except ValueError as exc:
        raise SystemExit(str(exc))

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
