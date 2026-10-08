#!/usr/bin/env python3
import json
from pathlib import Path

B=Path(__file__).resolve().parents[1]
A=json.loads((B/"NAV_O2_RELATION_ASSERTIONS_BATCH_01_V0_1.json").read_text())
V=json.loads((B/"NAV_O2_RELATION_VERIFICATION_RECEIPTS_V0_1.json").read_text())
R=json.loads((B/"relations/NAV_RELATION_SHARD_O2_BATCH_01_V0_1.json").read_text())

def main():
    bad=[]
    assertions=A["assertions"]
    verifications=V["verifications"]
    relations=R["confirmed_relations"]

    if len(assertions)!=8:bad.append("assertion-count")
    if len(verifications)!=8:bad.append("verification-count")
    if len(relations)!=7:bad.append("promoted-count")

    by_a={x["assertion_id"]:x for x in assertions}
    by_v={x["assertion_id"]:x for x in verifications}

    conditional=by_a.get("O2_P4_CONDITIONAL_HANDOFF_TO_P5")
    if not conditional:bad.append("missing-P4-P5")
    else:
        if conditional["scope_class"]!="CURRENT_CONDITIONAL_SEAM":bad.append("P4-P5-scope")
        if conditional["global_route_effect"]!="CONDITIONAL_ONLY":bad.append("P4-P5-global-effect")
        if conditional.get("promotion_state")!="NOT_PROMOTED_CONDITIONAL":bad.append("P4-P5-promotion")
        if "enable_p5=true" not in conditional["conditions"]:bad.append("P4-P5-condition")
        if by_v[conditional["assertion_id"]]["verdict"]!="SUPPORTED_CONDITIONAL":bad.append("P4-P5-verdict")

    if any(r["source_id"]=="ELYX_REC_P4" and r["target_id"]=="ELYX_REC_P5" for r in relations):
        bad.append("conditional-promoted")

    for r in relations:
        if r.get("scope_class")!="CURRENT_LOCAL_SEAM":bad.append(r["id"]+":scope")
        if r.get("global_route_effect")!="NONE_LOCAL_ONLY":bad.append(r["id"]+":global")
        if r.get("composition_policy")!="NO_IMPLICIT_GLOBAL_ROUTE":bad.append(r["id"]+":composition")
        if r["kind"]!="HANDS_OFF_TO" or r["state"]!="CONFIRMED":bad.append(r["id"]+":kind-state")
        if not r.get("o2_verification_id"):bad.append(r["id"]+":verification")

    promoted_assertions={x["assertion_id"] for x in assertions if x.get("promotion_state")=="ELIGIBLE_FOR_BASE_RELATION_LOCAL_ONLY"}
    if len(promoted_assertions)!=7:bad.append("eligible-count")
    if any(by_v[x]["verdict"]!="SUPPORTED_WITH_LIMITS" for x in promoted_assertions):bad.append("eligible-verdict")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O2 batch01 assertions=8 verified=8 promoted-local=7 conditional-unpromoted=1 no-implicit-global-route")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
