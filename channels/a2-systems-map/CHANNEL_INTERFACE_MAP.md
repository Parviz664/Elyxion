# CHANNEL INTERFACE MAP

## Upstream interfaces

### A0 / Binding provenance
A2 laws can accept:
- A0 routed packet,
- wrapper/bare `CANON_BINDING_PACKET_V2`.

Observed A1 packets often preserve:
- source_type=A0_ROUTED_PACKET,
- source_payload_type=CANON_BINDING_PACKET_V2,
- source_task_id,
- stage_scope,
- source_binding_integrity.

A2 must preserve that provenance rather than pretending A1 became the original author/source.

### A1
Observed primary immediate handoff:
`A1_ARCH_ANCHOR_V3` -> A2.

Older v1.4 law also accepts A1 V1/V2 anchors.

Later A1 v3.3 dual-view:
- `meaning_lane_view_v1` is semantic surface,
- `implementation_lane_v1` is builder surface.

A2 semantic authority should consume meaning view only when explicitly supplied.

### A_MINUS_1
Accepted historically as vision artifact / canon-bearing fallback source.
A2 does not become vision author.

### P5
Accepted by v1.6.2 input contract.
This is input compatibility, not proof that every active route uses P5.

## Internal A2 interfaces

Core map:
- artifact_identity
- source_trace
- trace_index
- systems_map
- domino_guard
- conflict_report
- quality_gates
- release_gate_result

Compact handoff:
- payload_type=A2_SYSTEMS_MAP_V4
- project_anchor
- task_id
- idea_title
- systems_compact
- deps_compact
- invariants_compact
- domino_compact
- trace_compact

Later additive interfaces:
- fidelity_report_v2
- semantic_judges_v1
- human_core_line_ref_only
- feel_anchors_ref_only
- quarantine_block_v2
- dream_vault_echo_v1
- input_fingerprint_v2
- export_packet

## Downstream interfaces

### A3
Default next agent.
A3 receives compact A2 map and performs downstream validation/sealing according to its own law.
A2 must not impersonate A3.

### E3.5
Later export profile:
`E3_5_INGEST_PROFILE_MIN_V1`.

Manifest is intended to prevent assembler inference:
- export_payload_type
- export_packet_id
- input_fingerprint_ref
- dream_vault_echo_ref
- handoff_packet_ref
- release_gate_status
- later v1.6.2: fidelity_report_ref, feel_anchors_ref_only_ref, quarantine_block_ref.

E3.5 consumption does not convert A2 output to canon.

### A0 fallback
Recovered laws keep A0 as fallback next agent when normal next-stage release cannot proceed.

## Separation rules

- source provenance != immediate handoff producer,
- handoff != canon promotion,
- export != seal,
- meaning lane != implementation lane,
- cap report != measured fidelity,
- quarantine != deletion.
