# CHANNEL_INTERFACE_MAP

## Upstream — P3

strongest recovered producer:
P3 Text Renderer.

Historical/recovered seam:
`P3 rendered candidates -> ELYX_P4_INPUT_V3`.

Current P4 compatibility supplied:
- `ELYX_P4_INPUT_V3_1`;
- `ELYX_P4_INPUT_V3_2`;
with primary current inputs contract named `ELYX_P4_INPUT_V3_2_2`.

### P4 reads

Identity:
- task_id;
- stage_scope;
- source_identity;
- source task/ladder/range/canon-map identity.

Candidate:
- B### id;
- source index;
- exact candidate line;
- confidence tag;
- micro transition tag;
- feel tags;
- dependencies;
- optional semantic fingerprint;
- optional binding refs.

Goal/control:
- feel_goal_profile;
- montage policy;
- risk tolerance;
- meta policy;
- selection mode;
- P5 author-enable flag;
- optional prior spine snapshot.

## Stable identity boundary

P4 does not own B-ID creation.
It consumes P3 canon IDs.

P4 must not:
- reuse an ID;
- silently change a line under same ID;
- invent missing binding;
- treat source hash as meaning.

## P4 internal transformation surface

Validation:
preflight.

Editorial analysis:
observables-first heuristic scoring.

Structure:
dependency closure + role tagging.

Selection:
strict order-safe shortlist/reserves.

Protection:
late-bridge and terminal-mass guards.

Reporting:
coverage/confidence/anti-boredom + patch/expand suggestions.

## Downstream packet

Current:
`ELYX_P4_FILTER_SHORTLIST_PACKET_V3_2_2`.

Main structural outputs:
- ordered spine IDs;
- exact candidate lines;
- P4 structural roles/reasons;
- reserves;
- coverage;
- confidence;
- maturity/overcompression diagnostics;
- next-channel handoff.

## Upstream patch loop

If defect is wording/observable sharpness:
P4 -> P3 (patch recommendation).

Boundary:
P4 does not perform the rewrite itself.

## Upstream expansion loop

If defect is bridge mass/maturity support:
P4 -> P2 (expand recommendation).

Boundary:
P4 does not invent missing bridge content itself.

## A-layer options

v3.2.1:
A_MINUS_1 / A0 appear as next options.

v3.2.2:
A_ULTRA / A0 appear as next options.

Evidence ceiling:
these are allowed/recommended route options.
This recovery does not prove one universal automatic P4 -> A route.

## P5 interface

`ready_for_p5` exists as a backward-compatibility field.

Current default:
`p5_enabled_by_author=false`.

Rule:
never recommend P5 as default unless explicitly enabled upstream.

## Canon interface

No direct canonization interface is recovered.

P4 output is candidate-selection/final-cut evidence, not owner canon.
