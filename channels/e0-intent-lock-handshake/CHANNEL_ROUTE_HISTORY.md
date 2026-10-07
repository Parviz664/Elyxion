# CHANNEL_ROUTE_HISTORY

## ROUTE-A — v1.1 original
E-Prime packet -> E0 <- A2 response
E0 -> downstream after dual validation

Status: HISTORICAL.
Base v1.1 downstream is generic; later bootstrap packet explicitly permits E1-E6.

## ROUTE-B — v1.1 patched / v1.2
E-Prime bootstrap anchor -> E0
A2 packet/system map from accepted location -> E0
E0 -> E1..E6 under BOOTSTRAP_LIMITED when not hard blocked
Closure evidence may arrive by delta.

Status: HISTORICAL.

## ROUTE-C — v1.3
A2 and/or A3-packaged handshake -> E0
E0 -> E1,D1,E2,D2,E3,D3,E4,D4,E5,E6
Sync ACK focus -> E1,D1,E4,D4

Status: HISTORICAL / TRANSITIONAL.

## ROUTE-D — v1.4
E-Prime registry+seal truth -> E0
A3/A2 sealed input -> E0
No verified registry+seal -> BLOCK

Observed A3 A2-only input: BLOCK.
Status: HISTORICAL / immediate precursor to v1.5.

## ROUTE-E — v1.5 strongest-known
E6_KERNEL_BUNDLE_REF_ONLY -> E0
A3 release/dream seal -> E0
E0 -> E0_LOCKED_CANON_BINDING_PACKET_V1

Planning:
E1,E2,E3,D1,D2,D3,D4,E4

Runtime-promotion-only:
E5,E6

Status: ACTIVE CONTRACT / NOT OPERATIONALLY PROVEN GREEN.

## E6 dual-role observation
v1.5 uses E6 both as upstream kernel-bundle carrier and later runtime-promotion stage.
This is explicit. Recovery does not invent an internal distinction.

Classification:
EXPLICIT_TOPOLOGY_WITH_UNRESOLVED_ROLE_DETAIL.

## P/A relationship
No direct P-channel -> E0 route is proved.

A relationship:
- A2 direct upstream historically;
- A3 carrier/packager by v1.3;
- A3 explicit dream-lock upstream in v1.5.
