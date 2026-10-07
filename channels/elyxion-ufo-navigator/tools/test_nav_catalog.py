#!/usr/bin/env python3
import json
from pathlib import Path
from nav_catalog import load_all

B=Path(__file__).resolve().parents[1]

def main():
    d=load_all()
    inv=json.loads((B/"NAV_REPOSITORY_BRANCH_INVENTORY_V0_4.json").read_text())
    bad=[]

    counts={
      "objects":len(d["objects"]["objects"]),
      "discovery":len(d["objects"]["discovery_targets"]),
      "confirmed":len(d["relations"]["confirmed_relations"]),
      "unresolved":len(d["relations"]["unresolved_relations"]),
      "evidence":len(d["evidence"]["entries"]),
      "fresh_sources":len(d["freshness"]["sources"]),
      "fresh_dependencies":len(d["freshness"]["dependencies"])
    }
    expected={"objects":33,"discovery":6,"confirmed":34,"unresolved":5,"evidence":67,"fresh_sources":31,"fresh_dependencies":73}
    if counts!=expected:bad.append(f"counts:{counts}")

    if inv["counts"]!={"represented_in_object_catalog":31,"observed_unmapped":0,"total":31}:
        bad.append("branch-inventory")

    ids=[x["id"] for x in d["objects"]["objects"]]
    if len(ids)!=len(set(ids)):bad.append("duplicate-object")
    rids=[x["id"] for x in d["relations"]["confirmed_relations"]]
    if len(rids)!=len(set(rids)):bad.append("duplicate-relation")
    eids=[x["evidence_id"] for x in d["evidence"]["entries"]]
    if len(eids)!=len(set(eids)):bad.append("duplicate-evidence")
    locs=[x["locator"] for x in d["evidence"]["entries"]]
    if len(locs)!=len(set(locs)):bad.append("duplicate-locator")

    oids=set(ids)
    for r in d["relations"]["confirmed_relations"]:
        if r["source_id"] not in oids or r["target_id"] not in oids:
            bad.append("relation-endpoint:"+r["id"])

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: catalogs objects=33 discovery=6 relations=34/5 evidence=67 freshness=31/73 branches=31/31")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
