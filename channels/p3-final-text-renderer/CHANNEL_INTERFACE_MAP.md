# CHANNEL_INTERFACE_MAP

## Upstream interface — P2

strongest_upstream:
P2 Ladder Builder.

Recovered upstream packet families seen in practice:
- ELYX_P2_LADDER_PACKET_V3_3_0
- ELYX_P2_LADDER_PACKET_V3_4_0
- ELYX_P2_LADDER_PACKET_V3_5_0

P3 input family:
- historical/recovered ELYX_P3_INPUT_V3
- current exact ELYX_P3_INPUT_V3_2

P3 reads semantically relevant fields including:
- task identity;
- stage scope;
- range;
- author intent lock;
- P2 ladder packet;
- source bindings;
- uncertainty;
- dependencies;
- closure/bridge/terminal hints when supplied;
- prior canon map when supplied.

Upstream authority rule:
P2 semantics are source truth for rendering unless higher-authority source evidence says otherwise.
P3 cannot fill missing P2 semantics.

## P1 lineage visibility

P3 normally receives P1 lineage indirectly through P2 source_binding.

P1 block identifiers:
- P1_BLOCK_LEGACY in older packets;
- P1_BLOCK_SAFE / BL### in later packets.

P3 v3.2 render_binding_hygiene must keep them upstream-only.

## Downstream interface — P4

Recovered downstream:
ELYX_P4_INPUT_V3.

Recovered reference:
candidate_items_ref points to P3-rendered candidate material.

Compatibility note from v3.1.1 and v3.2:
P4 may ignore newer proof/role fields and continue consuming stable rendered item identity such as id/line/depends_on.

Boundary:
P3 renders.
P4 filters/shortlists/final-cuts.
Neither may silently rewrite source meaning.

## A3 interface-readiness

v3.1.1:
one_root_ready_for_A3 = true.

v3.2:
one_root_ready_for_A3 retained via one-root contract.

Interpretation:
P3 packet is shaped to be consumable by the next agent/A3-style gate.

Evidence ceiling:
exact direct A3 input contract and production routing from P3 are not recovered here.

## Canon-ID interface

P3 ID namespace:
P3_CANON_B.

Format:
B###.

Stable mapping:
source_semantic_fingerprint.

Historical trace:
source_line_hash only.

Merge:
status merged + merged_into when contract permits and meaning proof survives.

Deletion/retirement:
ID must not be reused.

## Error/reporting interface

P3 quality_report reports renderer quality, not world truth.

P3 patch_notes must explain:
before -> after -> why safe.

Cycle fix:
WARN + required upstream fix hint, bounded in v3.1.1+.

Speculative rendering:
must expose bounded uncertainty rather than hiding it.
