# CHANNEL CONTRACT — RECOVERED CURRENT STRONGEST-KNOWN

**Source contract:** `ELYX_D1_CHANNEL_SPEC_V2_4_MASTER`  
**Version:** 2.4.0  
**Recovery mode:** faithful extraction, not a new version.

## Determinism

The exact supplied v2.4 contract requires:

- deterministic output;
- locked field order;
- no free text outside JSON;
- no schema drift;
- semantic versioning;
- SHA-256 input/output hash policy;
- same input → same output hash.

## Strict schema

The contract requires:

- additional input properties: false;
- additional output properties: false;
- fail fast on schema mismatch;
- reject unknown fields;
- reject type mismatch;
- reject enum violations;
- reject missing required fields.

This requirement is historically important because several assistant-generated reports in the conversation did not satisfy it. Those are preserved as errors, not silently normalized.

## D Registry + Seal no-inference contract

Required refs:

- `D_PACKET_REGISTRY_REF`
- `D_REGISTRY_SEAL_REF`

D1 cannot make `PASS` or `PASS_WITH_WARNINGS` and cannot propose interventions when required D-registry refs are missing, seal is untrusted, hashes mismatch, or a required input is marked `MISSING`.

Waiver is bounded and never permits:

- severe-harm override for critical segments;
- locked-context desync;
- critical uncertainty breach;
- implementation-fidelity breach;
- dark patterns/compulsion.

## Prompt-injection hardening

v2.4 explicitly blocks attempts to:

- override policy;
- ignore rules;
- waive severe-harm guards;
- bypass uncertainty;
- bypass Registry/Seal or no-inference;
- mutate locked context/sync seed;
- introduce compulsion/dark patterns;
- inject E-channel logic/refs;
- authorize runtime.

## Release decision

Allowed:

- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCK`

PASS requires all hard gates:

- comfort;
- fairness;
- harm;
- uncertainty;
- recovery;
- anti-boredom;
- fidelity;
- locked-context consistency;
- D Registry + Seal verification.

PASS_WITH_WARNINGS is limited to non-critical issues and additionally requires:

- no severe harm;
- fidelity >= 98.8;
- locked-context PASS;
- D Registry+Seal PASS;
- uncertainty PASS.

## Statistical / causal gate

Both must pass:

- statistical gate;
- causal-stability gate.

Interventions also require positive holdout/replay behavior.

## Current KPI thresholds

Global:

- FPS p95 >= 48;
- frame time p95 <= 20 ms;
- touch-to-response p95 <= 75 ms;
- crash-free sessions >= 99.75%;
- battery drop <= 9.5% / 30 min;
- comfort coverage CI95 lower >= 96.5;
- recovery resilience >= 90;
- boredom drift <= 34;
- contemplation presence >= 64;
- cognitive strain <= 40;
- return quality >= 66;
- implementation fidelity >= 99.3%;
- locked-context consistency 100%;
- Registry/Seal pass 100%.

Critical segments:

- coverage CI95 lower >= 92;
- CI width <= 6.5%;
- recovery resilience >= 86;
- boredom drift <= 39;
- cognitive strain <= 43;
- severe harm allowed = 0.

## Fidelity

`D_Implementation_Fidelity_Report` fields per requirement:

- requirement_id;
- specified;
- implemented;
- matched_pct;
- evidence_ref;
- status;
- reason_if_not_matched;
- fix_plan.

Thresholds:

- critical requirements = 100%;
- non-critical >= 97%;
- overall >= 99.3%.

## Locked-context contract

Must match:

- `d0_locked_anchor_id`
- `d0_input_contract_hash`
- `d0_trace_root_id`
- `d0_schema_version`
- `d0_mode`
- `d_sync_seed_packet_id`

The exact v2.4 scope names current expected values:

- anchor: `D0-ANCHOR-DLINE-LOCK-V1`
- input hash: `DLINE_SCOPE_LOCKED_HASH_V1`
- trace root: `TRACE-DLINE-BOOTSTRAP-V1`
- schema: `D0_SCHEMA_VNEXT`
- mode: `DLINE_CANON_STRICT`

These are contract expectations; this recovery does not claim they have been observed in a real runtime packet.

## Governance

Can block:

- D1 lead;
- Technical Director.

Block override requires Program Owner + Technical Director joint signoff.

No override for:

- critical severe harm;
- schema failure;
- critical uncertainty breach;
- fidelity breach;
- critical harm/recovery breach;
- locked-context failure;
- Registry/Seal failure;
- prompt-injection detection.

## Current contract status

`CONTRACTED`, but runtime execution readiness is not proven because no trusted D Registry/Seal + real-device evidence bundle was recovered in this archaeology.
