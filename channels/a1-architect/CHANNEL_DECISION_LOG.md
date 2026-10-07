# CHANNEL_DECISION_LOG

## D001 — zero-manual direct-paste architecture
Order: v3.1 exact artifact.
Question: should A1 require manual mode/module/task configuration?
Selected contract state: no; auto-resolve from a single pasted upstream artifact.
Provenance: USER_SUPPLIED_ARTIFACT.
Explicit author rationale: UNKNOWN.
Status: ACTIVE / PRESERVED THROUGH v3.3.

## D002 — exactly three architecture variants
Order: v3.1.
Selection: A/B/C count fixed to exactly three; missing count is hard fail.
Status: ACTIVE.

## D003 — A2 as downstream handoff
Order: v3.1.
Selection: `A1_ARCH_ANCHOR_V3` packet; `next_agent=A2` in successful work.
Status: ACTIVE.

## D004 — DreamVault ref-only passthrough
Order: v3.2.
Selection: echo upstream refs 1:1; missing -> null + WARN; never synthesize hash/ID.
Contract rationale: preserve no-drift hooks while staying A1.
Author rationale beyond supplied artifact: UNKNOWN.
Status: ACTIVE.

## D005 — role integrity vs E-Prime
Order: v3.2.
Selection: A1 may emit alignment hints but may not emit E-Prime-owned artifact families.
Status: ACTIVE.

## D006 — quarantine v2
Order: v3.2.
Selection: classify meaning-layer vs implementation-layer tokens; do not remove tokens.
Later status: SUPERSEDED BY v3.3 quarantine semantics.

## D007 — Meaning Cleanroom dual view
Order: v3.3.
Selection: A1 must emit both meaning-only view and isolated implementation lane; A2 defaults to meaning view.
Contract rationale explicitly supplied: prevent engine/build nouns from polluting the dream/meaning surface.
Status: ACTIVE.

## D008 — Quarantine v3
Order: v3.3.
Selection: implementation lane existence is normal; quarantine/warning only if implementation tokens leak outside the proper lane.
Status: ACTIVE.

## D009 — conditional dream-preservation target
Order: v3.3.
Selection: target 99.9% only under listed conditions; degraded/no claim on broken binding/cleanroom failure.
Important: this is a contract target, not independently measured performance.
Status: ACTIVE AS TARGET / NOT VERIFIED.

## D010 — P1 compact side-handoff includes A1
External historical evidence: P1 v3.2.2 and v3.2.4 target A1 among A consumers.
Who selected: original authorship not proved in this recovery.
Status: HISTORICAL INTERFACE FACT.
