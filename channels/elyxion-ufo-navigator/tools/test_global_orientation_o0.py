#!/usr/bin/env python3
from build_global_orientation_o0 import build_o0

def main():
    o=build_o0()
    bad=[]
    if o["orientation_level"]!="O0_TOPOLOGY_INDEX":bad.append("level")
    if o["topology_readiness"]!="READY_TOPOLOGY_ORIENTATION":bad.append("topology-readiness")
    if o["semantic_readiness"]!="PARTIAL_NOT_GLOBAL_SEMANTIC_COMPLETENESS":bad.append("semantic-readiness")
    if len(o["sector_capsules"])!=6:bad.append("sector-count")
    if o["topology_totals"]!={
      "branches":31,"branches_mapped":31,"objects":33,"confirmed_relations":34,
      "unresolved_relations":5,"collisions":1,"discovery_targets":6,
      "verified_o1_capsules":5,"normalized_object_claims_present":11
    }:bad.append("totals")
    if o["pressure"]["individual_evidence_identities_loaded"]!=0:bad.append("evidence-load")
    if o["pressure"]["exact_source_bodies_loaded"]!=0:bad.append("body-load")
    if o["pressure"]["full_history_replay"] is not False:bad.append("replay")
    if o["consumer_boundary"]["build_or_define_global_c0"] is not False:bad.append("global-c0-build")
    if o["consumer_boundary"]["global_c0_durable_location"]!="UNKNOWN":bad.append("global-c0-location")
    if not o["orientation_fingerprint"]["value"]:bad.append("fingerprint")
    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: O0 sectors=6 branches=31 objects=33 O1_verified=5 normalized_claim_objects=11 evidence_ids_loaded=0 bodies=0 semantic=PARTIAL")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
