# CHANNEL_VERSION_LINEAGE

## Lineage summary

PRE_V1_0_CREATION_SEED
-> v1.0
-> v1.1
-> v1.2
-> v1.3
-> v1.4
-> v1.4.1 ASSISTANT_PROPOSAL_ONLY

## PRE_V1_0_CREATION_SEED

recovery_status:
PARTIALLY_RECOVERED.

evidence:
user raw “хорошо сделай этот Е3.5” at 2026-02-18T10:16:05Z;
assistant channel creation output at 10:16:08Z.

content ceiling:
the exact first contract body before v1.0 is not recovered.

## v1.0

exact_version:
1.0.0.

recovery_status:
EXACT_VERSION_RECOVERED from current-chat user-supplied artifact.

artifact_type:
ELYX_E3_5_INPUT_ASSEMBLER_AND_COVERAGE_PROOF_V1_0.

major traits:
assembler template;
SIM-only lane;
10 required sources;
waiver-capable partial path;
no-drop proof;
no mutation;
no runtime claims.

status in artifact:
DRAFT_READY_FOR_USE.

historical status:
SUPERSEDED by v1.1.

## v1.1

exact_version:
1.1.0.

recovery_status:
EXACT_VERSION_RECOVERED.

artifact_type:
ELYX_E3_5_INPUT_ASSEMBLER_AND_COVERAGE_PROOF_V1_1.

delta:
REF_ONLY_STRICT;
no reserialization;
no source content aggregation;
no-shadow guard;
exact E4 contract/type matching;
deterministic pass/block rules.

historical status:
SUPERSEDED by v1.2.

## v1.2

exact_version:
1.2.0.

recovery_status:
EXACT_VERSION_RECOVERED.

artifact_type:
ELYX_E3_5_INPUT_ASSEMBLER_AND_COVERAGE_PROOF_V1_2.

delta:
guarantee_scope;
contract_sync_guard;
strict ref integrity proof;
E4 missing-input BLOCK-class elimination map.

historical status:
SUPERSEDED by v1.3.

## v1.3

exact_version:
1.3.0.

recovery_status:
EXACT_VERSION_RECOVERED.

artifact_type:
ELYX_E3_5_CHANNEL_SPEC_V1_3_MASTER.

delta:
second lane variant LANE_V2_BOOTSTRAP_DUAL_ROOT_REF_ONLY;
two roots may coexist but never merge;
root_binding per required ref;
dual-root integrity proof.

reason_explicit:
yes — the supplied artifact says v1.3 adds BOOTSTRAP_LIMITED dual-root support without permitting merge and keeps SIM lane unchanged/default.

historical status:
SUPERSEDED by v1.4.

## v1.4

exact_version:
1.4.0.

recovery_status:
EXACT_VERSION_RECOVERED.

artifact_type:
ELYX_E3_5_CHANNEL_SPEC_V1_4_MASTER.

delta:
registry/seal presence proof;
anti-injection;
deterministic hash fields;
MIN_VERSION_SAME_MAJOR;
E4_REQUIRED_SOURCES_CONTRACT_V1_1;
bundle packet V1_1.

status in artifact:
DRAFT_READY_FOR_USE.

current historical status:
LATEST USER-SUPPLIED WORKING SPEC RECOVERED.

canon caveat:
user supply does not itself prove OWNER_AUTHORED or global CANON acceptance.

## v1.4.1

recovery_status:
REFERRED_TO_ONLY AS ASSISTANT PROPOSAL.

origin:
assistant spec review after v1.4.

proposed changes:
environment-mode wording;
minimum type compatibility;
template lane-selection clarity;
deterministic-only guarantee wording.

owner acceptance:
UNKNOWN / not recovered.

status:
NOT CANONIZED.
Do not present as active E3.5 version.
