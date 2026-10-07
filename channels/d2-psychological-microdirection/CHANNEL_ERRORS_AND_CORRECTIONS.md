# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-D2-001 — early assistant role over-definition

Initial assistant behavior:
D2 was described as:
- onboarding / first-minutes optimizer;
- later a Психо-динамический Сценарный Валидатор и Калибратор Воздействия.

Problem:
these were assistant framings while the user still considered D2's actual function unresolved.

Detection:
user stated they would explain what D2 actually does.

Author correction:
exact full correction message is not recovered, but the later author Cosmic Awe intent and formal v1.1 microdirection contract supersede those assistant framings.

Repair:
mark early names as ASSISTANT_PROPOSAL / HISTORICAL, not owner-canonical.

Resulting invariant:
assistant role naming does not become D2 identity without owner confirmation or stronger artifact evidence.

## ERR-D2-002 — first v1.1 execution invented grounded-looking context

Initial assistant response after v1.1:
created zone IDs, candidate IDs, route bindings, scores and trace IDs before a demonstrably complete upstream packet bundle had been supplied in the visible sequence.

Problem:
structural completeness looked like provenance.

Detection:
later user supplied actual E2 execution result packets, revealing what grounded source binding should look like.

Repair:
later D2 executions bind to explicit E2 packet IDs and variants.

Resulting invariant:
no concrete zone/variant/trace facts without actual upstream evidence.

Historical status:
ERROR_RECORDED.

## ERR-D2-003 — placeholder hashes could be mistaken for verification

Recovered assistant outputs contain:
PENDING_IN_RUNTIME_VALIDATOR
and earlier placeholder hash strings.

Problem:
these are not cryptographic proof.

Repair:
this recovery marks deterministic hashing as CONTRACTED_NOT_VERIFIED.

Resulting invariant:
placeholder != SHA256 evidence.

## ERR-D2-004 — v1.2 missing registry/seal handled correctly

This is a correction success.

Earlier pattern:
assistant could produce a structurally complete packet from incomplete context.

v1.2:
no-inference + registry/seal became explicit.

Assistant behavior:
BLOCK rather than invent registry/seal refs.

Resulting invariant:
missing sealed source evidence stops normal microdirection.

## ERR-D2-005 — v1.3 missing evidence misclassified as detected mutation

Assistant v1.3 BLOCK triggered:
FC_D2_002 any_mutation_of_immutable_fields_detected

Details claimed:
immutable validation cannot be performed because packets are missing, treated as unsafe/unknown.

Problem:
UNKNOWN/unvalidated is not semantically identical to mutation_detected.

Correct block basis already existed:
FC_D2_011 D-registry/seal missing plus missing mandatory packets.

Repair in recovery:
retain overall BLOCK;
do not retain factual claim that mutation occurred.

Resulting invariant:
absence of proof != proof of mutation.

## ERR-D2-006 — possible versioning inconsistency in supplied v1.3 artifact

Artifact:
v1.3 calls patch breaking_dependency_cleanup_with_schema_preservation.

Own semver rule:
breaking authority changes -> major.

Observed:
all E dependencies removed and authority route rebound to D-line, yet version increments minor.

This is not an assistant error and not automatically an author error.

Classification:
INTERNAL_ARTIFACT_TENSION.

Repair:
none; preserve as GAP.

## ERR-D2-007 — possible seal-waiver contradiction

Artifact simultaneously contains:
- cannot operate without verified registry+seal;
- no-inference absolute;
- waiver_mode enabled.

No explicit resolution recovered.

Classification:
CONTRACT_AMBIGUITY.

Repair:
none; preserve as GAP, do not choose interpretation.

## Error-handling law

Errors are historical evidence.
Do not erase them to make D2 look cleaner.
