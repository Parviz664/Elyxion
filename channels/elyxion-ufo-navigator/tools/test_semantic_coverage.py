#!/usr/bin/env python3
from build_semantic_coverage import build_semantic_coverage

def main():
    s=build_semantic_coverage()
    bad=[]
    if s["objects_total"]!=33:bad.append("objects")
    if s["objects_with_normalized_claims"]!=15:bad.append("covered")
    if s["objects_without_normalized_claims"]!=18:bad.append("uncovered")
    if abs(s["coverage_ratio"]-(15/33))>1e-12:bad.append("ratio")
    covered={x["object_id"] for x in s["rows"] if x["normalized_claim_coverage"]=="PRESENT"}
    expected={
      "ELYX_CHANNEL_ECO_SYSTEMS",
      "ELYX_GOV_CREATOR_REALITY_STABILIZER",
      "ELYX_SURFACE_E_PRIME",
      "ELYX_SURFACE_PHASE1_SCAFFOLD",
      "ELYX_SURFACE_P_CONTROL_POINT",
      "ELYX_SURFACE_UFO_NAVIGATOR",
      "ELYX_REC_E_PRIME_KERNEL",
      "ELYX_REC_E_CHAIN_RESEARCH",
      "ELYX_REC_DISPATCHER",
      "ELYX_REC_PAE_HISTORY",
      "ELYX_REC_A_ULTRA",
      "ELYX_REC_A0_ORCHESTRATOR",
      "ELYX_REC_A1_ARCHITECT",
      "ELYX_REC_A2_SYSTEMS_MAP",
      "ELYX_REC_A3_PRE_E0_HANDOFF"
    }
    if covered!=expected:bad.append("covered-set")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: normalized semantic object coverage=15/33; global semantic completeness remains partial")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
