# EVIDENCE_INDEX

## E1 — current channel v3.1.1 spec
class:
USER_SUPPLIED_ARTIFACT.
strength:
VERY_HIGH for contract content.
authorship strength:
UNKNOWN.
supports:
v3.1.1 exact version, proof-binding, B-ID semantics, one-root rule, observable-marker gate.

## E2 — current channel v3.2.0 spec
class:
USER_SUPPLIED_ARTIFACT.
strength:
VERY_HIGH for contract content.
authorship strength:
UNKNOWN.
supports:
current strongest identity, role-aware rendering, anti-montage, speculative discipline, namespace hygiene.

## E3 — current channel P2 practice packets
class:
USER_SUPPLIED_ARTIFACT.
strength:
HIGH for real upstream input shapes.
supports:
P2->P3 seam, role/bridge/terminal input evolution, source-binding practice.

## E4 — current channel assistant P3 output
class:
ASSISTANT_OUTPUT.
strength:
HIGH for implementation-in-chat behavior.
does_not_prove:
runtime implementation or owner authorship.
supports:
actual v3.2 packet generation and WARN preservation.

## E5 — GitHub P3 contract recovery
path:
channels/p-control-point/recovery/P3_CONTRACT_RECOVERY_PASS_V0_1.md
branch:
channel/p-control-point-v0.1
commit:
d929e8e503ff
date:
2026-10-06T03:02:35Z
class:
GITHUB_ARTIFACT.
supports:
role core, P2 upstream, P4 downstream, patch-safe anti-drift boundary.

## E6 — GitHub P-system route timeline
path:
channels/p-control-point/P_SYSTEM_ROUTE_AUTHORITY_TIMELINE_V0_1.md
class:
GITHUB_ARTIFACT.
supports:
2026-02-12 route family A, March route family B, current route HOLD.

## E7 — P Channel Registry v0.2
path:
channels/p-control-point/P_CHANNEL_REGISTRY_V0_2.yaml
class:
GITHUB_ARTIFACT.
supports:
role spine, truth model, P2->P3 semantic mutation prohibition, P3->P4 candidate rewrite prohibition.

## E8 — P Chain Role Spine Crosscheck
path:
channels/p-control-point/P_CHAIN_ROLE_SPINE_CROSSCHECK_V0_1.md
class:
GITHUB_ARTIFACT.
supports:
P3 renderer vs P4 selector distinction and RAW preservation boundary.

## E9 — Source Provenance Correction
path:
channels/p-control-point/recovery/SOURCE_PROVENANCE_CORRECTION_V0_1.md
class:
GITHUB_ARTIFACT.
supports:
supplied_by != authored_by rule.

## E10 — prior conversation recovery
class:
RECOVERED_FROM_PRIOR_CONVERSATION.
supports:
March role label, input family, route and direct user constraints.
strength:
HIGH semantic recovery, lower than direct current artifact for exact bytes.

## Evidence ordering used in conclusions

E1/E2 direct current supplied specs
> E3 direct current practice inputs
> E5-E9 durable GitHub recovery
> E10 prior conversation recovery
> assistant interpretation
> inference.

No inference may overwrite a stronger source.
