#!/usr/bin/env python3
import json
from pathlib import Path
from nav_catalog import load_objects, load_evidence

B=Path(__file__).resolve().parents[1]
CAPS=json.loads((B/"NAV_O1_ROLE_BOUNDARY_CAPSULES_BATCH_06_V0_1.json").read_text())

def main():
    objects={x["id"] for x in load_objects()["objects"]}
    evidence={x["evidence_id"] for x in load_evidence()["entries"]}
    bad=[]
    cs=CAPS["capsules"]
    if len(cs)!=1:bad.append("capsule-count")
    c=cs[0]
    if c["capsule_id"]!="O1_MAIN_REPOSITORY_SURFACE":bad.append("capsule-id")
    if c["object_id"]!="ELYX_SURFACE_MAIN" or c["object_id"] not in objects:bad.append("object")
    if c["source_identity_evidence_id"]!="EVID_MAIN_README" or c["source_identity_evidence_id"] not in evidence:bad.append("identity")
    if c["source_boundary_evidence"]!=["EVID_MAIN_README"]:bad.append("boundary")
    if c["relation_assertions"]!=[]:bad.append("relation-inference")
    if c["capsule_state"]!="VERIFIED_WITH_LIMITS":bad.append("state")
    if c.get("materialization_receipt_ids")!=["MAT_O1_MAIN_README_M1_2026_10_08"]:bad.append("materialization")
    if c.get("semantic_verification_id")!="VERIFY_O1_MAIN_REPOSITORY_SURFACE_ROLE_BOUNDARY_2026_10_08":bad.append("verification")
    if c["status_and_evidence_ceiling"]["authority_dimensions"]!="UNKNOWN_UNLESS_SEPARATELY_EVIDENCED":bad.append("authority-drift")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O1 batch06 main verified-with-limits; repository containment grants no authority")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
