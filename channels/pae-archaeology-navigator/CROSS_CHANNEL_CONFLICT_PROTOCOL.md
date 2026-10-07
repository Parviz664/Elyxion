# CROSS_CHANNEL_CONFLICT_PROTOCOL

## Purpose

When two recovered channels disagree, PAE must expose the disagreement without stealing Global C0 authority.

## Required conflict record

For each material conflict capture:

- conflict_id
- claim_A
- source_A
- time_A
- scope_A
- authority_A
- claim_B
- source_B
- time_B
- scope_B
- authority_B
- possible_classification
- evidence_for_supersession
- evidence_against_supersession
- current PAE verdict
- escalation_required

## PAE verdicts

NO_CONFLICT_DIFFERENT_SCOPE
HISTORICAL_SUPERSESSION_STRONGLY_SUPPORTED
SUPERSESSION_CANDIDATE
PARALLEL_VALID_ROUTES
HOLD
UNKNOWN
GLOBAL_C0_REQUIRED

## Example: A0 vs A3 route history

A0 recovery:
latest local v4.1 says A_ULTRA -> A0 -> E0;
A1/A2/A3 legacy/recovery.

A3 recovery:
later March evidence reconstructs A1 -> A2 -> A3 -> E0 adult path after A2 v2.x changes.

PAE status:
CROSS_CHANNEL_TEMPORAL_CONFLICT / GLOBAL_RECONCILIATION_REQUIRED.

PAE may explain the chronology.
PAE must not declare the final global route unless authority is supplied.

## Example: P5

P5 exists and has a recovered current contract.
P4 recovery says P5 is disabled by default.

PAE interpretation:
NO_CONFLICT.
Existence and activation are separate dimensions.

## Example: -P1

Historical route with -P1 and later NO_-P1 route both exist.
Owner Decision C keeps present route unresolved.

PAE verdict:
HOLD.
No automatic resolution.

## Escalation rule

If the user's question requires:
- globally current route;
- global activation;
- authority ownership;
- canon reconciliation;
- cross-front precedence;

then PAE prepares evidence and hands the question to Global C0 rather than answering beyond evidence.
