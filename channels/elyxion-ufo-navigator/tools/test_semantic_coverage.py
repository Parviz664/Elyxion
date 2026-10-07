#!/usr/bin/env python3
from build_semantic_coverage import build_semantic_coverage

def main():
    s=build_semantic_coverage()
    bad=[]
    if s["objects_total"]!=33:bad.append("objects")
    if s["objects_with_normalized_claims"]!=27:bad.append("covered")
    if s["objects_without_normalized_claims"]!=6:bad.append("uncovered")
    if abs(s["coverage_ratio"]-(27/33))>1e-12:bad.append("ratio")
    required={"ELYX_REC_E0","ELYX_REC_E1","ELYX_REC_E2","ELYX_REC_E3_5","ELYX_REC_E3","ELYX_REC_E4"}
    covered={x["object_id"] for x in s["rows"] if x["normalized_claim_coverage"]=="PRESENT"}
    if not required.issubset(covered):bad.append("operational-e-not-covered")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: normalized semantic object coverage=27/33; operational E sector O1 covered; global semantic completeness remains partial")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
