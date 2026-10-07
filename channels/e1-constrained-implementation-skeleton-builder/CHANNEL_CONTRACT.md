# CHANNEL_CONTRACT

This file records the strongest-known contract without erasing historical contracts.

## Current contract basis

Version:
v1.6, partially recovered from a full user-supplied artifact dated 2026-03-13 14:27:08Z.

Technical ID:
E1_CONSTRAINED_IMPLEMENTATION_SKELETON_BUILDER

Input:
E0_LOCKED_CANON_BINDING_PACKET_V1_7

Outputs:
- E1_CONSTRAINED_IMPLEMENTATION_SKELETON_PACKET_V3
- E1_TO_E2_ENGINE_CONTRACT_INPUT_V2
- E1_TO_E3_WEAK_VISIBILITY_INPUT_V1

## Contract invariants

1. E0 binding is upstream authority.
2. E1 may structure but not reinterpret bound truth.
3. Missing refs remain missing/unresolved; no inference.
4. Skeleton legality cannot silently become readiness.
5. Skeleton cannot silently become engine contracts.
6. Skeleton cannot silently become build tasks.
7. Weak E3 visibility cannot become hidden E3 co-authority.
8. Trace/provenance must survive handoff.
9. Dream/canon meaning is not rewritten.
10. Unresolved content is not silently compressed away.

## Historical contracts

v1.0–v1.3:
E1 contract explicitly included step synthesis, measurable exits, rollback and execution-draft packets.

v1.4:
contract was deliberately broken/realigned to skeleton-only.

Therefore any consumer that expects E1_EXECUTION_DRAFT_PACKET belongs to the historical v1.0–v1.3 route, not current strongest-known v1.6.

## Implementation status

Contract documentation:
RECOVERED with gaps.

Executable code/runtime implementation:
UNKNOWN / NOT RECOVERED.

GitHub main before this branch:
no E1 source/docs discovered by code search.
