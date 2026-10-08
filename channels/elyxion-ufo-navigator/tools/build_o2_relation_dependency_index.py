#!/usr/bin/env python3
import json
from pathlib import Path

B=Path(__file__).resolve().parents[1]

def J(p): return json.loads((B/p).read_text())

def build():
    A=J("NAV_O2_RELATION_ASSERTIONS_BATCH_01_V0_1.json")["assertions"]
    V=J("NAV_O2_RELATION_VERIFICATION_RECEIPTS_V0_1.json")["verifications"]
    R=J("relations/NAV_RELATION_SHARD_O2_BATCH_01_V0_1.json")["confirmed_relations"]

    by_assertion_v={x["assertion_id"]:x for x in V}
    by_verification_relation={x["o2_verification_id"]:x for x in R}

    a2e={}; a2m={}; a2v={}; a2r={}; e2a={}
    for a in A:
        aid=a["assertion_id"]
        a2e[aid]=sorted(set(a["evidence_ids"]))
        a2m[aid]=sorted(set(a["materialization_receipt_ids"]))
        v=by_assertion_v[aid]
        a2v[aid]=v["verification_id"]
        rel=by_verification_relation.get(v["verification_id"])
        a2r[aid]=rel["id"] if rel else None
        for eid in a2e[aid]:
            e2a.setdefault(eid,[]).append(aid)

    for eid in e2a:e2a[eid]=sorted(set(e2a[eid]))

    return {
      "index_id":"ELYXION_NAV_O2_RELATION_DEPENDENCY_INDEX_V0_1",
      "status":"DERIVED_CACHE",
      "authority":"NAVIGATION_ONLY",
      "project_scope":"ELYXION",
      "source_refs":{
        "assertions":"NAV_O2_RELATION_ASSERTIONS_BATCH_01_V0_1.json",
        "verifications":"NAV_O2_RELATION_VERIFICATION_RECEIPTS_V0_1.json",
        "promoted_relations":"relations/NAV_RELATION_SHARD_O2_BATCH_01_V0_1.json"
      },
      "assertion_to_evidence":a2e,
      "assertion_to_materialization_receipts":a2m,
      "assertion_to_verification":a2v,
      "assertion_to_promoted_relation":a2r,
      "evidence_to_assertions":e2a,
      "laws":{
        "derived_cache_is_not_authority":True,
        "changed_evidence_must_invalidate_only_dependent_assertions":True,
        "conditional_assertion_has_no_promoted_relation":True,
        "promoted_relation_must_not_survive_failed_reverification":True,
        "repair_does_not_expand_relation_scope":True
      }
    }

if __name__=="__main__":
    print(json.dumps(build(),indent=2,ensure_ascii=False))
