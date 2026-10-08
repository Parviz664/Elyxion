#!/usr/bin/env python3
import argparse, json
from pathlib import Path

B=Path(__file__).resolve().parents[1]
CLAIMS=json.loads((B/"NAV_CLAIM_INDEX_V0_7.json").read_text())
MATS=json.loads((B/"NAV_MATERIALIZATION_RECEIPTS_V0_1.json").read_text())
VERS=json.loads((B/"NAV_CLAIM_VERIFICATION_RECEIPTS_V0_1.json").read_text())

by_claim={x["claim_id"]:x for x in CLAIMS["claims"]}
by_receipt={x["receipt_id"]:x for x in MATS["receipts"]}
by_verification={x["claim_id"]:x for x in VERS["verifications"]}

def evaluate_claim(claim_id):
    claim=by_claim.get(claim_id)
    if not claim:
        return {"claim_id":claim_id,"state":"UNKNOWN_CLAIM"}
    verification=by_verification.get(claim_id)
    if not verification:
        return {"claim_id":claim_id,"state":"NOT_VERIFIED","epistemic_state":claim["epistemic_state"]}

    receipts=[]
    for rid in verification.get("materialization_receipt_ids",[]):
        r=by_receipt.get(rid)
        if not r:
            return {"claim_id":claim_id,"state":"INSUFFICIENT_EVIDENCE","reason":f"missing receipt {rid}"}
        receipts.append(r)

    if any(r.get("result")!="MATERIALIZED" or r.get("integrity")!="MATCH" for r in receipts):
        return {"claim_id":claim_id,"state":"INSUFFICIENT_EVIDENCE","reason":"receipt not integrity-matched materialization"}

    if claim["epistemic_state"]=="AUTHOR_DECLARED":
        has_author=any(r.get("source_identity",{}).get("source_kind")=="CURRENT_AUTHOR_DECLARATION" for r in receipts)
        if not has_author:
            return {"claim_id":claim_id,"state":"INSUFFICIENT_EVIDENCE","reason":"missing author declaration receipt"}
        if verification.get("verdict")!="SUPPORTED_AT_DECLARED_LEVEL":
            return {"claim_id":claim_id,"state":"INVALID_VERDICT","reason":"author claim promoted beyond declared level"}
        return {"claim_id":claim_id,"state":"SUFFICIENT","maximum_verdict":"SUPPORTED_AT_DECLARED_LEVEL"}

    if claim["claim_class"]=="COLLISION":
        sides={r.get("source_identity",{}).get("ref") for r in receipts}
        if len(sides)<2:
            return {"claim_id":claim_id,"state":"INSUFFICIENT_EVIDENCE","reason":"one-sided collision evidence"}
        if verification.get("verdict") not in {"SUPPORTED_WITH_LIMITS","CONTRADICTED"}:
            return {"claim_id":claim_id,"state":"INSUFFICIENT_EVIDENCE","reason":"collision lacks bounded semantic verdict"}
        return {"claim_id":claim_id,"state":"SUFFICIENT","maximum_verdict":verification["verdict"]}

    return {
        "claim_id":claim_id,
        "state":"SUFFICIENT",
        "maximum_verdict":verification.get("verdict")
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--claim-id")
    a=p.parse_args()
    if a.claim_id:
        print(json.dumps(evaluate_claim(a.claim_id),indent=2))
        return 0 if evaluate_claim(a.claim_id)["state"]=="SUFFICIENT" else 1
    results=[evaluate_claim(x["claim_id"]) for x in CLAIMS["claims"]]
    print(json.dumps(results,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
