#!/usr/bin/env python3
from build_global_orientation import topology_readiness, semantic_readiness

def main():
    topology_cases=[
      ("ready","FRESH",1.0,1.0,1.0,"READY_TOPOLOGY_ORIENTATION"),
      ("stale","STALE_TARGETED",1.0,1.0,1.0,"BLOCKED_FRESHNESS"),
      ("unknown-freshness","UNKNOWN_FRESHNESS",1.0,1.0,1.0,"BLOCKED_FRESHNESS"),
      ("topology-expansion","FRESH",5/31,1.0,1.0,"BLOCKED_TOPOLOGY_EXPANSION"),
      ("object-gap","FRESH",1.0,32/33,1.0,"BLOCKED_OBSERVED_OBJECT_COVERAGE"),
      ("discovery-gap","FRESH",1.0,1.0,5/6,"BLOCKED_DISCOVERY_HORIZON_COVERAGE"),
      ("precedence-freshness","STALE_TARGETED",5/31,32/33,5/6,"BLOCKED_FRESHNESS"),
      ("precedence-topology","FRESH",5/31,32/33,5/6,"BLOCKED_TOPOLOGY_EXPANSION")
    ]
    semantic_cases=[
      ("semantic-full",1.0,"READY_NORMALIZED_SEMANTIC_COVERAGE"),
      ("semantic-current",6/33,"PARTIAL_NORMALIZED_SEMANTIC_COVERAGE"),
      ("semantic-zero",0.0,"PARTIAL_NORMALIZED_SEMANTIC_COVERAGE"),
      ("semantic-unknown",None,"UNKNOWN_SEMANTIC_COVERAGE")
    ]

    bad=[]
    for cid,fresh,branch_cov,obj,disc,expected in topology_cases:
        got=topology_readiness(fresh,branch_cov,obj,disc)
        if got!=expected:
            bad.append(f"{cid}:{got}!={expected}")
    for cid,ratio,expected in semantic_cases:
        got=semantic_readiness(ratio)
        if got!=expected:
            bad.append(f"{cid}:{got}!={expected}")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print(f"PASS: topology blocking cases={len(topology_cases)} semantic readiness cases={len(semantic_cases)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
