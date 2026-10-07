#!/usr/bin/env python3
from build_global_c0_handoff import handoff_readiness

def main():
    cases=[
      ("fresh_ok","FRESH",[],"READY_FOR_GLOBAL_C0_REVIEW"),
      ("stale_blocks","STALE_TARGETED",[],"BLOCKED_FRESHNESS"),
      ("unknown_freshness_blocks","UNKNOWN_FRESHNESS",[],"BLOCKED_FRESHNESS"),
      ("critical_evidence_blocks","FRESH",["CLAIM_GLOBAL_C0_EXISTS"],"BLOCKED_EVIDENCE"),
      ("freshness_precedes_evidence","STALE_TARGETED",["CLAIM_GLOBAL_C0_EXISTS"],"BLOCKED_FRESHNESS")
    ]
    bad=[]
    for cid,fresh,critical,expected in cases:
        got=handoff_readiness(fresh,critical)
        if got!=expected:
            bad.append(f"{cid}:{got}!={expected}")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print(f"PASS: handoff blocking cases={len(cases)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
