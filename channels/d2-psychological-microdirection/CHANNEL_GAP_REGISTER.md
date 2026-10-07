# CHANNEL_GAP_REGISTER

## GAP-D2-001 — exact birth moment not fully recovered

We have:
- possible sensory-channel precursor RAW;
- early D2 route slot;
- explicit author D2 Cosmic Awe statement.

We do not have:
the exact first-ever message where the D2 identifier was created.

Status:
OPEN.

## GAP-D2-002 — exact immediately-preceding author message

The archaeology request asks what the author wrote immediately before channel appearance.

Recovered:
nearby early route/Cosmic Awe material.

Not recovered:
a complete, exact transcript proving the immediately previous message.

Status:
UNKNOWN / OPEN.

## GAP-D2-003 — D2_ONBOARDING_OPTIMIZER content

Existence/reference is recovered.
Formal contents and origin are not.

Status:
REFERRED_TO_ONLY.

## GAP-D2-004 — final-name emergence between assistant proposal and v1.1

We know:
assistant proposed a different name;
user indicated D2 actual function was still to be explained;
v1.1 has the final mature name.

Missing:
the exact full transition conversation that minted the final name.

Status:
PARTIALLY_RECOVERED.

## GAP-D2-005 — exact original v1.1/v1.2/v1.3 byte archives

The full artifacts are visible in the current conversation and are semantically recoverable.

This branch currently records structured recovery, not guaranteed byte-identical transcript dumps.

Reason:
copying by model transcription could introduce accidental differences.

Status:
OPEN_ARCHIVAL_GAP.

## GAP-D2-006 — v1.3 semver tension

Artifact says:
patch_type = breaking_dependency_cleanup_with_schema_preservation

Artifact version change:
1.2.0 -> 1.3.0

Its own version rule says:
major = breaking schema/authority/decision model changes.

Removing all E dependencies and rebinding authority appears at least potentially authority-breaking.

Recovery verdict:
INTERNAL_CONTRACT_TENSION.

Do not silently renumber.

## GAP-D2-007 — v1.3 seal waiver vs absolute no-inference wording

v1.3 says:
- D2_cannot operate_without_d_registry_seal_verified_inputs;
- d_registry_seal_no_inference_absolute;
- block if registry/seal missing/untrusted.

But waiver_mode.enabled = true and defines signoff/timebox/risk packet requirements.

Unresolved question:
does waiver permit limited operation with a missing/unverified seal, or only waive non-critical registry deficiencies after some verification?

Artifact does not resolve this clearly.

Status:
CONTRACT_AMBIGUITY.

## GAP-D2-008 — v1.3 long-session policy lacks dedicated gate/fail condition

v1.2 had:
D2-G11 long_session_adaptation_gate
FC_D2_010 long_session_intensity_policy_violation.

v1.3 core still includes long_session_adaptation_policy, but quality gates end at G13 without a named long-session gate, and fail conditions omit FC_D2_010.

Possible meanings:
- intentional simplification;
- accidental omission.

Reason:
UNKNOWN.

Status:
OPEN.

## GAP-D2-009 — current D0/D1 packet instances not recovered

v1.3 contract names required packets and must-equal values.

Last execution:
they were missing.

Therefore:
current D0/D1 compatibility is contractual, not verified.

Status:
BLOCKING_IMPLEMENTATION_GAP.

## GAP-D2-010 — D-Registry/Seal real instances not recovered

Required:
D_PACKET_REGISTRY_REF
D_REGISTRY_SEAL_REF

Last execution:
MISSING.

Status:
BLOCKING_IMPLEMENTATION_GAP.

## GAP-D2-011 — D3-D6 downstream concrete contracts not inspected in this recovery

v1.3 routes to D3/D4/D5/D6.

This recovery has not proved their current concrete contract versions or ingestion compatibility.

Status:
OPEN.

## GAP-D2-012 — no runtime proof

No repository code, executable, UE integration, telemetry run, or device evidence was found for D2.

Status:
NOT_IMPLEMENTED_OR_NOT_DISCOVERED; exact alternative UNKNOWN.

## GAP-D2-013 — deterministic hash claims not verified

Specs require SHA256 determinism.

Recovered assistant executions used placeholders such as:
PENDING_IN_RUNTIME_VALIDATOR
or non-real placeholder text.

Therefore:
same-input/same-output cryptographic determinism is CONTRACTED, not VERIFIED.

Status:
OPEN.

## GAP-D2-014 — 50-70 microlever catalog not recovered

Contract target:
50_70.

Recovered explicit classes:
12.

No full 50-70 item catalog is present in current recovered evidence.

Status:
OPEN.

## GAP-D2-015 — exact reason for E-line removal

v1.3 patch change_intent tells us what changed.

It does not provide a separate author statement explaining why the author chose to remove all E dependencies.

reason_explicit:
false outside supplied artifact wording.

reason:
UNKNOWN.

## GAP-D2-016 — current authority of supplied master artifacts

User supplied and used v1.3 as the latest master in this channel.

That is strong current-channel authority.

Whether an external later Elyxion artifact superseded v1.3 outside this channel was not found.

Status:
NO_LATER_D2_SPEC_FOUND, not proof none exists globally.
