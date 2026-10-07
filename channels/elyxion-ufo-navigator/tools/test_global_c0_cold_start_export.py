#!/usr/bin/env python3
import json
from pathlib import Path
from build_global_c0_cold_start_export import build_export

B=Path(__file__).resolve().parents[1]
FX=json.loads((B/"tests/NAV_GLOBAL_C0_COLD_START_EXPORT_EXPECTATIONS_V0_1.json").read_text())

def main():
    bad=[]
    for x in FX["cases"]:
        e=build_export(x["start_id"],x["max_hops"],x["direction"])
        if e["handoff_readiness"]!=x["expected_readiness"]:bad.append(x["id"]+":readiness")
        if len(e["verified_claims"])!=x["expected_verified_claims"]:bad.append(x["id"]+":verified")
        if len(e["unresolved_boundary_ids"])!=x["expected_unresolved"]:bad.append(x["id"]+":unresolved")
        if len(e["collision_ids"])!=x["expected_collisions"]:bad.append(x["id"]+":collisions")
        if e["consumer"]["durable_location"]!=x["expected_location"]:bad.append(x["id"]+":location")
        if e["non_duplication_boundary"]["build_global_c0"] is not False:bad.append(x["id"]+":build")
        if e["non_duplication_boundary"]["duplicate_global_c0"] is not False:bad.append(x["id"]+":duplicate")
        if e["recovery_contract"]["global_replay_default"] is not False:bad.append(x["id"]+":global-replay")
        if e["verification_summary"]["verification_coverage"]!=1.0:bad.append(x["id"]+":coverage")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print(f"PASS: {len(FX['cases'])} cold-start export cases.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
