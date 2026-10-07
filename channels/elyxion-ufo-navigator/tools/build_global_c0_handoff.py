#!/usr/bin/env python3
import argparse, json
from build_context_pack import build_pack
from check_context_pack_staleness import evaluate_pack

def build_handoff(start_id,max_hops=1,direction="both"):
    pack=build_pack(start_id,max_hops,direction,True)
    fresh=evaluate_pack(pack)
    readiness="READY_FOR_GLOBAL_C0_REVIEW" if fresh["state"]=="FRESH" else "BLOCKED_FRESHNESS"
    return {
      "handoff_version":"0.1",
      "producer":{
        "id":"ELYX_SURFACE_UFO_NAVIGATOR",
        "role":"NAVIGATION_ONLY"
      },
      "consumer":{
        "id":"GLOBAL_C0_UFO",
        "existence_basis":"AUTHDECL_GLOBAL_C0_EXISTS_2026_10_07"
      },
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
    p=argparse.ArgumentParser();p.add_argument("start_id");p.add_argument("--max-hops",type=int,default=1);p.add_argument("--direction",choices=["outgoing","incoming","both"],default="both");a=p.parse_args()
    print(json.dumps(build_handoff(a.start_id,a.max_hops,a.direction),indent=2,ensure_ascii=False))
if __name__=="__main__":main()
