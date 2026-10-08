#!/usr/bin/env python3
from build_semantic_coverage import build_semantic_coverage

def main():
    s=build_semantic_coverage()
    bad=[]
    if s["objects_total"]!=33:bad.append("objects")
    if s["objects_with_normalized_claims"]!=33:bad.append("covered")
    if s["objects_without_normalized_claims"]!=0:bad.append("uncovered")
    if abs(s["coverage_ratio"]-1.0)>1e-12:bad.append("ratio")
    covered={x["object_id"] for x in s["rows"] if x["normalized_claim_coverage"]=="PRESENT"}
    if "ELYX_SURFACE_MAIN" not in covered:bad.append("main-not-covered")
    if len(covered)!=33:bad.append("covered-set-size")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: normalized semantic object coverage=33/33; object coverage READY; global semantic/O2 completeness remains unproven")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
