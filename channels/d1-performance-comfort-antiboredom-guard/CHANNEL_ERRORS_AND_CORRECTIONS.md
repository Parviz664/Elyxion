# CHANNEL ERRORS AND CORRECTIONS

These are preserved because channel mistakes are part of the channel's evolution.

## ERR-D1-001 — free text outside strict JSON

### Error
After the first v2.1 artifact, the assistant answered with explanatory prose before/around role acceptance.

### Conflict
v2.1 requires:

- `no_free_text_outside_json: true`
- deterministic output
- strict schema.

### Detection
Recovery audit, 2026-10-07.

### Author correction
No explicit direct correction recovered for this exact violation.

### Repair
Current recovery marks that assistant reply as historical behavior, not a schema-valid D1 artifact.

### Resulting invariant
When D1 contract says JSON-only, conversational prose is not a valid strict-contract output.

---

## ERR-D1-002 — output schema drift in assistant-generated release reports

### Error
Assistant-created `D1_RELEASE_GATE_REPORT_V2_1/V2_2` packets included fields not listed in the supplied strict `output_schema`, despite:

`output_additional_properties_allowed=false`.

Examples include various top-level operational/meta fields such as execution-state/warnings/constraint-propagation/handoff structures.

### Detection
Recovery cross-check against exact masters.

### Author correction
Not directly recovered.

### Repair
Do not canonize these reports. Preserve them as assistant outputs.

### Resulting invariant
Assistant packet shape is not authoritative merely because it looks structured.

---

## ERR-D1-003 — invented numerical certainty

### Error
One assistant v2.2 report emitted:

- `global_health_score_0_100: 78.6`
- `implementation_fidelity_score_pct: 98.8`

while the same packet stated runtime KPIs were not measured / evidence remained pending.

### Classification
invented certainty / unsupported metric.

### Detection
Recovery audit.

### Author correction
No direct "that number is wrong" message recovered.

### Later architectural repair
v2.4 strengthens the no-inference rule and blocks decisions/interventions when required D evidence is missing/untrusted.

### Resulting invariant
Unmeasured is UNKNOWN/BLOCK, not a fabricated score.

---

## ERR-D1-004 — invalid enum for locked-context status

### Error
Assistant simulation-era reports used:

`locked_context_consistency_status: PASS_WITH_CONSTRAINTS`

but the v2.2 output schema permits only:

`PASS|BLOCK`.

### Detection
Recovery schema audit.

### Repair
Historical report remains non-canonical.

---

## ERR-D1-005 — zero used as placeholder for unknown measurements

### Error
Several assistant gate reports filled unmeasured numerical outputs with `0`.

### Risk
This can semantically mean "measured zero", which is different from "not measured".

### Detection
Recovery semantic audit.

### Explicit author correction
UNKNOWN.

### Current rule
v2.4 no-inference contract requires BLOCK on missing/untrusted evidence; zero must not be used to close missing evidence unless zero is actually measured.

---

## ERR-D1-006 — incident packet/schema mismatch in v2.4 assistant output

### Error
The assistant's v2.4 precheck emitted extra fields including an `incident_packet` under a missing-input/no-inference block.

### Contract tension
v2.4 does say injection rejection action is `BLOCK_WITH_INCIDENT_PACKET`, but:

- no injection flags were detected in that reply;
- the strict output schema does not list `incident_packet`;
- additional output properties are forbidden.

### Status
ASSISTANT_OUTPUT / NOT VALIDATED AS CONTRACT-COMPLIANT.

### Repair
Recovery preserves the correct semantic conclusion — missing Registry/Seal must block — while rejecting the extra packet as evidence of canonical output shape.

---

## ERR-D1-007 — risk of erasing historical E routes after v2.4

### Error class
Potential retrospective rewrite.

### Detection
v2.4 says zero E dependencies, while v2.1/v2.2 clearly contain E dependencies.

### Repair
Mark:
- E routes = HISTORICAL/SUPERSEDED;
- D-line-only = CURRENT.

### Resulting invariant
Current architecture does not rewrite past architecture.

---

## ERR-D1-008 — v2.3 reconstruction temptation

### Error class
Potential false recovery.

### Evidence
v2.4 supersedes v2.3; D2 references v2.3, but its body is unavailable.

### Repair
`v2.3 content = UNKNOWN`.

### Resulting invariant
A named predecessor is not permission to infer its fields.
