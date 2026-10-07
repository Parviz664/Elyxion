#!/usr/bin/env python3
import argparse, json
from build_global_c0_handoff import build_handoff

def build_export(start_id,max_hops=1,direction="both"):
    h=build_handoff(start_id,max_hops,direction)
    verified=[]
    for x in h["claim_verifications"]:
        v=x.get("verification_receipt")
        if not v:
            continue
        verified.append({
          "claim_id":x["claim_id"],
          "claim_class":x["claim_class"],
          "epistemic_state":x["epistemic_state"],
          "critical_for_handoff":x["critical_for_handoff"],
          "sufficiency_state":x["sufficiency"]["state"],
          "verification_id":v["verification_id"],
          "verification_verdict":v["verdict"],
          "materialization_receipt_ids":v["materialization_receipt_ids"],
          "limits":v["limits"]
        })

    return {
      "export_version":"ELYXION_NAV_GLOBAL_C0_COLD_START_EXPORT_V0_1",
      "producer":h["producer"],
      "consumer":{
        "id":h["consumer"]["id"],
        "existence":h["consumer_existence"],
        "durable_location":h["consumer_location"]
      },
      "non_duplication_boundary":{
        "build_global_c0":h["navigator_authority"]["may_build_global_c0"],
        "duplicate_global_c0":h["navigator_authority"]["may_duplicate_global_c0"],
        "define_global_c0_internals":h["non_authority"]["global_c0_internal_architecture_defined"]
      },
      "pack_identity":{
        "kind":h["payload_kind"],
        "fingerprint":h["payload_fingerprint"],
        "start_id":h["payload"]["request"]["start_id"]
      },
      "pack_summary":{
        "object_count":h["payload"]["budget"]["selected_object_count"],
        "claim_count":h["payload"]["budget"]["selected_claim_count"],
        "evidence_identity_count":h["payload"]["budget"]["selected_evidence_count"],
        "risk":h["risk"]["band"],
        "recommended_materialization":h["payload"]["materialization_plan"]["recommended_minimum_level"],
        "freshness":h["freshness"]["state"]
      },
      "verification_summary":h["verification_summary"],
      "verified_claims":verified,
      "unresolved_boundary_ids":[x["id"] for x in h["payload"]["unresolved_boundary"]],
      "collision_ids":[x["id"] for x in h["payload"]["collisions"]],
      "discovery_boundary_ids":[x["id"] for x in h["payload"]["discovery_boundary"]],
      "recovery_contract":{
        "stale_pack_action":"TARGETED_REPAIR",
        "global_replay_default":False,
        "unknown_source_action":"BLOCK_HIGH_CONFIDENCE_HANDOFF"
      },
      "handoff_readiness":h["handoff_readiness"],
      "caveat":"Navigator export semantics only; does not define Global C0 internals."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("start_id")
    p.add_argument("--max-hops",type=int,default=1)
    p.add_argument("--direction",choices=["outgoing","incoming","both"],default="both")
    a=p.parse_args()
    print(json.dumps(build_export(a.start_id,a.max_hops,a.direction),indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
