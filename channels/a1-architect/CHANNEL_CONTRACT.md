# CHANNEL_CONTRACT

This is a recovery statement of the strongest-known contract, not a new version.

## Inputs

Contract-accepted families (v3.1-v3.3):
- `A0 output JSON`;
- `A_MINUS_1 output JSON`;
- `P5 packet JSON`;
- raw vision text.

Observed real inputs in this conversation:
- `A_MINUS_1_VISION_ARTIFACT_V4_2`;
- `CANON_BINDING_PACKET_V2`;
- A0 reports containing a forwardable `copy_paste_payload_object`;
- P5-derived canon routed through A0/A_MINUS_1/A_ULTRA wrappers.

Historical external input evidence:
- P1 v3.2.2/v3.2.4 compact A handoffs explicitly target `A1`.

## Ingest discipline

Stable rules:
- one payload only;
- user should paste upstream artifact as-is;
- no manual task_id crafting;
- no manual target-module override;
- no silent guessing of source binding;
- if source missing/broken: WARN + best effort unless input unusable;
- if input unusable/vision intent absent: contract says FAIL.

## Transformations

A1 may:
- translate feel/canon constraints into architecture variants;
- define contracts and boundaries;
- choose a recommended variant as implementation guidance;
- define deterministic runtime/test strategies;
- create bounded assumptions where source is underspecified;
- create vertical-slice plan and regression gates.

A1 may not:
- change protected source order/IDs when upstream locks them;
- create canon facts not grounded upstream;
- introduce UI under `NO_UI`;
- use hidden unseeded randomness;
- create unbounded latent behavior that breaks determinism;
- silently create cross-module hard references;
- infer missing DreamVault identity/hash refs;
- emit artifacts owned by E-Prime.

## Output

Stable v3.1 core required output family:
- status/task/source;
- vision translation;
- three variants;
- contracts;
- anti-domino plan;
- metrics;
- test scene;
- determinism protocol;
- impact map;
- vertical-slice plan;
- quality gates;
- release readiness;
- warnings/questions;
- A2 handoff;
- `A1_ARCH_ANCHOR_V3` packet.

v3.2 append-only fields:
- `dream_vault_echo`;
- `input_fingerprint`;
- `quarantine_block_v2`;
- alignment hints;
- role-integrity report.

v3.3 append-only fields:
- `meaning_lane_view_v1`;
- `implementation_lane_v1`;
- `quarantine_block_v3`;
- handoff pointers `meaning_view_ref` / `implementation_lane_ref`;
- `guarantee_report_v3_3`.

## Downstream

Current strongest contract target: `A2`.

v3.3 says A2 consumes the meaning view by default; builders consume implementation lane.
