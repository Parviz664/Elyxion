# EV-AU-003 — ROUTE / RUNTIME EVIDENCE

This file preserves event-level recovery facts and exact short excerpts where available. It is not a raw transcript archive.

## 2026-02-26 — early A0/A_MINUS_1 gateway

Recovered user-supplied A0 v2.2 identity:
`A0_ORCHESTRATOR_v2.2_ZERO_MANUAL_STABLE_GATEWAY`.

Recovered behavior:
P5 packet accepted by A0 and prepared for next agent `A_MINUS_1`.

Recovered A_MINUS_1 v4.2 task:
`ELYX-SEAL-V8-SOUND-STABILITY-20260226-2a7f8c19`.

Provenance:
RECOVERED_FROM_CONVERSATION_INDEX + USER_SUPPLIED_CHAT_ARTIFACT.

## 2026-03-02 — A0 v3.0

Recovered law:
`ELYX_A0_LAW_v3.0_COPY_PASTE_PROOF_GATEWAY`.

Recovered behavior:
A0 accepted A_MINUS_1/P/A/unknown/raw families and could route unknown material to A_MINUS_1.

## 2026-03-09 — later adult topology

Recovered A0 v4.1 artifact:
`P → A_ULTRA → A0 → E0`.

## Direct P4 evidence

Current user-supplied P4 packet includes:

`"p5_enabled_by_author": false`

`"next_channel_options": ["P3 (patch)", "P2 (expand)", "A_ULTRA", "A0"]`

and:

`"Рациональный следующий шаг — P2 (expand) по B012..B019, затем уже A_ULTRA."`

This proves the P4 artifact considered A_ULTRA reachable while P5 was disabled for that packet.

It does not prove that A-Ultra v4.3 formally recognized P4.

## Observed A-Ultra handling

Assistant runtime output classified that direct P4 packet as `UNKNOWN_JSON` and used `hard_guard_with_dreamvault_only`, producing WARN.

Provenance:
ASSISTANT_RUNTIME_OUTPUT. Behavior evidence only.

## GitHub pre-write state

Navigator V0.2 previously classified A-channel surfaces as:
`NOT OBSERVED IN CURRENT GITHUB SURFACES`.

Fresh inventory before this recovery also contained no A-Ultra recovery branch.

This branch is therefore a new durable recovery surface.
