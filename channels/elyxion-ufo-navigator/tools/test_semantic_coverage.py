#!/usr/bin/env python3
from build_semantic_coverage import build_semantic_coverage

def main():
    s=build_semantic_coverage()
    bad=[]
    if s["objects_total"]!=33:bad.append("objects")
    if s["objects_with_normalized_claims"]!=21:bad.append("covered")
    if s["objects_without_normalized_claims"]!=12:bad.append("uncovered")
    if abs(s["coverage_ratio"]-(21/33))>1e-12:bad.append("ratio")
    covered={x["object_id"] for x in s["rows"] if x["normalized_claim_coverage"]=="PRESENT"}
    required={
      "ELYX_REC_P0","ELYX_REC_P1","ELYX_REC_P2","ELYX_REC_P3","ELYX_REC_P4","ELYX_REC_P5"
    }
    if not required.issubset(covered):bad.append("p-sector-not-covered")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: normalized semantic object coverage=21/33; P sector O1 covered; global semantic completeness remains partial")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
