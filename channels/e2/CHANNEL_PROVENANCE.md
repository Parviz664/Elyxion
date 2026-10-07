# CHANNEL_PROVENANCE

## Provenance classes used

- AUTHOR_RAW
- AUTHOR_CONFIRMED
- AUTHOR_DECISION
- USER_SUPPLIED_ARTIFACT
- ASSISTANT_PROPOSAL
- ASSISTANT_INTERPRETATION
- JOINT_ITERATION
- RECOVERED_FROM_LATER_REFERENCE
- GITHUB_ARTIFACT
- UNKNOWN_ORIGIN

## Source register

### Current conversation — highest available source class for exact artifacts

- **SRC-CUR-001** — full user-supplied `ELYX_E2_CHANNEL_SPEC_V1_0_MASTER`. Provenance: USER_SUPPLIED_ARTIFACT.
- **SRC-CUR-002** — full user-supplied `ELYX_E2_CHANNEL_SPEC_V1_1_MASTER`. Provenance: USER_SUPPLIED_ARTIFACT.
- **SRC-CUR-003** — exact command: “Работать строго по контракту Е2.” Provenance: AUTHOR_RAW.
- **SRC-CUR-004** — assistant-generated `ELYX_E2_EXECUTION_RESULT_V1_1` for D1 closure. Provenance: ASSISTANT_PROPOSAL/OPERATIONAL.
- **SRC-CUR-005** — user-supplied `ELYX_E1_SIMULATION_LANE_CONSTRAINT_RESPONSE_V1_2`.
- **SRC-CUR-006** — assistant-generated E2 SIM execution result.
- **SRC-CUR-007** — user-supplied `D1_CONSUMER_COMPAT_ACK_V2_2`.
- **SRC-CUR-008** — assistant-generated E2 REF_ONLY execution result.
- **SRC-CUR-009** — full user-supplied `ELYX_E2_CHANNEL_SPEC_V1_2_MASTER`.
- **SRC-CUR-010** — assistant-generated v1.2 BLOCK execution result.
- **SRC-CUR-011** — full user-supplied `ELYX_E2_CHANNEL_SPEC_V2_1_MASTER`.
- **SRC-CUR-012** — assistant-generated v2.1 BLOCK execution result.

### Prior-conversation recovered sources

- **SRC-MEM-001** — 2026-02-16 21:46:59Z earliest E2 seed. RECOVERED_FROM_LATER_REFERENCE; exact RAW unavailable.
- **SRC-MEM-002** — 2026-02-16 21:53:22Z historical v1.0 appearance.
- **SRC-MEM-003** — 2026-03-13 12:59:12Z full v2.2 was user-supplied; body not recovered here.
- **SRC-MEM-004** — 2026-03-13 13:10:07Z author “чистая E-цепочка” decision.
- **SRC-MEM-005** — 2026-03-13 14:50:32Z full v2.3 was user-supplied; exact identifiers/delta recovered, body not recovered here.
- **SRC-MEM-006** — 2026-03-13 07:09–07:12Z assistant proposes narrower translator role; user explicitly accepts and asks for mature E2 update.

### GitHub sources observed during recovery

Repository: `Parviz664/Elyxion`.

- **SRC-GH-001** — main head at recovery: `01b97c8edd19fdd59f81de827fb5f4a99861048f`, 2026-10-07, “docs: index Eco-Systems Elyxion channel”.
- **SRC-GH-002** — branch inventory before recovery contained E-Prime, P-channel recovery branches, UFO navigator, main; no branch matching “e2”.
- **SRC-GH-003** — code-search index reported unavailable/no E2 results; therefore this is **not** used as proof that no historical E2 content existed anywhere.
- **SRC-GH-004** — repository main commit history before this recovery contained no E2 recovery commit.

## Critical provenance law

`USER_SUPPLIED_ARTIFACT ≠ AUTHOR_RAW`.

A user-supplied JSON may have assistant-originated wording. Prior context indicates the assistant proposed/drafted the v2.2 direction before the full v2.2 master was later supplied by the user. The recovery therefore records origin evidence and later owner acceptance separately.
