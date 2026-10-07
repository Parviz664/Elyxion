# CHANNEL_ROUTE_HISTORY

## Route R1 — early execution-planning route

Versions:
v1.0–v1.2

Route:
E-Prime + E0 + D0 + A2 -> E1 -> D1 + E2
with feedback to E0 in v1.2.

Meaning:
E1 consumes locked constraints and produces execution draft / dependency / rollback planning.

Status:
HISTORICAL / SUPERSEDED.

## Route R2 — v1.3 registry-sealed execution route

Version:
v1.3

Route:
E-Prime registry+seal + E0 + D0 + A2 -> E1 -> D1 + E2
plus E0 feedback.

Meaning:
same execution-draft role, now with no-inference/registry hard gate.

Status:
HISTORICAL / SUPERSEDED.

## Route R3 — SIMULATION_ONLY side route

Observed:
2026-02-18 operational response

Route:
D0 SIM ACK/constraints -> E1 guard adaptation -> E0 simulation-only ingest support.

Constraints:
SIM trace cannot merge with CANON; no runtime claims; no Gate_11/12 canon PASS without REAL_OBSERVED.

Status:
HISTORICAL OPERATIONAL SIDE ROUTE.

Provenance caveat:
E1 response was assistant-generated.

## Route R4 — kernel update REF_ONLY compatibility route

Observed:
2026-02-18

Route:
E-Prime canonical patch -> D0 ref-only ingest -> E1 compatibility ACK / consumer requests -> E0 relock decision + downstream ACK ledger.

Status:
HISTORICAL OPERATIONAL SIDE ROUTE.

## Route R5 — v1.4 dream-safe skeleton route

Version:
v1.4

Route:
E0_LOCKED_CANON_BINDING_PACKET_V1+ -> E1 skeleton
-> E2 Engine Contract Translation
and optional/parallel E3 deterministic build plan.

D1:
optional consumer; psycho touchpoints are not authored in E1.

Status:
HISTORICAL BASIS, evolved further in v1.5/v1.6.

## Route R6 — v1.5 hardened skeleton route

Version:
v1.5

Route:
E0 dual-lock handle -> E1 constrained skeleton -> E2 / E3 bounded handoffs.

Exact packet details:
partially recovered.

Status:
SUPERSEDED by v1.6.

## Route R7 — strongest-known v1.6 route

Version:
v1.6

Route:
E0_LOCKED_CANON_BINDING_PACKET_V1_7
-> E1_CONSTRAINED_IMPLEMENTATION_SKELETON_PACKET_V3
-> E1_TO_E2_ENGINE_CONTRACT_INPUT_V2

Weak visibility:
E1_TO_E3_WEAK_VISIBILITY_INPUT_V1

Interpretation:
E2 is primary functional downstream.
E3 visibility is deliberately weak; E1 does not smuggle build authority.

Status:
ACTIVE STRONGEST-KNOWN.

## P/A bridge status

No direct P -> E1 bridge is recovered.

Historical A relation:
v1.0–v1.3 directly references immutable A2 input.
v1.4+ A2/A3 become ref-only pointers carried through E0 locked handle.

Direct E1 -> A output:
NOT RECOVERED.
