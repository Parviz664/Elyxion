#!/usr/bin/env python3
import json
from pathlib import Path
from build_global_c0_handoff import build_handoff
B=Path(__file__).resolve().parents[1]
FX=json.loads((B/"tests/NAV_GLOBAL_C0_HANDOFF_EXPECTATIONS_V0_1.json").read_text())
def main():
    bad=[]
    for x in FX["cases"]:
        h=build_handoff(x["start_id"],x["max_hops"],x["direction"])
        if h["consumer_existence"]!=x["expected_consumer_existence"]:bad.append(x["id"]+":existence")
        if h["consumer_location"]!=x["expected_consumer_location"]:bad.append(x["id"]+":location")
        if h["non_authority"]["global_c0_construction_performed"]!=x["expected_build_flag"]:bad.append(x["id"]+":build")
        if h["payload_kind"]!=x["expected_payload_kind"]:bad.append(x["id"]+":payload")
        if h["freshness"]["state"]!=x["expected_freshness"]:bad.append(x["id"]+":freshness")
        if not h["payload_fingerprint"]["value"]:bad.append(x["id"]+":fingerprint")
        if h["navigator_authority"]["global_c0_authority"]!="NONE":bad.append(x["id"]+":authority")
    if bad:
        [print("FAIL:",x) for x in bad];return 1
    print(f"PASS: {len(FX['cases'])} existing-Global-C0 handoff cases.")
    return 0
if __name__=="__main__":raise SystemExit(main())
