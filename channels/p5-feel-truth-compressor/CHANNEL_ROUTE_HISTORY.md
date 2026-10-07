# CHANNEL_ROUTE_HISTORY

## R-P5-0 — unnamed precursor route
route:
UNKNOWN.
time:
UNKNOWN.
evidence:
archived feeling/trajectory concept.
status:
UNKNOWN / POSSIBLE_PRECURSOR_ONLY.

## R-P5-1 — v1.1 local seam
route:
P4 shortlist/spine -> P5.
date:
2026-02-05.
downstream:
UNKNOWN.
evidence:
prior-conversation recovery.
status:
HISTORICAL_STRONGLY_RECOVERED_LOCAL_INPUT.

## R-P5-2 — v1.2 local seam
route:
P4 -> P5.
date:
2026-02-05 onward.
downstream:
NOT_RECOVERED.
status:
HISTORICAL_PARTIAL.

## R-P5-3 — current v1.3 optional route
route:
P4 -> P5 -> A0 or A_MINUS_1.
condition:
P5 only if explicit `enable_p5=true`.
A usage:
presentation-only; canonical trace still requires upstream P3/P4.
status:
ACTIVE CURRENT CONTRACT.

## R-P5-4 — E-channel consumption
route:
P4 -> optional P5 -> E-channel.
condition:
optional.
allowed payload:
text/rhythm/experience layer only.
forbidden:
implementation causality.
status:
ACTIVE CURRENT CONTRACT.

## R-P5-5 — current P4 bypass route when P5 disabled
source:
current supplied P4 packet.
route options:
P4 -> P3 (patch)
or
P4 -> P2 (expand)
or
P4 -> A_MINUS_1
or
P4 -> A0.
P5:
not default; explicitly disabled in that task.
status:
ACTIVE TASK PRACTICE.

## Durable P-system topology caveat

GitHub P Control Point branch recovers a core P0..P4 role spine:
P0 -> P1 -> P2 -> P3 -> P4
with a historical alternate including -P1.

P5 is absent from that durable core registry.

Interpretation allowed:
P5 is not proven to be part of that core spine.

Interpretation forbidden:
"P5 never existed" or "P5 was deleted" — neither follows from the omission.
