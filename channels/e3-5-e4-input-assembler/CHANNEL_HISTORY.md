# CHANNEL_HISTORY

## 1. Birth

The earliest directly recovered user wording connected to the creation event is:

“хорошо сделай этот Е3.5”

Timestamp recovered from prior-conversation context:
2026-02-18T10:16:05Z.

Three seconds later, at 10:16:08Z, a prior assistant output is recovered as creating:
E3_5_E4_INPUT_ASSEMBLER_AND_NO_DROP_COVERAGE_PROOF.

That assistant output described it as an engineering assembler for E4 required_sources with append-only/no-mutation/no-drop behavior in a SIM-only lane.

What the user wrote immediately before that command is UNKNOWN.
The preceding problem discussion was not recovered byte-for-byte.
Therefore the exact original author rationale for creating E3.5 remains UNKNOWN.

## 2. v1.0 — assembler template

At 2026-02-18T10:21:18Z the user supplied ELYX_E3_5_INPUT_ASSEMBLER_AND_COVERAGE_PROOF_V1_0.

Recovered properties:
- status DRAFT_READY_FOR_USE;
- BOOTSTRAP_LIMITED__SIMULATION_ONLY lane;
- append-only;
- no field mutation;
- no source shadowing;
- no SIM->CANON merge;
- no runtime claims;
- 10 required sources;
- optional E3/E2 full execution results;
- waiver path for missing required inputs;
- E4_REQUIRED_SOURCES_BUNDLE_V1;
- E3_5_NO_DROP_COVERAGE_PROOF_V1.

The same user turn begins with the direct instruction:
“Работать строго по контракту Е3.5!!!”

## 3. First execution error

The assistant's first v1.0 execution declared PASS_WITH_CONSTRAINTS and populated several refs that had not actually been supplied in that turn, while also creating unsigned waivers.

This violated the spirit and parts of the supplied contract:
missing packets were not supposed to be invented;
waivers required a D0 source-of-truth or operator signature.

This is historical assistant overreach, not channel truth.

## 4. v1.1 — ref-only hardening

At 2026-02-18T10:22:53Z the user supplied v1.1.

Additions explicitly stated by that artifact:
- REF_ONLY_STRICT default;
- no reserialization;
- no compacting/aggregating source content;
- no-shadow guard;
- exact E4 required-sources contract;
- exact type matching by default;
- deterministic PASS/WARN/BLOCK rules;
- waivers forbidden in REF_ONLY_STRICT;
- partial bundles only in PARTIAL_WITH_WAIVERS.

This is a decisive narrowing of transformation authority.

The author's explicit psychological reason for the change is not recovered.
Chronologically, it follows the assistant overreach, but causality is not asserted.

## 5. v1.2 — guarantee scope

At 2026-02-18T10:25:04Z the user supplied v1.2.

New recovered structures:
- guarantee_scope;
- contract_sync_guard;
- strict_ref_integrity_proof;
- E4_BLOCK_CLASS_ELIMINATION_MAP;
- explicit statement that E3.5 only eliminates the missing-input/unprovable-coverage class of E4 BLOCK;
- explicit non-guarantee of E4_TOTAL_PASS.

This version clarified what “100%” could legitimately mean:
100% required inputs + 0% semantic mutation + 100% provable coverage, not total E4 success.

## 6. Packet-registry relationship appears

At 2026-02-18T10:32:56Z a related E-Prime v1.2 assistant output is recovered as adding an append-only Packet Registry:
ref-only generation by trace_root_id,
required refs for E3.5/E4,
missing items represented as UNKNOWN/MISSING,
fabrication prohibited.

This is upstream integration context, not an E3.5 version.

## 7. Real source packets expose lane-model limits

A user-supplied D3 SIM execution packet later in the conversation exposed concrete trace references and an E3 superiority packet reference.

A later user-supplied D3 packet used:
lane_mode BOOTSTRAP_LIMITED,
a bootstrap trace root,
a canon-patch trace root,
REF_ONLY policy,
no merge,
no release/runtime promotion.

Under E3.5 v1.2 this produced a legitimate scope mismatch:
v1.2 expected a single SIM root.
The assistant blocked rather than silently merging the roots.

## 8. v1.3 — dual-root support

At 2026-02-18T21:37:37Z the user supplied ELYX_E3_5_CHANNEL_SPEC_V1_3_MASTER.

Its explicit upgrade note:
BOOTSTRAP_LIMITED dual-root lane support was added without permitting merge;
SIMULATION_ONLY remained unchanged and default.

New lane:
LANE_V2_BOOTSTRAP_DUAL_ROOT_REF_ONLY.

New rules:
- exactly two allowed roots;
- every required ref needs root_binding;
- no cross-root trace stitching;
- dual-root integrity proof;
- still ref-only and no embedding.

This change has an explicit reason in the supplied artifact:
the earlier dual-root BOOTSTRAP case had to become legal without weakening no-merge.

## 9. v1.4 — proof hardening

At 2026-02-20T11:55:46Z the user supplied ELYX_E3_5_CHANNEL_SPEC_V1_4_MASTER.

Explicit additions:
- registry/seal presence proof;
- prompt-injection hardening;
- deterministic manifest/bundle/index hashing fields;
- MIN_VERSION_SAME_MAJOR type policy;
- guarantee scope;
- E4_REQUIRED_SOURCES_CONTRACT_V1_1;
- bundle packet V1_1.

The stated intent was to avoid false BLOCKs on newer same-major packet versions while preserving proofability.

## 10. v1.4 review did not become v1.4.1

At 2026-02-20T11:56:06Z the assistant reviewed v1.4 and returned PASS_WITH_PATCH_REQUIRED.

It proposed fixes for:
- environment mode wording vs dual-root support;
- minimum packet versions;
- template lane-selection ambiguity;
- unverifiable numeric probability/guarantee wording.

These are ASSISTANT_PROPOSAL findings.
No later user acceptance of a v1.4.1 patch is recovered in this channel.
Therefore v1.4.1 is not part of the recovered owner-confirmed lineage.

## 11. A2 interface evidence

A separate A2 artifact on 2026-02-20 explicitly targeted E3.5 and exported:
A2_SYSTEMS_MAP_V4
with E3_5_INGEST_PROFILE_MIN_V1.

This strengthens the A2 -> E3.5 upstream interface, but does not prove a newer E3.5 contract.

## 12. Current recovery

On 2026-10-07 the user instructed this channel to recover itself historically, preserve provenance/UNKNOWNs, and only then write the durable recovery to GitHub.

That recovery is recorded on a separate channel recovery branch and does not modify E-Prime Chat Archive.
