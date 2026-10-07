# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-P0-001 — provenance overclaim

Error:
earlier recovery language used labels such as "owner-origin artifact" too strongly.

Detection:
a supplied chat artifact may have been assistant-generated earlier.

Correction:
sibling record `SOURCE_PROVENANCE_CORRECTION_V0_1.md` changed the safe class to `USER_SUPPLIED_CHAT_ARTIFACT` unless direct owner wording is separately proved.

Resulting invariant:
`SUPPLIED_BY_OWNER != AUTHORED_BY_OWNER`.

Status:
REPAIRED.

## ERR-P0-002 — stale override semantic misroute

Observed in current channel:
raw intent changed topics while stale/custom stage_scope remained authoritative.

Examples:
- "Как возникла пианино?" while stage_scope still pointed at Elyxion Cell Stage vocabulary;
- piano ancestry follow-up with same stale scope;
- later Elyxion Phases 1–3 raw while override still pointed at `human_chaos_root_structure_under_migration_pressure`.

Failure:
P0 could remain syntactically contract-valid while semantically routing the wrong subject.

Detection:
current conversation behavior and later supplied V2_7 output artifact.

Correction signal:
V2_7 supplied artifact treats the conflicting scope as legacy misroute and patches it to `elyxion_cell_stage_phases_1_3`.

Resulting invariant:
`NO_SILENT_SEMANTIC_MISROUTE` is a strong desired invariant, but its exact formal authority after v2.6 remains unresolved because no v2.7 spec is recovered.

Status:
WORKING_PATCH_SIGNAL / FORMAL_SPEC_GAP.

## ERR-P0-003 — mechanics deadlock

Observed:
raw author material explicitly required extraction of mechanics and joystick/control evolution, while carried override/hard rule said `no_mechanics=true`.

Failure:
downstream contract could prohibit a layer the author explicitly asked P0 to preserve.

Correction signal:
supplied V2_7 artifact changes:
- `no_mechanics=false`
- `mechanics_representation_mode=SURFACE_ONLY_NO_STEPS`
while retaining bans on UI walkthrough/tutorial and implementation recipes.

Resulting invariant candidate:
meaning/surface extraction is distinct from tutorial/gameplay implementation generation.

Status:
WORKING_PATCH_SIGNAL / FORMAL_SPEC_GAP.

## ERR-P0-004 — route removal could be misread as function deletion

Risk:
v2.4 removes -P1 node from route.

Incorrect inference:
therefore -P1 function disappeared.

Recovery:
strong function-migration signals appear in P0→P1 guards and P1 causal responsibilities.

Resulting invariant:
`REMOVED_NODE != REMOVED_FUNCTION`.

Status:
RECOVERED.

## ERR-P0-005 — assistant self-guarantee inflation

Observed in current conversation:
assistant outputs used phrases such as `guarantee_level: 100_of_100`.

Problem:
self-declared confidence is not evidence of contract fidelity.

Correction:
this recovery never treats self-guarantee fields as proof.

Resulting invariant:
`SELF_CERTIFICATION_IS_NOT_EVIDENCE`.

Status:
REPAIRED_IN_RECOVERY.

## ERR-P0-006 — one-line noise rule can drop distributed constraints

Recovered rule:
if author sends more text, extract first core question and ignore rest as noise.

Known audit concern:
important constraints may appear later in a long author message.

Evidence class:
assistant audit concern + current long-input practice.

Owner correction:
not fully recovered as a formal spec.

Status:
OPEN_RISK.

## ERR-P0-007 — v2.7 schema ambiguity

Supplied V2_7 output artifact:
- announces `ELYX_P0_OUTPUT_V2_7`;
- still binds to v2.6 channel spec;
- uses autopatch fields/types that are not a clean byte-for-byte match to the declared v2.6 autopatch schema.

Risk:
mistaking output evolution for formal contract evolution.

Resulting invariant:
do not declare `ELYX_P0_CHANNEL_SPEC_V2_7` without evidence.

Status:
OPEN_GAP / SAFELY_BOUNDED.
