# P0_ROUTE_RECOVERY_PASS_V0_1

Status: `RECOVERY_COMPLETE_WITH_VERSIONED_ROUTE_CHANGE`

Target: `P0`

Parent control: `P_CONTROL_POINT_V0.1`

## 1. Purpose

Recover how P0 routing changed across historical Elyxion P-channel versions, without silently deciding the present authority of `-P1`.

## 2. February 2026 state

Recovered direct user-supplied P0 rules from February 2026 define:

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

P0 behavior at that point:

- normalize one author line;
- emit JSON-only;
- do not generate world/lore/code;
- do not skip channels;
- do not output P5;
- emit downstream inputs including a `minus_p1_input`.

Historical `-P1` role in that route:

`reality_skeleton_causal_chain`.

## 3. March 5 — P0 output v2.3

Recovered direct user-supplied output:

`ELYX_P0_OUTPUT_V2_3`

Routing:

`["P0","-P1","P1","P2","P3","P4"]`

Normalized inputs included:

- `minus_p1_input`
- `p1_input`
- `p2_input`
- `p3_input`
- `p4_input`

This confirms route family A was still active in P0 output v2.3.

## 4. March 5 — P0 spec v2.4

Recovered direct user-supplied spec:

- `payload_type = ELYX_P0_CHANNEL_SPEC_V2_4`
- `channel_id = ELYX_P0_INTENT_NORMALIZER_v2.4`
- channel name ends with `NO_-P1`

Recovered canonical routing:

`P0 -> P1 -> P2 -> P3 -> P4`

Recovered rules:

- must not skip channels;
- must not output P5;
- P5 disabled by author;
- P0 mission becomes strict JSON input for P1 and onward;
- no `-P1` node appears in the route.

## 5. March 5 — P0 output v2.4

Recovered direct user-supplied output:

`ELYX_P0_OUTPUT_V2_4`

Routing:

`["P0","P1","P2","P3","P4"]`

Recovered process guarantee:

`no_-P1_enforced: true`

This is a record-level confirmation that P0 v2.4 no longer routed through `-P1`.

## 6. March 6 — P0 spec v2.6

Recovered direct user-supplied spec:

- `ELYX_P0_CHANNEL_SPEC_V2_6`
- `ELYX_P0_INTENT_NORMALIZER_v2.6`

Routing remains:

`P0 -> P1 -> P2 -> P3 -> P4`

Recovered binding again includes:

`no_-P1_enforced: true`

v2.6 also adds later P0 mechanics such as index-only range semantics and trace-full autopatch, while preserving the no-`-P1` route.

## 7. What changed

A clear versioned route transition is historically recoverable:

`P0_OUTPUT_V2_3`
uses:
`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

then:

`P0_SPEC/OUTPUT_V2_4`
uses:
`P0 -> P1 -> P2 -> P3 -> P4`

and:

`P0_SPEC_V2_6`
continues:
`P0 -> P1 -> P2 -> P3 -> P4`.

Therefore the P0 branch itself has a strong chronological shift away from routing through `-P1`.

## 8. What is still not proved

No recovered explicit field states:

- `P0_V2_4 supersedes P0_V2_3 globally`;
- `-P1 is deleted from Elyxion forever`;
- `-P1 is deprecated project-wide`;
- `-P1 was renamed to P1`;
- `-P1 moved before P0`;
- why the author chose `NO_-P1`.

Later August RAW again names `−P1/P0/P1/P2/P3/P4` as possible thought decomposition.

Therefore:

the **P0 route change is strongly recovered**;

the **global status of `-P1` remains unresolved**.

## 9. Current safe P0 verdict

Historical latest recovered P0 route candidate:

`P0 -> P1 -> P2 -> P3 -> P4`

Classification:

`LATEST_RECOVERED_P0_ROUTE_CANDIDATE`

Not yet:

`CURRENT_GLOBAL_P_SYSTEM_CONTRACT`

because project-wide supersession evidence is still missing.

## 10. P1 absorption check trigger

Because P0 v2.4 removed `-P1` from the route, the next question is whether P1 absorbed the former reality-skeleton/causal-continuity responsibility.

NEXT:

`P1_MINUS_P1_FUNCTION_ABSORPTION_CHECK_V0_1`

Required comparison:

- historical `-P1` mission;
- P1 v3.2.x mission;
- field-by-field overlap;
- missing capabilities;
- newly added capabilities;
- explicit evidence vs inferred functional overlap.

No merge/rename conclusion may be made from similarity alone.
