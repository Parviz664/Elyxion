# CHANNEL_CONTRACT

## Current contract authority

Source:
current-chat user-supplied artifact
`ELYX_P5_FEEL_TRUTH_COMPRESSOR_SPEC_V1_3`.

Semver:
1.3.0.

Change policy:
append_only.

ID freeze:
true.

## Activation

Default:
DISABLED.

Only enable if:
`enable_p5=true`.

Logic micro-patch only if:
`enable_p5=true AND logic_patch_explicit=true`.

## Backbone lock

Source:
P4.shortlist_spine.

Rule:
every shortlist node is `backbone=true`;
reserves are `backbone=false`.

Forbidden:
- backbone drop;
- backbone reorder.

Allowed backbone operations:
- text-only clarity/strength patch with no meaning change;
- merge semantic duplicate with one backbone survivor;
- add missing triplet fields;
- add observability trace.

Limits:
- max_patch_nodes_percent = 25;
- max_backbone_nodes_touched_percent = 10;
- max_backbone_drops = 0;
- max_logic_patches_percent_when_unlocked = 8;
- max_merges_per_12_nodes = 2.

## Required per-node feel truth

Required triplet:
- truth_anchor;
- stakes;
- why_not_else.

Observability required.

Allowed observability trace types:
- constraint;
- asymmetry;
- before_after_regime;
- retention_vs_loss.

## Direct answer

Default:
`direct_answer`.

In direct_answer:
- no question-form rewrite;
- nodes end as claims, not questions;
- question_mark_rate above contract threshold hard-fails.

## Rhythm

Structural only.
No self-measured real time.

Required:
- tempo_class = fast | medium | dense;
- feel_pulse = setup | rise | peak | release.

Runtime timing validation only through external runtime feedback.

## Patch proof

Every patch requires:
- patch_id;
- node_id;
- patch_type;
- severity;
- before_excerpt;
- after_excerpt;
- binding_refs;
- triplet_delta;
- observability_delta;
- why_causality_preserved;
- why_backbone_safe;
- risk_notes.

## Canon boundary

P5 is a presentation-layer post-processor.
P3/P4 remain required upstream references for canonical trace.
For E channels, P5 can provide text/rhythm/experience only, not implementation causality.

## Historical projection guard

None of these v1.3 safety fields are projected backward into v1.1/v1.2 unless separately recovered.
