# P2_CONTRACT_RECOVERY_PASS_V0_1

Status: `ROLE_CORE_STRONGLY_RECOVERED / VERSION_LINEAGE_PARTIAL`

Target: `P2`

Purpose:

recover P2's exact role, input/output contract, source-binding rules, and split/merge semantics without assuming P3/P4 behavior.

## 1. Recovered P2 identity

Recovered channel:

`ELYX_P2_LADDER_BUILDER_v3.2.1`

Recovered mission:

`P1 handoff -> bounded causal ladder data`

Recovered scale:

`1..500` ladder items in the v3.2.1 contract family.

P2 is a structuring/expansion layer over P1's causal map, not a free-form generator.

## 2. Required input

Recovered input identity:

`ELYX_P2_INPUT_V3_2_1`

Required P1-bound material includes:

- `task_id`
- `stage_scope`
- range/bounds
- `author_intent_lock`
- `map_id`
- compact topic-scope entities
- compact linear order
- compact micro-stage catalog
- drift guards
- resume token

Hard boundary:

P2 must consume P1 structure rather than reconstruct it independently.

## 3. Recovered output

Recovered packet:

`ELYX_P2_LADDER_PACKET_V3_2_1`

Recovered output families include:

- `ladder_items`
- binding report
- quality report
- drift report
- A-bridge / downstream bridge material
- resume information

## 4. Ladder item contract

Recovered item fields include:

- `i`
- `candidate_id`
- label / science tag
- `world_state`
- `pressure`
- `pressure_axis`
- `transition_trigger`
- deprecated alias `trigger` only if equal to the preferred field
- `trigger_type`
- `mechanism_class`
- `micro_transition`
- `stabilized_state_after`
- `why_plausible`
- dependency / next-link fields
- `source_binding`
- `scope_entities_used`
- `feel_pressure`
- uncertainty
- anti-repeat / anti-boredom controls

## 5. Source binding

Every material ladder item must bind back to P1.

Recovered key:

`source_binding.p1_micro_stage_id`

P2 is therefore not allowed to emit a materially important ladder item with no P1 lineage.

This is a direct fit with P Control Point's no-drop/no-invent law.

## 6. Split / merge semantics

Recovered:

- split is allowed only when P1 permits split;
- merge must preserve explicit lineage;
- split/merge tracing is required;
- source identity cannot be silently lost.

This means P2 may refine granularity, but it does not gain authority to rewrite upstream causal truth.

## 7. Hard guards

Recovered P2 guards include:

- no UI
- no gameplay mechanics
- no lore injection
- no formulas/models as implementation output
- no code
- no new entities/mechanisms outside allowed scope
- canon anchor / P1 binding as hard gates
- deterministic ordering
- uncertainty propagation
- source-preserving handoff

## 8. Later working evolution — v3.5.0

Later user-supplied P2 work uses:

`ELYX_P2_LADDER_BUILDER_v3.5.0`

and packet:

`ELYX_P2_LADDER_PACKET_V3_5_0`

Recovered later behavior includes:

- direct binding from P1 stages into P2 ladder items;
- explicit phase-spine preservation;
- no silent raw-mass promotion;
- no premature later-phase/world expansion;
- canon/direction/raw separation;
- a supported-but-immature bridge may remain WARN instead of being silently promoted;
- late-cluster densification can be required before terminal preseal.

Example recovered later task state:

`P2I001..P2I006` bound to `M001..M006`

with no split/merge in that specific packet.

Important:

this task-level direct-bind behavior does not erase the general split/merge capabilities of the v3.2.1 contract.

## 9. Version-lineage ceiling

Recovered:

- v3.2.1 exact role/core is strong;
- v3.5.0 later working architecture exists.

Not yet recovered:

- exact v3.3/v3.4 lineage;
- explicit generic supersession chain from v3.2.1 to v3.5.0;
- whether every v3.5 task uses identical schema fields.

Therefore:

`VERSION_LINEAGE = PARTIAL`

not:

`FULLY_PROVED`.

## 10. Safe current P2 statement

Allowed:

`P2 is a source-bound ladder builder that expands/refines P1 causal stages into ordered ladder items while preserving P1 lineage, uncertainty, scope, and split/merge traceability.`

Not allowed:

`P2 invents the causal structure independently.`

Not allowed:

`P2 may silently promote RAW or unresolved bridges into canon.`

## 11. Current status

`ROLE_CORE = STRONGLY_RECOVERED`

`SOURCE_BINDING = STRONGLY_RECOVERED`

`SPLIT_MERGE_AUTHORITY = BOUNDED_AND_TRACE_REQUIRED`

`VERSION_LINEAGE = PARTIAL`

`IMPLEMENTATION_STATUS = NOT_STARTED`

## 12. Next object

`P3_CONTRACT_RECOVERY_PASS_V0_1`

Goal:

recover P3's renderer/ladder transformation role, exact source-binding requirements, merge rules, and the boundary between rendering and semantic invention.
