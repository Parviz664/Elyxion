#!/usr/bin/env python3
from build_semantic_coverage import build_semantic_coverage

def main():
    s=build_semantic_coverage()
    bad=[]
    if s["objects_total"]!=33:bad.append("objects")
    if s["objects_with_normalized_claims"]!=6:bad.append("covered")
    if s["objects_without_normalized_claims"]!=27:bad.append("uncovered")
    if abs(s["coverage_ratio"]-(6/33))>1e-12:bad.append("ratio")
    covered={x["object_id"] for x in s["rows"] if x["normalized_claim_coverage"]=="PRESENT"}
    expected={
      "ELYX_CHANNEL_ECO_SYSTEMS",
      "ELYX_GOV_CREATOR_REALITY_STABILIZER",
      "ELYX_SURFACE_E_PRIME",
      "ELYX_SURFACE_PHASE1_SCAFFOLD",
      "ELYX_SURFACE_P_CONTROL_POINT",
      "ELYX_SURFACE_UFO_NAVIGATOR"
    }
    if covered!=expected:bad.append("covered-set")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: normalized semantic object coverage=6/33; global semantic completeness remains unproven")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
