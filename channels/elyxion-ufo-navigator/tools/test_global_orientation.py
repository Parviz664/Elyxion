#!/usr/bin/env python3
from build_global_orientation import build_global_orientation

def main():
    o=build_global_orientation()
    bad=[]

    if o["readiness"]!="READY_TOPOLOGY_ORIENTATION":bad.append("readiness")
    if o["topology_readiness"]!="READY_TOPOLOGY_ORIENTATION":bad.append("topology-readiness")
    if o["semantic_readiness"]!="READY_NORMALIZED_SEMANTIC_COVERAGE":bad.append("semantic-readiness")
    if o["relation_authority_readiness"]!="PARTIAL_VERIFIED_LOCAL_RELATIONS":bad.append("relation-readiness")
    if o["freshness"]["state"]!="FRESH":bad.append("freshness")

    cov=o["coverage"]
    if cov["branch_inventory_mapping"]!={"represented":31,"total":31,"ratio":1.0,"observed_unmapped":0}:bad.append("branch-mapping")
    if cov["observed_objects"]!={"selected":33,"total":33,"ratio":1.0}:bad.append("objects")
    if cov["discovery_horizon"]!={"selected":6,"total":6,"ratio":1.0}:bad.append("discovery")
    if cov["selected_claim_verification"]!={"sufficient":36,"selected":36,"ratio":1.0}:bad.append("claims")
    if cov["normalized_object_claim_coverage"]!={"covered":33,"total":33,"ratio":1.0,"uncovered":0}:bad.append("semantic-coverage")
    if cov["evidence_identity"]["selected"]!=68 or cov["evidence_identity"]["total"]!=72:bad.append("evidence")
    if cov["verified_o2_relations"]!={"local_promoted":23,"conditional_verified":1,"historical_verified":1,"open_tensions":1,"known_total_relation_universe":"UNKNOWN"}:bad.append("o2-relations")

    h=o["ambient_discovery_horizon"]
    connected={x["id"] for x in h if x["visibility"]=="CONNECTED_BOUNDARY"}
    observed={x["id"] for x in h if x["visibility"]=="AMBIENT_OBSERVED"}
    ambient={x["id"] for x in h if x["visibility"]=="AMBIENT_REGISTERED_UNKNOWN"}
    if connected!={"DISCOVERY_E_CHANNELS_BEYOND_E_PRIME","DISCOVERY_GLOBAL_C0"}:bad.append("connected-horizon")
    if observed!={"DISCOVERY_A_CHANNEL"}:bad.append("observed-horizon")
    if ambient!={"DISCOVERY_RAW_0_0_1_0_TO_0_0_1_4","DISCOVERY_TOOLS_UNDER_ELYXION","DISCOVERY_DREAM_RAW_SURFACE"}:bad.append("ambient-horizon")

    if len(o["bounded_pack"]["slice"]["objects"])!=33:bad.append("pack-objects")
    if len(o["bounded_pack"]["slice"]["confirmed_relations"])!=57:bad.append("relations")
    if len(o["bounded_pack"]["unresolved_boundary"])!=5:bad.append("unresolved")
    if len(o["bounded_pack"]["collisions"])!=1:bad.append("collision")
    if o["pressure"]["default_loaded_file_bodies"]!=0:bad.append("body-load")
    if o["laws"]["full_history_replay_default"] is not False:bad.append("global-replay")
    if o["laws"]["global_c0_construction_performed"] is not False:bad.append("global-c0-build")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: topology=READY branches=31/31 objects=33/33 discovery=6/6; indexed claims=36/36; normalized semantic objects=33/33 READY; O2 local=23 conditional=1 historical=1 tensions=1 PARTIAL; evidence=68/72 bodies=0")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
