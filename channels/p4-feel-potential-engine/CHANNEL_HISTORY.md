# CHANNEL_HISTORY

## Recovery principle

This file preserves different historical states instead of projecting v3.2.2 backward.

## Epoch 0 — before earliest recovered P4 evidence

Exact birth message: **UNKNOWN**.

No recovered evidence in this pass proves:
- the first day P4 was invented;
- the exact first name;
- a pre-v3.2 contract;
- the author's original rationale.

Status:
`UNKNOWN_PREHISTORY`.

## Epoch 1 — P4 exists in the separated -P1 route

Recovered prior-conversation evidence dated 2026-02-12 contains a user-supplied Elyxion passport with:

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

Recovered P4 label:
`feel_potential_sorter_final` / later recovered as `feel_potential_sorter_final_cut`.

Recovered packet family:
`ELYX_P4_INPUT_V3`.

Recovered fields include:
- `feel_goal_profile`;
- `candidate_items_ref`.

Recovered role:
final feel-potential sorting / final cut from candidate ladder material.

A v3.2.0 P4 existence is recovered from prior conversation context, but the full byte-exact v3.2.0 body is not present in this branch.

Status:
`EXISTENCE_AND_ROLE_RECOVERED / FULL_CONTRACT_PARTIAL`.

## Epoch 2 — March route transition; P4 remains terminal P node

Recovered P0 artifacts on 2026-03-05 move the working route to:

`P0 -> P1 -> P2 -> P3 -> P4`

with:
- `NO_-P1`;
- `P5: disabled by author`;
- `must_not_output_P5`.

P4 remains downstream of P3.

The owner rationale for removing standalone -P1 is not recovered.
Do not attribute a reason.

Status:
`HISTORICALLY_ACTIVE_ROUTE_STATE`.

## Epoch 3 — v3.2.1 deterministic/order-safe hardening

Exact user-supplied artifact in this conversation:

`ELYX_P4_SPEC_V3_2`
with semver `3.2.1`.

Human name:
`P4 Feel Potential Engine (Canon-ID, Order-Safe, Deterministic v3.2.x)`.

The artifact explicitly says v3.2.1 is an append-only patch to v3.2.0.

Named deltas:
1. observables-first axes replace emotion labels as primary selection basis;
2. scoring weights are internal heuristics, not a world model;
3. no-guess duplicate policy;
4. `ready_for_next` replaces default P5 routing;
5. backbone quota protects the shortlist from becoming a “трейлер”;
6. source fingerprints/binding refs become optional evidence for duplicate/binding proof.

Legacy fields `required_axes` and `ready_for_p5` remain only for compatibility.

Status:
`EXACT_VERSION_RECOVERED`.

## Epoch 4 — first recovered v3.2.1 execution exposes implementation defects

A P3 packet with B001..B026 was processed.

P4 produced a 12-node shortlist and reserves.

However, the selected spine omitted intermediate required dependencies while reporting `dependency_integrity=true`.
Example:
B004 depended on B003, but B003 was reserve/not spine.

The same output also treated range length 26 as `full (range_len<=20)`, contradicting the adaptive window rule.

This is part of P4 history and is not erased.

Status:
`IMPLEMENTATION_IN_CHAT / CONTRACT_VIOLATION_DETECTED`.

## Epoch 5 — v3.2.2 role-aware and late-bridge-safe hardening

Exact user-supplied artifact:
`ELYX_P4_SPEC_V3_2_2`, semver `3.2.2`, superseding 3.2.1.

New hardening:
- node-role discipline;
- late speculative bridge anti-overcompression;
- structural-first reasons;
- shortlist role balance;
- terminal mass control;
- confidence diagnostics v2;
- role-balance scoring adjustments;
- reserve reason taxonomy;
- next-channel policy hardening.

Human name becomes:
`P4 Feel Potential Engine (Canon-ID, Order-Safe, Deterministic v3.2.x, Role-Aware, Late-Bridge-Safe)`.

Output family becomes:
`ELYX_P4_FILTER_SHORTLIST_PACKET_V3_2_2`.

Status:
`EXACT_VERSION_RECOVERED`.

## Epoch 6 — early v3.2.2 execution still violates dependency closure

The first v3.2.2 re-selection over the older 26-node linear ladder still omitted dependencies while claiming integrity.

Therefore the contract upgrade did not instantly guarantee correct execution.

Status:
`IMPLEMENTATION_ERROR_PERSISTED_AFTER_CONTRACT_UPGRADE`.

## Epoch 7 — full-spine repair behavior emerges

Later P3 packets are already role-aware/densified:
- 14-node origin-to-replicators packet;
- 19-node densified origin-to-replicators packet;
- 28-node robotic affective architecture;
- 5-node Stage 1 minimal visual vocabulary;
- 6-node Phases 1–3 normalization.

P4 increasingly preserves complete dependency-critical paths, even when that means overriding the target shortlist cardinality.

This produces:
- full spine when structurally mandatory;
- reserves only for non-prerequisite support nodes;
- explicit late-bridge maturity debt;
- terminal seal/preseal preservation.

This is the first recovered practice that actually matches the strongest dependency/late-bridge contract consistently.

Status:
`IMPLEMENTATION_IN_CHAT_STRONGLY_ALIGNED`.

## Epoch 8 — P Control Point durable recovery

GitHub branch recovery contains:
`channels/p-control-point/recovery/P4_CONTRACT_RECOVERY_PASS_V0_1.md`.

It independently recovers:
- P4 as feel-potential/final-cut layer;
- P3 -> P4 seam;
- author-selection boundary;
- source-order/dependency preservation;
- no semantic invention;
- P4 as terminal P-layer in recovered role spine.

That recovery marked version lineage PARTIAL.
The present channel contains stronger direct v3.2.1 and v3.2.2 artifacts, so version recovery can now be narrowed without erasing the earlier evidence ceiling.

## Current strongest interpretation

Evidence-backed evolution:

`P4 exists as final feel sorter`
-> `v3.2.0 partial historical recovery`
-> `v3.2.1 observables-first deterministic hardening`
-> `execution defects expose closure/window failures`
-> `v3.2.2 role-aware late-bridge hardening`
-> `later full-spine execution repairs actual dependency behavior`.

No pre-v3.2 detailed contract is invented.
