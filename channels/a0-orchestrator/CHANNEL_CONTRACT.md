# CHANNEL_CONTRACT — recovered, not redesigned

## Contract invariants

1. **Structural-only authority.**
2. **No canon invention.**
3. **No semantic paraphrase as repair.**
4. **One payload at ingest in v2.2/v3.0.**
5. **Deterministic repair only.**
6. **Explicit patch evidence for any repair.**
7. **No unresolved placeholders/concat artifacts in routed payload.**
8. **Uncertainty remains uncertainty.**
9. **Routing is contract-driven, not guessed.**
10. **A0 is stateless across messages unless a future explicit contract says otherwise.**

## Exact v2.2 contract facts

- law: `ELYX_A0_LAW_v2.2_ZERO_MANUAL_STABLE_GATEWAY`
- semver: 2.2.0
- statuses: PASS / PASS_WITH_PATCH / FAIL
- default unknown parse-valid route: A_MINUS_1
- fail route: USER
- binding payload type: CANON_BINDING_PACKET_V2
- patch pipeline:
  S1_UNICODE_CLEAN → S2_WHITESPACE_NORMALIZE → S3_QUOTE_NORMALIZE → S4_TRAILING_COMMA_REPAIR → S5_ESCAPE_REPAIR → S6_CONCAT_ARTIFACT_REPAIR → S7_PARSE_VALIDATE
- direct-paste / one-payload gate
- output forward field: string `next_message_to_next_agent`

## Exact v3.0 contract facts

- law: `ELYX_A0_LAW_v3.0_COPY_PASTE_PROOF_GATEWAY`
- semver: 3.0.0
- supersedes v2.2
- routed payload must be JSON object, never stringified JSON
- single forward field: `copy_paste_payload_object`
- operator-grade chunking: ORDERED_CONCAT
- same deterministic repair pipeline
- route overrides:
  - CANON_BINDING_PACKET_V2 → A1
  - A1_ARCH_ANCHOR_V3 → A2
  - A2_SYSTEMS_MAP_V4 → A3
- A3 bundle auto-build is limited by statelessness + one-payload gate

## Recovered v4.1 contract facts

- law: `ELYX_A0_LAW_v4.1_POST_A_ULTRA_CRYSTAL_CARRY_GATE_E0_ALIGNED`
- supersedes v4.0/v3.0/v2.2
- CRYSTAL_CARRY
- zero-mutation structural bridge
- adult route P → A_ULTRA → A0 → E0
- legacy A1/A2/A3 only compatibility/recovery
- adult mode cannot silently downgrade
- recovered readiness values:
  - READY_FOR_E0
  - READY_FOR_E0_WITH_CONSTRAINTS
  - BLOCKED_FOR_E0
- missing/broken source trace can block E0
- full schema: UNKNOWN

## Contract ambiguity retained

v3.0 says:
- allowlist-first extraction;
- do not inject new canon fields;
- bind output payload type = CANON_BINDING_PACKET_V2.

For upstream P packets that do not already contain `canon_spec`, the exact lawful projection shape is not fully specified in the recovered text. Earlier assistant executions nested P5 content under a new `canon_spec` wrapper. That may be packaging, but it is not explicitly proven by the law text.

Status: **OPEN CONTRACT AMBIGUITY**, not silently resolved here.
