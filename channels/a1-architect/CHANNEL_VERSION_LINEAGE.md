# CHANNEL_VERSION_LINEAGE

| Version/state | Recovery status | Proved | Not proved |
|---|---|---|---|
| pre-v3.1 v2.0 input compatibility | REFERRED_TO_ONLY | v3.1 says accepts v2.0 inputs | A1 law contents, exact schema, creation time |
| pre-v3.1 v2.1 input compatibility | REFERRED_TO_ONLY | v3.1 says accepts v2.1 inputs | A1 law contents, exact schema, creation time |
| pre-v3.1 v3.0 input compatibility | REFERRED_TO_ONLY | v3.1 says accepts v3.0 inputs; `new_in_v3_1` exists | full v3.0 A1 contract |
| v3.1 | EXACT_VERSION_RECOVERED | full user-supplied law artifact | original authorship, exact creation timestamp |
| v3.2 | EXACT_VERSION_RECOVERED | full user-supplied law artifact, explicit supersedes v3.1 | original authorship, exact creation timestamp |
| v3.3 | EXACT_VERSION_RECOVERED | full user-supplied law artifact, explicit supersedes v3.2 | original authorship, exact creation timestamp |

## v3.1 exact identity

Law:
`ELYX_A1_LAW_v3.1_ZERO_MANUAL_BUILD_GATED`

Version:
`A1_ARCHITECT_v3.1_ZERO_MANUAL_BUILD_GATED`

Primary additions listed by artifact:
- one-payload direct-paste gate;
- stable auto task_id contract;
- A0 extraction of next-message payload;
- source-integrity-aware release gate;
- tighter A2 handoff mapping.

## v3.2 exact identity

Law:
`ELYX_A1_LAW_v3.2_DREAMVAULT_ECHO_EPRIME_ALIGNMENT_ROLE_GUARD_APPEND_ONLY`

Adds:
- DreamVault ref-only passthrough;
- input fingerprint;
- alignment hints;
- quarantine v2;
- role integrity guard;
- placeholder no-inference policy.

## v3.3 exact identity

Law:
`ELYX_A1_LAW_v3.3_MEANING_CLEANROOM_DUAL_VIEW_QUARANTINE_ZERO_FRICTION_APPEND_ONLY`

Adds:
- meaning-cleanroom dual view;
- isolated implementation lane;
- quarantine v3;
- warning-noise reduction;
- zero-friction pointers;
- conditional dream-preservation target report.

## Forbidden reconstruction

Do not synthesize the missing pre-v3.1 law contents from v3.1.

`accepts_v2_0_inputs` does not mean a complete `A1 v2.0 law` has been recovered.
