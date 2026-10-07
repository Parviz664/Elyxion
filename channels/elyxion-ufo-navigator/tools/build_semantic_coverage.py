#!/usr/bin/env python3
import json
from pathlib import Path
from nav_catalog import load_objects

B=Path(__file__).resolve().parents[1]
CLAIMS=json.loads((B/"NAV_CLAIM_INDEX_V0_2.json").read_text())

def build_semantic_coverage():
    objects=load_objects()["objects"]
    object_ids={x["id"] for x in objects}
    covered={}
    for claim in CLAIMS["claims"]:
        for ref in claim.get("subject_refs",[]):
            if ref.startswith("OBJECT:"):
                oid=ref.split(":",1)[1]
                if oid in object_ids:
                    covered.setdefault(oid,[]).append(claim["claim_id"])

    rows=[]
    for o in sorted(objects,key=lambda x:x["id"]):
        cids=sorted(set(covered.get(o["id"],[])))
        rows.append({
          "object_id":o["id"],
          "normalized_claim_coverage":"PRESENT" if cids else "ABSENT",
          "claim_ids":cids,
          "identity_evidence_state":o.get("evidence_state","UNKNOWN")
        })

    n=len(rows); k=sum(1 for x in rows if x["normalized_claim_coverage"]=="PRESENT")
    return {
      "snapshot_version":"0.1",
      "project_scope":"ELYXION",
      "metric":"NORMALIZED_OBJECT_CLAIM_COVERAGE",
      "objects_total":n,
      "objects_with_normalized_claims":k,
      "coverage_ratio":k/n if n else 1.0,
      "objects_without_normalized_claims":n-k,
      "rows":rows,
      "interpretation":{
        "coverage_is_semantic_indexing_not_truth_completeness":True,
        "identity_artifact_without_claim_is_not_counted_as_normalized_semantic_coverage":True,
        "absence_of_claim_does_not_mean_object_has_no_meaning":True,
        "global_semantic_completeness_not_proven":True
      }
    }

if __name__=="__main__":
    print(json.dumps(build_semantic_coverage(),indent=2,ensure_ascii=False))
