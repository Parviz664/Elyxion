#!/usr/bin/env python3
import copy
from build_context_pack import build_pack
from plan_context_pack_repair import plan_repair

def snap(pack,eid):
    return next(x for x in pack["source_snapshot"] if x["evidence_id"]==eid)

def main():
    bad=[]
    base=build_pack("ELYX_CHANNEL_ECO_SYSTEMS",1,"both",True)

    head_only=copy.deepcopy(base)
    s=snap(head_only,"EVID_ECO_SYSTEMS")
    s["source_head"]="SIMULATED_OLD_HEAD"
    p=plan_repair(head_only)
    if p["state"]!="REVALIDATED_UNCHANGED" or p["reverify_claim_ids"]:
        bad.append("head-only")

    body=copy.deepcopy(base)
    s=snap(body,"EVID_ECO_SYSTEMS")
    s["source_head"]="SIMULATED_OLD_HEAD"; s["blob_sha"]="SIMULATED_OLD_BLOB"
    p=plan_repair(body)
    if p["state"]!="REPAIR_REQUIRED":bad.append("body-state")
    if p["rematerialize_evidence_ids"]!=["EVID_ECO_SYSTEMS"]:bad.append("body-rematerialize")
    expected={"CLAIM_ECO_SYSTEMS_ROLE","CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN"}
    if set(p["reverify_claim_ids"])!=expected:bad.append("body-claims")
    if "EVID_EPRIME_LOCK" not in p["reuse_fresh_support_evidence_ids"]:bad.append("collision-reuse")

    author=copy.deepcopy(base)
    s=snap(author,"EVID_AUTHOR_GLOBAL_C0_EXISTS")
    s["registry_blob_sha"]="SIMULATED_OLD_AUTHOR_BLOB"
    p=plan_repair(author)
    expected={"CLAIM_GLOBAL_C0_EXISTS","CLAIM_NAV_MUST_NOT_BUILD_GLOBAL_C0"}
    if set(p["reverify_claim_ids"])!=expected:bad.append("author-claims")
    if p["global_replay_required"] is not False:bad.append("global-replay")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: targeted pack repair planner scenarios=3")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
