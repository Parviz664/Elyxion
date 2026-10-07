# CHANNEL_GAP_REGISTER

## GAP-P3-001 — original birth event
severity: historical_completeness
status: OPEN
known:
P3 exists by recovered 2026-02-12 route.
unknown:
exact first creation date, first name, first contract, first owner wording.
impact:
does not block current role use; blocks full origin archaeology.

## GAP-P3-002 — v3.1.0 exact body
severity: lineage
status: OPEN
known:
v3.1.1 explicitly says it is append-only strengthening of v3.1.0.
unknown:
full v3.1.0 schema and exact fields.
impact:
do not reconstruct by subtraction.

## GAP-P3-003 — pre-v3.1 contract versions
severity: lineage
status: OPEN
known:
P3 node existed before v3.1 evidence.
unknown:
version numbers, schemas, names.
impact:
historical lineage remains partial before v3.1.

## GAP-P3-004 — exact artifact authorship
severity: provenance
status: OPEN
known:
v3.1.1 and v3.2.0 were supplied by the user as active specs.
unknown:
who originally authored each line and which parts were AI-proposed/joint.
impact:
must retain USER_SUPPLIED_ARTIFACT rather than AUTHOR_RAW for whole specs.

## GAP-P3-005 — direct A3 route
severity: interface
status: OPEN
known:
v3.1.1/v3.2 output is one_root_ready_for_A3.
unknown:
exact A3 input contract and whether P3 is a direct production upstream.
impact:
classify as readiness, not route.

## GAP-P3-006 — external runtime implementation
severity: implementation
status: OPEN
known:
chat execution of v3.2 behavior exists.
unknown:
runtime code, test suite, CI or engine implementation of P3.
impact:
IMPLEMENTED_IN_CHAT != RUNTIME_VERIFIED.

## GAP-P3-007 — complete raw transcript preservation
severity: evidence
status: PARTIAL
known:
strong artifacts are present in current conversation and prior-context recovery.
unknown:
whether every historical P3-related message has been durably archived byte-for-byte.
impact:
some direct-user wording remains RECOVERED_FROM_PRIOR_CONVERSATION rather than immutable RAW file.

## GAP-P3-008 — current global P-route
severity: architecture_authority
status: INTENTIONALLY_OPEN
known:
route family A and B both existed.
current owner decision:
C = HOLD_UNRESOLVED.
impact:
P3 recovery must not freeze standalone -P1 status.

## GAP-P3-009 — generic merge/split semantics before v3.1.1
severity: historical_contract
status: OPEN
known:
v3.1.1+ supplies bounded merge/dedup/patch behavior.
unknown:
whether earlier P3 had materially different generic merge/split semantics.
impact:
do not project current behavior backward.

## GAP-P3-010 — status relationship between channel spec and global canon
severity: authority
status: BOUNDED
known:
specs are active working contracts in conversation.
known:
P3 has no automatic project-canon authority.
unknown:
which external owner action, if any, formally canonized each contract globally beyond use in conversation.
impact:
mark CONTRACTED/WORKING, not global canon unless separately evidenced.
