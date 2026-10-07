# CHANNEL_INTERFACE_MAP

## Upstream — P1

Strongest recovered producer:
P1 Map Planner.

P1 handoff fields strongly observed:
- map_id;
- author_intent_lock;
- topic_scope_entities_compact;
- blocks_compact / block refs;
- linear_order_compact;
- micro_stage_catalog_compact;
- drift_guards_compact;
- resume_token.

P2 must bind ladder items to P1 micro_stage IDs.

## Internal identity seam

Primary:
`ladder_item_id`.

Lineage:
`source_binding.p1_micro_stage_id`.

Legacy:
candidate_id only as compatibility/trace.

## Downstream — P3

Recovered P2 packet families visible from P3:
- `ELYX_P2_LADDER_PACKET_V3_3_0`;
- `ELYX_P2_LADDER_PACKET_V3_4_0`;
- `ELYX_P2_LADDER_PACKET_V3_5_0`.

P3 receives:
- task/stage/range;
- ladder semantics;
- source binding;
- uncertainty;
- dependencies;
- closure/bridge/terminal hints;
- maturity debt where present.

Authority:
P3 may render; P3 may not fill missing P2 semantics.

## A-side interface

Current v3.5:
`ELYX_P2_A_BRIDGE_HANDOFF_V1_3`.

Must preserve at least:
- item identity;
- node role;
- pressure axis;
- trigger type;
- mechanism class;
- P1 source micro-stage;
- feel primary;
- uncertainty;
- maturity summary.

Naming:
A_ULTRA is primary; A_MINUS_1 is legacy alias.

## Error/report interface

binding_integrity_report:
structural lineage/binding failures.

quality_report:
report-only telemetry.

zone_maturity_report:
v3.5 late-zone maturity view.

batch_completion_diagnostics:
clean vs safe vs mature distinction.

No score may become world truth.
