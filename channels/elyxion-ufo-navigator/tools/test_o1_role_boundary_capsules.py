#!/usr/bin/env python3
import json
from pathlib import Path
from nav_catalog import load_objects, load_evidence

B=Path(__file__).resolve().parents[1]
CAPS=json.loads((B/"NAV_O1_ROLE_BOUNDARY_CAPSULES_BATCH_01_V0_1.json").read_text())

def main():
    objects={x["id"] for x in load_objects()["objects"]}
    evidence={x["evidence_id"] for x in load_evidence()["entries"]}
    bad=[]
    capsules=CAPS["capsules"]

    if len(capsules)!=5:bad.append("capsule-count")
    if len({x["capsule_id"] for x in capsules})!=len(capsules):bad.append("duplicate-capsule")
    if len({x["object_id"] for x in capsules})!=len(capsules):bad.append("duplicate-object")

    for c in capsules:
        if c["object_id"] not in objects:bad.append(c["capsule_id"]+":object")
        if c["source_identity_evidence_id"] not in evidence:bad.append(c["capsule_id"]+":identity-evidence")
        for eid in c["source_boundary_evidence"]:
            if eid not in evidence:bad.append(c["capsule_id"]+":boundary-evidence")
        if c["relation_assertions"]!=[]:bad.append(c["capsule_id"]+":relation-inference")
        if c["capsule_state"]!="VERIFIED_WITH_LIMITS":bad.append(c["capsule_id"]+":state")
        if len(c.get("materialization_receipt_ids",[]))!=2:bad.append(c["capsule_id"]+":materialization-receipts")
        if not c.get("semantic_verification_id"):bad.append(c["capsule_id"]+":verification")
        if not c["documented_non_authorities"]:bad.append(c["capsule_id"]+":non-authority")
        if not c["unknowns"]:bad.append(c["capsule_id"]+":unknowns")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O1 batch01 capsules=5 source-bound relation-assertions=0 state=VERIFIED_WITH_LIMITS")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
