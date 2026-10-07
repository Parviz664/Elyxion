# CHANNEL_ERROR_CORRECTION_LOG

## ERR-A1-001 — v3.1 law used as work payload
After the v3.1 law was pasted, the assistant treated the law itself as a vision task and produced an AnomalousValley architecture. This conflicts with the contract hard-fail condition for absent usable vision intent. No explicit author correction was recovered. Preserve this as ASSISTANT_EXECUTION_ERROR, not canon.

Resulting recovery invariant: contract installation and stage execution are separate operations.

## ERR-A1-002 — v3.2 law used as work payload
The same pattern recurred after the v3.2 law: governance architecture was generated from the law instead of waiting for usable stage vision. Classification: ASSISTANT_OVERREACH / ROUTING_AMBIGUITY. Historical practice only.

## ERR-A1-003 — v3.3 law used as work payload
The same pattern recurred after the v3.3 law. Classification: ASSISTANT_OVERREACH / ROUTING_AMBIGUITY. Do not treat the generated governance architecture as a new channel function.

## ERR-A1-004 — invented implementation context
The first invalid v3.1 execution introduced a concrete test context despite absent upstream stage vision. Preserve as INVENTED_IMPLEMENTATION_CONTEXT and do not back-project it into canon.

## ERR-A1-005 — declared percentages are not measurements
Later laws contain 99.x target/guarantee language. This recovery found no independent measurement evidence. Preserve them as contract targets, not VERIFIED results.

## ERR-A1-006 — v3.3 lane duplication tension
v3.3 says build nouns belong in the implementation lane, while append-only legacy root schema still requires implementation-bearing fields. The observed outputs keep both. Final owner interpretation is UNKNOWN / HOLD; no silent repair.
