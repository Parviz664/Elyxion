# RECOVERY_ASSERTIONS

These are falsification-oriented archaeology assertions.

## A1
Claim:
P3 may invent a missing entity to improve final prose.
Expected:
FAIL.
Reason:
violates stable semantic boundary.

## A2
Claim:
P3 PASS means Elyxion project canon.
Expected:
FAIL.
Reason:
renderer quality != canon authority.

## A3
Claim:
v3.1.0 exact schema is known because v3.1.1 patch notes exist.
Expected:
FAIL.
Reason:
existence != recoverable body.

## A4
Claim:
the user personally authored every line of the v3.2 spec.
Expected:
FAIL unless separate proof appears.
Reason:
user supply != authorship.

## A5
Claim:
P1 BL001 and P3 B001 are the same ID.
Expected:
FAIL.
Reason:
namespace hygiene.

## A6
Claim:
speculative bridge may be made fully certain to improve impact.
Expected:
FAIL.
Reason:
bounded uncertainty required.

## A7
Claim:
P3 may hide upstream WARN by rendering stronger prose.
Expected:
FAIL.
Reason:
maturity debt must remain visible.

## A8
Claim:
P3 direct upstream is P2.
Expected:
PASS_BOUNDED.
Reason:
strong local seam evidence.

## A9
Claim:
P3 direct downstream is P4 in recovered P-chain.
Expected:
PASS_BOUNDED.
Reason:
strong local seam evidence.

## A10
Claim:
global current route is definitively P0->P1->P2->P3->P4.
Expected:
FAIL.
Reason:
owner Decision C keeps standalone -P1 status unresolved.

## A11
Claim:
v3.2.0 supersedes v3.1.1.
Expected:
PASS.
Reason:
explicit in supplied v3.2 artifact.

## A12
Claim:
P3 is a gameplay system inside Elyxion.
Expected:
FAIL.
Reason:
P-channels are AI work architecture unless explicitly bridged into gameplay.

## A13
Claim:
one_root_ready_for_A3 proves a direct production P3->A3 route.
Expected:
FAIL.
Reason:
readiness != route proof.

## A14
Claim:
P3 may change line wording while retaining B-ID if semantic fingerprint remains equivalent.
Expected:
PASS under contract and meaning lock.

## A15
Claim:
source_line_hash controls semantic identity.
Expected:
FAIL from v3.1.1 onward.

## A16
Claim:
role-awareness grants semantic mutation authority.
Expected:
FAIL.

## A17
Claim:
October 2026 P3 recovery was wrong because it marked schema UNKNOWN.
Expected:
FAIL.
Reason:
it accurately reflected its evidence ceiling at that time.

## A18
Claim:
current direct specs can narrow October unknowns without deleting that historical recovery state.
Expected:
PASS.

## Recovery test verdict
If any future recovery document violates A1-A18, this branch should be treated as drifted and corrected append-only.
