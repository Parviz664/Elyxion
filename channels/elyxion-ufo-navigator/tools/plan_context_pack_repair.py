#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path
from nav_catalog import load_evidence

B=Path(__file__).resolve().parents[1]
REPO=B.parents[1]
INDEX=load_evidence()
CLAIMS=json.loads((B/"NAV_CLAIM_INDEX_V0_4.json").read_text())
BY_E={x["evidence_id"]:x for x in INDEX["entries"]}
BY_C={x["claim_id"]:x for x in CLAIMS["claims"]}
AUTHOR_PATH=REPO/"channels/elyxion-ufo-navigator/NAV_AUTHOR_DECLARATIONS_V0_1.json"

def git_hash(path):
    try:
        return subprocess.check_output(["git","hash-object",str(path)],cwd=REPO,text=True,stderr=subprocess.DEVNULL).strip()
    except Exception:
        return None

def current_identity(evidence_id):
    e=BY_E.get(evidence_id)
    if not e:
        return None
    if e["source_type"]=="AUTHOR_DECLARATION":
        return {"kind":"AUTHOR_DECLARATION","registry_blob_sha":git_hash(AUTHOR_PATH)}
    if e["tracking_mode"]=="SELF_RESOLVE_AT_PACK_BUILD":
        p=REPO/e["path"]
        return {"kind":"SELF","blob_sha":git_hash(p) if p.exists() else None}
    return {
      "kind":"EXTERNAL",
      "source_head":e.get("observed_source_head"),
      "blob_sha":e.get("observed_blob_sha")
    }

def plan_repair(pack):
    revalidated=[]
    changed=[]
    blocked=[]

    for snap in pack.get("source_snapshot",[]):
        eid=snap["evidence_id"]
        cur=current_identity(eid)
        if not cur:
            blocked.append({"evidence_id":eid,"reason":"UNKNOWN_CURRENT_IDENTITY"})
            continue

        if snap["source_type"]=="AUTHOR_DECLARATION":
            old=snap.get("registry_blob_sha"); new=cur.get("registry_blob_sha")
            if not new:
                blocked.append({"evidence_id":eid,"reason":"AUTHOR_REGISTRY_UNAVAILABLE"})
            elif old!=new:
                changed.append({"evidence_id":eid,"reason":"AUTHOR_REGISTRY_BLOB_CHANGED","old_blob":old,"new_blob":new})
            continue

        if snap.get("tracking_mode")=="SELF_RESOLVE_AT_PACK_BUILD":
            old=snap.get("blob_sha"); new=cur.get("blob_sha")
            if not new:
                blocked.append({"evidence_id":eid,"reason":"SELF_FILE_UNAVAILABLE"})
            elif old!=new:
                changed.append({"evidence_id":eid,"reason":"SELF_BLOB_CHANGED","old_blob":old,"new_blob":new})
            continue

        old_head=snap.get("source_head"); old_blob=snap.get("blob_sha")
        new_head=cur.get("source_head"); new_blob=cur.get("blob_sha")
        if not new_head or not new_blob:
            blocked.append({"evidence_id":eid,"reason":"PINNED_CURRENT_IDENTITY_INCOMPLETE"})
        elif old_head!=new_head and old_blob==new_blob:
            revalidated.append({"evidence_id":eid,"reason":"HEAD_CHANGED_BLOB_UNCHANGED","new_head":new_head})
        elif old_blob!=new_blob:
            changed.append({"evidence_id":eid,"reason":"BLOB_CHANGED","old_blob":old_blob,"new_blob":new_blob,"new_head":new_head})

    changed_ids={x["evidence_id"] for x in changed}
    affected=[]
    reuse=set()
    for claim in pack.get("claims",[]):
        cid=claim["claim_id"]
        deps=set(BY_C.get(cid,{}).get("evidence_ids",[]))
        if deps & changed_ids:
            affected.append(cid)
            reuse |= (deps-changed_ids)

    selected_claims={x["claim_id"] for x in pack.get("claims",[])}
    unaffected=sorted(selected_claims-set(affected))

    return {
      "state":"BLOCKED" if blocked else ("REPAIR_REQUIRED" if changed else "REVALIDATED_UNCHANGED"),
      "revalidated_without_semantic_recheck":revalidated,
      "rematerialize_evidence_ids":sorted(changed_ids),
      "reverify_claim_ids":sorted(affected),
      "reuse_fresh_support_evidence_ids":sorted(reuse),
      "preserve_unaffected_claim_ids":unaffected,
      "blocked":blocked,
      "global_replay_required":False,
      "new_pack_fingerprint_required":bool(revalidated or changed)
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("pack_json")
    a=p.parse_args()
    pack=json.loads(Path(a.pack_json).read_text())
    print(json.dumps(plan_repair(pack),indent=2))
if __name__=="__main__":
    main()
