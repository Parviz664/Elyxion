#!/usr/bin/env python3
import json
from pathlib import Path

B=Path(__file__).resolve().parents[1]
A=json.loads((B/"NAV_O2_RELATION_ASSERTIONS_BATCH_02_V0_1.json").read_text())
V=json.loads((B/"NAV_O2_RELATION_VERIFICATION_RECEIPTS_BATCH_02_V0_1.json").read_text())
R=json.loads((B/"relations/NAV_RELATION_SHARD_O2_BATCH_02_V0_1.json").read_text())

def main():
    bad=[]
    assertions=A["assertions"]; verifications=V["verifications"]; relations=R["confirmed_relations"]
    if len(assertions)!=11:bad.append("assertion-count")
    if len(verifications)!=11:bad.append("verification-count")
    if len(relations)!=11:bad.append("relation-count")

    by_assertion={x["assertion_id"]:x for x in assertions}
    by_verification={x["assertion_id"]:x for x in verifications}
    expected_kinds={
      "O2_A2_HANDS_OFF_TO_A3":"HANDS_OFF_TO",
      "O2_A3_HANDS_OFF_TO_E0":"HANDS_OFF_TO",
      "O2_D1_DEPENDS_ON_D0":"DEPENDS_ON",
      "O2_D2_DEPENDS_ON_D0":"DEPENDS_ON",
      "O2_D2_DEPENDS_ON_D1":"DEPENDS_ON",
      "O2_D3_DEPENDS_ON_D0":"DEPENDS_ON",
      "O2_D3_DEPENDS_ON_D1":"DEPENDS_ON",
      "O2_D3_DEPENDS_ON_D2":"DEPENDS_ON",
      "O2_D4_DEPENDS_ON_D1":"DEPENDS_ON",
      "O2_D4_DEPENDS_ON_D2":"DEPENDS_ON",
      "O2_D3_HANDS_OFF_TO_D4":"HANDS_OFF_TO"
    }
    for aid,kind in expected_kinds.items():
        a=by_assertion.get(aid)
        if not a: bad.append(aid+":missing"); continue
        if a["base_kind"]!=kind:bad.append(aid+":kind")
        if a["scope_class"]!="CURRENT_LOCAL_SEAM":bad.append(aid+":scope")
        if a["global_route_effect"]!="NONE_LOCAL_ONLY":bad.append(aid+":global")
        if a.get("promotion_state")!="ELIGIBLE_FOR_BASE_RELATION_LOCAL_ONLY":bad.append(aid+":promotion")
        if by_verification[aid]["verdict"]!="SUPPORTED_WITH_LIMITS":bad.append(aid+":verdict")

    for r in relations:
        if r["state"]!="CONFIRMED" or r["traversal"]!="ALLOWED_AS_FACT":bad.append(r["id"]+":state")
        if r.get("scope_class")!="CURRENT_LOCAL_SEAM":bad.append(r["id"]+":scope")
        if r.get("global_route_effect")!="NONE_LOCAL_ONLY":bad.append(r["id"]+":global")
        if r.get("composition_policy")!="NO_IMPLICIT_GLOBAL_ROUTE":bad.append(r["id"]+":composition")

    d_edges=[r for r in relations if r["source_id"].startswith("ELYX_REC_D") or r["target_id"].startswith("ELYX_REC_D")]
    if sum(1 for r in d_edges if r["kind"]=="DEPENDS_ON")!=8:bad.append("D-dependency-count")
    if sum(1 for r in d_edges if r["kind"]=="HANDS_OFF_TO")!=1:bad.append("D-handoff-count")
    if any(r["id"]=="REL_O2_D0_HANDS_OFF_TO_D1" for r in relations):bad.append("fake-D-pipeline-edge")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O2 batch02 assertions=11 promoted=11; A/E handoffs=2; D dependencies=8; D handoff=1; no numbered D pipeline")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
