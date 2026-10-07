# RAW EVIDENCE INDEX

This file preserves exact fragments that are directly available, while explicitly recording that the complete raw conversation export was not available as a byte-addressable source during this recovery.

## AUTHOR_RAW fragments

### RAW-D1-001
> принимаете роль эту

Context: immediately after a supplied D1 v2.1 master in the current conversation.

### RAW-D1-002
> Работать строго по контракту Д1!

Recovered historical timestamp: 2026-02-17T22:51:01Z.

### RAW-D1-003
> История канала является частью архитектуры канала.

Context: 2026-10-07 recovery instruction.

### RAW-D1-004
> НЕ ИЗОБРЕТАТЬ НЕДОСТАЮЩУЮ ИСТОРИЮ.

Context: recovery absolute rule.

## USER_SUPPLIED_ARTIFACT identifiers

### ART-D1-001 — v2.1
- `artifact_type: ELYX_D1_CHANNEL_SPEC_V2_1_MASTER`
- `step_id: D1_PERFORMANCE_COMFORT_AND_ANTI_BOREDOM_GUARD`
- `owner_role: D1_Performance_Comfort_AntiBoredom_Guard_Lead`
- `mode: CANON_STRICT`
- `micro_lever_library.version: D1_LEVER_PACK_V1_1_48`
- `meta.schema_version: 2.1.0`
- `meta.derived_from: ELYX_D1_CHANNEL_SPEC_V2_0_MASTER`

### ART-D1-002 — v2.2
- `artifact_type: ELYX_D1_CHANNEL_SPEC_V2_2_MASTER`
- `spec_version: 2.2.0`
- `patch_id: D1-V2_2-E0D0E1-SYNC-E4D4-ALIGN-20260217-01`
- `operating_model.model: D1_CORE_PLUS_D1_COMPOSER_V2_2`
- `locked_context_gate.gate_id: D1-G08_LOCKED_CONTEXT_CONSISTENCY`
- `micro_lever_library.version: D1_LEVER_PACK_V1_2_60`
- `meta.derived_from: ELYX_D1_CHANNEL_SPEC_V2_1_MASTER`

### ART-D1-003 — v2.4
- `artifact_type: ELYX_D1_CHANNEL_SPEC_V2_4_MASTER`
- `spec_version: 2.4.0`
- `patch_id: D1-V2_4-DLINE_ONLY-D0_INDEPENDENT-REGISTRY_SEAL_NO_INFERENCE-20260226-01`
- `supersedes_artifact_type: ELYX_D1_CHANNEL_SPEC_V2_3_MASTER`
- `operating_model.model: D1_CORE_PLUS_D1_COMPOSER_V2_4_DLINE`
- `D_PACKET_REGISTRY_REF`
- `D_REGISTRY_SEAL_REF`
- `any_E_channel_integration` in non-scope
- `meta.compatibility.zero_e_dependencies: true`

Exact supplied v2.4 purpose includes:

> "D-line only"

and:

> "zero E-channel dependencies"

and its patch intent explicitly removes E* dependencies and rebinds D1 to D0-only locked context.

## Historical E1-supplied packets

### ART-D1-004
`ELYX_E1_EXECUTION_RESULT_V1_2`

Key exact states:
- `PASS_WITH_CONSTRAINTS`
- planning-only
- `runtime_promotion_allowed=false`

### ART-D1-005
`ELYX_E1_SIMULATION_LANE_CONSTRAINT_RESPONSE_V1_2`

Key exact states:
- `simulation: true`
- `non_canon: true`
- `promotion_to_canon_allowed: false`
- no runtime/performance/thermal/FPS claims
- no SIM/CANON trace merge

### ART-D1-006
`ELYX_E1_KERNEL_UPDATE_COMPAT_ACK_V1_2`

Key exact states:
- EPrime kernel 1.2.1 REF_ONLY in bootstrap;
- bootstrap pinned to 1.1.0;
- `COMPAT_UNKNOWN_WITH_GUARDS`;
- no silent upgrade.

## Missing raw payload archive

The full raw JSON bodies remain available in the conversation source but were not exposed to the recovery process as a byte-exportable transcript file.

Therefore this repository does **not** claim byte-for-byte archival completeness of the chat.

That limitation is intentional and must remain visible until a real transcript export is attached.
