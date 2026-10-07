# CHANNEL VERSION LINEAGE

## v1.2
Recovery class: REFERRED_TO_ONLY.
Evidence: v1.4 declares `accepts_v1_2_inputs=true`.
Exact law_id: NOT_RECOVERED.
Exact content: NOT_RECOVERED.
Do not reconstruct from later versions.

## v1.3
Recovery class: REFERRED_TO_ONLY.
Evidence: v1.4 declares `accepts_v1_3_inputs=true`.
Exact law_id: NOT_RECOVERED.
Exact content: NOT_RECOVERED.
Do not reconstruct from later versions.

## v1.4.0
Recovery class: EXACT_VERSION_RECOVERED.
Law: `ELYX_A2_LAW_v1.4_ZERO_MANUAL_RELEASE_GATED`.

Recovered state:
- direct-paste one-payload gate,
- A0/BINDING/A1/fallback mode resolution,
- stable system registry,
- anti-leak scan,
- domino typing,
- append-only map deltas,
- trace coverage,
- release gate,
- compact A3 handoff,
- output `A2_SYSTEMS_MAP_V4`.

Historical status: SUPERSEDED, foundational.

## v1.5
Recovery class: PARTIALLY_RECOVERED.
Law: `ELYX_A2_LAW_v1.5_EXPORT_REF_ONLY_DUAL_ROOT_READY`.

Recovered:
- supersedes v1.4,
- export-first,
- exact A2 export,
- lane/root echo,
- root bindings `bootstrap_root` / `canon_patch_root`,
- A3 handoff,
- E3.5 ref-ready posture.

Missing:
- full exact master text,
- all exact field definitions.

Historical status: SUPERSEDED.

## v1.6.0
Recovery class: EXACT_PATCH_RECOVERED.
Law: `ELYX_A2_LAW_v1.6_DREAM_VAULT_PROOF_QUARANTINE_DOUBLE_JUDGE`.

Base: v1.5.
Adds:
- Sacred Dream Vault,
- fidelity proof gate,
- two judges,
- quarantine,
- human core line,
- drift locks,
- fingerprint,
- release-gate extension.

Historical status: SUPERSEDED.

## v1.6.1
Recovery class: EXACT_VERSION_RECOVERED.
Law: `ELYX_A2_LAW_v1.6.1_INFINITE_CLONE_E3_5_READY_MASTER`.

Adds:
- strict E3.5 export manifest,
- deterministic/idempotent regeneration posture,
- anti-deadlock iteration guard,
- judge strictness/beautification guard,
- cloning guidance.

Historical status: explicitly superseded by v1.6.2.

## v1.6.2
Recovery class: EXACT_VERSION_RECOVERED.
Law: `ELYX_A2_LAW_v1.6.2_FIDELITY_GUARANTEE_FEEL_ANCHORS_QUARANTINE_SPLIT_DV_OPTIONAL`.

Adds/changes:
- bounded fidelity cap model,
- DreamVault optionality,
- missing DreamVault is WARN-only,
- REF-only feel anchors,
- quarantine class split,
- input fingerprint v2,
- expanded E3.5 manifest refs.

Historical status: CURRENT STRONGEST-KNOWN.

## Output family lineage

Recovered output identifier remains `A2_SYSTEMS_MAP_V4`.

The payload-family V4 persisted while governing law versions changed.
Do not confuse payload version V4 with law version v1.4.
