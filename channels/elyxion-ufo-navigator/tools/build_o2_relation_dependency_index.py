#!/usr/bin/env python3
import json
from pathlib import Path

B=Path(__file__).resolve().parents[1]
def J(p): return json.loads((B/p).read_text())

ASSERTION_FILES=[
  "NAV_O2_RELATION_ASSERTIONS_BATCH_01_V0_1.json",
  "NAV_O2_RELATION_ASSERTIONS_BATCH_02_V0_1.json",
  "NAV_O2_RELATION_ASSERTIONS_BATCH_03_V0_1.json"
]
VERIFICATION_FILES=[
  "NAV_O2_RELATION_VERIFICATION_RECEIPTS_V0_1.json",
  "NAV_O2_RELATION_VERIFICATION_RECEIPTS_BATCH_02_V0_1.json",
  "NAV_O2_RELATION_VERIFICATION_RECEIPTS_BATCH_03_V0_1.json"
]
RELATION_FILES=[
  "relations/NAV_RELATION_SHARD_O2_BATCH_01_V0_1.json",
  "relations/NAV_RELATION_SHARD_O2_BATCH_02_V0_1.json",
  "relations/NAV_RELATION_SHARD_O2_BATCH_03_V0_1.json"
]

def build():
    assertions=[]
    for p in ASSERTION_FILES: assertions.extend(J(p)["assertions"])
    verifications=[]
    for p in VERIFICATION_FILES: verifications.extend(J(p)["verifications"])
    relations=[]
    for p in RELATION_FILES: relations.extend(J(p)["confirmed_relations"])
    by_v={x["assertion_id"]:x for x in verifications}
    by_rel_v={x["o2_verification_id"]:x for x in relations}
    a2e={};a2m={};a2v={};a2r={};e2a={}
    for a in assertions:
        aid=a["assertion_id"]
        a2e[aid]=list(dict.fromkeys(a["evidence_ids"]))
        a2m[aid]=list(dict.fromkeys(a["materialization_receipt_ids"]))
        v=by_v.get(aid)
        a2v[aid]=v["verification_id"] if v else None
        rel=by_rel_v.get(v["verification_id"]) if v else None
        a2r[aid]=rel["id"] if rel else None
        for eid in a2e[aid]: e2a.setdefault(eid,[]).append(aid)
    for eid in e2a:e2a[eid]=sorted(set(e2a[eid]))
    return {
      "index_id":"ELYXION_NAV_O2_RELATION_DEPENDENCY_INDEX_V0_3",
      "status":"DERIVED_CACHE","authority":"NAVIGATION_ONLY","project_scope":"ELYXION",
      "supersedes_candidate":"ELYXION_NAV_O2_RELATION_DEPENDENCY_INDEX_V0_3",
      "source_refs":{"assertion_batches":ASSERTION_FILES,"verification_batches":VERIFICATION_FILES,"promoted_relation_shards":RELATION_FILES},
      "assertion_to_evidence":a2e,
      "assertion_to_materialization_receipts":a2m,
      "assertion_to_verification":a2v,
      "assertion_to_promoted_relation":a2r,
      "evidence_to_assertions":e2a,
      "laws":{
        "derived_cache_is_not_authority":True,
        "changed_evidence_must_invalidate_only_dependent_assertions":True,
        "conditional_assertion_has_no_promoted_relation":True,
        "historical_assertion_has_no_current_promoted_relation":True,
        "promoted_relation_must_not_survive_failed_reverification":True,
        "repair_does_not_expand_relation_scope":True,
        "cross_batch_dependency_regeneration_is_required":True
      }
    }

if __name__=="__main__": print(json.dumps(build(),indent=2,ensure_ascii=False))
