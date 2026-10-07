#!/usr/bin/env python3
from build_global_orientation import build_global_orientation

def main():
    o=build_global_orientation()
    bad=[]

    if o["readiness"]!="BLOCKED_TOPOLOGY_EXPANSION":bad.append("readiness")
    if o["freshness"]["state"]!="FRESH":bad.append("freshness")

    cov=o["coverage"]
    if cov["branch_inventory_mapping"]!={"represented":5,"total":31,"ratio":5/31,"observed_unmapped":26}:bad.append("branch-mapping")
    if cov["observed_objects"]!={"selected":7,"total":7,"ratio":1.0}:bad.append("objects")
    if cov["discovery_horizon"]!={"selected":6,"total":6,"ratio":1.0}:bad.append("discovery")
    if cov["selected_claim_verification"]!={"sufficient":9,"selected":9,"ratio":1.0}:bad.append("claims")
    if cov["evidence_identity"]["selected"]!=16 or cov["evidence_identity"]["total"]!=20:bad.append("evidence")

    h=o["ambient_discovery_horizon"]
    connected={x["id"] for x in h if x["visibility"]=="CONNECTED_BOUNDARY"}
    ambient={x["id"] for x in h if x["visibility"]=="AMBIENT_REGISTERED_UNKNOWN"}
    if connected!={"DISCOVERY_E_CHANNELS_BEYOND_E_PRIME","DISCOVERY_GLOBAL_C0"}:bad.append("connected-horizon")
    if ambient!={"DISCOVERY_RAW_0_0_1_0_TO_0_0_1_4","DISCOVERY_A_CHANNEL","DISCOVERY_TOOLS_UNDER_ELYXION","DISCOVERY_DREAM_RAW_SURFACE"}:bad.append("ambient-horizon")

    if len(o["bounded_pack"]["unresolved_boundary"])!=5:bad.append("unresolved")
    if len(o["bounded_pack"]["collisions"])!=1:bad.append("collision")
    if o["pressure"]["default_loaded_file_bodies"]!=0:bad.append("body-load")
    if o["laws"]["full_history_replay_default"] is not False:bad.append("global-replay")
    if o["laws"]["global_c0_construction_performed"] is not False:bad.append("global-c0-build")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: topology expansion correctly blocks old 7-object orientation; branches=5/31 mapped")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
