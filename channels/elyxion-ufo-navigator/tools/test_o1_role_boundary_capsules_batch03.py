#!/usr/bin/env python3
import json
from pathlib import Path
from nav_catalog import load_objects, load_evidence

B=Path(__file__).resolve().parents[1]
CAPS=json.loads((B/"NAV_O1_ROLE_BOUNDARY_CAPSULES_BATCH_03_V0_1.json").read_text())

def main():
    objects={x["id"] for x in load_objects()["objects"]}
    evidence={x["evidence_id"] for x in load_evidence()["entries"]}
    bad=[]
    cs=CAPS["capsules"]
    if len(cs)!=6:bad.append("capsule-count")
    if len({x["object_id"] for x in cs})!=6:bad.append("object-count")
    for c in cs:
        if c["object_id"] not in objects:bad.append(c["capsule_id"]+":object")
        if c["source_identity_evidence_id"] not in evidence:bad.append(c["capsule_id"]+":identity")
        if any(x not in evidence for x in c["source_boundary_evidence"]):bad.append(c["capsule_id"]+":boundary")
        if c["relation_assertions"]!=[]:bad.append(c["capsule_id"]+":relation-inference")
        if c["capsule_state"]!="VERIFIED_WITH_LIMITS":bad.append(c["capsule_id"]+":state")
        if len(c.get("materialization_receipt_ids",[]))!=2:bad.append(c["capsule_id"]+":materialization")
        if not c.get("semantic_verification_id"):bad.append(c["capsule_id"]+":verification")
    p0=next(x for x in cs if x["capsule_id"]=="O1_P0_INTENT_NORMALIZER")
    p5=next(x for x in cs if x["capsule_id"]=="O1_P5_FEEL_TRUTH")
    if p0["status_and_evidence_ceiling"]["current_global_route"]!="HOLD_UNRESOLVED":bad.append("P0-route-drift")
    if p5["status_and_evidence_ceiling"]["default_activation"]!="disabled_by_default=true":bad.append("P5-default-drift")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O1 batch03 P0-P5 verified-with-limits; route HOLD preserved; P5 disabled-by-default preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
