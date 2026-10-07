# CHANNEL PROVENANCE

## Provenance laws

`SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR`

`ASSISTANT_RATIONALE != AUTHOR_RATIONALE`

`ASSISTANT_OUTPUT != CANON`

## Source catalogue

### SRC-D0-001
Date: 2026-02-16 11:52:28Z
Class: AUTHOR_RAW / RECOVERED_FROM_PRIOR_CONVERSATION
Exact:
«D0 тоже создаем, как ты сказал, ядро, то, чего нельзя изменять»
Supports: earliest recovered D0 seed.
Ceiling: HIGH.

### SRC-D0-002
Date: 2026-02-16 20:38:16Z
Artifact: ELYX_D0_CHANNEL_SPEC_V1_0_MASTER
Class: USER_SUPPLIED_ARTIFACT
Supports: first recovered versioned master.
Ceiling: VERY HIGH for artifact content; UNKNOWN for line authorship.

### SRC-D0-003
Immediately after v1.0
Class: ASSISTANT_PROPOSAL
Supports: six hardening suggestions.
Ceiling: HIGH as history of assistant behavior; zero owner-authority by itself.

### SRC-D0-004
Date: 2026-02-17 21:36:35Z
Artifact: ELYX_D0_CHANNEL_SPEC_V1_1_MASTER
Class: USER_SUPPLIED_ARTIFACT
Supports: v1.1 lineage, E0 v1.3/E4/D4 alignment.
Ceiling: VERY HIGH for artifact content.

### SRC-D0-005
Date: 2026-02-17 21:44:17Z
Class: AUTHOR_RAW / RECOVERED_FROM_PRIOR_CONVERSATION
Exact excerpt:
«…копи-пасту делаю в D0. D0 уже тоже самое делает, ядро… психологическое ядро… для D1-канала… скорее всего… для Е1…»
Supports: owner-facing role meaning.
Ceiling: HIGH.

### SRC-D0-006
Date: 2026-02-17 21:46:54Z
Class: AUTHOR_RAW / RECOVERED_FROM_PRIOR_CONVERSATION
Exact route:
`E’ → A2 → E0 → D0 → E1 → D1`
Ceiling: HIGH.

### SRC-D0-007
Date: 2026-02-17 22:44:58Z
Class: AUTHOR_RAW
Exact:
«Просьба работать строго по контракту Д0!!!»
Ceiling: VERY HIGH.

### SRC-D0-008
Artifact: ELYX_E0_DECISION_PACKET_V1_3
Class: USER_SUPPLIED_ARTIFACT
Supports: historical v1.1 ingress.
Ceiling: VERY HIGH for supplied fields.

### SRC-D0-009
Artifact: ELYX_D0_EXECUTION_RESULT_V1_1
Class: ASSISTANT_OUTPUT
Supports: historical execution attempt.
Ceiling: HIGH for what assistant emitted; LOW for empirical psych claims.

### SRC-D0-010
Artifact: ELYX_D0_ACK_PROCESSING_RESULT_V1_1
Class: ASSISTANT_EXTENSION
Supports: SIM lane handling history.
Ceiling: MEDIUM as D0 authority because master interface did not explicitly define this side path.

### SRC-D0-011
Artifact: ELYX_D0_EPRIME_PATCH_INGEST_RESULT_V1_1
Class: ASSISTANT_EXTENSION
Supports: EPrime v1.2.1 ref-only handling history.
Ceiling: MEDIUM as authority.

### SRC-D0-012
Date: 2026-02-20 11:10:23Z
Artifact: ELYX_D0_CHANNEL_SPEC_V1_2_MASTER
Class: USER_SUPPLIED_ARTIFACT
Supports: registry+seal/no-inference era.
Ceiling: VERY HIGH.

### SRC-D0-013
Artifact: ELYX_D0_INGRESS_EVALUATION_RESULT_V1_2
Class: ASSISTANT_OUTPUT
Supports: historical block against insufficient upstream state.
Ceiling: HIGH for assistant action.

### SRC-D0-014
Date: 2026-02-26 19:52:52Z
Artifact: ELYX_D0_CHANNEL_SPEC_V2_0_MASTER
Class: USER_SUPPLIED_ARTIFACT
Supports: current strongest-known D-only refactor.
Ceiling: VERY HIGH for artifact content.

### SRC-D0-015
Artifact: ELYX_D0_SPEC_REVIEW_RESULT_V2_0
Class: ASSISTANT_INTERPRETATION
Supports: unresolved coverage/binding/migration gaps.
Ceiling: MEDIUM-HIGH; not owner-confirmed.

### SRC-D0-016
Date: 2026-10-07
Source: GitHub searches in Parviz664/Elyxion
Class: GITHUB_ARTIFACT / NEGATIVE_SEARCH_RESULT
Result:
- no D0 branch before this recovery
- no D0 code-search match on main
- no D0 issue/PR/commit search hit
Supports: no previously found durable D0 recovery implementation.
Ceiling: HIGH for searched surfaces, not proof of universal absence across all historical inaccessible data.

## Authority ordering used

1. exact author raw / explicit author decision
2. user-supplied historical artifact
3. GitHub durable evidence
4. later references
5. assistant output
6. recovered summaries/context
7. inference

Inference is never promoted to fact.
