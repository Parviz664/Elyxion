# CHANNEL_IDENTITY

## Stable technical identity
channel_id: E0_INTENT_LOCK_AND_HANDSHAKE_GATE
project_anchor: ELYXION

Earliest recovered owner-supplied channel artifact:
ELYX_E0_CHANNEL_SPEC_V1_1_MASTER

Latest recovered owner-supplied channel spec:
ELYX_E0_CHANNEL_SPEC_V1_5_MASTER

## Historical names

STATE_EARLY — v1.1 through at least v1.4  
Human name: E0 Канал Фиксации Намерения и Входного Handshake  
Role: mandatory ingress gate around current E-Prime anchor + A2 handshake.

STATE_CURRENT_STRONGEST — v1.5  
Human name: E0 Канал Двойного Замка (Kernel Truth + Dream Seal) и Входного Bind/Dispatch  
Role: bind kernel truth from E6/E-Prime-side registry+seal refs with dream seal from A3, then emit a locked handle and separate planning from runtime promotion.

## Identity continuity assessment

The technical channel_id is unchanged across the recovered lineage. The human name and mission changed materially.

Classification:
SAME_CHANNEL_LINEAGE_WITH_ROLE_REALIGNMENT

Evidence ceiling:
HIGH, because v1.5 explicitly supersedes ELYX_E0_INGRESS_PACKET_V1_4_MASTER and labels itself role_realignment_to_dual_ingest_binder_with_deadlock_free_planning.

## Not proved
- an earlier v0.x E0;
- a pre-v1.1 name;
- a natural-language AUTHOR_RAW birth message;
- that every supplied JSON line was directly authored by the owner.
