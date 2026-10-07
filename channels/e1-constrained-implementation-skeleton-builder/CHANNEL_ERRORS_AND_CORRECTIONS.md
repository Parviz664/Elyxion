# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-E1-001 — provenance overclaim risk at v1.0

Pattern:
a contract is supplied by the user later, but evidence indicates it was first assistant-generated.

Risk:
incorrectly labeling the full v1.0 text AUTHOR_RAW.

Correction:
classify as ASSISTANT_PROPOSAL -> USER_SUPPLIED_ARTIFACT / later operationally accepted.

Resulting invariant:
SUPPLIED_BY_AUTHOR != AUTHORED_BY_AUTHOR.

## ERR-E1-002 — assistant rationale mistaken for owner rationale

The assistant explained why E1 design choices were “right” or “production-grade”.

Correction:
those explanations are ASSISTANT_INTERPRETATION unless the user independently states the reason.

Resulting invariant:
reason_explicit=false => reason=UNKNOWN.

## ERR-E1-003 — invented operational fields in assistant response

The assistant-generated ELYX_E1_EXECUTION_RESULT_V1_2 introduced concrete IDs/timestamps such as a created_at_utc value.

Risk:
treating synthesized operational metadata as upstream fact.

Correction:
response packet remains evidence of assistant operation only; generated IDs/timestamps are not historical source truth unless echoed/accepted by authoritative upstream.

## ERR-E1-004 — audit recommendations could be mistaken for lineage

Assistant audits proposed:
- v1.0 hardening ideas;
- a v1.3 delta;
- v1.4.1 fixes.

Correction:
none become accepted versions without owner artifact/decision evidence.

## ERR-E1-005 — epoch collapse

Risk:
describing E1 as skeleton-only for all history.

Correction:
preserve two fundamentally different eras:
1. v1.0–v1.3 execution-thinking/drafting;
2. v1.4+ skeleton-only.

Resulting invariant:
current role must never overwrite historical role.

## ERR-E1-006 — direct registry ownership after v1.4

v1.3 directly required registry+seal.
v1.4 explicitly moves to E0 locked-handle-only ingress.

Correction:
do not carry v1.3 direct-registry behavior into v1.4+.

## ERR-E1-007 — psycho-touchpoint authorship after v1.4

v1.2/v1.3 allowed E1 psycho-operational annotations.
v1.4 states D1 touchpoints are not authored here.

Correction:
do not silently preserve removed D1-authoring power.

## ERR-E1-008 — E3 authority leakage

v1.4 initially had parallel E3 handoff for build plan.
v1.6 explicitly hardens weak E3 visibility and no hidden E2/E3.

Correction:
E1 cannot use the E3 visibility packet as hidden build-plan authority.
