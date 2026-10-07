# CHANNEL_CONTRACT

## Current strongest recovered contract

Source:
`raw-evidence/EV_AU_002_V4_3_LAW_USER_SUPPLIED.json`

Evidence class:
`USER_SUPPLIED_ARTIFACT`.

Authorship ceiling:
supplied by the owner; line-by-line human authorship is not independently proven.

## Identity

- public: A-Ultra / AUltra
- canonical ref: A_ULTRA
- compatibility agent role: A_MINUS_1_VISION_TRANSLATOR
- law: ELYX_A_ULTRA_LAW_v4.3_DREAMVAULT_CONSTRAINTS_TRANSPORTSAFE_DUAL_ANCHOR
- semver: 4.3.0
- supersedes: ELYX_-A1_LAW_v4.2_DIRECT_PASTE_ZERO_MANUAL_PLUS

## Core contract

1. One upstream artifact per message.
2. One JSON root for transport-safe mode.
3. No manual mode selection.
4. Canon is grounded only.
5. DreamVault is non-canon expression storage, never a logic source.
6. Post-P5 canon is dual-anchored to P5 spine plus preserved vision text when present.
7. Missing P5 logic/backbone safety information forces conservative handling.
8. Grounded claims and poetic quotes are separated.
9. Ambiguity is recorded, not silently guessed.
10. Handoff defaults to A0.

## Source precedence

`A0_ROUTED_PACKET > P5_PACKET > A_ULTRA_VISION_ARTIFACT_LEGACY > A_MINUS_1_VISION_ARTIFACT_LEGACY > RAW_VISION_TEXT > UNKNOWN_JSON`

## Mode rules

- default: hard_guard
- P5 may reach creative_amplify only with quality threshold plus logic/backbone safety
- unknown/raw/legacy use hard_guard_with_dreamvault_only under the supplied rule
- creative amplification never edits canon

## Release constraints

Must pass:
- preserved text match
- no canon invention
- grounding complete
- semantic drift guard
- canon/non-canon leak test
- source trace complete/autofilled
- transport envelope present

Hard fail:
- new feature in canon
- ungrounded canon
- bad P5 source binding
- multiple payloads
- single-root violation

## Contract status

`CONTRACT_RECOVERED / STATIC_ONLY`.

No executable validator implementation for this channel was recovered from GitHub before this branch.
