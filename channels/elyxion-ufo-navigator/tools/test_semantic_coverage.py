#!/usr/bin/env python3
from build_semantic_coverage import build_semantic_coverage

def main():
    s=build_semantic_coverage()
    bad=[]
    if s["objects_total"]!=33:bad.append("objects")
    if s["objects_with_normalized_claims"]!=32:bad.append("covered")
    if s["objects_without_normalized_claims"]!=1:bad.append("uncovered")
    if abs(s["coverage_ratio"]-(32/33))>1e-12:bad.append("ratio")
    required={"ELYX_REC_D0","ELYX_REC_D1","ELYX_REC_D2","ELYX_REC_D3","ELYX_REC_D4"}
    covered={x["object_id"] for x in s["rows"] if x["normalized_claim_coverage"]=="PRESENT"}
    if not required.issubset(covered):bad.append("d-sector-not-covered")
    if "ELYX_SURFACE_MAIN" in covered:bad.append("main-prematurely-covered")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: normalized semantic object coverage=32/33; D sector O1 covered; main remains the only uncovered object")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
