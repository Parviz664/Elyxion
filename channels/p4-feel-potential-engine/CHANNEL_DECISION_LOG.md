# CHANNEL_DECISION_LOG

## D-P4-001 — P4 is the final feel-potential sorter

order:
earliest recovered by 2026-02-12.

question:
what does the final P node do after P3 candidate rendering?

recovered selection:
`feel_potential_sorter_final` / `feel_potential_sorter_final_cut`.

options considered:
UNKNOWN.

provenance:
RECOVERED_FROM_PRIOR_CONVERSATION / USER_SUPPLIED_ARTIFACT.

explicit author rationale:
false.

consequence:
P4 sits after P3 and performs selection/final-cut rather than text generation.

status:
ACTIVE ROLE LINEAGE.

## D-P4-002 — P5 disabled; P4 remains terminal P node

date:
2026-03-05 recovered route artifacts.

question:
should the recovered P-chain continue to P5 by default?

owner-controlled result:
`P5: disabled by author`.

route guard:
`must_not_output_P5`.

provenance:
AUTHOR_CONSTRAINT recovered through P0 artifacts/prior context.

explicit author rationale:
UNKNOWN.

consequence:
P4 must not default-route to P5.

later status:
ACTIVE in v3.2.1/v3.2.2 through `p5_enabled_by_author=false`.

## D-P4-003 — observables-first over emotion-label-first

version:
v3.2.1.

selection:
required observable axes become primary;
legacy emotion axes remain aliases only.

provenance:
USER_SUPPLIED_ARTIFACT.
authorship:
UNKNOWN.

explicit reason in supplied patch:
compatibility with observables-first P3 practice; avoid emotion labels as sole basis.

status:
ACTIVE.

## D-P4-004 — scores are editorial heuristics, not world truth

version:
v3.2.1.

selection:
weights retained only as internal deterministic/editorial heuristics.

forbidden:
score as truth/world-model/simulation metric.

provenance:
USER_SUPPLIED_ARTIFACT.

status:
ACTIVE.

## D-P4-005 — no-guess duplicate removal

version:
v3.2.1.

selection:
drop only when duplicate status is provable through admitted signatures.

otherwise:
reserve with suspicion flag.

status:
ACTIVE.

## D-P4-006 — ready_for_next replaces P5-default routing

version:
v3.2.1.

selection:
canonical routing field becomes `ready_for_next`;
`ready_for_p5` retained only as legacy alias.

provenance:
USER_SUPPLIED_ARTIFACT.

explicit upstream condition:
P5 disabled by author by default.

status:
ACTIVE.

## D-P4-007 — backbone quota against “трейлер”

version:
v3.2.1.

selection:
minimum backbone ratio introduced.

purpose explicitly supplied:
prevent a shortlist that is only peak/trailer-like lines.

status:
ACTIVE, later strengthened by v3.2.2.

## D-P4-008 — role-aware backbone and late-bridge protection

version:
v3.2.2.

selection:
add core/bridge/terminal/reserve roles;
protect thin speculative late clusters from overcompression.

provenance:
USER_SUPPLIED_ARTIFACT.

status:
ACTIVE.

## D-P4-009 — structural-first explanations

version:
v3.2.2.

selection:
why-kept/why-reserved must explain bottleneck/dependency/observability/bridge/terminal function before interpretive language.

status:
ACTIVE.

## D-P4-010 — terminal mass control

version:
v3.2.2.

selection:
a chosen terminal peak cannot automatically push terminal seal/support to reserve without explicit mass check.

status:
ACTIVE.

## D-P4-011 — A-layer option changes from A_MINUS_1 to A_ULTRA

observed:
v3.2.1 `ready_for_next.next_channel_options` contains `A_MINUS_1`.
v3.2.2 contains `A_ULTRA`.

provenance:
DIRECT USER_SUPPLIED CONTRACT COMPARISON.

explicit author rationale:
false.

reason:
UNKNOWN.

status:
ACTIVE AS CURRENT OPTION / HISTORICAL OLD OPTION PRESERVED.

Do not infer that A_MINUS_1 and A_ULTRA are the same channel.

## D-P4-012 — full structural spine may exceed target shortlist size

origin:
later execution practice under v3.2.2.

problem:
linear dependency/terminal paths cannot be safely trimmed to the target cardinality.

implemented behavior:
retain all structurally mandatory nodes and document shortlist-size override.

provenance:
ASSISTANT IMPLEMENTATION aligned with contract hard guards.

owner decision:
not separately recovered.

status:
IMPLEMENTED PRACTICE, NOT OWNER-CANON DECISION.

## Decision law

Assistant recommendations are not automatically owner decisions.
Where owner rationale is not explicit, this log records `UNKNOWN`.
