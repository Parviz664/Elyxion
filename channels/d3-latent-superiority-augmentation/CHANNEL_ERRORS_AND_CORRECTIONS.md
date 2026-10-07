# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-D3-001 — route contradiction preserved

ERROR / MISMATCH:
earliest recovered chain places D3 before E3:
... D2 -> E2 -> D3 -> E3.

Later same-day AUTHOR_RAW says D3 takes E3 and leaves it unchanged, and v1.0-v1.2 formalize E3 -> D3 -> E4.

Detection:
recovery cross-check.

Author correction:
no exact explicit "the earlier route was wrong" message recovered.

Repair:
preserve both as historical states; do not invent reconciliation.

Resulting recovery invariant:
route conflict must remain visible.

## ERR-D3-002 — premature assistant PASS after v1.1 contract

ERROR:
after receiving only the v1.1 channel contract, assistant emitted a fully populated PASS augmentation packet with specific synthetic-looking refs, scores, adversarial pass rates, friction scores and byte-equivalence conclusion.

Why invalid as durable evidence:
required E3/D2/E2/E1/D1 packets and immutability evidence had not been supplied in that turn.

Detection:
current-conversation archaeology.

Author correction:
no explicit rebuke recovered in the immediate next message; user instead supplied an actual E3 execution artifact.

Repair:
classify initial packet as ASSISTANT_OUTPUT / PREMATURE_EXECUTION / NOT VERIFIED.

Resulting invariant:
never convert contract alone into evidence-backed execution PASS.

## ERR-D3-003 — invented quantitative evidence in assistant executions

ERROR:
normal v1.1 assistant execution generated exact evidence strengths, adversarial rates, budget usage and superiority values without demonstrated external measurement/test source.

Detection:
recovery provenance audit.

Author correction:
not explicitly recovered.

Repair:
these numbers remain historical assistant-generated simulation/analysis values, not observed runtime facts.

Resulting invariant:
predicted/synthetic evaluation must be labeled as such; observed evidence requires source IDs.

v1.2/v1.3 reinforcement:
evidence_id_set and registry/seal/no-inference make this boundary explicit.

## ERR-D3-004 — supplied artifact authorship risk

ERROR CLASS:
a user-pasted contract could be incorrectly labeled AUTHOR_RAW/AUTHOR_AUTHORED.

Detection:
current recovery instruction explicitly states:
SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR.

Repair:
v1.1/v1.2/v1.3 full JSON contracts classified USER_SUPPLIED_ARTIFACT, artifact_origin UNKNOWN_OR_JOINT unless separately proved.

Resulting invariant:
do not assign assistant-generated wording to author.

## ERR-D3-005 — assistant interpretation inflation

Historical assistant explanations used phrases such as:
"боевой D3", "охранник мечты", "абсолютный" conclusions.

These may be useful explanations but are not contract fields unless the user separately confirms them.

Repair:
classified ASSISTANT_INTERPRETATION, excluded from current role core unless supported by supplied spec.

## ERR-D3-006 — v1.3 waiver/no-inference tension

Not necessarily an error; an unresolved contract tension.

v1.3 says:
D-registry+seal/no-inference absolute and D3 cannot operate without verified inputs.

It also contains waiver_mode.

No owner-authoritative interpretation of whether registry/seal absence itself can be waived is recovered.

Repair:
preserve as GAP/UNKNOWN; do not resolve by inference.
