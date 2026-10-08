#!/usr/bin/env python3
import json
from pathlib import Path
from nav_catalog import load_objects, load_evidence

B=Path(__file__).resolve().parents[1]
CAPS=json.loads((B/"NAV_O1_ROLE_BOUNDARY_CAPSULES_BATCH_05_V0_1.json").read_text())

def main():
    objects={x["id"] for x in load_objects()["objects"]}
    evidence={x["evidence_id"] for x in load_evidence()["entries"]}
    bad=[]
    cs=CAPS["capsules"]
    if len(cs)!=5:bad.append("capsule-count")
    for c in cs:
        if c["object_id"] not in objects:bad.append(c["capsule_id"]+":object")
        if c["source_identity_evidence_id"] not in evidence:bad.append(c["capsule_id"]+":identity")
        if any(x not in evidence for x in c["source_boundary_evidence"]):bad.append(c["capsule_id"]+":boundary")
        if c["relation_assertions"]!=[]:bad.append(c["capsule_id"]+":relation-inference")
        if c["capsule_state"]!="VERIFIED_WITH_LIMITS":bad.append(c["capsule_id"]+":state")
        if len(c.get("materialization_receipt_ids",[]))!=2:bad.append(c["capsule_id"]+":materialization")
        if not c.get("semantic_verification_id"):bad.append(c["capsule_id"]+":verification")
    d1=next(x for x in cs if x["capsule_id"]=="O1_D1")
    if d1["status_and_evidence_ceiling"]["E_channel_integration_current"]!="FORBIDDEN_IN_v2_4":bad.append("D1-E-boundary-drift")
    d2=next(x for x in cs if x["capsule_id"]=="O1_D2")
    if d2["status_and_evidence_ceiling"]["last_recovered_execution"]!="BLOCK":bad.append("D2-block-drift")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O1 batch05 D0-D4 verified-with-limits; current D-line boundaries preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
