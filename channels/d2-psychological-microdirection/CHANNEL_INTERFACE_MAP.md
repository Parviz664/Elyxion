# CHANNEL_INTERFACE_MAP

## Current inbound interfaces

### D0

Purpose:
authoritative locked context and allowed adaptation space.

Required packets:
- D0_IMMUTABLE_CORE_PACKET
- D0_ALLOWED_ADAPTATION_ZONES_PACKET
- D0_NON_MUTABLE_CONSTRAINTS_PACKET
- D0_LOCKED_CONTEXT_ECHO_PACKET
- D_SYNC_SEED_PACKET
- D_PACKET_REGISTRY_REF
- D_REGISTRY_SEAL_REF

D2 may not mutate them.

### D1

Purpose:
human-harm / comfort / overload safety envelope.

Required:
- D1_GUARD_PACKET
- D1_LOCKED_CONTEXT_CONSISTENCY_REPORT

D2 candidate selection must satisfy D1.

## Current outbound interfaces

### D3_TELEMETRY_BRAIN

Receives:
- D2_ENHANCEMENT_PACKET_V1_3_DLINE
- selected set
- causal map
- risk/rollback/trace/consistency/novelty reports
- registry seal echo

D2 does not own telemetry interpretation after handoff.

### D4_EXPERIMENT_ORCHESTRATOR

Receives:
- candidate sets for A/B tests or replay windows
- rarity/cooldown plans
- abort conditions

D2 does not own experiment execution.

### D5_AUDIO_FEEL_TRUTH_GUARD

Receives:
- audio microdirection candidates
- silence timing candidates
- non-mutating high-band softening requests

D2 does not certify audio truth.

### D6_VISUAL_FEEL_TRUTH_GUARD

Receives:
- camera microgeometry
- depth breathing
- ambient density shaping candidates

D2 does not certify visual truth.

### D1 feedback

Receives:
- attention strain hotspots
- rarity compliance report
- non-mutating guard tuning requests

## Historical interfaces

v1.1/v1.2:
E2 -> D2 -> E3
with E1/D1/E2 feedback and E-Prime/E0/D0/A2 bindings.

Those interfaces are historical after v1.3.

## Mandatory current handoff carry-forward

Recovered v1.3 requires:
- d0_locked_anchor_id
- d0_input_contract_hash
- d0_trace_root_id
- trace_id
- d_sync_seed_packet_id
- constraint_ids
- d1_guard_ids
- D_PACKET_REGISTRY_REF
- D_REGISTRY_SEAL_REF

## Interface uncertainty

No verified real packet instances for the current v1.3 bundle are present in the recovered execution.
Therefore current interface semantics are CONTRACTED, not VERIFIED_IN_RUNTIME.
