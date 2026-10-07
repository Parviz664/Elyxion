#!/usr/bin/env python3
import argparse, hashlib, json, subprocess
from pathlib import Path
from build_context_slice import build_slice, load_documents
from nav_catalog import load_evidence

BASE=Path(__file__).resolve().parents[1]
CLAIM_INDEX=BASE/"NAV_CLAIM_INDEX_V0_4.json"
FRESHNESS_POLICY=BASE/"NAV_FRESHNESS_CATALOG_V0_1.json"
MATERIALIZATION_POLICY=BASE/"NAV_EVIDENCE_MATERIALIZATION_POLICY_V0_1.json"
RISK_POLICY=BASE/"NAV_CONTEXT_PACK_RISK_POLICY_V0_1.json"
INVALIDATION_POLICY=BASE/"NAV_CONTEXT_PACK_INVALIDATION_POLICY_V0_1.json"
AUTHOR_REGISTRY_PATH="channels/elyxion-ufo-navigator/NAV_AUTHOR_DECLARATIONS_V0_1.json"

def git_value(*args):
    try:
        return subprocess.check_output(["git",*args],text=True,stderr=subprocess.DEVNULL).strip()
    except Exception:
        return None

def git_blob(path):
    return git_value("rev-parse",f"HEAD:{path}")

def collect_refs(v,out):
    if isinstance(v,list):
        for x in v: collect_refs(x,out)
    elif isinstance(v,dict):
        for k,x in v.items():
            if k=="evidence" and isinstance(x,list):
                out.update(y for y in x if isinstance(y,str) and ":" in y)
            else: collect_refs(x,out)

def snapshot_entry(e):
    if e["source_type"]=="AUTHOR_DECLARATION":
        return {
          "evidence_id":e["evidence_id"],
          "source_type":"AUTHOR_DECLARATION",
          "declaration_id":e["declaration_id"],
          "registry_blob_sha":git_blob(AUTHOR_REGISTRY_PATH)
        }
    if e["tracking_mode"]=="SELF_RESOLVE_AT_PACK_BUILD":
        return {
          "evidence_id":e["evidence_id"],
          "source_type":"GITHUB_FILE",
          "tracking_mode":"SELF_RESOLVE_AT_PACK_BUILD",
          "ref":e["ref"],"path":e["path"],
          "blob_sha":git_blob(e["path"])
        }
    return {
      "evidence_id":e["evidence_id"],
      "source_type":"GITHUB_FILE",
      "tracking_mode":"PINNED_BLOB_AND_HEAD",
      "ref":e["ref"],"path":e["path"],
      "source_head":e["observed_source_head"],
      "blob_sha":e["observed_blob_sha"]
    }

def build_pack(start_id,max_hops=1,direction="both",include_unresolved_boundary=True):
    objects_doc,relations_doc,collisions_doc=load_documents()
    sl=build_slice(objects_doc,relations_doc,collisions_doc,start_id,max_hops,direction,include_unresolved_boundary)
    objreg=objects_doc
    evid=load_evidence()
    claims_doc=json.loads(CLAIM_INDEX.read_text())
    disc={x["id"]:x for x in objreg["discovery_targets"]}

    discovery_ids={r["target_discovery_id"] for r in sl["unresolved_boundary"] if r.get("target_discovery_id")}
    discovery_boundary=[disc[x] for x in sorted(discovery_ids) if x in disc]

    subjects={f"OBJECT:{x['id']}" for x in sl["objects"]}
    subjects|={f"RELATION:{x['id']}" for x in sl["confirmed_relations"]}
    subjects|={f"UNRESOLVED_RELATION:{x['id']}" for x in sl["unresolved_boundary"]}
    subjects|={f"COLLISION:{x['id']}" for x in sl["collisions"]}
    subjects|={f"DISCOVERY:{x['id']}" for x in discovery_boundary}
    claims=[c for c in claims_doc["claims"] if subjects.intersection(c.get("subject_refs",[]))]

    refs=set();collect_refs(sl["objects"],refs);collect_refs(sl["confirmed_relations"],refs);collect_refs(sl["unresolved_boundary"],refs);collect_refs(sl["collisions"],refs)
    byloc={x["locator"]:x for x in evid["entries"] if x["source_type"]=="GITHUB_FILE"}
    bydecl={x["declaration_id"]:x for x in evid["entries"] if x["source_type"]=="AUTHOR_DECLARATION"}
    byid={x["evidence_id"]:x for x in evid["entries"]}

    missing=[x for x in refs if x not in byloc]
    decls={x.get("author_declaration_ref") for x in discovery_boundary if x.get("author_declaration_ref")}
    decls|={x.get("author_declaration_ref") for x in sl["unresolved_boundary"] if x.get("author_declaration_ref")}
    missing_decl=[x for x in decls if x not in bydecl]

    evidence_ids={byloc[x]["evidence_id"] for x in refs if x in byloc}
    evidence_ids|={bydecl[x]["evidence_id"] for x in decls if x in bydecl}
    for claim in claims:
        for eid in claim.get("evidence_ids",[]):
            if eid not in byid: missing.append("claim-evidence:"+eid)
            else: evidence_ids.add(eid)

    if missing or missing_decl:
        raise ValueError(json.dumps({"missing":sorted(missing),"missing_declarations":sorted(missing_decl)}))

    if sl["collisions"]:
        risk_band="HIGH"; materialization="M2_CONFLICT_SET"
    elif sl["unresolved_boundary"] or any(c["epistemic_state"]=="AUTHOR_DECLARED" for c in claims):
        risk_band="ELEVATED"; materialization="M1_EXACT_ARTIFACT"
    else:
        risk_band="LOW"; materialization="M0_MANIFEST_ONLY"

    manifest=[byid[x] for x in sorted(evidence_ids)]
    snapshots=[snapshot_entry(x) for x in manifest]
    fingerprint_payload={
      "objects":sorted(x["id"] for x in sl["objects"]),
      "relations":sorted(x["id"] for x in sl["confirmed_relations"]),
      "unresolved":sorted(x["id"] for x in sl["unresolved_boundary"]),
      "collisions":sorted(x["id"] for x in sl["collisions"]),
      "claims":sorted(x["claim_id"] for x in claims),
      "evidence":sorted(x["evidence_id"] for x in manifest),
      "source_snapshot":sorted(snapshots,key=lambda x:x["evidence_id"])
    }
    fingerprint=hashlib.sha256(json.dumps(fingerprint_payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()

    return {
      "pack_version":"0.4","project_scope":"ELYXION",
      "request":{"start_id":start_id,"max_hops":max_hops,"direction":direction,"include_unresolved_boundary":include_unresolved_boundary},
      "slice":{"objects":sl["objects"],"confirmed_relations":sl["confirmed_relations"]},
      "discovery_boundary":discovery_boundary,"unresolved_boundary":sl["unresolved_boundary"],"collisions":sl["collisions"],
      "claims":claims,"evidence_manifest":manifest,
      "risk":{"band":risk_band,"policy_ref":RISK_POLICY.name,
        "reason_flags":{"collision_present":bool(sl["collisions"]),"unresolved_boundary_present":bool(sl["unresolved_boundary"]),"author_declared_claim_present":any(c["epistemic_state"]=="AUTHOR_DECLARED" for c in claims)}},
      "materialization_plan":{"policy_ref":MATERIALIZATION_POLICY.name,"recommended_minimum_level":materialization,"default_loaded_file_bodies":[],"manifest_only_evidence_ids":[x["evidence_id"] for x in manifest],"exact_source_loading_is_escalation":True},
      "source_snapshot":snapshots,
      "pack_fingerprint":{"algorithm":"SHA-256","value":fingerprint,"policy_ref":INVALIDATION_POLICY.name},
      "freshness_contract":{"policy_ref":FRESHNESS_POLICY.name,"invalidation_policy_ref":INVALIDATION_POLICY.name,"must_check_before_high_confidence_use":True,"stale_means_targeted_recovery_not_global_replay":True},
      "budget":{"selected_object_count":len(sl["objects"]),"total_known_object_count":len(objreg["objects"]),"selected_claim_count":len(claims),"total_indexed_claim_count":len(claims_doc["claims"]),"selected_evidence_count":len(manifest),"total_indexed_evidence_count":len(evid["entries"])},
      "laws":{"pack_is_bounded_not_complete_world":True,"claims_are_evidence_linked":True,"unresolved_relations_not_traversed":True,"collisions_not_auto_resolved":True,"file_bodies_not_loaded_by_default":True,"existing_global_c0_not_built_by_pack":True,"fingerprint_is_not_semantic_truth":True}
    }

def main():
    p=argparse.ArgumentParser();p.add_argument("start_id");p.add_argument("--max-hops",type=int,default=1);p.add_argument("--direction",choices=["outgoing","incoming","both"],default="both");p.add_argument("--exclude-unresolved-boundary",action="store_true");a=p.parse_args()
    try:r=build_pack(a.start_id,a.max_hops,a.direction,not a.exclude_unresolved_boundary)
    except ValueError as e:raise SystemExit(str(e))
    print(json.dumps(r,indent=2,ensure_ascii=False))
if __name__=="__main__":main()
