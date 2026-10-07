# CHANNEL_ERROR_CORRECTION_LOG

## ERR-001 — provenance overclaim
Problem:
early recovery language used terms like "owner-origin" too strongly for chat artifacts merely supplied by the user.

Detection:
P Control Point `SOURCE_PROVENANCE_CORRECTION_V0_1.md`.

Repair:
use `USER_SUPPLIED_ARTIFACT` unless authorship is separately proved.

Resulting invariant:
`SUPPLIED_BY != AUTHORED_BY`.

## ERR-002 — semantic scope misrouting packets
Observed practice:
P0 packets sometimes carried a stage_scope unrelated to raw_author_text, e.g. NPC content under origin-to-replicators scope, Cell Stage content under NPC scope, piano content under Cell Stage scope.

P1 behavior:
assistant execution returned FAIL and refused to build a fake bridge.

Status:
CORRECT_BOUNDARY_BEHAVIOR, not a P1 contract error.

Resulting invariant:
full thematic mismatch cannot be repaired by bridge discipline.

## ERR-003 — range/count ambiguity
Earlier supplied material used range-like values such as 60..110 in a way later architecture treats as count-hint misuse.

Later repair:
P0 v2.6 and P1 v3.2.4 lock `range_semantics=index_range`; count hints move to output-size/target-step-count hints; trace required for autofix.

Status:
CONTRACT_HARDENING.

## ERR-004 — invalid pressure-axis PASS
Assistant-generated human-chaos P1 packet:
M004 used `pressure_axis = reaction_stable_product`.

But `reaction_stable_product` is a mechanism class, not a declared pressure axis.

The packet still reported PASS.

Classification:
ASSISTANT_EXECUTION_ERROR / VALIDATOR_FALSE_PASS.

Repair in this recovery:
do not rewrite the old packet; record the error and add a regression assertion.

## ERR-005 — mechanics contract ambiguity
v3.2.4 generic hard rule:
`no_gameplay_mechanics=true`.

Later P0 v2.7 task packet:
`no_mechanics=false`, `mechanics_representation_mode=SURFACE_ONLY_NO_STEPS`.

Assistant P1 execution accepted mechanics as meaning/surface.

Classification:
CONTRACT_BOUNDARY_CONFLICT.

Repair status:
NOT RESOLVED. Preserved as UNKNOWN/HOLD.

## ERR-006 — final_hard_verdict role creep
Several assistant-generated P1 packets added `final_hard_verdict` to satisfy upstream single-output demands.

v3.2.4 required output list does not include that family.

Classification:
PRACTICE_ROLE_EXPANSION / GENERIC_AUTHORITY_NOT_PROVED.

Repair:
document, do not retroactively promote.

## ERR-007 — cross-domain mechanism ontology tension
The recovered mechanism allowlist is strongly physical/chemical in vocabulary.
Assistant executions reused those classes metaphorically for human/AI architecture.

Intentional genericity is not proved.

Classification:
SEMANTIC_FIT_GAP.

Repair:
none in this archaeology; requires later explicit contract decision if changed.
