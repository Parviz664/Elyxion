# CHANNEL_VERSION_LINEAGE

## Lineage table

### PRE_V3_1
status: INFERRED_EXISTENCE_ONLY
evidence:
P3 node exists in the 2026-02-12 route.
content: NOT_RECOVERED.
do_not_infer:
no version number, schema or exact role contract may be synthesized.

### v3.1.0
status: REFERRED_TO_ONLY
evidence:
the full current-channel v3.1.1 artifact states that v3.1.1 is an append-only strengthening of v3.1.0.
exact_content: NOT_RECOVERED.
safe statement:
v3.1.0 existed as the immediate predecessor named by v3.1.1.
unsafe statement:
reconstructing v3.1.0 by deleting v3.1.1 patch fields.

### v3.1.1
status: EXACT_VERSION_RECOVERED
artifact:
ELYX_P3_SPEC_V3_1_1
channel_id:
ELYX_P3_TEXT_RENDERER_v3.1
human_name:
P3 Финальный рендер (Feel-First, Anti-Drift, Anti-Noise, Patch-Safe, Canon-ID, Proof-Bound v3.1.1)

recovered deltas named by artifact:
- PATCH-1: source_binding + meaning_lock.
- PATCH-2: source_semantic_fingerprint + source_binding_ref; source_line_hash no longer basis of stability.
- PATCH-3: FEEL_COVERAGE_MIN deprecated_warn_only; observable markers introduced.
- PATCH-4: depends_on_cycle_fix becomes WARN, requires upstream hint, max one per 1..80.
- PATCH-5: one_root_ready / no text outside JSON.

role:
proof-bound final-text renderer.

### v3.2.0
status: EXACT_VERSION_RECOVERED
artifact:
ELYX_P3_SPEC_V3_2_0
channel_id:
ELYX_P3_TEXT_RENDERER_v3.2
human_name:
P3 Финальный рендер (Role-Aware, Feel-First, Anti-Drift, Anti-Noise, Patch-Safe, Canon-ID, Proof-Bound v3.2.0)
supersedes:
3.1.1

recovered deltas:
- PATCH-6 ROLE_AWARE_RENDER;
- PATCH-7 ANTI_MONTAGE_FLOW;
- PATCH-8 LATE_BRIDGE_RENDER_DISCIPLINE;
- PATCH-9 NAMESPACE_HYGIENE;
- PATCH-10 INEVITABILITY_SHARPENING;
- PATCH-11 CLOSURE_TONE_CONTROL;
- PATCH-12 ROLE_SENSITIVE_QUALITY_GATE;
- PATCH-13 SPECULATIVE_WEIGHT_CONTROL;
- PATCH-14 TEXT_FLOW_VARIANTS_SAFE.

role:
role-aware proof renderer.

## Version-lineage confidence

v3.2.0: VERY HIGH content recovery.
v3.1.1: VERY HIGH content recovery.
v3.1.0 existence: HIGH.
v3.1.0 content: UNKNOWN.
pre-v3.1 role existence: HIGH.
pre-v3.1 version content: UNKNOWN.

## Non-version practice artifacts

P2 v3.3.0 / v3.4.0 / v3.5.0 packets are not P3 versions.
P3 output packets for particular tasks are executions, not contract versions.
P Control Point v0.1/v0.2 are recovery/control artifacts, not P3 contract versions.

## Supersession law

v3.2.0 supersedes v3.1.1 by explicit supplied contract statement.

No evidence currently proves a P3 version newer than v3.2.0.
Do not invent v3.2.1 or v3.3.
