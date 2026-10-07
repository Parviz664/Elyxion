#!/usr/bin/env python3
import json
from pathlib import Path

B=Path(__file__).resolve().parents[1]

def J(path):
    return json.loads((B/path).read_text())

def _unique(items,key,label):
    seen=set()
    for x in items:
        k=x[key]
        if k in seen:
            raise ValueError(f"duplicate {label}: {k}")
        seen.add(k)

def load_objects():
    cat=J("NAV_OBJECT_CATALOG_V0_1.json")
    core=J(cat["core_registry"]["path"])
    objects=list(core["objects"])
    for s in cat["shards"]:
        objects.extend(J(s["path"])["objects"])
    _unique(objects,"id","object id")
    discovery=J(cat["discovery_ledger_ref"])["targets"]
    _unique(discovery,"id","discovery id")
    return {
      "registry_id":"ELYXION_NAV_OBJECT_CATALOG_MERGED_V0_1",
      "status":"DERIVED_VIEW",
      "authority":"NAVIGATION_ONLY",
      "project_scope":"ELYXION",
      "objects":objects,
      "discovery_targets":discovery
    }

def load_relations():
    cat=J("NAV_RELATION_CATALOG_V0_1.json")
    core=J(cat["core_registry"]["path"])
    confirmed=list(core["confirmed_relations"])
    for s in cat["shards"]:
        confirmed.extend(J(s["path"])["confirmed_relations"])
    unresolved=list(core["unresolved_relations"])
    _unique(confirmed,"id","confirmed relation id")
    _unique(unresolved,"id","unresolved relation id")
    return {
      "registry_id":"ELYXION_NAV_RELATION_CATALOG_MERGED_V0_1",
      "status":"DERIVED_VIEW",
      "authority":"NAVIGATION_ONLY",
      "project_scope":"ELYXION",
      "confirmed_relations":confirmed,
      "unresolved_relations":unresolved
    }

def load_evidence():
    cat=J("NAV_EVIDENCE_CATALOG_V0_1.json")
    entries=[]
    for s in cat["indices"]:
        entries.extend(J(s["path"])["entries"])
    _unique(entries,"evidence_id","evidence id")
    locs=set()
    for x in entries:
        loc=x["locator"]
        if loc in locs:
            raise ValueError(f"duplicate evidence locator: {loc}")
        locs.add(loc)
    return {
      "index_id":"ELYXION_NAV_EVIDENCE_CATALOG_MERGED_V0_1",
      "status":"DERIVED_VIEW",
      "authority":"NAVIGATION_ONLY",
      "project_scope":"ELYXION",
      "entries":entries
    }

def load_freshness():
    cat=J("NAV_FRESHNESS_CATALOG_V0_1.json")
    core=J(cat["core_policy"]["path"])
    sources=list(core["sources"])
    dependencies=list(core["dependencies"])
    for s in cat["shards"]:
        d=J(s["path"])
        sources.extend(d["sources"])
        dependencies.extend(d["dependencies"])
    _unique(sources,"id","freshness source id")
    return {
      "policy_id":"ELYXION_NAV_FRESHNESS_CATALOG_MERGED_V0_1",
      "status":"DERIVED_VIEW",
      "authority":"NAVIGATION_ONLY",
      "project_scope":"ELYXION",
      "sources":sources,
      "dependencies":dependencies
    }

def load_all():
    return {
      "objects":load_objects(),
      "relations":load_relations(),
      "evidence":load_evidence(),
      "freshness":load_freshness()
    }

if __name__=="__main__":
    docs=load_all()
    print(json.dumps({
      "objects":len(docs["objects"]["objects"]),
      "discovery_targets":len(docs["objects"]["discovery_targets"]),
      "confirmed_relations":len(docs["relations"]["confirmed_relations"]),
      "unresolved_relations":len(docs["relations"]["unresolved_relations"]),
      "evidence_identities":len(docs["evidence"]["entries"]),
      "freshness_sources":len(docs["freshness"]["sources"]),
      "freshness_dependencies":len(docs["freshness"]["dependencies"])
    },indent=2))
