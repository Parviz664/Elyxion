# E1 v1.4 recovery

Status:
EXACT_VERSION_RECOVERED

Artifact:
ELYX_E1_CHANNEL_SPEC_V1_4_MASTER

Internal patch ID:
E1-V1_4-E0V1_4-DUAL_LOCK-HANDLE_ONLY-SKELETON_ONLY-SEALED_FENCES-20260303-01

Supersedes:
ELYX_E1_CHANNEL_SPEC_V1_3_MASTER

## Identity transition

channel_id remains:
E1_CONSTRAINED_IMPLEMENTATION_THINKING_ENGINE

human name becomes:
E1 Канал Скелета Реализации (Dream-Safe Skeleton Builder поверх E0 Dual-Lock)

owner role:
E1_Skeleton_Lead

step:
E1_DREAM_SAFE_SKELETON_BUILD_OVER_E0_LOCKED_CANON_HANDLE

## Explicit breaking changes

1. E1 no longer emits execution draft.
2. Steps / rollback / DoD move to E3.
3. Registry+seal no longer arrive as independent required operator inputs; E1 accepts E0_LOCKED_CANON_HANDLE.
4. success_metrics are removed from E1 and replaced by proof_hooks.
5. E2 is redefined as Engine Contract Translation.

## New role

Build:
- systems_skeleton;
- deps_skeleton;
- invariants_fences;
- contracts_skeleton;
- proof_hooks;
- quarantine block;
- E2/E3 handoffs;
- open questions.

## SEALED guard

Meaning lane forbids:
- discretization of drift;
- metrics/thresholds;
- goals/rewards/progress framing;
- instant reset;
- formalized protection systems;
- implementation vocabulary promoted into meaning.

## Proof hooks

Audit-only internal evidence, explicitly not player-facing gameplay metrics.

## Ingress

Only:
E0_LOCKED_CANON_BINDING_PACKET_V1 or higher.

## Downstream

E2:
Engine Contract Translation.

E3:
Deterministic Build Plan.

D1:
optional consumer; psycho touchpoints are not authored by E1.

## Historical significance

This is the decisive role reversal:
implementation planning authority leaves E1.

## Audit note

Assistant later proposed four clarifications.
No accepted v1.4.1 artifact is recovered.
