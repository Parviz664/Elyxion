# CHANNEL_CONTRACT

## Contract status

Current strongest-known formal contract:
ELYX_D2_CHANNEL_SPEC_V1_3_MASTER
spec_version 1.3.0

Historical formal contracts:
- ELYX_D2_CHANNEL_SPEC_V1_1_MASTER
- ELYX_D2_CHANNEL_SPEC_V1_2_MASTER

This file is a recovery summary, not a substitute for an exact byte archive of the original chat artifacts.

## Current v1.3 recovered contract core

### Mission

Transform flat/boring micro-segments into meaningful, convincingly strong experience through minimal context-appropriate micro-interventions while preserving causality, rarity of peaks and rollback readiness.

### Current topology law

D-line only.

Required active sources:
- D0_PSYCHOLOGICAL_ORCHESTRATION_GOVERNOR_DLINE_ONLY
- D1_PERFORMANCE_COMFORT_AND_ANTI_BOREDOM_GUARD_DLINE_ONLY

No active E dependencies.

### Locked values in supplied v1.3 artifact

d0_locked_anchor_id:
D0-ANCHOR-DLINE-LOCK-V1

d0_input_contract_hash:
DLINE_SCOPE_LOCKED_HASH_V1

d0_trace_root_id:
TRACE-DLINE-BOOTSTRAP-V1

d0_mode:
DLINE_CANON_STRICT

These values are part of the user-supplied v1.3 artifact. Their actual existence in upstream packets was not proven in the last execution.

### Registry/seal rule

Required:
- D_PACKET_REGISTRY_REF
- D_REGISTRY_SEAL_REF

No inference:
missing/untrusted/inconsistent registry or seal blocks ordinary operation.

### Candidate shape

A candidate must carry:
- candidate_id
- zone_id
- problem_type
- hidden_potential_hypothesis
- intervention_class
- intervention_brief
- causal_justification
- expected_psychological_effect
- intensity_level_0_5
- trigger_condition
- exit_condition
- rollback_trigger
- rollback_action
- d1_guard_bindings
- d0_invariant_bindings
- d0_zone_bindings
- candidate_trace_id
- trace_ref

### Intervention classes

Recovered v1.3 taxonomy:
- camera_microgeometry
- focal_attention_shift
- tempo_pause_architecture
- contrast_relief_waves
- light_temperature_nudges
- color_noise_control
- spatial_depth_breathing
- ambient_density_shaping
- acoustic_width_dynamics
- silence_timing
- ui_signal_competition_control
- recovery_microflows

### Rarity

controlled_awe_max_per_30min:
1

controlled_awe_min_causal_maturity_score_0_100:
85

block_repeated_awe_within_min:
20

awe_recovery_window_min:
3

### Limits

max_active_enhancements_per_10min:
2

max_candidates_per_zone:
6

max_selected_per_zone:
2

max_new_assumptions_per_cycle:
8

### Long-session adaptation

0-30 min:
max intensity 3; max new enhancements/10min 2

31-60:
max intensity 3; max new enhancements/10min 2

61-90:
max intensity 2; max new enhancements/10min 1

90+:
max intensity 2; max new enhancements/10min 1

### Novelty fatigue

max novelty events / 10min:
3

cooldown on breach:
6 min

breach action:
throttle_to_minimal_effective_set

### Selection thresholds

context_fit_min:
85

causal_plausibility_min:
90

d1_safety_alignment_min:
95

rollback_readiness_min:
90

cross_packet_consistency_min:
100

overall_candidate_score_min:
80

### Decision outcomes

PASS
PASS_WITH_CONSTRAINTS
BLOCK

### Hard-block classes

Recovered:
- locked-anchor mismatch;
- immutable mutation;
- missing causal justification;
- missing trigger/exit/rollback;
- D1 alignment below 95;
- cross-packet consistency violation;
- CRITICAL interference pair;
- D-registry/seal block;
- prompt-injection detection.

### Current output

D2_ENHANCEMENT_PACKET_V1_3_DLINE

## Historical contract deltas

v1.1:
E-bound; no registry/seal hard gate; output to E3 plus E1/D1/E2 feedback.

v1.2:
still E-bound; adds EPRIME registry+seal/no-inference and anti-injection.

v1.3:
breaking dependency cleanup; removes all E dependencies; D-line only; D-registry/seal.

## Recovery caveat

The v1.3 artifact itself contains unresolved internal tensions documented in CHANNEL_GAP_REGISTER.md. This recovery does not silently repair them.
