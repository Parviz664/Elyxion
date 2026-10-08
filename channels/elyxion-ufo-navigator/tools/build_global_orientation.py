#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from build_context_pack import build_pack
from check_context_pack_staleness import evaluate_pack
from check_claim_sufficiency import evaluate_claim
from nav_catalog import load_objects, load_evidence
from build_semantic_coverage import build_semantic_coverage

B=Path(__file__).resolve().parents[1]
PROFILE=json.loads((B/"NAV_GLOBAL_ORIENTATION_PROFILE_V0_2.json").read_text())
OBJECTS=load_objects()
EVIDENCE=load_evidence()
CLAIMS=json.loads((B/"NAV_CLAIM_INDEX_V0_7.json").read_text())
BRANCH_INVENTORY=json.loads((B/"NAV_REPOSITORY_BRANCH_INVENTORY_V0_4.json").read_text())

def topology_readiness(fresh_state,branch_mapping_coverage,object_coverage,discovery_coverage):
    req=PROFILE["topology_requirements"]
    if fresh_state!="FRESH":
        return "BLOCKED_FRESHNESS"
    if branch_mapping_coverage < req["branch_inventory_mapping_coverage"]:
        return "BLOCKED_TOPOLOGY_EXPANSION"
    if object_coverage < req["observed_object_catalog_coverage"]:
        return "BLOCKED_OBSERVED_OBJECT_COVERAGE"
    if discovery_coverage < req["discovery_horizon_coverage"]:
        return "BLOCKED_DISCOVERY_HORIZON_COVERAGE"
    return "READY_TOPOLOGY_ORIENTATION"

def semantic_readiness(normalized_object_claim_coverage):
    threshold=PROFILE["semantic_measurement"]["readiness_threshold_for_full_normalized_semantic_coverage"]
    if normalized_object_claim_coverage is None:
        return "UNKNOWN_SEMANTIC_COVERAGE"
    if normalized_object_claim_coverage >= threshold:
        return "READY_NORMALIZED_SEMANTIC_COVERAGE"
    return "PARTIAL_NORMALIZED_SEMANTIC_COVERAGE"

def build_global_orientation():
    t=PROFILE["traversal"]
    pack=build_pack(
        t["start_id"],
        t["max_hops"],
        t["direction"],
        t["include_unresolved_boundary"]
    )
    fresh=evaluate_pack(pack)

    connected={x["id"] for x in pack["discovery_boundary"]}
    all_discovery=OBJECTS["discovery_targets"]
    horizon=[]
    for x in all_discovery:
        if x["id"] in connected:
            visibility="CONNECTED_BOUNDARY"
        elif str(x.get("evidence_state","")).startswith("OBSERVED_"):
            visibility="AMBIENT_OBSERVED"
        else:
            visibility="AMBIENT_REGISTERED_UNKNOWN"
        horizon.append({
          "id":x["id"],
          "visibility":visibility,
          "evidence_state":x.get("evidence_state"),
          "repository_location":x.get("repository_location"),
          "existence_elsewhere":x.get("existence_elsewhere"),
          "author_declaration_ref":x.get("author_declaration_ref")
        })

    verifications=[]
    for claim in pack["claims"]:
        verifications.append({
          "claim_id":claim["claim_id"],
          "result":evaluate_claim(claim["claim_id"])
        })

    selected_objects=len(pack["slice"]["objects"])
    total_objects=len(OBJECTS["objects"])
    selected_claims=len(pack["claims"])
    sufficient=sum(1 for x in verifications if x["result"].get("state")=="SUFFICIENT")
    discovery_count=len(horizon)
    total_discovery=len(OBJECTS["discovery_targets"])

    object_coverage=selected_objects/total_objects if total_objects else 1.0
    claim_coverage=sufficient/selected_claims if selected_claims else 1.0
    discovery_coverage=discovery_count/total_discovery if total_discovery else 1.0
    mapped=BRANCH_INVENTORY["counts"]["represented_in_object_catalog"]
    branch_total=BRANCH_INVENTORY["counts"]["total"]
    branch_mapping_coverage=mapped/branch_total if branch_total else 1.0

    topo_readiness=topology_readiness(
        fresh["state"],branch_mapping_coverage,object_coverage,discovery_coverage
    )
    semantic=build_semantic_coverage()
    sem_readiness=semantic_readiness(semantic.get("coverage_ratio"))

    return {
      "orientation_version":"0.2",
      "profile_id":PROFILE["profile_id"],
      "project_scope":"ELYXION",
      "readiness":topo_readiness,
      "topology_readiness":topo_readiness,
      "semantic_readiness":sem_readiness,
      "freshness":fresh,
      "coverage":{
        "branch_inventory_mapping":{"represented":mapped,"total":branch_total,"ratio":branch_mapping_coverage,"observed_unmapped":BRANCH_INVENTORY["counts"]["observed_unmapped"]},
        "observed_objects":{"selected":selected_objects,"total":total_objects,"ratio":object_coverage},
        "discovery_horizon":{"selected":discovery_count,"total":total_discovery,"ratio":discovery_coverage},
        "selected_claim_verification":{"sufficient":sufficient,"selected":selected_claims,"ratio":claim_coverage},
        "normalized_object_claim_coverage":{"covered":semantic["objects_with_normalized_claims"],"total":semantic["objects_total"],"ratio":semantic["coverage_ratio"],"uncovered":semantic["objects_without_normalized_claims"]},
        "evidence_identity":{"selected":len(pack["evidence_manifest"]),"total":len(EVIDENCE["entries"]),"ratio":len(pack["evidence_manifest"])/len(EVIDENCE["entries"]) if EVIDENCE["entries"] else 1.0}
      },
      "bounded_pack":pack,
      "ambient_discovery_horizon":horizon,
      "claim_verifications":verifications,
      "pressure":{
        "default_loaded_file_bodies":len(pack["materialization_plan"]["default_loaded_file_bodies"]),
        "selected_evidence_identities":len(pack["evidence_manifest"]),
        "total_indexed_evidence_identities":len(EVIDENCE["entries"]),
        "selected_claims":selected_claims,
        "total_indexed_claims":len(CLAIMS["claims"])
      },
      "laws":{
        "orientation_covers_current_observed_registry_not_all_history":True,
        "observed_unmapped_branches_block_ready":True,
        "ambient_unknowns_are_preserved":True,
        "full_history_replay_default":False,
        "global_c0_construction_performed":False,
        "topology_ready_does_not_mean_semantically_complete":True,
        "selected_claim_verification_does_not_equal_all_surface_semantic_coverage":True
      }
    }

def main():
    p=argparse.ArgumentParser()
    p.parse_args()
    print(json.dumps(build_global_orientation(),indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
