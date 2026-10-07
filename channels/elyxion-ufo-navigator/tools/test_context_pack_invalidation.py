#!/usr/bin/env python3
import copy
from build_context_pack import build_pack
from check_context_pack_staleness import evaluate_pack, policy_heads

def main():
    bad=[]
    pack=build_pack("ELYX_CHANNEL_ECO_SYSTEMS",1,"both",True)
    fresh=evaluate_pack(pack)
    if fresh["state"]!="FRESH":bad.append("fresh-baseline")

    heads=policy_heads()
    main_changed=dict(heads);main_changed["main"]="SIMULATED_CHANGED_MAIN"
    r=evaluate_pack(pack,external_heads=main_changed)
    if r["state"]!="STALE_TARGETED":bad.append("main-change-not-stale")

    p_changed=dict(heads);p_changed["channel/p-control-point-v0.1"]="SIMULATED_CHANGED_P"
    r=evaluate_pack(pack,external_heads=p_changed)
    if r["state"]!="FRESH":bad.append("unrelated-p-change-leaked")

    self_pack=copy.deepcopy(pack)
    self_snap=next((x for x in self_pack["source_snapshot"] if x.get("tracking_mode")=="SELF_RESOLVE_AT_PACK_BUILD"),None)
    if not self_snap:bad.append("no-self-snapshot")
    else:
        self_snap["blob_sha"]="SIMULATED_OLD_SELF_BLOB"
        if evaluate_pack(self_pack)["state"]!="STALE_TARGETED":bad.append("self-blob-change-not-stale")

    author_pack=copy.deepcopy(pack)
    author_snap=next((x for x in author_pack["source_snapshot"] if x["source_type"]=="AUTHOR_DECLARATION"),None)
    if not author_snap:bad.append("no-author-snapshot")
    else:
        author_snap["registry_blob_sha"]="SIMULATED_OLD_AUTHOR_BLOB"
        if evaluate_pack(author_pack)["state"]!="STALE_TARGETED":bad.append("author-change-not-stale")

    if bad:
        [print("FAIL:",x) for x in bad];return 1
    print("PASS: targeted context-pack invalidation cases.")
    return 0
if __name__=="__main__":raise SystemExit(main())
