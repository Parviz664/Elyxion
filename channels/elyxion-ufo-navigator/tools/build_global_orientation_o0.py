#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

B=Path(__file__).resolve().parents[1]

def J(name):
    return json.loads((B/name).read_text())

def build_o0():
    sectors=J("NAV_SECTOR_CATALOG_V0_7.json")
    discovery=J("NAV_DISCOVERY_LEDGER_V0_1.json")
    branch=J("NAV_REPOSITORY_BRANCH_INVENTORY_V0_4.json")
    collision=J("NAV_COLLISION_REGISTRY_V0_1.json")
    relations=J("NAV_RELATION_REGISTRY_V0_3.json")
    author=J("NAV_AUTHOR_DECLARATIONS_V0_1.json")

    global_decl=next(
        (x for x in author["declarations"] if x["id"]=="AUTHDECL_GLOBAL_C0_EXISTS_2026_10_07"),
        None
    )
    horizon=[]
    for x in discovery["targets"]:
        horizon.append({
          "id":x["id"],
          "evidence_state":x["evidence_state"],
          "repository_location":x.get("repository_location","UNKNOWN"),
          "existence_elsewhere":x.get("existence_elsewhere","UNKNOWN")
        })

    payload={
      "orientation_level":"O0_TOPOLOGY_INDEX",
      "project_scope":"ELYXION",
      "producer":{"id":"ELYX_SURFACE_UFO_NAVIGATOR","authority":"NAVIGATION_ONLY"},
      "consumer_boundary":{
        "global_c0_existence":"AUTHOR_DECLARED_EXISTS" if global_decl else "UNKNOWN",
        "global_c0_durable_location":"UNKNOWN",
        "navigator_global_c0_authority":"NONE",
        "build_or_define_global_c0":False
      },
      "sector_capsules":[
        {
          "sector_id":x["sector_id"],
          "label":x["label"],
          "object_count":x["object_count"],
          "confirmed_relation_count":x["confirmed_relation_count"],
          "verified_o1_capsules":x.get("verified_o1_capsules",0),
          "normalized_object_claims_present":x.get("normalized_object_claims_present",0),
          "semantic_completeness":x["semantic_completeness"]
        }
        for x in sectors["sectors"]
      ],
      "topology_totals":{
        "branches":branch["counts"]["total"],
        "branches_mapped":branch["counts"]["represented_in_object_catalog"],
        "objects":sectors["totals"]["objects"],
        "confirmed_relations":sectors["totals"]["confirmed_relations"],
        "unresolved_relations":len(relations["unresolved_relations"]),
        "collisions":len(collision["collisions"]),
        "discovery_targets":len(horizon),
        "verified_o1_capsules":sectors["totals"].get("verified_o1_capsules",0),
        "normalized_object_claims_present":sectors["totals"].get("normalized_object_claims_present",0)
      },
      "discovery_horizon":horizon,
      "pressure":{
        "sector_capsules":len(sectors["sectors"]),
        "individual_evidence_identities_loaded":0,
        "exact_source_bodies_loaded":0,
        "full_history_replay":False
      },
      "descent_contract":{
        "next_level_for_surface_role":"O1_ROLE_BOUNDARY",
        "next_level_for_cross_surface_relation":"O2_RELATION_AUTHORITY",
        "next_level_for_evidence_backed_decision":"O3_CLAIM_EVIDENCE",
        "exact_source_only_when_needed":"O4_EXACT_SOURCE",
        "primary_raw_only_when_required":"O5_PRIMARY_RAW"
      },
      "semantic_readiness":"READY_NORMALIZED_SEMANTIC_COVERAGE",
      "global_semantic_completeness":"NOT_PROVEN",
      "relation_authority_readiness":"PARTIAL_NOT_O2_COMPLETE",
      "topology_readiness":"READY_TOPOLOGY_ORIENTATION"
    }
    fp=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    payload["orientation_fingerprint"]={"algorithm":"SHA-256","value":fp}
    return payload

if __name__=="__main__":
    print(json.dumps(build_o0(),indent=2,ensure_ascii=False))
