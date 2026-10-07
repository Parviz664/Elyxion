# CHANNEL_INTERFACE_MAP

## Current inbound interfaces — v2.0

E0:
E0_LOCKED_CANON_HANDLE_PACKET_V1_4_OR_HIGHER.
Carries locked_anchor_id, kernel_schema_version, input_contract_hash, trace_root_id, packet_registry_ref, registry_seal_ref, a3_seal_ref, intent_statement_locked_ref_only.
E3 authority: echo/equality only.

D0:
invariant freeze v2.0+ and allowed adaptation zones.

D1:
guard packet v2.4+.

E1:
skeleton packet + skeleton dependency graph.

E2:
Engine Contract Map v2.1+.
Microstep Affordance Map v2.1+.
Dream Fidelity Proof Summaries v2.1+.

A2/A3:
meaning/seal lineage, protected and non-mutating; routed through E0 where specified.

## Current outbound interfaces

E4:
production bundle, consistency report, rollback/trace/closure/dual-lock/registry echo.

E5:
microstep-ready bundle ref, node_affordance_matrix, stop conditions and verification hints.

E6:
production bundle + handoff_integrity_manifest_v2_0.

Feedback:
E2 affordance gaps / missing refs / quarantine issues.
E1 dependency/order conflicts.
D1 overload warnings.
E0 lock conflicts and trace updates.

## Historical interfaces

v1.x consumed D2 as required input and emitted superiority packets to E4.
v2.0 does not preserve that as its core role.
