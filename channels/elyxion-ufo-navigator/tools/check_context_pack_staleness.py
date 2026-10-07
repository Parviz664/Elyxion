#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path
from nav_catalog import load_freshness

BASE=Path(__file__).resolve().parents[1]
AUTHOR_PATH="channels/elyxion-ufo-navigator/NAV_AUTHOR_DECLARATIONS_V0_1.json"

def git_blob(path):
    try:return subprocess.check_output(["git","rev-parse",f"HEAD:{path}"],text=True,stderr=subprocess.DEVNULL).strip()
    except Exception:return None

def policy_heads():
    p=load_freshness()
    return {x["ref"]:x.get("observed_head") for x in p["sources"] if x["tracking_mode"]=="PINNED_OBSERVED_HEAD"}

def evaluate_pack(pack,external_heads=None,blob_resolver=git_blob):
    heads=external_heads or policy_heads()
    stale=[];unknown=[]
    for s in pack.get("source_snapshot",[]):
        eid=s["evidence_id"]
        if s["source_type"]=="AUTHOR_DECLARATION":
            cur=blob_resolver(AUTHOR_PATH)
            if not cur or not s.get("registry_blob_sha"):unknown.append(eid)
            elif cur!=s["registry_blob_sha"]:stale.append(eid)
        elif s.get("tracking_mode")=="SELF_RESOLVE_AT_PACK_BUILD":
            cur=blob_resolver(s["path"])
            if not cur or not s.get("blob_sha"):unknown.append(eid)
            elif cur!=s["blob_sha"]:stale.append(eid)
        else:
            cur=heads.get(s.get("ref"))
            if not cur:unknown.append(eid)
            elif cur!=s.get("source_head"):stale.append(eid)
    state="STALE_TARGETED" if stale else ("UNKNOWN_FRESHNESS" if unknown else "FRESH")
    return {"state":state,"stale_evidence_ids":sorted(set(stale)),"unknown_evidence_ids":sorted(set(unknown)),"global_rebuild_required":False}

def main():
    p=argparse.ArgumentParser();p.add_argument("pack_json");a=p.parse_args()
    pack=json.loads(Path(a.pack_json).read_text())
    print(json.dumps(evaluate_pack(pack),indent=2))
if __name__=="__main__":main()
