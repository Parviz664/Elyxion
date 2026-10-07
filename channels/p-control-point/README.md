# Elyxion P Control Point

Dedicated control layer for the Elyxion P-channel work architecture.

## Mission

Preserve the exact architecture of the P-system and prevent semantic drift across chats, models, versions, and implementations.

Root question:

> **Как собрано? / How is it assembled?**

The Control Point does **not** invent gameplay, does **not** canonize ideas, does **not** silently repair unknowns, and does **not** manage the author's live dream stream.

## Current branch

`channel/p-control-point-v0.1`

Current frozen control contract:

`P_CONTROL_POINT_V0_2_FROZEN`

Freeze state:

`FROZEN_CONTROL_LAYER / ROUTE_HOLD`

Current route state:

`HOLD_UNRESOLVED`

Owner route decision:

`C`

## Safe high-level flow

`FREE AUTHOR DREAM / RAW -> capture/preservation -> P-channel structuring when invoked -> separate author/canon authority`

P-channels are a work/AI architecture. They are not automatically gameplay systems.

## Frozen role spine

- `P0` — intent normalization / strict downstream routing.
- `P1` — causal/reality map + seed + linear order.
- `P2` — source-bound ladder builder over P1.
- `P3` — patch-safe final-text renderer.
- `P4` — feel-potential filter / final cut with author-selection boundary.
- `-P1` — historically recovered reality-skeleton / causal-continuity layer; current routing remains unresolved.

Historical route families are both preserved:

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

and later:

`P0 -> P1 -> P2 -> P3 -> P4`

The frozen Control Point does not choose between them.

## Core laws

- USER RAW is immutable.
- Corrections are append-only deltas.
- Lower-authority interpretation cannot silently overwrite higher-authority source.
- UNKNOWN remains UNKNOWN until evidence or owner confirmation resolves it.
- CONTRACTED status requires an authoritative source reference.
- Unsupported creation is a failure.
- Material loss without an explicit traceable reason is a failure.
- Automatic canonization is forbidden.
- Provenance must distinguish supplied-by from authored-by.
- Node identity and function set are separate axes.
- Functional similarity does not prove rename/absorption.
- P3 rendering may not mutate P2 semantics.
- P4 selection may not rewrite candidates or bypass author authority.
- Free author dreaming remains outside continuous P-channel control.

## Control artifacts

- `P_CONTROL_POINT_V0_1.md` — original source-grounded foundation.
- `P_CONTROL_POINT_V0.2_CANDIDATE.md` — pre-freeze consolidation.
- `P_CONTROL_POINT_V0_2_FROZEN.md` — current frozen control contract.
- `P_CHANNEL_REGISTRY_V0_2.yaml` — current frozen machine-readable registry.
- `P_CONTROL_POINT_V0_2_GAP_REGISTER.md` — prioritized open gaps.
- `P_SYSTEM_ROUTE_AUTHORITY_TIMELINE_V0_1.md` — February→March→August→October route history.
- `P_CHAIN_ROLE_SPINE_CROSSCHECK_V0_1.md` — end-to-end seam/authority cross-check.
- `P_CONTROL_POINT_INVARIANTS_V0_1.yaml` — 25 machine-readable invariants.
- `tests/P_CONTROL_POINT_FALSIFICATION_CASES_V0_1.json` — 25 falsification fixtures.
- `tools/validate_p_control_point.py` — executable regression sentinel.
- `P_CONTROL_POINT_V0_2_FREEZE_READINESS_AUDIT.md` — pre-freeze readiness audit.
- `decisions/P_CONTROL_POINT_V0_2_FREEZE_DECISION_2026_10_07.md` — owner freeze record.

## Validation

GitHub Actions workflow:

`P Control Point Validate`

The validator now checks the frozen v0.2 state itself, including:

- frozen control-layer status;
- Decision C / route HOLD;
- both historical route families;
- no merge authorization hidden inside the freeze;
- no disputed-route implementation authorization;
- free-author-dream boundary;
- domain/canonization guards;
- 25 invariants;
- 25 falsification fixtures.

This proves static control-contract consistency, not perfect semantic truth or complete historical recovery.

## Current critical gap

`GAP-G0-001`

Current `-P1` route authority remains intentionally unresolved under Decision C.

This gap blocks runtime implementation across the disputed P0/-P1/P1 boundary, but does not invalidate the frozen Control Point.

## Repository stage

The Control Point is frozen.

The next repository stage is:

`PR READY FOR REVIEW`

Freeze does **not** authorize merge to `main`; merge remains a separate action after review/checks.
