# CHANNEL_FUNCTION_EVOLUTION_MAP

## CHANNEL_STATE_0 — existence-only / early final sorter

time:
by 2026-02-12.

name:
P4 exact human name UNKNOWN.

role label:
`feel_potential_sorter_final` / `feel_potential_sorter_final_cut`.

mission:
select final feel/cut from candidate ladder material.

input:
`ELYX_P4_INPUT_V3` recovered.

upstream:
P3.

downstream:
not fully recovered.

authority:
selection/final-cut role recovered; detailed constraints partial.

status:
PARTIALLY_RECOVERED.

## CHANNEL_STATE_1 — v3.2.0

time:
historically prior to v3.2.1.

version:
3.2.0.

mission:
ordered max-feel shortlist/spine, reserves, montage curve under causal order.

detailed content:
PARTIAL.

known likely historical issue:
later patch explicitly removes/default-decouples P5 binding and makes observables/scoring rules stricter.

status:
PARTIALLY_RECOVERED.

## CHANNEL_STATE_2 — v3.2.1

name:
Canon-ID, Order-Safe, Deterministic v3.2.x.

inputs:
P3 candidate set with IDs/deps; v3.1/v3.2 compatible packet families.

transformation:
preflight -> heuristic scoring -> dependency closure -> order-safe selection -> observable coverage repair -> no-guess duplicate trim -> meta handoff.

new core:
observables-first;
scoring disclaimer;
no-guess duplicates;
ready_for_next;
backbone quota.

forbidden:
rewrite, reorder, invent, world-model scoring, default P5.

outputs:
V3_2 shortlist packet.

status:
EXACT CONTRACT.

## CHANNEL_STATE_3 — v3.2.2

name:
Role-Aware, Late-Bridge-Safe.

new transformation:
role tagging before selection;
late bridge retention check;
terminal mass;
structural-first reason taxonomy;
confidence diagnostics;
role-balance adjustments.

new output:
`ELYX_P4_FILTER_SHORTLIST_PACKET_V3_2_2`.

new route option:
A_ULTRA replaces A_MINUS_1 in options.

status:
EXACT CURRENT CONTRACT.

## CHANNEL_STATE_4 — corrected execution practice

contract version:
still v3.2.2.

what changed:
not a new contract version; execution became stricter.

behavior:
- full dependency-critical spine retained;
- shortlist target can be exceeded by structural necessity;
- late support not cut for climax;
- terminal seal/preseal preserved;
- non-prerequisite support may go to reserves;
- WARN maturity debt carried forward.

why this state matters:
earlier outputs did not actually satisfy dependency closure despite claiming they did.

status:
IMPLEMENTATION-IN-CHAT REPAIR.

## Evolution summary

`final sorter`
-> `deterministic observables-first final cut`
-> `role-aware late-bridge-safe final cut`
-> `contract-faithful full-spine practice`.

No new semantic-authoring authority appears anywhere in the recovered evolution.
