# CHANNEL_VERSION_LINEAGE

## v1.0

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_0_MASTER.

Recovery status:
PARTIALLY_RECOVERED.

Existence proof:
- prior assistant output recovered at 2026-02-16 23:52:50Z;
- exact v1.1 patch metadata says it supersedes ELYX_D3_CHANNEL_SPEC_V1_0_MASTER.

Known content:
- E3 immutable baseline;
- D2 player-feel dependency;
- append-only/non-mutating augmentation;
- latent/impossible reserve search;
- E4 handoff;
- acceptance gain >=20%;
- GENIUS_60_BAND >=60%;
- integrity/safety/causality/rollback thresholds.

Unknown:
full field order and full exact JSON body.

Provenance:
ASSISTANT_OUTPUT for recovered initial artifact.

Do not reconstruct full v1.0 by subtracting later versions.

## v1.1.0

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_1_MASTER.

Recovery status:
EXACT_VERSION_RECOVERED from current conversation.

Supersedes:
v1.0.

Baseline:
E3.

Important additions stated in patch metadata:
deepening verification/adversarial;
anti-hallucination for latent hypotheses;
budget/cycle guards;
semantic shadow protection;
downstream-friction control.

Route:
E4.

Status:
SUPERSEDED.

## v1.2.0

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_2_MASTER.

Recovery status:
EXACT_VERSION_RECOVERED.

Supersedes:
v1.1.

Patch:
D3-V1_2-REGISTRY_SEAL-ANTI_INJECTION-SEM_SHADOW_PROOF-TIGHT_COMPAT-20260220-01.

Key additions:
- deterministic/schema discipline;
- registry+seal/no-inference;
- prompt injection hardening;
- evidence_id_set;
- stronger semantic shadow including handoff outcome;
- G00..G16.

Baseline:
E3.

Route:
E4.

Status:
SUPERSEDED.

## v1.3.0

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_3_MASTER.

Recovery status:
EXACT_VERSION_RECOVERED.

Supersedes:
v1.2.

Patch:
D3-V1_3-DLINE_ONLY-D0_LOCKED-DREGISTRY_SEAL_NO_INFERENCE-ANTI_INJECTION-SEM_SHADOW_PROOF-20260226-01.

Patch type:
breaking_dependency_cleanup_with_schema_preservation.

Breaking changes:
- remove E-Prime/E0/E1/E2/E3/E4 dependencies;
- D2 becomes immutable baseline;
- D0/D1/D2 become active upstream;
- registry/seal replaced by D-registry/seal;
- active E-channel injection becomes blocked;
- D0 allowed-zone gate explicit;
- output routes to D4/D5/D6.

Status:
CURRENT_STRONGEST_KNOWN_CONTRACT.

## No later version recovered

No v1.4+ artifact is present in this conversation or discovered by the bounded GitHub searches used in this recovery.

Status:
UNKNOWN, not "does not exist".
