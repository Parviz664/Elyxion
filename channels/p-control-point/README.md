# Elyxion P Control Point

Dedicated control layer for Elyxion P-channels.

## Mission

Preserve the exact architecture of the P-system and prevent semantic drift across chats, models, versions, and implementations.

Root question:

> **Как собрано? / How is it assembled?**

The control point does **not** invent gameplay, does **not** canonize ideas, and does **not** silently repair unknowns.

## Current branch

`channel/p-control-point-v0.1`

This branch is intentionally isolated from `main` while the control architecture is recovered and verified.

## Known P-channel set

`-P1 -> P0 -> P1 -> P2 -> P3 -> P4`

Important: the existence and order of these names are source-supported, but the exact role of each channel is not assumed unless separately recovered and referenced.

## Core laws

- USER RAW is immutable.
- Corrections are append-only deltas.
- Lower-authority interpretation cannot silently overwrite higher-authority source.
- UNKNOWN remains UNKNOWN until resolved by evidence or owner confirmation.
- No field becomes CONTRACTED without an authoritative source reference.
- Every material output should be traceable to input lineage.
- Unsupported creation is a failure.
- Material loss without an explicit reason is a failure.

## Initial files

- `P_CONTROL_POINT_V0_1.md` — source-grounded control contract.
- `P_CHANNEL_REGISTRY_V0_1.yaml` — initial channel registry with unresolved roles explicitly preserved.

## Source anchors currently used

- `ELYXION_PRRS_RAW_0.0.0.1.md`
- `ELYXION_PRRS_RAW_0.0.0.2.md`

These source files are not yet copied into this branch. Their names are recorded as provenance anchors only.

## Next object

`-P1 RECOVERY PASS`

Goal: recover every authoritative mention of `-P1`, compare later versions, identify conflicts, preserve unknowns, and produce a first falsifiable contract draft.
