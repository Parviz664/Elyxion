#!/usr/bin/env python3
import copy, json
from pathlib import Path
from check_claim_sufficiency import evaluate_claim

B=Path(__file__).resolve().parents[1]
M=json.loads((B/"NAV_MATERIALIZATION_RECEIPTS_V0_1.json").read_text())
V=json.loads((B/"NAV_CLAIM_VERIFICATION_RECEIPTS_V0_1.json").read_text())
C=json.loads((B/"NAV_CLAIM_INDEX_V0_5.json").read_text())

def main():
    errors=[]
    receipts={x["receipt_id"]:x for x in M["receipts"]}

    for r in receipts.values():
        if r["result"]=="MATERIALIZED" and r["integrity"]!="MATCH":
            errors.append(r["receipt_id"]+":integrity")
        if r["body_handling"]["durably_duplicated"] is not False:
            errors.append(r["receipt_id"]+":body-copy")

    for v in V["verifications"]:
        if any(x not in receipts for x in v["materialization_receipt_ids"]):
            errors.append(v["verification_id"]+":missing-receipt")
        if v["claim_epistemic_state"]=="AUTHOR_DECLARED" and v["verdict"]!="SUPPORTED_AT_DECLARED_LEVEL":
            errors.append(v["verification_id"]+":epistemic-promotion")

    collision=evaluate_claim("CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN")
    author=evaluate_claim("CLAIM_GLOBAL_C0_EXISTS")
    if collision["state"]!="SUFFICIENT": errors.append("collision:not-sufficient")
    if author["state"]!="SUFFICIENT" or author.get("maximum_verdict")!="SUPPORTED_AT_DECLARED_LEVEL":
        errors.append("global-c0:bad-author-level")

    deps={x["claim_id"]:set(x["evidence_ids"]) for x in C["claims"]}
    affected=lambda stale:{cid for cid,ev in deps.items() if ev & set(stale)}
    if affected({"EVID_EPRIME_LOCK"}) != {"CLAIM_EPRIME_CHAT_TRANSCRIPTS_ONLY","CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN"}:
        errors.append("repair:eprime-lock-scope")
    if affected({"EVID_AUTHOR_GLOBAL_C0_EXISTS"}) != {"CLAIM_GLOBAL_C0_EXISTS","CLAIM_NAV_MUST_NOT_BUILD_GLOBAL_C0"}:
        errors.append("repair:author-scope")

    if errors:
        for e in errors: print("FAIL:",e)
        return 1
    print(f"PASS: receipts={len(M['receipts'])} verifications={len(V['verifications'])} sufficiency=2 repair_scopes=2")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
