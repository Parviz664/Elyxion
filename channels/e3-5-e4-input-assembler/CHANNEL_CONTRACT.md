# CHANNEL_CONTRACT

This file reconstructs the strongest-known contract without pretending all historical versions were identical.

## Current strongest-known working contract

source:
USER_SUPPLIED_ARTIFACT ELYX_E3_5_CHANNEL_SPEC_V1_4_MASTER.

status inside artifact:
DRAFT_READY_FOR_USE.

owner-authorship:
UNKNOWN.

## Core mode

Default:
REF_ONLY_STRICT.

Alternative:
PARTIAL_WITH_WAIVERS.

### REF_ONLY_STRICT

Recovered rule:
PASS only when all required refs are present and the configured type/lane/index/guard proofs pass.

Waivers:
not allowed.

Payload embedding:
not allowed.

### PARTIAL_WITH_WAIVERS

Recovered rule:
partial bundle can progress only when every missing required source is covered by an allowed signed waiver and all other applicable integrity checks pass.

Ceiling:
PASS_WITH_CONSTRAINTS.

Missing items remain unprovable to E4.

## v1.4 required keys

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

## Type policy

v1.0-v1.3 history:
exact-match orientation.

v1.4 supplied contract:
MIN_VERSION_SAME_MAJOR by default, with strict exact override available.

Important:
an assistant later argued that some v1.4 minimum versions might exceed then-seen producer versions.
That is a review finding, not an accepted contract patch.

## Lane contracts

### LANE_V1_SIMULATION_ONLY

lane_mode:
BOOTSTRAP_LIMITED__SIMULATION_ONLY.

root model:
single root.

required posture:
simulation=true;
non_canon=true;
promotion_to_canon_allowed=false;
runtime_promotion_allowed=false.

### LANE_V2_BOOTSTRAP_DUAL_ROOT_REF_ONLY

introduced:
v1.3.

lane_mode:
BOOTSTRAP_LIMITED.

root model:
bootstrap_root + canon_patch_root may coexist as refs.

hard prohibition:
no merge or cross-root stitching.

every required ref:
must declare root_binding.

## Guards

Recovered current guard families:
- no-shadow;
- contract sync;
- strict ref integrity;
- lane lock integrity;
- registry/seal presence;
- anti-injection;
- type policy validation;
- deterministic no-drop coverage.

## Handoff rule

E3.5 may hand a bundle to E4 only when its own coverage and integrity policy allows it.

This handoff means:
“inputs are assembled/provable to the E3.5 ceiling.”

It does not mean:
“E4 has passed.”

## Canon boundary

A PASS here is not a CANON promotion.
A user-supplied DRAFT_READY_FOR_USE spec is not automatically global Elyxion canon.
No recovered artifact proves E3.5 itself can promote content to canon.
