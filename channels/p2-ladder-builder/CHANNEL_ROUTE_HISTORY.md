# CHANNEL_ROUTE_HISTORY

## R1 — historical separated -P1 route

time:
2026-02-12.

route:
`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`.

P2 position:
after P1, before P3.

status:
HISTORICALLY_ACTIVE.

evidence:
P Control Point route authority timeline.

## R2 — direct P0->P1 route

time:
2026-03-05 and 2026-03-06.

route:
`P0 -> P1 -> P2 -> P3 -> P4`.

P2 position:
after P1, before P3.

status:
HISTORICALLY_ACTIVE.

reason for -P1 removal:
NOT_RECOVERED.

## R3 — strong local structural seam

route:
`P1 handoff_packet -> P2 ladder packet -> P3 input/render`.

status:
STRONGLY_RECOVERED.

evidence:
- P1 CHANNEL_INTERFACE_MAP;
- P3 CHANNEL_INTERFACE_MAP;
- multiple supplied/executed P2 packets.

This seam is common to both R1 and R2.

## R4 — P2 side A bridge

route:
P2 ladder-derived compact carry -> A-family targets.

v3.5 primary names:
`A_ULTRA, A0, A1, A2, A3`.

legacy alias:
`A_MINUS_1`.

status:
INTERFACE_RECOVERED / exact production consumers not fully proved.

rule:
A-side handoff does not replace P3.

## Current global route authority

status:
`HOLD_UNRESOLVED`.

owner decision:
C, 2026-10-06.

meaning:
do not declare either R1 or R2 the globally frozen current route.

## Route prohibitions

Do not:
- route P2 directly from free RAW without recovered upstream boundary;
- bypass P1 source lineage;
- treat P2 A-bridge as proof of P3 bypass;
- route P2 directly to canonization;
- resolve -P1 silently.
