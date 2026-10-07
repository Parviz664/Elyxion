# CHANNEL_INTERFACE_MAP

## Current inbound

### From D0
- D0_IMMUTABLE_CORE_PACKET
- D0_ALLOWED_ADAPTATION_ZONES_PACKET
- D0_NON_MUTABLE_CONSTRAINTS_PACKET
- D0_LOCKED_CONTEXT_ECHO_PACKET
- D_SYNC_SEED_PACKET
- D_PACKET_REGISTRY_REF
- D_REGISTRY_SEAL_REF

### From D1
- D1_GUARD_PACKET
- D1_LOCKED_CONTEXT_CONSISTENCY_REPORT

### From D2
- D2_ENHANCEMENT_PACKET_V1_3_DLINE
- selected_enhancement_set
- trace_lineage_map
- d_registry_seal_echo
- d2_immutability_proof
- D2_BASELINE_IMMUTABILITY_PROOF_V1

## Current output packet

D3_AUGMENTATION_PACKET_V1_3_DLINE.

Required candidate fields:
- augmentation_id
- source_zone_id
- derived_from_d2_ref
- latent_potential_hypothesis
- why_invisible_previously
- augmentation_type
- intervention_brief
- causal_justification
- player_feel_effect_hypothesis
- applicability_conditions
- safety_bindings_d1
- invariant_bindings_d0
- d0_zone_bindings
- superiority_gain_pct_vs_d2
- confidence_score_0_100
- verification_evidence_2of3_status
- adversarial_pass_rate_pct
- downstream_friction_score
- trigger_condition
- exit_condition
- rollback_trigger
- rollback_action
- overlay_trace_id
- evidence_id_set
- trace_ref

Allowed augmentation types:
latent_dependency_unlock;
micro_rhythm_stability_boost;
trust_continuity_hardening;
awe_rarity_preservation_refinement;
overload_preemption_overlay;
integration_resilience_overlay;
counterfactual_survivability_overlay.

## Current outbound

### To D4_EXPERIMENT_ORCHESTRATOR
- D3_AUGMENTATION_PACKET_V1_3_DLINE
- recommended_overlay_set
- superiority_evidence_matrix
- latent_hypothesis_verification_matrix
- adversarial_test_report
- downstream_friction_report
- risk_register
- rollback_matrix
- trace_lineage_map
- d_registry_seal_echo
- d2_immutability_proof
- d2_semantic_immutability_proof

### To D2 feedback
- latent_reserve_discovery_report
- feel_alignment_notes_non_mutating

### To D1 feedback
- strain_preemption_notes
- long_session_stress_findings

### To D5/D6
- audio_overlay_candidates_if_relevant
- visual_overlay_candidates_if_relevant

## Historical E-era interfaces

v1.1 required:
E3 superiority;
D2 enhancement;
E2 variants;
E1 execution draft;
D1 guard;
D0/E0/E-Prime/A2 locked context.

v1.2 additionally required:
E3.registry_seal_echo;
EPRIME_PACKET_REGISTRY_REF;
EPRIME_REGISTRY_SEAL_REF.

Historical outbound:
E4 integration/readiness routing.

Status:
SUPERSEDED.
