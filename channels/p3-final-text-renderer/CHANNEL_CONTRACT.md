# CHANNEL_CONTRACT

## Contract state

strongest_exact_version: 3.2.0
channel_id: ELYX_P3_TEXT_RENDERER_v3.2
payload_type_spec: ELYX_P3_SPEC_V3_2_0
status_in_artifact: active
supersedes: 3.1.1
change_policy: append_only
id_freeze: true
rollback_policy: revert_to_last_passed_version

## Mission

Receive P2 ladder_items as data and render final text/packet:
- readable;
- realism-safe;
- dense without filler;
- no semantic drift;
- proof-bound;
- patch-safe;
- role-aware in v3.2.

P3 may cut noise or merge true semantic duplicates only when traceability remains exact.
P3 may not add world structure to make the text feel stronger.

## Required input family

ELYX_P3_INPUT_V3_2

Required:
- task_id
- stage_scope
- range
- author_intent_lock
- p2_packet

Optional:
- render_mode
- style_profile
- patch_mode
- target_output_format
- canon_id_seed
- prior_canon_id_map
- render_role_hints

Historical recovered predecessor input:
ELYX_P3_INPUT_V3.

## Default v3.2 posture

render_mode: FEEL_FIRST_RENDER
style_profile: cold_clear_genz
target_output_format: TEXT_PLUS_PACKET
B-ID seed enabled from B001 unless prior map controls stability.
patch mode enabled only for enumerated safe patch types.

## Exact semantic prohibitions

P3 must not:
- invent new entities;
- invent new mechanisms;
- reorder causality;
- inject lore;
- inject UI;
- inject gameplay mechanics;
- use numbers as a new system;
- introduce formulas/models as world logic;
- personify an observer;
- silently convert uncertainty to certainty;
- silently merge anchors or identities;
- emit free text outside required one-root JSON when using the v3.2 contract.

## Allowed transformations

- clarity_rewrite_no_meaning_change
- uncertainty_labeling
- semantic_dedup_merge with binding/map evidence
- noise_trim
- canon_id_freeze_update
- bounded depends_on_cycle_fix
- role_tone_rebalance_no_meaning_change
- closure_flow_smoothing_no_meaning_change
- speculative_intensity_sharpen_no_meaning_change

## Output family

ELYX_P3_RENDERED_LADDER_PACKET_V3_2

Required top-level fields:
- status
- channel_id
- task_id
- stage_scope
- ladder_id
- range
- header
- rendered_text
- rendered_items
- canon_id_map
- patch_notes
- quality_report
- drift_guard
- resume
- next_agent_ready_one_root_json

Optional:
- role_aware_text
- render_role_report

## Per-item proof requirements

v3.2 rendered item includes:
- i
- id
- render_role
- render_weight
- line
- confidence_tag
- micro_transition_tag
- feel_tag_primary
- feel_tag_hidden
- depends_on using P3 B IDs
- source_binding
- render_binding_hygiene
- meaning_lock
- render_intent

## Stable identity rule

B-ID stability is semantic, not textual.

Primary stability signal:
source_semantic_fingerprint.

source_line_hash is historical trace only and must not decide identity.

render_role does not by itself change mapping.

## Uncertainty contract

Allowed labels:
plausible
speculative
unknown

A speculative line may be made sharper in forced-next phrasing only while preserving:
- locality;
- bottleneck narrowness;
- uncertainty;
- absence of false chemical or causal specificity.

## Quality-gate consequence

P3 PASS is a renderer-quality verdict.
It is not project canonization.

The current v3.2 thresholds in the supplied artifact require overall/canon/proof/role conditions.
A WARN remains lawful output and must not be beautified into PASS.

## Current route caveat

Local seam P2 -> P3 -> P4 is strongly recovered.
Global route before P2 remains subject to the project's current HOLD_UNRESOLVED around historical -P1 routing.
