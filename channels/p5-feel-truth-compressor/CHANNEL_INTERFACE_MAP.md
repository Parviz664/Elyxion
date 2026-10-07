# CHANNEL_INTERFACE_MAP

## P4 -> P5

Producer:
P4 Feel Potential Engine.

P4 object bound by current v1.3:
`p4_packet`.

Required P4 fields:
- shortlist_spine;
- reserves;
- montage_curve;
- selection_reasons;
- source_binding.

Binding identity:
B### shortlist nodes become backbone=true.

## P5 input wrapper

Expected payload:
`ELYX_P5_INPUT_V1_3`.

Required wrapper fields:
- task_id;
- stage_scope;
- p4_packet;
- author_intent_lock;
- experience_priority_profile;
- enable_p5.

Important:
a naked P4 packet is not the same interface object.

## P5 -> downstream

Output:
`ELYX_P5_FEEL_TRUTH_PACKET_V1_3`.

Default downstream:
A0 or A_MINUS_1, presentation-only.

E-channel:
optional text/experience layer only.

## Runtime feedback -> P5

Optional input:
`ELYX_RUNTIME_FEEL_FEEDBACK_V1`.

P5 can react to:
- node timing;
- dropoff;
- replay;
- confusion spikes;
- engagement spikes.

But P5 itself does not originate factual runtime timing.

## Interface invariant

No downstream consumer may treat a P5 refinement as stronger causal authority than its bound P3/P4 sources.
