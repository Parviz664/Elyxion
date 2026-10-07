# CHANNEL_INTERFACE_MAP

## Formal inbound v4.3

| Source | Accepted? | Behavior |
|---|---:|---|
| A0_ROUTED_PACKET | yes | hard_guard when binding integrity OK |
| P5_PACKET | yes | fail-fast source checks + P5 safety locks |
| A_ULTRA legacy artifact | yes | hard_guard_with_dreamvault_only |
| A_MINUS_1 legacy artifact | yes | hard_guard_with_dreamvault_only |
| RAW vision text | yes | stream + DreamVault-only amplification |
| UNKNOWN JSON | yes | stream + DreamVault-only amplification |
| P4 packet | **not listed** | direct use historically falls through to UNKNOWN_JSON |

## Formal outbound v4.3

Primary next agent:
A0.

Transport:
`next_message_to_next_agent` compact JSON.

Artifact:
`A_ULTRA_VISION_ARTIFACT_V4_3`.

## Semantic interfaces

### canon_constraints_vector
Downstream-safe must-preserve / must-not-do / allowed-ambiguity / stability-intent contract. No implementation instructions.

### d_requirements_echo_v1
D-sense references only. No conversion to mechanics/UI/economy/algorithms.

### DreamVault
Tone/image/rhythm/phrasing reinforcement only. Never a logic source.

## Adjacent channels

- P4 = feel-potential selection/filtering
- P5 = feel-truth compression/presentation
- A0 = gateway/binding role whose exact function changes by epoch
- A1 = separate architecture/meaning channel
- E0 = later intent/bind handoff layer
