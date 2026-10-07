# CHANNEL_ERROR_CORRECTION_LOG

## E-P2-001 — incomplete v3.2.1 practice expansion
type:
ASSISTANT_EXECUTION_WEAKNESS.
detected:
recovered execution only covered part of target range and binding was weak.
author correction:
not recovered.
repair:
later contracts hardened range/binding/IDs.
resulting invariant:
binding integrity and range semantics became explicit.

## E-P2-002 — range semantics contract mine
type:
HISTORICAL_CONTRACT_RISK.
detected:
later specs explicitly warn against treating count-hints as index ranges.
repair:
v3.3+ locks `range_semantics=index_range`, count-hints move to separate fields.
resulting invariant:
range means index range only.

## E-P2-003 — bridge-safe mistaken for depth
type:
STRUCTURAL_MATURITY_RISK.
detected:
v3.5 patch rationale.
repair:
zone maturity + support mass + terminal preseal.
resulting invariant:
contract-clean/safe != structurally mature.

## E-P2-004 — current assistant auto-range reinterpretation
type:
ASSISTANT_OVERREACH_RISK.
context:
current Phases 1–3 P2 execution.
behavior:
P1 range 1..80 was converted to P2 1..6 and source range was called legacy trace.
problem:
no recovered source proved the upstream range was a legacy count-hint misuse.
author correction:
none yet.
repair:
NOT APPLIED; recorded as gap.
resulting invariant:
future recovery must not treat that execution as contract truth.

## E-P2-005 — current count-hint mismatch not escalated
type:
ASSISTANT_VALIDATION_MISS.
context:
P1 `output_size_hint={min:1,max:1}`; P2 emitted six items.
problem:
execution did not surface this as a decisive contract mismatch.
repair:
recorded, not silently normalized.
status:
OPEN.

## E-P2-006 — generic zone telemetry inserted into unrelated scope
type:
ASSISTANT_SCHEMA_OVERAPPLICATION_RISK.
context:
current Phases 1–3 execution emitted M068/M076/M080 compatibility telemetry even though task used M001..M006.
problem:
may confuse origin-specific maturity defaults with universal domain truth.
repair:
recorded as GAP-P2-007.
status:
OPEN.

## E-P2-007 — upstream split contradiction
type:
UPSTREAM_CONTRACT_CONFLICT.
context:
P1 M005 both demands split-support and forbids split.
P2 execution chose not to split and marked underbuilt.
assessment:
this avoided unauthorized splitting, but did not resolve the contradiction.
resulting invariant:
conflicting upstream permissions must be surfaced, not synthesized away.
