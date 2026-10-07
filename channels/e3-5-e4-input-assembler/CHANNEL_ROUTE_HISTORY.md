# CHANNEL_ROUTE_HISTORY

E3.5 is a fan-in channel, not a simple one-predecessor pipeline stage.

## Route family R1 — v1.0-v1.2 SIM single-root fan-in

status:
HISTORICAL, superseded in capability but still supported as a lane family.

route:

E3_SUPERIORITY_PACKET
D3_AUGMENTATION_PACKET
E2_VARIANT_PACKET
D2_ENHANCEMENT_PACKET
E1_SIM_CONSTRAINTS
D1_RELEASE_GATE_REPORT
D0_ACK_PROCESSING_RESULT
E0_DECISION_PACKET
EPRIME_SIMULATION_RESPONSE
A2_SYSTEMS_MAP
    -> E3.5
    -> E4_INTEGRATION_AND_EXECUTION_READINESS_ROUTING

lane:
BOOTSTRAP_LIMITED__SIMULATION_ONLY.

root:
single SIM trace root.

evidence:
v1.0-v1.2 supplied contracts.

## Route family R2 — E-Prime registry assisted resolution

status:
HISTORICAL/INTERFACE_ACTIVE_EVIDENCE.

route:

upstream packet producers
    -> E-Prime Packet Registry / ref resolution
    -> E3.5 manifest refs
    -> E4

evidence:
recovered E-Prime v1.2 output at 2026-02-18T10:32:56Z.

important:
E-Prime registry can help resolve refs.
It does not replace the required source packet semantics.

## Route family R3 — v1.3+ BOOTSTRAP dual-root ref-only fan-in

status:
ACTIVE in v1.3/v1.4 supplied contracts.

route:
required source refs bound individually to either
bootstrap_root
or
canon_patch_root
    -> E3.5 dual-root integrity proof
    -> E4

rule:
the two roots may coexist as refs but may not be stitched into one lineage.

evidence:
v1.3/v1.4 supplied contracts.

## Route family R4 — A2 direct export dependency

status:
ACTIVE interface evidence.

route:
A2
    -> A2_SYSTEMS_MAP_V4 / E3_5_INGEST_PROFILE_MIN_V1
    -> E3.5 RS-10
    -> E4

evidence:
user-side A2 v1.6.1 artifact recovered on 2026-02-20.

## Current strongest-known route

The current strongest recovered contract is v1.4.
It supports either:
LANE_V1_SIMULATION_ONLY
or
LANE_V2_BOOTSTRAP_DUAL_ROOT_REF_ONLY.

The run must choose exactly one lane variant.

## Route unknowns

- no recovered successful 10/10 current-lane handoff to E4;
- no recovered proof that every named producer actually emitted the v1.4 minimum packet version;
- no recovered external runtime implementation of registry/seal/type/hash validators;
- no recovered newer E4 contract that supersedes the v1.4 embedded E4_REQUIRED_SOURCES_CONTRACT_V1_1.
