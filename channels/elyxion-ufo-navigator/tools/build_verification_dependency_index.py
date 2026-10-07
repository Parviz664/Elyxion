#!/usr/bin/env python3
import json
from pathlib import Path
from nav_catalog import load_evidence

B=Path(__file__).resolve().parents[1]

def build_index():
    E=load_evidence()
    C=json.loads((B/"NAV_CLAIM_INDEX_V0_5.json").read_text())
    M=json.loads((B/"NAV_MATERIALIZATION_RECEIPTS_V0_1.json").read_text())
    V=json.loads((B/"NAV_CLAIM_VERIFICATION_RECEIPTS_V0_1.json").read_text())

    e2c={x["evidence_id"]:[] for x in E["entries"]}
    e2m={x["evidence_id"]:[] for x in E["entries"]}
    c2e={}
    c2v={}
    m2c={x["receipt_id"]:[] for x in M["receipts"]}

    for c in C["claims"]:
        c2e[c["claim_id"]]=sorted(set(c["evidence_ids"]))
        c2v[c["claim_id"]]=[]
        for eid in c["evidence_ids"]:
            e2c.setdefault(eid,[]).append(c["claim_id"])

    for m in M["receipts"]:
        e2m.setdefault(m["evidence_id"],[]).append(m["receipt_id"])

    for v in V["verifications"]:
        c2v.setdefault(v["claim_id"],[]).append(v["verification_id"])
        for rid in v["materialization_receipt_ids"]:
            m2c.setdefault(rid,[]).append(v["claim_id"])

    for mapping in (e2c,e2m,c2v,m2c):
        for key in mapping:
            mapping[key]=sorted(set(mapping[key]))

    return {
      "index_id":"ELYXION_NAV_VERIFICATION_DEPENDENCY_INDEX_V0_5",
      "status":"DERIVED_CACHE",
      "authority":"NAVIGATION_ONLY",
      "project_scope":"ELYXION",
      "source_refs":{
        "evidence_catalog":"NAV_EVIDENCE_CATALOG_V0_1.json",
        "claim_index":"NAV_CLAIM_INDEX_V0_5.json",
        "materialization_receipts":"NAV_MATERIALIZATION_RECEIPTS_V0_1.json",
        "verification_receipts":"NAV_CLAIM_VERIFICATION_RECEIPTS_V0_1.json"
      },
      "evidence_to_claims":e2c,
      "claim_to_evidence":c2e,
      "evidence_to_materialization_receipts":e2m,
      "claim_to_verification_receipts":c2v,
      "materialization_receipt_to_claims":m2c,
      "laws":{
        "derived_cache_is_not_authority":True,
        "regenerate_after_source_registry_change":True,
        "reverse_index_must_not_create_new_relations":True,
        "repair_scope_may_use_index_but_truth_remains_in_source_registries":True
      }
    }

if __name__=="__main__":
    print(json.dumps(build_index(),indent=2,ensure_ascii=False))
