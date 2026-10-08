#!/usr/bin/env python3
import json
from pathlib import Path
from build_o2_relation_dependency_index import build

B=Path(__file__).resolve().parents[1]

def main():
    expected=json.loads((B/"NAV_O2_RELATION_DEPENDENCY_INDEX_V0_4.json").read_text())
    got=build()
    bad=[]
    if got!=expected:bad.append("derived-cache-drift")
    if len(got["assertion_to_evidence"])!=25:bad.append("assertion-count")
    if got["assertion_to_promoted_relation"]["O2_P4_CONDITIONAL_HANDOFF_TO_P5"] is not None:
        bad.append("conditional-promoted")
    if got["assertion_to_promoted_relation"]["O2_A0_HANDS_OFF_TO_A1_HISTORICAL_V3_0"] is not None:
        bad.append("historical-promoted")
    if sum(1 for x in got["assertion_to_promoted_relation"].values() if x is not None)!=23:
        bad.append("promoted-count")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O2 dependency index v0.2 reproducible assertions=25 promoted=23 conditional=1 historical=1")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
