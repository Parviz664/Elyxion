# CHANNEL_INTERFACE_MAP

## Later upstream: P0
Observed P1 input family: `ELYX_P1_INPUT_V1`.
Common fields:
project anchor, stage scope, mode, index range, output-size hint, author-intent lock, raw author text.

## Historical upstream: -P1
Route A placed -P1 before P1.
Exact -P1->P1 packet schema is not recovered.

## Main downstream: P2
P1 `handoff_packet` carries at least:
map ID, author intent lock, compact topic entities, compact blocks, linear order, compact micro-stage catalog, drift guards, resume token.
P2 must preserve binding to P1 micro-stage IDs.

## A interface
`handoff_packet_to_A` carries compact entities/blocks/invariants/nogo/domino risks/pressure axes/trigger types/mechanism classes/resume token.
It must not contain full micro-stage bodies or implementation leakage.

## P3/P4
They are downstream in the wider P-chain, but the structural handoff from P1 is primarily to P2.

Authority law:
P1 maps -> P2 refines/expands with lineage -> P3 renders without semantic strengthening -> P4 filters/selects without rewrite or auto-canonization.
