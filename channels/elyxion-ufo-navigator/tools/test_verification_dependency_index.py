#!/usr/bin/env python3
import json
from pathlib import Path
from build_verification_dependency_index import build_index

B=Path(__file__).resolve().parents[1]

def main():
    expected=json.loads((B/"NAV_VERIFICATION_DEPENDENCY_INDEX_V0_3.json").read_text())
    actual=build_index()
    if actual!=expected:
        print("FAIL: derived verification dependency index drift")
        return 1

    if set(actual["evidence_to_claims"]["EVID_EPRIME_LOCK"]) != {
        "CLAIM_EPRIME_CHAT_TRANSCRIPTS_ONLY",
        "CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN"
    }:
        print("FAIL: E-Prime reverse dependency")
        return 1

    if set(actual["evidence_to_claims"]["EVID_AUTHOR_GLOBAL_C0_EXISTS"]) != {
        "CLAIM_GLOBAL_C0_EXISTS",
        "CLAIM_NAV_MUST_NOT_BUILD_GLOBAL_C0"
    }:
        print("FAIL: Global C0 author reverse dependency")
        return 1

    if set(actual["materialization_receipt_to_claims"]["MAT_ECO_SYSTEMS_M2_2026_10_07"]) != {
        "CLAIM_ECO_SYSTEMS_ROLE",
        "CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN"
    }:
        print("FAIL: Eco materialization reverse dependency")
        return 1

    print("PASS: verification dependency index matches source registries")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
