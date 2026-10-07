#!/usr/bin/env python3
import json
from pathlib import Path
from build_context_pack import build_pack
B=Path(__file__).resolve().parents[1]
FX=json.loads((B/"tests/NAV_CONTEXT_PACK_EXPECTATIONS_V0_2.json").read_text())
S=lambda xs:{x["id"] for x in xs}
E=lambda xs:{x["evidence_id"] for x in xs}
C=lambda xs:{x["claim_id"] for x in xs}
def main():
  bad=[]
  for x in FX["cases"]:
    p=build_pack(x["start_id"],x["max_hops"],x["direction"],True)
    if S(p["slice"]["objects"])!=set(x["expected_object_ids"]):bad.append(x["id"]+":objects")
    if any(y in S(p["slice"]["objects"]) for y in x["forbidden_object_ids"]):bad.append(x["id"]+":leak")
    if S(p["discovery_boundary"])!=set(x["expected_discovery_ids"]):bad.append(x["id"]+":discovery")
    if C(p["claims"])!=set(x["expected_claim_ids"]):bad.append(x["id"]+":claims")
    if len(E(p["evidence_manifest"]))!=x["expected_evidence_count"]:bad.append(x["id"]+":evidence")
    if p["risk"]["band"]!=x["expected_risk_band"]:bad.append(x["id"]+":risk")
    if p["materialization_plan"]["recommended_minimum_level"]!=x["expected_materialization"]:bad.append(x["id"]+":materialization")
    if p["materialization_plan"]["default_loaded_file_bodies"]:bad.append(x["id"]+":body-leak")
  if bad:
    [print("FAIL:",x) for x in bad];return 1
  print(f"PASS: {len(FX['cases'])} claim-aware context-pack cases.")
  return 0
if __name__=="__main__": raise SystemExit(main())
