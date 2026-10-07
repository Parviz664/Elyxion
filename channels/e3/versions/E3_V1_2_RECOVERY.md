# E3 v1.2 Recovery

Status: EXACT_VERSION_RECOVERED_AS_USER_SUPPLIED_ARTIFACT
Master type: ELYX_E3_CHANNEL_SPEC_V1_2_MASTER
version: 1.2.0
supersedes: ELYX_E3_CHANNEL_SPEC_V1_1_MASTER
patch_type: backward_compatible_contract_hardening

Role continuity:
Still E3_EXTREME_REALIZATION_SELECTION_AND_PACKAGING and still a superiority hardener.

New recovered controls:
- deterministic output/field order/hash policy;
- strict schema;
- prompt injection hardening;
- registry+seal/no-inference absolute;
- evidence_id_set mandatory;
- updated upstream version minima;
- new registry/seal and injection P0 risks/gates.

Important mechanism:
At v1.2, E3 directly requires EPRIME_PACKET_REGISTRY_REF and EPRIME_REGISTRY_SEAL_REF.

First recovered execution:
BLOCK because both refs are missing.
No scoring, hardened variants, or E4 handoff executed.

Historical status: SUPERSEDED by v2.0.

Do not project v2.0 echo-only behavior backward into this version.
