#!/usr/bin/env python3
from build_global_orientation import orientation_readiness

def main():
    cases=[
      ("ready","FRESH",1.0,1.0,1.0,"READY_GLOBAL_ORIENTATION"),
      ("stale","STALE_TARGETED",1.0,1.0,1.0,"BLOCKED_FRESHNESS"),
      ("unknown-freshness","UNKNOWN_FRESHNESS",1.0,1.0,1.0,"BLOCKED_FRESHNESS"),
      ("object-gap","FRESH",6/7,1.0,1.0,"BLOCKED_OBSERVED_OBJECT_COVERAGE"),
      ("discovery-gap","FRESH",1.0,5/6,1.0,"BLOCKED_DISCOVERY_HORIZON_COVERAGE"),
      ("verification-gap","FRESH",1.0,1.0,8/9,"BLOCKED_VERIFICATION"),
      ("precedence-freshness","STALE_TARGETED",6/7,5/6,8/9,"BLOCKED_FRESHNESS")
    ]
    bad=[]
    for cid,fresh,obj,disc,claims,expected in cases:
        got=orientation_readiness(fresh,obj,disc,claims)
        if got!=expected:
            bad.append(f"{cid}:{got}!={expected}")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print(f"PASS: global orientation blocking cases={len(cases)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
