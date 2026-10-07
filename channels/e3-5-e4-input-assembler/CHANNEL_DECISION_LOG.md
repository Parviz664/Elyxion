# CHANNEL_DECISION_LOG

## D-001 — create E3.5

date:
2026-02-18T10:16:05Z.

question:
whether to create the proposed E3.5 channel.

author selection:
“хорошо сделай этот Е3.5”

assistant recommendation before this:
not recovered.

explicit author rationale:
UNKNOWN.

consequence:
assistant creates E3.5 three seconds later.

status:
ACTIVE historical origin decision.

## D-002 — strict-contract operation

date:
2026-02-18T10:21:18Z.

author raw:
“Работать строго по контракту Е3.5!!!”

selection:
use the supplied E3.5 contract strictly.

consequence:
v1.0 becomes the first exact recovered working contract.

status:
ACTIVE principle, later strengthened.

## D-003 — ref-only strict architecture

date:
2026-02-18T10:22:53Z.

artifact:
v1.1 user-supplied.

options explicitly represented:
REF_ONLY_STRICT
PARTIAL_WITH_WAIVERS.

default selected by supplied artifact:
REF_ONLY_STRICT.

explicit author rationale:
not separately stated outside artifact.

consequence:
source content is no longer to be compacted, aggregated or reserialized.

status:
ACTIVE lineage principle.

## D-004 — scope “100%” to inputs/coverage, not total E4 PASS

date:
2026-02-18T10:25:04Z.

artifact:
v1.2.

selection:
hard guarantees are bounded to no semantic mutation, no-drop coverage and elimination of E4 missing-input/unprovable-coverage BLOCK class.

explicit non-selection:
E4_TOTAL_PASS.

consequence:
channel authority ceiling becomes explicit.

status:
ACTIVE.

## D-005 — allow BOOTSTRAP dual roots without merge

date:
2026-02-18T21:37:37Z.

trigger evidence:
earlier supplied BOOTSTRAP_LIMITED D3 input had separate bootstrap and canon-patch roots and v1.2 could not validate it.

artifact:
v1.3.

selection:
add LANE_V2_BOOTSTRAP_DUAL_ROOT_REF_ONLY.

alternatives:
silent merge is explicitly forbidden;
SIM-only remains default.

explicit rationale:
yes, supplied v1.3 states this fixes the dual-root BOOTSTRAP case while preserving no-merge.

status:
ACTIVE in v1.3+.

## D-006 — change type validation from exact-only to same-major minimum

date:
2026-02-20T11:55:46Z.

artifact:
v1.4.

selection:
MIN_VERSION_SAME_MAJOR default;
strict exact remains available as override.

explicit artifact rationale:
avoid false BLOCKs on later same-major packets while preserving proofable version compatibility.

status:
ACTIVE in latest supplied spec.

## D-007 — add registry/seal proof and anti-injection

date:
2026-02-20T11:55:46Z.

artifact:
v1.4.

selection:
fail-closed registry/seal presence proof;
anti-injection reject rules;
deterministic hash fields.

status:
ACTIVE in latest supplied spec.

## D-008 — assistant v1.4.1 patch proposal

date:
2026-02-20T11:56:06Z.

origin:
ASSISTANT_PROPOSAL.

proposal:
four compatibility/clarity patches.

author selection:
NOT RECOVERED.

status:
HOLD / NOT OWNER-CONFIRMED.

## D-009 — full archaeology before GitHub write

date:
2026-10-07.

author decision:
recover real channel history first, preserve provenance and UNKNOWNs, self-audit, then write to Parviz664/Elyxion on a separate channel recovery branch.

status:
ACTIVE for this recovery operation.
