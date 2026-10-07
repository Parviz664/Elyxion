# CHANNEL_CONTRACT

Current authority:
`ELYX_D4_CHANNEL_SPEC_V1_2_MASTER` (`1.2.0`).

Provenance:
`USER_SUPPLIED_ARTIFACT`.

Authorship caveat:
user-supplied does not prove line-by-line original authorship.

## Required upstream

- `D3_EXTREME_LATENT_SUPERIORITY_AUGMENTATION`
- `D2_PSYCHOLOGICAL_MICRODIRECTION_AND_AWE_ORCHESTRATION`
- `D1_PERFORMANCE_COMFORT_AND_ANTI_BOREDOM_GUARD`
- `D0_DLINE_EXECUTION_GOVERNOR_AND_CANON_FREEZE`

## Required packets

- `D3_AUGMENTATION_PACKET_V1_2_OR_HIGHER`
- `D3_RECOMMENDED_OVERLAY_SET_REF`
- `D2_ENHANCEMENT_PACKET_V1_2_OR_HIGHER`
- `D1_GUARD_PACKET_V2_4_DLINE_OR_HIGHER`
- `D0_IMMUTABLE_CORE_PACKET_DLINE`
- `D_SYNC_SEED_PACKET`
- `D_PACKET_REGISTRY_REF`
- `D_REGISTRY_SEAL_REF`
- `D4_D3_BASELINE_IMMUTABILITY_PROOF_V1`

## Locked D0 values

- `D0-ANCHOR-DLINE-LOCK-V1`
- `DLINE_SCOPE_LOCKED_HASH_V1`
- `TRACE-DLINE-BOOTSTRAP-V1`
- `DLINE_CANON_STRICT`

Mismatch blocks.

## Immutable inputs

D4 may not mutate:
- D3 recommended overlay set;
- D3 baseline hash;
- D2 selected enhancement set;
- D1 non-mutable constraints;
- D0 locked fields;
- registry/seal refs.

Overlay mode:
`append_only_stabilization_overlay`.

## Pipeline

1. verify registry/seal and locked context
2. verify D3 byte immutability
3. verify D3 semantic immutability
4. ingest D3 + D2 + D1 signals
5. detect portability risks
6. generate non-mutating candidates
7. run safety/causality/rhythm/rarity filters
8. verify latent hypotheses 2-of-3
9. score gain vs D3
10. counterfactual stress
11. select minimal high-impact set
12. attach trigger/exit/rollback/recovery
13. emit trace-bound packet

## Limits

- <=6 candidates/zone
- <=2 selected/zone
- <=2 active stabilizations/10min
- <=8 new assumptions/cycle
- <=2 parallel branches
- <=4 deepening iterations
- default intensity <=3
- intensity 4–5 requires D1 clearance

## Hypothesis rule

`2_of_3_independent_evidence_required`

Sources:
- D3 structural signal
- D2 player-feel signal
- D1 guard or runtime-proxy signal

Unverified selected hypothesis => BLOCK.

## Minimum thresholds

- D3 non-mutation = 100
- D1 guard alignment >=95
- cognitive-load safety >=92
- causal plausibility >=90
- rollback/recovery >=90
- overall score >=84
- portability gain vs D3 >=20%

## Outcomes

`PASS`
`PASS_WITH_CONSTRAINTS_A`
`PASS_WITH_CONSTRAINTS_B`
`BLOCK`

Last recovered strict instance:
`BLOCK`.

## Current handoff

Primary:
`D4_STABILIZATION_PACKET_V1_2`

Next channel:
`D5_AUDIO_FEEL_TRUTH_GUARD`.
