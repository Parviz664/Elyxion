# CHANNEL_ERROR_LOG

Errors and corrections are part of E2's history and are not normalized away.

## ERR-E2-001 — v1.1 kernel lock mismatch in assistant execution

### Contract
The recovered v1.1 master requires:
`kernel_schema_version = 1.0.0`.

### Assistant execution
A later assistant-generated `ELYX_E2_EXECUTION_RESULT_V1_1` ingested/echoed `kernel_schema_version = 1.1.0` and marked locked-context integrity as PASS.

### Detection
Current recovery cross-check of the exact v1.1 master against the assistant-generated execution.

### Repair
v1.2 later explicitly aligns the locked kernel schema to `1.1.0`.

### Resulting invariant
Execution packets cannot silently substitute a later upstream lock value for the active master contract.

Provenance: ASSISTANT_ERROR → later USER_SUPPLIED_ARTIFACT repair.

---

## ERR-E2-002 — confidence-governor rule falsely reported as triggered

In the first assistant-generated v1.1 D1-closure result:
- recommendation band = MEDIUM;
- unresolved critical assumptions = 1;
- packet reports `forced_outcome_rule_triggered = E2-CG-002`.

But v1.1 `E2-CG-002` condition is:
`MEDIUM and unresolved_critical_assumptions > 1`.

With value 1, the condition is not satisfied.

Status: assistant-generated operational inconsistency; no evidence that owner canonized it.

---

## ERR-E2-003 — rejected frontier entry conflicts with checkpoint-completeness claim

In the assistant-generated REF_ONLY v1.1 packet:
- `E2-VAR-REF-003` is inside `variant_set`;
- it has only one checkpoint;
- v1.1 contract requires at least three checkpoints per variant;
- packet nevertheless states `min_checkpoints_per_variant_satisfied = true`.

The same item is conceptually described as a rejected frontier and should not be silently counted as a valid variant.

Status: assistant-generated operational inconsistency.

---

## ERR-E2-004 — declared determinism vs under-specified math

v1.0/v1.1 declare deterministic same-input/same-output behavior, while assistant review identified missing explicit aggregation/rounding/penalty rules for overall scoring.

This is preserved as:
- CONTRACT CLAIM: deterministic;
- ASSISTANT REVIEW: implementation ambiguity remained.

No owner correction proving the exact proposed math was adopted has been recovered.

---

## CORR-E2-001 — v1.2 no-inference hardening

v1.2 adds registry+seal/no-inference and blocks when the registry/seal is missing. The assistant v1.2 execution then correctly emits BLOCK instead of inventing missing locked state.

Historical effect: moves E2 from permissive reasoning over incomplete packet sets toward evidence-gated refusal.

---

## CORR-E2-002 — v2.1 missing-input BLOCK

The assistant v2.1 execution correctly refuses to emit Engine Contract Map / E5 affordances when E0 dual-lock and E1 skeleton inputs are missing.

This is a repair in behavior relative to earlier over-eager operational packets, but not proof of a new owner-authored rule beyond the supplied v2.1 master.
