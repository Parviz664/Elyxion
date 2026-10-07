# CHANNEL_DECISION_LOG

## D-P3-001 — separate final rendering from ladder construction
order: HISTORICAL / exact birth point unknown
question:
Should P2 data itself be treated as final text?
recovered decision:
No. P2 produces ladder data; P3 produces final text.
provenance:
USER_SUPPLIED_ARTIFACT / RECOVERED_FROM_PRIOR_CONVERSATION.
author_selection:
strongly recovered as working architecture.
assistant_recommendation:
not required to establish fact.
explicit_author_rationale:
UNKNOWN.
consequence:
P2 and P3 remain separate authorities.
status:
ACTIVE.

## D-P3-002 — patch-safe / no semantic drift
date: recovered by 2026-03-05
question:
May P3 improve source meaning while rendering?
selection:
No. Rendering is patch-safe and truth-first.
provenance:
USER_CONSTRAINT + USER_SUPPLIED_ARTIFACT.
explicit_author_rationale:
not fully recovered.
consequence:
P3 becomes representation layer, not semantic generator.
status:
ACTIVE.

## D-P3-003 — B-ID stable identity layer
version: v3.1.x
question:
How should rendered items remain patch-safe?
selection:
Use B### P3 IDs with append-only freeze behavior.
provenance:
USER_SUPPLIED_ARTIFACT.
explicit_author_rationale:
artifact states patch-safe P4 connectivity and stable mapping needs.
originator_of_exact_design:
UNKNOWN / may be joint iteration.
consequence:
rendered items gain stable identity independent of fragile list position.
status:
ACTIVE.

## D-P3-004 — semantic fingerprint outranks line hash
version: v3.1.1
question:
Should source line text/hash determine semantic identity?
selection:
No. source_semantic_fingerprint becomes the stable meaning criterion; source_line_hash becomes historical trace only.
provenance:
USER_SUPPLIED_ARTIFACT.
consequence:
rewrites do not automatically break B-ID identity when meaning is unchanged.
status:
ACTIVE.

## D-P3-005 — replace emotion-word coverage with observable pressure markers
version: v3.1.1
question:
Must final text contain explicit emotion words to pass feel coverage?
selection:
No. FEEL_COVERAGE_MIN is deprecated warn-only; observable markers must carry unknownness, progress tension and awe-scale causally.
provenance:
USER_SUPPLIED_ARTIFACT.
consequence:
feel is inferred from world pressure rather than inserted emotion vocabulary.
status:
ACTIVE.

## D-P3-006 — one-root JSON discipline
version: v3.1.1+
question:
May TEXT_PLUS_PACKET emit prose outside the packet?
selection:
No. Text lives inside rendered_text / role_aware_text in one JSON root.
provenance:
USER_SUPPLIED_ARTIFACT.
consequence:
A3/agent compatibility and deterministic packaging improve.
status:
ACTIVE.

## D-P3-007 — role-aware rendering
version: v3.2.0
question:
Should core, closure, bridge and terminal lines receive the same rhetorical weight?
selection:
No.
provenance:
USER_SUPPLIED_ARTIFACT.
consequence:
render_role/render_weight become explicit.
status:
ACTIVE.

## D-P3-008 — anti-montage
version: v3.2.0
question:
Should core->closure pairs remain visibly editorial when not semantically necessary?
selection:
No. Closure tone should be smoothed into causal flow without dropping lineage.
provenance:
USER_SUPPLIED_ARTIFACT.
consequence:
P3 may alter role-tone, not causality.
status:
ACTIVE.

## D-P3-009 — speculative honesty over smoothness
version: v3.2.0
question:
May late speculative bridges be rendered as smooth facts for stronger prose?
selection:
No.
provenance:
USER_SUPPLIED_ARTIFACT.
consequence:
bounded inevitability: strong forced-next phrasing with uncertainty preserved.
status:
ACTIVE.

## D-P3-010 — namespace hygiene
version: v3.2.0
question:
May P1 block echoes and P3 B IDs share implicit identity?
selection:
No.
provenance:
USER_SUPPLIED_ARTIFACT.
consequence:
render_binding_hygiene explicitly separates P3_CANON_B from P1_BLOCK_SAFE / P1_BLOCK_LEGACY.
status:
ACTIVE.

## D-P3-011 — current global route remains unresolved
date: 2026-10-06 owner Decision C in P Control Point
question:
Which global route family is current with respect to standalone -P1?
selection:
C = HOLD_UNRESOLVED.
provenance:
OWNER_EXPLICIT_DECISION recorded in durable GitHub control artifact.
consequence_for_P3:
do not freeze P3's global upstream route beyond the strongly recovered local P2 seam.
status:
ACTIVE_HOLD.

## Reversals

No P3-specific owner reversal is strongly proved in the currently recovered evidence.

Important non-reversal:
the October P Control Point saying P3 output schema was UNKNOWN was an evidence-gap statement, not a design decision to remove the schema.
Current-channel full artifacts narrow that gap; they do not reverse the October architecture.
