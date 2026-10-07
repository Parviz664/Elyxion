# CHANNEL ERRORS AND CORRECTIONS

## ERR-D0-001 — risk of assistant rationale becoming owner rationale
Detection:
v1.0 review proposed six hardening areas.

Repair:
stored as ASSISTANT_PROPOSAL only. v1.1's explicit change_intent is the only accepted reason text from the supplied artifact.

Resulting invariant:
ASSISTANT_RATIONALE != AUTHOR_RATIONALE.

## ERR-D0-002 — generated psych evidence without recovered empirical source
Event:
assistant v1.1 execution created latent pressure entries, segment assignments and confidence values from technical ACK/closure conditions.

Detection:
no recovered segment registry/runtime psych observations accompanied the supplied E0 packet.

Repair:
artifact preserved as historical assistant output, but those empirical-looking fields are not promoted to verified truth.

Resulting invariant:
contract arithmetic / assistant confidence != observed human evidence.

## ERR-D0-003 — side-interface expansion
Event:
assistant created D0 ACK-processing and EPrime-patch-ingest result types under v1.1.

Detection:
recovered v1.1 master does not explicitly define these as primary ingress/handoff contracts.

Repair:
preserve as ASSISTANT_EXTENSION, not master-contract authority.

## ERR-D0-004 — v1.2 activation from stale upstream
Event:
v1.2 required E0 v1.4 + registry/seal, but available prior E0 was v1.3 and refs absent.

Correction:
assistant BLOCKED ingress rather than inferring missing material.

Resulting invariant:
no-inference / seal gate became behaviorally enforced in that historical attempt.

## ERR-D0-005 — current v2.0 coverage inconsistency
Event:
v2.0 says D1–D10 while concrete outputs cover D1/D2/D3/D4/D8; D9 appears in authority but not handoff.

Detection:
assistant spec review.

Repair:
none owner-confirmed.

Status:
OPEN. Do not silently add or remove D channels.

## ERR-D0-006 — potential historical rewrite after v2.0
Risk:
reading current D-only D0 as if it had always been D-only.

Repair:
this recovery keeps v1.x E-coupled epochs and the breaking-refactor boundary explicit.
