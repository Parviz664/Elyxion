# D4 — Psycho-Operational Trajectory Stabilization

Recovery status: `SELF_RECOVERY_PASS_WITH_GAPS`

Channel ID: `D4_PSYCHO_OPERATIONAL_TRAJECTORY_STABILIZATION`

Current strongest-known contract: `ELYX_D4_CHANNEL_SPEC_V1_2_MASTER` / `1.2.0`

Current execution posture: `BLOCKED_UNTIL_D_REGISTRY_AND_SEAL_VERIFIED`

## Purpose of this recovery

This directory reconstructs the historical D4 channel without pretending that the current v1.2 form existed from the beginning.

Two proven eras are preserved separately:

1. **E4-baseline era** — D4 operated as a psycho-operational stabilization layer over immutable E4, inside a mixed E/D dependency graph.
2. **D-line-only era** — v1.2 explicitly removed all E* dependencies and rebound D4 to D0→D1→D2→D3, with immutable D3 baseline, D-registry+seal, no-inference, anti-injection and semantic-shadow protection.

The older route is historical and superseded, not erased.

## Evidence law

- `SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR`
- `ASSISTANT_RATIONALE != AUTHOR_RATIONALE`
- `RECOVERED_SUMMARY != EXACT_RAW`
- assistant PASS packets do not self-certify missing evidence;
- missing history remains `UNKNOWN`;
- artifact-internal IDs/dates are not treated as conversation timestamps unless independently supported.

## Current truth

The v1.2 spec says D4 is D-line only. It may evaluate psycho-operational portability and emit append-only stabilization overlays over D3, but may not mutate D3/D2/D1/D0, infer missing registry inputs, bypass D1 guards, import E-channel logic, or perform runtime/build/release execution.

The last recovered strict v1.2 run BLOCKED because `D_PACKET_REGISTRY_REF` and `D_REGISTRY_SEAL_REF` were missing.

`SPEC_READY != EXECUTION_READY`

## Files

- `CHANNEL_IDENTITY.md`
- `CHANNEL_HISTORY.md`
- `CHANNEL_TIMELINE.md`
- `CHANNEL_ROLE_CORE.md`
- `CHANNEL_CONTRACT.md`
- `CHANNEL_BOUNDARIES.md`
- `CHANNEL_VERSION_LINEAGE.md`
- `CHANNEL_DECISION_LOG.md`
- `CHANNEL_ROUTE_HISTORY.md`
- `CHANNEL_INTERFACE_MAP.md`
- `CHANNEL_PROVENANCE.md`
- `CHANNEL_ERRORS_AND_CORRECTIONS.md`
- `CHANNEL_GAP_REGISTER.md`
- `CHANNEL_UNKNOWN_REGISTER.md`
- `CHANNEL_SELF_UNDERSTANDING_REPORT.md`
- `raw-evidence/README.md`
- `recovery/SELF_AUDIT.md`

No recovery content is written into the E-Prime Chat Archive.
