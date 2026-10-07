# P3_CONTRACT_RECOVERY_PASS_V0_1

Status: `ROLE_CORE_STRONGLY_RECOVERED / OUTPUT_SCHEMA_PARTIAL`

Target: `P3`

Purpose:

recover P3's rendering role, upstream/downstream bindings, and anti-drift boundary without inventing missing output schema or merge semantics.

## 1. Recovered P3 identity

Recovered role label:

`final_text_renderer_patch_safe`

Recovered input packet:

`ELYX_P3_INPUT_V3`

Recovered mission:

render the P2 ladder into final text form while preserving source meaning, truth constraints, and patch safety.

P3 is not a free semantic generator.

## 2. Recovered input fields

User-supplied P3 input material includes:

- `task_id`
- `stage_scope`
- `range`
- `author_intent_lock`
- `p2_packet_ref`

Recovered example upstream binding:

`p2_packet_ref = ELYX-P2-20260329-STAGE1-MINIMAL-VOCAB-V26-01`

## 3. Recovered rendering locks

Recovered locks include:

- `render_mode: final_text_patch_safe`
- `proof_blocks_required: true`
- `single_final_verdict_only: true`
- `truth_first_required: true`
- `anti_bloat_required: true`
- `anti_premature_complexity_required: true`
- `uncertainty_marking_required: true`

Recovered uncertainty labels:

- `plausible`
- `speculative`
- `unknown`

## 4. Semantic boundary

Recovered P3 constraints include:

- strict realism;
- continuity;
- anti-jump;
- no UI invention;
- no lore invention;
- no gameplay-mechanics invention;
- no semantic drift.

Therefore the safe P3 transformation boundary is:

`P2 ladder semantics -> rendered/final-text representation`

not:

`P2 ladder -> newly invented world structure`

P3 may improve render form and patch-safe presentation only within the admitted source meaning.

## 5. Downstream binding to P4

Recovered downstream packet:

`ELYX_P4_INPUT_V3`

Recovered handoff reference:

`candidate_items_ref = ELYX-P3-20260329-STAGE1-MINIMAL-VOCAB-V26-01`

This establishes:

`P3 output -> P4 candidate input`

Recovered later P4 working packets identify their source payload type as:

`ELYX_P3_RENDERED_LADDER_PACKET_V3`

Examples of later P4 source identity include:

- a P3-rendered ladder ID;
- source range;
- canon-map version;
- P3 packet as the immediate upstream source.

## 6. Recovered later working role

A later user-confirmed P-chain description identifies:

`P0 intent normalization -> P1 reality map -> P2 microstep ladder -> P3 final text renderer -> P4 final cut`

P5 remains disabled in that architecture.

This supports P3 as a render/representation layer between structural ladder construction and final potential/cut selection.

## 7. What is NOT yet recovered

No exact persistent source artifact has yet been located for:

- full `ELYX_P3_RENDERED_LADDER_PACKET_V3` schema;
- exact per-item output field list;
- generic P3 merge rules;
- generic P3 split rules;
- exact P3 source-binding sub-schema;
- complete P3 version lineage;
- explicit P3 supersedes/superseded_by chain.

Therefore those fields remain:

`UNKNOWN`

They must not be reconstructed from P4 expectations alone.

## 8. Safe role statement

Allowed:

`P3 is a patch-safe final-text renderer that renders the P2 ladder under truth-first, anti-bloat, anti-premature-complexity, uncertainty, continuity, and no-semantic-drift constraints, then hands rendered candidate material to P4.`

Not allowed:

`P3 freely rewrites or improves the semantic content of P2.`

Not allowed:

`P3's full output schema is known.`

## 9. Control-point transformation law for P3

P3 must preserve:

- P2 item order unless an exact contract says otherwise;
- P2 source identity;
- P2 causal meaning;
- upstream uncertainty state;
- author intent lock;
- truth/realism boundary.

P3 may transform:

- textual/rendered expression;
- patch-safe presentation;
- proof-block packaging where required;
- final-text readability within semantic fidelity.

P3 must not transform:

- causal truth;
- canon status;
- entity scope;
- uncertainty into certainty;
- raw/candidate material into confirmed truth;
- missing content into invented content.

## 10. Current status

`ROLE_CORE = STRONGLY_RECOVERED`

`INPUT_CONTRACT = STRONGLY_RECOVERED`

`DOWNSTREAM_P4_BINDING = STRONGLY_RECOVERED`

`OUTPUT_PACKET_IDENTITY = PARTIALLY_RECOVERED`

`OUTPUT_SCHEMA = UNKNOWN`

`MERGE_SPLIT_RULES = UNKNOWN`

`VERSION_LINEAGE = PARTIAL`

## 11. Next object

`P4_CONTRACT_RECOVERY_PASS_V0_1`

Goal:

recover P4 final-cut / feel-potential role, exact author-selection boundary, shortlist semantics, source-order preservation, and the distinction between selection and semantic invention.
