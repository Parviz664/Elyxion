#!/usr/bin/env python3
import json
from pathlib import Path
from build_global_c0_handoff import build_handoff

B=Path(__file__).resolve().parents[1]
FX=json.loads((B/"tests/NAV_GLOBAL_C0_HANDOFF_EXPECTATIONS_V0_2.json").read_text())

def main():
    bad=[]
    for x in FX["cases"]:
        h=build_handoff(x["start_id"],x["max_hops"],x["direction"])
        if h["consumer_existence"]!=x["expected_consumer_existence"]:bad.append(x["id"]+":existence")
        if h["consumer_location"]!=x["expected_consumer_location"]:bad.append(x["id"]+":location")
        if h["non_authority"]["global_c0_construction_performed"]!=x["expected_build_flag"]:bad.append(x["id"]+":build")
        if h["payload_kind"]!=x["expected_payload_kind"]:bad.append(x["id"]+":payload")
        if h["freshness"]["state"]!=x["expected_freshness"]:bad.append(x["id"]+":freshness")
        if h["handoff_readiness"]!=x["expected_readiness"]:bad.append(x["id"]+":readiness")
        if not h["payload_fingerprint"]["value"]:bad.append(x["id"]+":fingerprint")
        if h["navigator_authority"]["global_c0_authority"]!="NONE":bad.append(x["id"]+":authority")

        s=h["verification_summary"]
        if s["selected_claim_count"]!=x["expected_verification_count"]:bad.append(x["id"]+":claim-count")
        if s["sufficient_claim_count"]!=x["expected_sufficient_count"]:bad.append(x["id"]+":sufficient-count")
        if s["verification_coverage"]!=x["expected_coverage"]:bad.append(x["id"]+":coverage")
        if s["critical_failure_claim_ids"]:bad.append(x["id"]+":critical-failure")

        for cv in h["claim_verifications"]:
            if cv["critical_for_handoff"] and cv["sufficiency"]["state"]!="SUFFICIENT":
                bad.append(x["id"]+":critical-insufficient:"+cv["claim_id"])

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print(f"PASS: {len(FX['cases'])} verification-aware existing-Global-C0 handoff cases.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
