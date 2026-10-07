#!/usr/bin/env python3
import copy, json, sys
from pathlib import Path

B=Path(__file__).resolve().parents[1]
J=lambda n: json.loads((B/n).read_text())
O=J("NAV_OBJECT_REGISTRY_V0_4.json")
OS=J("NAV_OBJECT_SCHEMA_V0_4.json")
R=J("NAV_RELATION_REGISTRY_V0_3.json")
RS=J("NAV_RELATION_SCHEMA_V0_3.json")
C=J("NAV_COLLISION_REGISTRY_V0_1.json")
F=J("NAV_FRESHNESS_POLICY_V0_3.json")
E=J("NAV_EVIDENCE_INDEX_V0_1.json")
ES=J("NAV_EVIDENCE_SCHEMA_V0_1.json")
A=J("NAV_AUTHOR_DECLARATIONS_V0_1.json")
REC=J("NAV_GLOBAL_C0_RECOVERY_LADDER_V0_1.json")
NAV="channel/elyxion-ufo-navigator-v0.1"

def setp(x,p,v):
    q=p.split("."); c=x
    for k in q[:-1]: c=c[k]
    c[q[-1]]=v

def evidence_refs(x,out):
    if isinstance(x,list):
        for y in x: evidence_refs(y,out)
    elif isinstance(x,dict):
        for k,v in x.items():
            if k=="evidence" and isinstance(v,list):
                out.update(y for y in v if isinstance(y,str) and ":" in y)
            else: evidence_refs(v,out)

def validate(objects=O,relations=R,collisions=C,evidence=E):
    err=[]
    oids={x["id"] for x in objects["objects"]}
    dids={x["id"] for x in objects["discovery_targets"]}
    aids={x["id"] for x in A["declarations"]}
    auth=set(OS["baseline_authority_dimensions"])
    authstates=set(OS["authority_state_values"])
    for o in objects["objects"]:
        if set(OS["required"])-set(o): err.append(o["id"]+":required")
        if o["project_scope"]!="ELYXION": err.append(o["id"]+":scope")
        if not isinstance(o.get("declared_status_labels"),list): err.append(o["id"]+":labels")
        s=o["semantic_status"]
        if s["value"]!="UNKNOWN" and not s["evidence"]: err.append(o["id"]+":status-evidence")
        if o["readiness"]["value"]!="UNKNOWN" and not o["readiness"]["evidence"]: err.append(o["id"]+":ready-evidence")
        if auth-set(o["authority"]): err.append(o["id"]+":authority-shape")
        for d in auth:
            z=o["authority"][d]
            if z["state"] not in authstates: err.append(o["id"]+":authority-state")
            if z["state"]!="UNKNOWN" and not z["evidence"]: err.append(o["id"]+":authority-evidence")
        for z in o["additional_authority_claims"]:
            if not z.get("domain") or not z.get("scope"): err.append(o["id"]+":extra-shape")
            if z["state"]!="UNKNOWN" and not z["evidence"]: err.append(o["id"]+":extra-evidence")
        if s["value"]=="CANON":
            z=o["authority"]["canon"]
            if z["state"]!="EXPLICIT" or not z["evidence"]: err.append(o["id"]+":canon")
    for d in objects["discovery_targets"]:
        if d.get("existence_elsewhere")=="AUTHOR_DECLARED_EXISTS":
            if d.get("author_declaration_ref") not in aids: err.append(d["id"]+":author-decl")

    kinds=set(RS["relation_kinds"])
    for r in relations["confirmed_relations"]:
        if r["source_id"] not in oids or r["target_id"] not in oids: err.append(r["id"]+":endpoint")
        if r["kind"] not in kinds or r["state"]!="CONFIRMED" or r["traversal"]!="ALLOWED_AS_FACT": err.append(r["id"]+":state")
        if not r["evidence"] or r["project_scope"]!="ELYXION": err.append(r["id"]+":evidence")
    for r in relations["unresolved_relations"]:
        if r["source_id"] not in oids: err.append(r["id"]+":source")
        if r.get("target_id") and r["target_id"] not in oids: err.append(r["id"]+":target")
        if r.get("target_discovery_id") and r["target_discovery_id"] not in dids: err.append(r["id"]+":discovery")
        if r["state"]!="UNRESOLVED" or r["traversal"]!="BLOCKED_UNRESOLVED" or not r["question"] or not r["evidence"]: err.append(r["id"]+":unresolved")
        if r.get("author_declaration_ref") and r["author_declaration_ref"] not in aids: err.append(r["id"]+":author-decl")

    for c in collisions["collisions"]:
        if len(c["object_ids"])<2 or any(x not in oids for x in c["object_ids"]): err.append(c["id"]+":objects")
        if not c["evidence"] or c["auto_resolution_forbidden"] is not True: err.append(c["id"]+":guard")

    freshsrc={x["id"]:x for x in F["sources"]}
    valid={"OBJECT":oids,"RELATION":{x["id"] for x in relations["confirmed_relations"]},
           "UNRESOLVED_RELATION":{x["id"] for x in relations["unresolved_relations"]},
           "COLLISION":{x["id"] for x in collisions["collisions"]}}
    tracked={k:set() for k in valid}
    for d in F["dependencies"]:
        if d["subject_kind"] not in valid or d["subject_id"] not in valid[d["subject_kind"]]: err.append(d["subject_id"]+":fresh-subject")
        else: tracked[d["subject_kind"]].add(d["subject_id"])
        if any(x not in freshsrc for x in d["source_ids"]): err.append(d["subject_id"]+":fresh-source")
    for k in valid:
        if valid[k]-tracked[k]: err.append("fresh-missing-"+k)

    if E["object_registry_ref"]!="NAV_OBJECT_REGISTRY_V0_4.json" or E["relation_registry_ref"]!="NAV_RELATION_REGISTRY_V0_3.json": err.append("evidence-registry-ref")
    ids=set(); locs=set(); byloc={}; bydecl={}
    roles=set(ES["source_roles"]); modes=set(ES["tracking_modes"])
    for x in evidence["entries"]:
        if x["evidence_id"] in ids or x["locator"] in locs: err.append(x["evidence_id"]+":duplicate")
        ids.add(x["evidence_id"]); locs.add(x["locator"])
        if x["source_role"] not in roles or x["tracking_mode"] not in modes: err.append(x["evidence_id"]+":enum")
        if x["source_type"]=="GITHUB_FILE":
            if x["ref"]==NAV and x["tracking_mode"]!="SELF_RESOLVE_AT_PACK_BUILD": err.append(x["evidence_id"]+":self")
            if x["ref"]!=NAV and (x["tracking_mode"]!="PINNED_BLOB_AND_HEAD" or not x.get("observed_blob_sha") or not x.get("observed_source_head")): err.append(x["evidence_id"]+":pin")
            byloc[x["locator"]]=x
        else:
            if x["tracking_mode"]!="AUTHOR_DECLARATION_RECORD" or x.get("declaration_id") not in aids: err.append(x["evidence_id"]+":decl")
            bydecl[x.get("declaration_id")]=x
    req=set(); evidence_refs(objects["objects"],req); evidence_refs(relations,req); evidence_refs(collisions,req)
    for x in req:
        if x not in byloc: err.append("missing-evidence:"+x)
    for d in objects["discovery_targets"]:
        if d.get("author_declaration_ref") and d["author_declaration_ref"] not in bydecl: err.append("missing-author-evidence")
    for r in relations["unresolved_relations"]:
        if r.get("author_declaration_ref") and r["author_declaration_ref"] not in bydecl: err.append("missing-author-evidence")

    if [x["level"] for x in REC["layers"]]!=list(range(6)): err.append("recovery-levels")
    return err

def mutate(doc,case,collection=None,key="id"):
    m=copy.deepcopy(doc); mu=case["mutation"]
    if collection: t=next(x for x in m[collection] if x[key]==case["target_id"])
    elif "target_object" in mu: t=next(x for x in m["objects"] if x["id"]==mu["target_object"])
    else: t=next(x for x in m["discovery_targets"] if x["id"]==mu["target_discovery"])
    setp(t,mu["path"],mu["value"]); return m

def main():
    base=validate()
    if base:
        [print("FAIL:",x) for x in base]; return 1
    failed=[]
    for c in J("tests/NAV_OBJECT_FALSIFICATION_CASES_V0_2.json")["cases"]:
        if not validate(objects=mutate(O,c)): failed.append(c["id"])
    for c in J("tests/NAV_RELATION_FALSIFICATION_CASES_V0_1.json")["cases"]:
        if not validate(relations=mutate(R,c,c["target_collection"])): failed.append(c["id"])
    for c in J("tests/NAV_COLLISION_FALSIFICATION_CASES_V0_1.json")["cases"]:
        if not validate(collisions=mutate(C,c,"collisions")): failed.append(c["id"])
    for c in J("tests/NAV_EVIDENCE_FALSIFICATION_CASES_V0_1.json")["cases"]:
        if not validate(evidence=mutate(E,c,"entries","evidence_id")): failed.append(c["id"])
    for c in J("tests/NAV_FRESHNESS_FALSIFICATION_CASES_V0_3.json")["cases"]:
        changed=set(c["changed_sources"])
        stale={d["subject_id"] for d in F["dependencies"] if changed.intersection(d["source_ids"])}
        if any(x not in stale for x in c.get("expected_stale_subjects",[])): failed.append(c["id"])
        if any(x in stale for x in c.get("forbidden_stale_subjects",[])): failed.append(c["id"])
    if failed:
        [print("FAIL:",x) for x in failed]; return 1
    print(f"PASS: objects={len(O['objects'])} relations={len(R['confirmed_relations'])}/{len(R['unresolved_relations'])} evidence={len(E['entries'])} freshness={len(F['dependencies'])}")
    return 0

if __name__=="__main__": raise SystemExit(main())
