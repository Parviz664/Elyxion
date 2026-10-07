# CHANNEL_ROUTE_HISTORY

## R-AU-001 — early P5/A0 gateway loop

Evidence date:
2026-02-26 recovered conversation.

Observed:
`P5 → A0 v2.2 → A_MINUS_1 v4.2 → A0`.

Evidence:
user-supplied gateway/runtime artifacts.

Status:
HISTORICAL.

## R-AU-002 — A0 v3.0 gateway relation

Date:
2026-03-02.

Observed:
A0 v3.0 accepts A_MINUS_1/P/A/unknown/raw inputs and can route unknown/vision material toward A_MINUS_1.

A_MINUS_1 v4.2 itself defaults handoff to A0.

Status:
HISTORICAL / RECOVERED.

## R-AU-003 — v4.2 formal inbound

`A0_ROUTED_PACKET → A_MINUS_1`
`P5_PACKET → A_MINUS_1`
legacy/raw/unknown → A_MINUS_1 conservatively.

Outbound:
A_MINUS_1 → A0.

Status:
HISTORICAL CONTRACT.

## R-AU-004 — v4.3 formal inbound

`A0_ROUTED_PACKET → A_ULTRA`
`P5_PACKET → A_ULTRA`
legacy/raw/unknown → A_ULTRA.

Outbound:
A_ULTRA → A0.

Status:
ACTIVE CONTRACT.

## R-AU-005 — later adult route

Recovered from A0 v4.1, 2026-03-09:
`P → A_ULTRA → A0 → E0`.

Status:
STRONGEST_KNOWN LATER TOPOLOGY.

Caveat:
"P" is aggregate; exact immediate producer is not established by this artifact alone.

## R-AU-006 — direct P4 route attempt

P4 advertises `A_ULTRA` while P5 is disabled for that packet.

Observed processing:
P4 direct → A_ULTRA source detection falls to UNKNOWN_JSON → WARN / hard_guard_with_dreamvault_only.

Status:
OBSERVED_BUT_CONTRACT_MISMATCHED.

## R-AU-007 — A1 adjacency across epochs

Earlier A0/A_MINUS_1 runtime flows could continue toward A1 through A0.

Later A0 v4.1 shifts the adult route toward E0.

Status:
MULTI-EPOCH; preserve both, do not choose one retroactively.
