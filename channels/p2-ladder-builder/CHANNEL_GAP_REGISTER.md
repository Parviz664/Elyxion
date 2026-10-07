# CHANNEL_GAP_REGISTER

## GAP-P2-001 — original birth rationale
status: OPEN
severity: historical-fidelity
known:
P2 exists by 2026-02-12.
unknown:
what exact problem the author explicitly named when creating it.
rule:
do not backfill with later architecture logic.

## GAP-P2-002 — earliest contract/name
status: OPEN
known:
distinct P2 node exists.
unknown:
pre-v3.2.1 human name, channel id, schema and version.

## GAP-P2-003 — v3.3 PATCH labels
status: OPEN
known:
PATCH-1..10 exist and behavior delta is partially recovered.
unknown:
exact full text of every patch label/body.

## GAP-P2-004 — v3.4 full bytes
status: OPEN
known:
v3.4 existed and was immediate predecessor to v3.5.
unknown:
complete exact contract body and patch list.

## GAP-P2-005 — range/count behavior on compressed inputs
status: OPEN
observed:
P1 packet can expose range 1..80 with only a few micro-stages and output_size_hint 1..1.
assistant practice converted range to 1..6 and emitted six items.
problem:
no recovered rule proves this exact conversion.
risk:
silent contract reinterpretation.

## GAP-P2-006 — upstream split contradiction
status: OPEN
observed:
current P1 M005:
- p2_mandatory_support asks for split/deepening;
- p2_split_permission.allowed=false.
P2 cannot obey both.
required behavior:
surface conflict; do not silently choose.

## GAP-P2-007 — origin-specific maturity zones in generic P2
status: OPEN
observed:
v3.5 hardcodes maturity attention to M056/M060/M068/M072/M076/M080 and tier-1 M068/M076/M080.
problem:
cross-domain tasks may not contain those IDs.
risk:
schema contamination / fake telemetry.

## GAP-P2-008 — mechanics boundary
status: OPEN
observed:
P2 hard rules forbid gameplay mechanics.
current P1 Phases 1–3 allows mechanics as SURFACE_ONLY_NO_STEPS.
unknown:
exact compatibility law.

## GAP-P2-009 — runtime implementation
status: OPEN
no standalone P2 code/runtime/validator was found in current repo search.
contract-in-chat != runtime implementation.

## GAP-P2-010 — global route
status: INTENTIONALLY_OPEN
authority:
owner Decision C.
question:
current -P1 route.
P2 local seam remains strong; global route cannot be frozen.
