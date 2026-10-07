# CHANNEL_PROVENANCE

## Provenance law

`SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR`.

`ASSISTANT_RATIONALE != AUTHOR_RATIONALE`.

## Source register

### P4-SRC-001
class:
RECOVERED_FROM_PRIOR_CONVERSATION / USER_SUPPLIED_ARTIFACT.

date:
2026-02-12.

content:
historical passport route with P4; role `feel_potential_sorter_final`; `ELYX_P4_INPUT_V3`; feel_goal_profile/candidate_items_ref.

strength:
HIGH for existence/role; MEDIUM for exact full v3.2.0 content.

### P4-SRC-002
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
full P4 v3.2.1 channel spec.

key identity:
`ELYX_P4_SPEC_V3_2`, semver 3.2.1.

strength:
VERY HIGH for supplied contract content.

authorship:
UNKNOWN.

### P4-SRC-003
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
P3 B001..B026 packet handed to P4.

strength:
VERY HIGH for execution input.

### P4-SRC-004
class:
CURRENT_CONVERSATION / PRIOR_ASSISTANT_OUTPUT.

content:
first v3.2.1 P4 shortlist over B001..B026.

use:
historical execution evidence, including dependency/window errors.

authority:
LOWER than supplied contract.

### P4-SRC-005
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
full P4 v3.2.2 spec.

strength:
VERY HIGH.

authorship:
UNKNOWN.

### P4-SRC-006
class:
CURRENT_CONVERSATION / PRIOR_ASSISTANT_OUTPUT.

content:
first v3.2.2 re-selection over older 26-node packet.

use:
evidence that dependency closure bug persisted after contract upgrade.

### P4-SRC-007
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
P3 14-node role-aware origin-to-replicators packet.

### P4-SRC-008
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
P3 19-node densified origin-to-replicators packet.

### P4-SRC-009
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
P3 28-node robotic affective architecture packet.

### P4-SRC-010
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
P3 5-node Stage 1 minimal visual vocabulary verdict.

### P4-SRC-011
class:
CURRENT_CONVERSATION / USER_SUPPLIED_ARTIFACT.

content:
P3 6-node Phases 1–3 normalization WARN packet.

### P4-SRC-012
class:
GITHUB_ARTIFACT.

branch/source:
historical recovery branch containing
`channels/p-control-point/recovery/P4_CONTRACT_RECOVERY_PASS_V0_1.md`.

content:
independent durable recovery of P4 final-cut role, P3 seam, source-order/dependency preservation, author-selection boundary and no-invention rule.

strength:
HIGH for recovered role core; explicitly partial on version lineage.

### P4-SRC-013
class:
GITHUB_ARTIFACT.

file:
`P_SYSTEM_ROUTE_AUTHORITY_TIMELINE_V0_1.md`.

content:
route families on 2026-02-12 and 2026-03-05/06; current HOLD.

### P4-SRC-014
class:
GITHUB_ARTIFACT.

file:
`P_CHANNEL_REGISTRY_V0_2.yaml`.

content:
role spine sets P4 = feel-potential sorter / final cut;
P3->P4 candidate rewrite forbidden;
author selection bypass forbidden.

### P4-SRC-015
class:
GITHUB_ARTIFACT.

file:
P3 recovery interface/route files.

content:
P3->P4 local seam and `ELYX_P4_INPUT_V3`.

### P4-SRC-016
class:
AUTHOR_RAW_CURRENT_REQUEST.

date:
2026-10-07.

exact fragments:
- `История канала является частью архитектуры канала.`
- `ABSOLUTE RULE: НЕ ИЗОБРЕТАТЬ НЕДОСТАЮЩУЮ ИСТОРИЮ.`
- `SUPPLIED_BY_AUTHOR ≠ NECESSARILY AUTHORED_BY_AUTHOR.`

authority:
recovery-law for this branch.

## Evidence hierarchy applied

1. direct author wording;
2. supplied historical artifacts;
3. durable Elyxion GitHub evidence;
4. confirmed decisions;
5. later references;
6. assistant outputs;
7. recovered summaries/context;
8. inference.

Inference never closes an UNKNOWN in this recovery.
