# CHANNEL_DECISION_LOG

## D001 — separated -P1/P1 route
Date: 2026-02-12 recovered state.
Observed architecture used both nodes.
Direct author rationale: UNKNOWN.
Status: HISTORICAL.

## D002 — direct P0->P1 route
Date: 2026-03-05 recovered state.
P0 v2.4 removes standalone -P1 from its route.
Direct author rationale: UNKNOWN.
Status: HISTORICAL; not global-current due later HOLD.

## D003 — v3.2.2 append-only extension
Selection in supplied contract: preserve causal core; add felt inevitability, entity budget, stronger binding, A handoff.
Provenance: USER_SUPPLIED_ARTIFACT.
Status: SUPERSEDED but preserved historically.

## D004 — v3.2.4 hardening
Selection in supplied contract: bridge proof, node roles, E015 guard, overview causality, BL namespace, stricter validation.
Status: ACTIVE strongest-known supplied P1 contract.

## D005 — A target change
v3.2.2: `A_MINUS_1, A1, A2, A3, A0`.
v3.2.4: `A_ULTRA, A1, A2, A3, A0`.
Reason/equivalence: UNKNOWN.
Status: unresolved lineage delta.

## D006 — route authority HOLD
Date: 2026-10-06.
Owner Decision C: `HOLD_UNRESOLVED`.
Consequence: role archaeology may proceed; current global route may not be silently selected.
Status: ACTIVE.

## D007 — mechanics surface exception
Later P0 v2.7 task packet allows mechanics meaning/surface while P1 v3.2.4 generically bans gameplay mechanics.
Owner-confirmed generic reconciliation: not recovered.
Status: HOLD / CONTRACT_CONFLICT.
