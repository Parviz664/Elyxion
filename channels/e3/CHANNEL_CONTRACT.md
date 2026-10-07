# CHANNEL_CONTRACT

Current contract snapshot derives from the user-supplied ELYX_E3_CHANNEL_SPEC_V2_0_MASTER. This recovery file does not replace that master artifact.

## Required invariants

1. Exactly one primary path.
2. Zero new assumptions per cycle.
3. E0 is sole dual-lock bind/dispatch truth.
4. Registry/seal is echo-only in E3.
5. Meaning lane uses ref-only sources through E0 lineage.
6. Engine/build vocabulary stays in impl_lane_quarantine.
7. Every primary-path node requires:
   - preconditions
   - actions_hint
   - expected_state
   - verification_hint
   - rollback_hint
   - stop_condition_if_uncertain
8. Missing affordance => closure item; any missing primary-path affordance is P0 BLOCKING.
9. Metric/scoring axis may not be used as a decision reason.
10. No runtime/build/test/package/release action.

## Allowed outcomes

PASS
PASS_WITH_CONSTRAINTS
BLOCK

PASS requires complete microstep readiness, one primary path, clean quarantine, consistent locked echoes, and no P0/P1 closure items.

## Current execution posture

The first recovered v2.0 execution is BLOCK because required upstream packets were not supplied.
This recovery therefore does not claim an emitted production bundle.

Source: SRC-CURRENT-010 + SRC-CURRENT-011.
