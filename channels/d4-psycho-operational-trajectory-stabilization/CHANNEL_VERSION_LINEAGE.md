# CHANNEL_VERSION_LINEAGE

## Conceptual pre-version state

Status:
`PARTIALLY_RECOVERED`.

Known:
- D4 created after E4;
- early E3/D3/E4 read-only relation;
- deep/hidden psycho-state mapping;
- preserve E4.

Formal artifact:
UNKNOWN.

## v1.0

Status:
`REFERRED_TO_ONLY / PARTIALLY_RECOVERED`.

Evidence:
a prior assistant output explicitly referred to "D4 v1.0".

Not recovered:
- exact artifact_type;
- exact schema;
- exact fields;
- exact owner approval of the version label;
- exact v1.0→v1.1 delta.

Rule:
do not reconstruct v1.0 by subtracting fields from v1.1.

## v1.1

Status:
`EXACT_VERSION_RECOVERED` as user-supplied artifact.

Artifact:
`ELYX_D4_CHANNEL_SPEC_V1_1_MASTER`

Version:
`1.1.0`

Baseline:
immutable E4.

Architecture:
mixed E/D dependencies, append-only stabilization overlays, 2-of-3 evidence, 14-class taxonomy, budgets, rollback/recovery, E5 handoff.

Historical status:
`SUPERSEDED`.

## v1.2

Status:
`EXACT_VERSION_RECOVERED` as user-supplied artifact.

Artifact:
`ELYX_D4_CHANNEL_SPEC_V1_2_MASTER`

Version:
`1.2.0`

Patch:
`D4-V1_2-DLINE_ONLY-D3_BASELINE-DREGISTRY_SEAL-NO_INFERENCE-ANTI_INJECTION-20260226-01`

Type:
`breaking_dependency_cleanup_with_schema_preservation`

Explicitly supersedes v1.1.

Major deltas:
- all E* dependencies removed;
- E4 baseline -> D3 baseline;
- D0→D1→D2→D3 only;
- D-registry+seal mandatory;
- no-inference hard block;
- prompt-injection hardening;
- semantic-shadow protection;
- current next step D5.

Historical status:
`ACTIVE_STRONGEST_KNOWN`.

## v1.3+

No later D4 spec was found in the accessible conversation recovery or current GitHub main searches.

Status:
`UNKNOWN whether later unrecovered versions exist elsewhere`.
