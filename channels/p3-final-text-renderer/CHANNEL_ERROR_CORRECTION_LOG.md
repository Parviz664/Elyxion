# CHANNEL_ERROR_CORRECTION_LOG

## EC-P3-001 — provenance overclaim in wider recovery

error:
Earlier P-system recovery language used labels such as owner-origin or direct-owner artifact where chat supply did not prove line-by-line authorship.

detection:
2026-10-06 durable P Control Point provenance correction.

correction:
USER_SUPPLIED_CHAT_ARTIFACT is separated from OWNER_EXPLICIT_DECISION and AUTHOR_RAW.

resulting_invariant:
SUPPLIED_BY_AUTHOR != AUTHORED_BY_AUTHOR.

applies_to_P3:
Yes. Full v3.1.1/v3.2.0 specs are user-supplied active artifacts, not automatically author-written RAW.

status:
REPAIRED / APPEND_ONLY.

## EC-P3-002 — recovery evidence ceiling too low, not a contract error

state:
P3_CONTRACT_RECOVERY_PASS_V0_1 on 2026-10-06 reported:
OUTPUT_SCHEMA = UNKNOWN
MERGE_SPLIT_RULES = UNKNOWN
VERSION_LINEAGE = PARTIAL.

later_detection:
current channel contains full v3.1.1 and v3.2.0 specs plus practice output.

repair:
do not modify the old recovery as if it had known more.
add this P3-specific recovery branch with stronger evidence.

resulting_invariant:
later evidence may raise confidence, but historical recovery-state must remain preserved.

status:
EVIDENCE_GAP_NARROWED.

## EC-P3-003 — namespace collision risk

historical risk:
older P2 packets echoed P1 identifiers such as B001 while P3 itself also used B###.

detection:
v3.2.0 supplied contract explicitly adds NAMESPACE_HYGIENE.

repair:
P3 B### = P3_CANON_B only.
P1 block echoes remain P1_BLOCK_LEGACY or P1_BLOCK_SAFE trace.

resulting_invariant:
same glyph pattern cannot imply same authority namespace.

status:
CONTRACT_REPAIR_ACTIVE.

## EC-P3-004 — closure montage risk

historical risk:
core -> closure pair rhythm can make service closures look like independent causal worlds.

detection:
v3.2.0 anti-montage and closure-tone policies.

repair:
closure_shift must read as bottleneck completion/shift, not a second core.
No causal reorder or untracked drop.

resulting_invariant:
role weight may change; meaning may not.

status:
CONTRACT_REPAIR_ACTIVE.

## EC-P3-005 — speculative smooth-fact risk

historical risk:
late bridges can be made rhetorically strong by removing visible uncertainty.

detection:
v3.2.0 speculative render policy.

repair:
bounded inevitability:
strong causal forced-next + preserved locality/uncertainty.

resulting_invariant:
stronger prose cannot create stronger evidence.

status:
CONTRACT_REPAIR_ACTIVE.

## EC-P3-006 — emotion-word feel gate risk

historical issue:
FEEL_COVERAGE_MIN could reward explicit emotion words rather than causal pressure.

detection:
v3.1.1 patch explicitly deprecates it.

repair:
OBSERVABLE_MARKERS_COVERAGE_MIN.

resulting_invariant:
feel must be inferable from causal world pressure.

status:
SUPERSEDED_BEHAVIOR / ACTIVE_REPLACEMENT.

## EC-P3-007 — observed assistant output hash caveat

artifact:
current assistant P3 v3.2 output before recovery.

observation:
source_line_hash fields use symbolic forms such as sha1:P2I001 rather than a demonstrated computed digest.

author_detection:
NOT RECOVERED.

classification:
IMPLEMENTATION_CAVEAT, not owner-confirmed error.

repair_in_this_recovery:
do not claim those values are cryptographically verified hashes.
retain that semantic fingerprint, not line hash, controls identity anyway.

status:
OPEN_CAVEAT / NON_BLOCKING_FOR_ROLE_RECOVERY.
