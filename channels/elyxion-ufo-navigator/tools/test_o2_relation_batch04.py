#!/usr/bin/env python3
import json
from pathlib import Path

B=Path(__file__).resolve().parents[1]
A=json.loads((B/"NAV_O2_RELATION_ASSERTIONS_BATCH_04_V0_1.json").read_text())
V=json.loads((B/"NAV_O2_RELATION_VERIFICATION_RECEIPTS_BATCH_04_V0_1.json").read_text())
R=json.loads((B/"relations/NAV_RELATION_SHARD_O2_BATCH_04_V0_1.json").read_text())
T=json.loads((B/"NAV_O2_RELATION_TENSIONS_V0_1.json").read_text())

def main():
    bad=[]
    if len(A["assertions"])!=2:bad.append("assertion-count")
    if len(V["verifications"])!=2:bad.append("verification-count")
    if len(R["confirmed_relations"])!=2:bad.append("relation-count")
    if len(T["tensions"])!=1:bad.append("tension-count")

    for a in A["assertions"]:
        if a["base_kind"]!="DECLARES_INTERFACE_WITH":bad.append(a["assertion_id"]+":kind")
        if a["verification_state"]!="VERIFIED_WITH_LIMITS":bad.append(a["assertion_id"]+":state")
        if a.get("promotion_state")!="ELIGIBLE_FOR_BASE_RELATION_LOCAL_ONLY":bad.append(a["assertion_id"]+":promotion")
        if a["global_route_effect"]!="NONE_LOCAL_ONLY":bad.append(a["assertion_id"]+":global")

    for r in R["confirmed_relations"]:
        if r["kind"]!="DECLARES_INTERFACE_WITH":bad.append(r["id"]+":handoff-upgrade")
        if r.get("target_acceptance")!="UNKNOWN_NOT_PROVEN":bad.append(r["id"]+":target-acceptance")
        if r.get("composition_policy")!="NO_IMPLICIT_GLOBAL_ROUTE":bad.append(r["id"]+":composition")

    if any(r["source_id"]=="ELYX_REC_A0_ORCHESTRATOR" and r["target_id"]=="ELYX_REC_E0" and r["kind"]=="HANDS_OFF_TO" for r in R["confirmed_relations"]):
        bad.append("A0-E0-false-handoff")

    t=T["tensions"][0]
    if t["state"]!="OPEN_TEMPORAL_SCOPE_RECONCILIATION":bad.append("tension-closed")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O2 batch04 source-declared interfaces=2; target acceptance UNKNOWN; no A0->E0 handoff; tension remains open")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
