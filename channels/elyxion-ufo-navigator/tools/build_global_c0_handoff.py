#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from build_context_pack import build_pack
from check_context_pack_staleness import evaluate_pack
from check_claim_sufficiency import evaluate_claim

B=Path(__file__).resolve().parents[1]
VERS=json.loads((B/"NAV_CLAIM_VERIFICATION_RECEIPTS_V0_1.json").read_text())
BY_VER={x["claim_id"]:x for x in VERS["verifications"]}

def handoff_readiness(fresh_state,critical_failure_claim_ids):
    if fresh_state!="FRESH":
        return "BLOCKED_FRESHNESS"
    if critical_failure_claim_ids:
        return "BLOCKED_EVIDENCE"
    return "READY_FOR_GLOBAL_C0_REVIEW"

def build_handoff(start_id,max_hops=1,direction="both"):
    pack=build_pack(start_id,max_hops,direction,True)
    fresh=evaluate_pack(pack)

    claim_results=[]
    critical_failures=[]
    sufficient_count=0

    for claim in pack["claims"]:
        cid=claim["claim_id"]
        suff=evaluate_claim(cid)
        if suff.get("state")=="SUFFICIENT":
            sufficient_count+=1
        critical=(
            claim.get("claim_class") in {"COLLISION","AUTHORITY"}
            or claim.get("epistemic_state")=="AUTHOR_DECLARED"
        )
        if critical and suff.get("state")!="SUFFICIENT":
            critical_failures.append(cid)
        claim_results.append({
          "claim_id":cid,
          "claim_class":claim.get("claim_class"),
          "epistemic_state":claim.get("epistemic_state"),
          "critical_for_handoff":critical,
          "sufficiency":suff,
          "verification_receipt":BY_VER.get(cid)
        })

    total=len(pack["claims"])
    coverage=(sufficient_count/total) if total else 1.0

    readiness=handoff_readiness(fresh["state"],critical_failures)

    return {
      "handoff_version":"0.2",
      "producer":{"id":"ELYX_SURFACE_UFO_NAVIGATOR","role":"NAVIGATION_ONLY"},
      "consumer":{"id":"GLOBAL_C0_UFO","existence_basis":"AUTHDECL_GLOBAL_C0_EXISTS_2026_10_07"},
      "consumer_existence":"AUTHOR_DECLARED_EXISTS",
      "consumer_location":"UNKNOWN",
      "navigator_authority":{
        "global_c0_authority":"NONE",
        "may_build_global_c0":False,
        "may_duplicate_global_c0":False
      },
      "payload_kind":"ELYXION_NAV_CONTEXT_PACK",
      "payload":pack,
      "payload_fingerprint":pack["pack_fingerprint"],
      "freshness":fresh,
      "risk":pack["risk"],
      "verification_summary":{
        "selected_claim_count":total,
        "sufficient_claim_count":sufficient_count,
        "verification_coverage":coverage,
        "critical_failure_claim_ids":critical_failures
      },
      "claim_verifications":claim_results,
      "boundary_summary":{
        "unresolved_count":len(pack["unresolved_boundary"]),
        "collision_count":len(pack["collisions"]),
        "discovery_count":len(pack["discovery_boundary"])
      },
      "handoff_readiness":readiness,
      "non_authority":{
        "canon_decision":False,
        "execution_authority":False,
        "global_c0_construction_performed":False,
        "global_c0_internal_architecture_defined":False
      }
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("start_id")
    p.add_argument("--max-hops",type=int,default=1)
    p.add_argument("--direction",choices=["outgoing","incoming","both"],default="both")
    a=p.parse_args()
    print(json.dumps(build_handoff(a.start_id,a.max_hops,a.direction),indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
