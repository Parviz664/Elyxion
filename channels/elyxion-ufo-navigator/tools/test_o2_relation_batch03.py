#!/usr/bin/env python3
import json
from pathlib import Path

B=Path(__file__).resolve().parents[1]
A=json.loads((B/"NAV_O2_RELATION_ASSERTIONS_BATCH_03_V0_1.json").read_text())
V=json.loads((B/"NAV_O2_RELATION_VERIFICATION_RECEIPTS_BATCH_03_V0_1.json").read_text())
R=json.loads((B/"relations/NAV_RELATION_SHARD_O2_BATCH_03_V0_1.json").read_text())

def main():
    bad=[]
    assertions=A["assertions"]; verifications=V["verifications"]; relations=R["confirmed_relations"]
    if len(assertions)!=4:bad.append("assertion-count")
    if len(verifications)!=4:bad.append("verification-count")
    if len(relations)!=3:bad.append("current-relation-count")

    by_a={x["assertion_id"]:x for x in assertions}
    by_v={x["assertion_id"]:x for x in verifications}

    current={
      "O2_A1_HANDS_OFF_TO_A2":"HANDS_OFF_TO",
      "O2_A2_HANDS_OFF_EXPORT_TO_E3_5":"HANDS_OFF_TO",
      "O2_A_ULTRA_DECLARES_INTERFACE_WITH_A1":"DECLARES_INTERFACE_WITH"
    }
    for aid,kind in current.items():
        a=by_a[aid]
        if a["base_kind"]!=kind:bad.append(aid+":kind")
        if a["scope_class"]!="CURRENT_LOCAL_SEAM":bad.append(aid+":scope")
        if a.get("promotion_state")!="ELIGIBLE_FOR_BASE_RELATION_LOCAL_ONLY":bad.append(aid+":promotion")
        if by_v[aid]["verdict"]!="SUPPORTED_WITH_LIMITS":bad.append(aid+":verdict")

    hist=by_a["O2_A0_HANDS_OFF_TO_A1_HISTORICAL_V3_0"]
    if hist["scope_class"]!="HISTORICAL_SEAM":bad.append("A0-A1-history-scope")
    if hist["verification_state"]!="HISTORICAL_ONLY":bad.append("A0-A1-history-state")
    if hist.get("promotion_state")!="NOT_PROMOTED_HISTORICAL":bad.append("A0-A1-history-promotion")
    if hist["global_route_effect"]!="HISTORICAL_ONLY":bad.append("A0-A1-history-effect")
    if by_v[hist["assertion_id"]]["promotion_eligibility"]!="NOT_ELIGIBLE":bad.append("A0-A1-history-verification")

    if any(r["source_id"]=="ELYX_REC_A0_ORCHESTRATOR" and r["target_id"]=="ELYX_REC_A1_ARCHITECT" for r in relations):
        bad.append("historical-promoted-current")

    iface=next(r for r in relations if r["id"]=="REL_O2_A_ULTRA_DECLARES_INTERFACE_WITH_A1")
    if iface["kind"]!="DECLARES_INTERFACE_WITH":bad.append("A-Ultra-interface-upgraded")
    if iface.get("composition_policy")!="NO_IMPLICIT_GLOBAL_ROUTE":bad.append("interface-composition")

    for r in relations:
        if r.get("scope_class")!="CURRENT_LOCAL_SEAM":bad.append(r["id"]+":scope")
        if r.get("global_route_effect")!="NONE_LOCAL_ONLY":bad.append(r["id"]+":global")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O2 batch03 current=3 historical=1; A-Ultra interface stays narrow; A0->A1 v3.0 not promoted")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
