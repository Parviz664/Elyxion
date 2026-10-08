#!/usr/bin/env python3
import json
from pathlib import Path
from build_o2_relation_dependency_index import build

B=Path(__file__).resolve().parents[1]

def main():
    expected=json.loads((B/"NAV_O2_RELATION_DEPENDENCY_INDEX_V0_1.json").read_text())
    got=build()
    bad=[]
    if got!=expected:bad.append("derived-cache-drift")
    if len(got["assertion_to_evidence"])!=8:bad.append("assertion-count")
    if len(got["evidence_to_assertions"])<8:bad.append("evidence-reverse-index")
    if got["assertion_to_promoted_relation"]["O2_P4_CONDITIONAL_HANDOFF_TO_P5"] is not None:
        bad.append("conditional-promoted")
    if sum(1 for x in got["assertion_to_promoted_relation"].values() if x is not None)!=7:
        bad.append("promoted-count")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O2 relation dependency index reproducible assertions=8 promoted=7 conditional=1")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
