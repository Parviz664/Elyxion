# CHANNEL_ROUTE_HISTORY

## Route R1 — historical separated -P1 family
time:
2026-02-12 recovered historical state.
route:
P0 -> -P1 -> P1 -> P2 -> P3 -> P4.
P3_local_position:
after P2, before P4.
status:
HISTORICAL / global current authority not implied.
evidence:
P_SYSTEM_ROUTE_AUTHORITY_TIMELINE_V0_1.md.

## Route R2 — direct P0->P1 family
time:
2026-03-05 and 2026-03-06 recovered working state.
route:
P0 -> P1 -> P2 -> P3 -> P4.
P3_local_position:
after P2, before P4.
status:
HISTORICALLY_ACTIVE.
evidence:
P Control Point route timeline and P3 contract recovery.

## Route R3 — exact P2->P3 input seam
time:
March 2026 practice.
route:
ELYX_P2_LADDER_PACKET / p2_packet_ref
-> ELYX_P3_INPUT_V3 / V3_2
-> rendered ladder packet.
status:
STRONGLY_RECOVERED.
evidence:
full P3 specs in current channel + multiple P2 packets.

## Route R4 — P3->P4 handoff
time:
recovered March practice.
route:
P3 rendered ladder
-> ELYX_P4_INPUT_V3 candidate_items_ref
-> P4 feel-potential / final-cut layer.
status:
STRONGLY_RECOVERED locally.
evidence:
P3_CONTRACT_RECOVERY_PASS_V0_1.md and P Chain role spine.

## Route R5 — one-root A3 readiness
time:
v3.1.1+.
route:
P3 output marked one_root_ready_for_A3.
status:
INTERFACE_READINESS_ONLY.
evidence:
full v3.1.1 and v3.2.0 supplied specs.
not_proved:
that A3 is the direct production downstream consumer of P3.

## Current route statement

Global route:
HOLD_UNRESOLVED because current standalone -P1 authority remains unresolved.

Local P3 seam:
P2 -> P3 -> P4 is common to both recovered route families and therefore currently strong.

## Route prohibitions

Do not:
- claim -P1 is currently removed;
- claim -P1 is currently active;
- route P3 directly from RAW without recovered intermediary contracts;
- route P3 directly to canonization;
- convert A3-readiness into a proved direct route;
- treat historical route family as current merely because it is newer than another historical family.
