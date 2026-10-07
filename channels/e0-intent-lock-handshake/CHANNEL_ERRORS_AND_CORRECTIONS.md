# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-E0-001 — spec treated as runtime packet
Observed:
after ELYX_E0_CHANNEL_SPEC_V1_1_MASTER, assistant immediately emitted runtime BLOCK for missing inputs.
Class:
ASSISTANT_INTERPRETATION / likely layer confusion.
Owner correction:
not explicitly verbalized.
Repair:
subsequent user supplied E0 ingress packet.
Invariant:
do not confuse channel contract with concrete ingress instance.

## ERR-E0-002 — semantic A2 blocked by strict field placement
Observed:
rich A2 systems map BLOCKed because E0 expected exact handshake structure.
Detection:
v1.2 explicitly says:
"A2 fields were valid semantically but not found in strict expected locations."
Repair:
accepted locations + deterministic resolution + safe lock-field autofill.
Invariant:
transport placement may be normalized; dream fields may not be invented.

## ERR-E0-003 — premature constrained progress before contract caught up
Observed:
some assistant E0 decisions allowed broad bootstrap downstream while A2 was still pending, although earliest v1.1 release condition required completed dual validation.
Class:
ASSISTANT_OVERREACH / transitional behavior.
Later repair:
v1.1 patched/v1.2 explicitly introduced no-ideal-waiting and phased constrained progress.
Important:
later repair does not retroactively canonize earlier assistant behavior.

## ERR-E0-004 — invented placeholder identity
Observed:
assistant introduced A2-PENDING-UNDECLARED-ID.
Class:
ASSISTANT_INVENTED_PLACEHOLDER.
Repair:
excluded from owner truth.
Invariant:
unknown IDs remain UNKNOWN.

## ERR-E0-005 — version/schema compatibility warnings
Assistant lint of v1.4/v1.5 found:
- E-Prime min 1.3.0 vs supplied 1.2.1;
- kernel schema 1.1.0 vs earlier 1.0.0;
- dual-ingress schema ambiguity.
Owner repair:
NOT RECOVERED.
Status:
OPEN GAP.

## ERR-E0-006 — A3/E-Prime responsibility confusion resolved by role realignment
Precursor:
A3 v1.4 says EPRIME_NOT_INCLUDED__MUST_BIND_IN_E0_FROM_E6.
v1.5 repair:
E0 becomes dual ingest: E6 kernel + A3 dream.
Invariant:
kernel truth is separate from A-lane dream seal.

## ERR-E0-007 — new A3 type rejected by old accepted-type list
Observed:
ELYX_A3_PRE_E0_RELEASE_BUNDLE_V2_2 supplied.
E0 v1.5 evaluation BLOCKed because accepted_artifact_types names ELYX_A3_RELEASE_BUNDLE_V1_4_OR_HIGHER.
Repair:
NOT RECOVERED.
Status:
CURRENT COMPATIBILITY GAP.
