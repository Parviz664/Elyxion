# CHANNEL_DECISION_LOG

## DEC-E2-001 — Multiple alternatives as core output
- Date/order: 2026-02-16, v1.0
- Question: should E2 emit one path or several?
- Selection: several; artifact explicitly says “alternative paths (not one path)”.
- Provenance: USER_SUPPLIED_ARTIFACT.
- Status: SUPERSEDED by v2.1.

## DEC-E2-002 — Strict contract operation
- Date: 2026-02-17
- RAW: “Работать строго по контракту Е2.”
- Provenance: AUTHOR_RAW.
- Consequence: assistant begins emitting E2-formatted execution packets.
- Status: historical control point; principle remains relevant.

## DEC-E2-003 — Registry+seal/no-inference
- Date: 2026-02-20
- Selection: E2 must not generate/rank/recommend when required registry/seal proof is absent.
- Explicit reason in v1.2 change_intent: prevent variants based on unconfirmed inputs and synchronize upstream contracts.
- Provenance: USER_SUPPLIED_ARTIFACT.
- Status: SUPERSEDED in mechanism by later E0 echo model, but no-invention principle persists.

## DEC-E2-004 — Registry/seal validation moves upstream
- Date: 2026-03-03, v2.1
- Options: direct E2 registry validation vs E0 dual-lock echo.
- Selection: E2 echo-only through E0 locked handle.
- Provenance: USER_SUPPLIED_ARTIFACT.
- Status: ACTIVE direction.

## DEC-E2-005 — Portfolio removed as default
- Date: 2026-03-03
- Selection: exactly one primary path; optional alternative only fallback-only.
- Artifact wording: “E2 перестаёт быть «портфелем стратегий» по умолчанию.”
- Provenance: USER_SUPPLIED_ARTIFACT.
- Status: later refined; current E2 no longer owns build-path choice.

## DEC-E2-006 — Metric axis removed
- Date: 2026-03-03
- Selection: no 0–100 scoring as decision axis; lexicographic/gate logic.
- Provenance: USER_SUPPLIED_ARTIFACT.
- Status: survives conceptually into later role purity.

## DEC-E2-007 — E2 as engine-contract/route translator
- Date: 2026-03-13 07:09–07:12Z
- Assistant proposal: engine-contract / route translation layer over E1 constrained skeleton.
- Author selection: user explicitly accepted (“Да”) and requested mature E2 update structure.
- Provenance: ASSISTANT_PROPOSAL → AUTHOR_DECISION.
- Status: ACTIVE.

## DEC-E2-008 — Clean E-mainline
- Date: 2026-03-13 13:10:07Z
- Selection: “чистая E-цепочка”: E0 bind → E1 skeleton → E2 contract translation → E3 build convergence → E4 readiness → E5 human execution → E6 runtime closure; D/G/M separate.
- Provenance: AUTHOR_DECISION.
- Status: ACTIVE.

## DEC-E2-009 — Remove D-core and E5-core from E2
- Date: 2026-03-13 14:50:32Z, v2.3
- Selection: E2 core is pure E-mainline translation + bounded routes + translation maturity + E3 handoff.
- Explicit delta recovered from patch metadata.
- Provenance: USER_SUPPLIED_ARTIFACT.
- Status: CURRENT_STRONGEST_KNOWN.

## Assistant proposals not proven adopted
The v1.0/v1.1 assistant reviews proposed:
- scoring formula;
- pending severity map;
- blocking-scope policy;
- ID regex;
- counterfactual pass criteria.

No recovered master proves that exact five-item patch was adopted as such.
