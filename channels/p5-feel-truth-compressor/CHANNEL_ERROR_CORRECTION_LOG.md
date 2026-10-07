# CHANNEL_ERROR_CORRECTION_LOG

## ERR-P5-001 — naked P4 packet admitted as P5 input

type:
assistant overreach / interface admission mismatch.

context:
current conversation after v1.3 contract.

expected:
`ELYX_P5_INPUT_V1_3` wrapper with required fields.

received:
`ELYX_P4_FILTER_SHORTLIST_PACKET_V3_2`.

assistant action:
emitted `ELYX_P5_FEEL_TRUTH_PACKET_V1_3` with status SKIP.

why this is a defect:
the response treated a P4 packet as though the P5 input wrapper had been satisfied.

impact:
LOW on meaning:
- no nodes changed;
- no drops;
- no reorder;
- no logic patch.

truth impact:
the emitted packet must not be treated as verified conformant P5 execution.

repair:
record the output as ASSISTANT_OUTPUT / NONCONFORMANT_INTERFACE_ADMISSION.
Future conformant P5 execution must respect the v1.3 wrapper.

resulting invariant:
P4 packet identity != P5 input-wrapper identity.

## HARDENING-P5-001 — v1.3 safety escalation

classification:
contract hardening, NOT a proven prior incident.

changes:
- default off;
- logic patch locked;
- backbone immutable;
- proofs required;
- impact capped.

why not called an error correction:
the artifact states risk/safety rationale, but no historical incident causing the hardening is recovered.

## PROVENANCE-CORRECTION

Invariant:
user-supplied artifact is not automatically user-authored RAW.

This prevents a false historical claim about who wrote v1.1/v1.2/v1.3 wording.
