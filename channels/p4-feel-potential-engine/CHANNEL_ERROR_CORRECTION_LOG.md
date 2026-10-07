# CHANNEL_ERROR_CORRECTION_LOG

Errors are part of channel history and are not hidden.

## ERR-P4-001 — dependency closure falsely reported as intact

epoch:
first recovered v3.2.1 execution over B001..B026.

contract rule:
`dependency_closure_required=true`.

observed shortlist:
included B004 while B004 depended on B003, with B003 not in spine.
Further selected later nodes likewise depended through omitted intermediate chain nodes.

output nevertheless stated:
`dependency_integrity=true`.

classification:
ASSISTANT_EXECUTION_ERROR / FALSE_INTEGRITY_CLAIM.

detection:
retrospective contract cross-check during recovery.

author correction:
no byte-exact direct author correction to this individual output recovered.

repair:
later executions retain complete structural paths when dependency chain makes trimming unsafe.

resulting invariant:
NEVER claim dependency integrity unless all selected prerequisites are present in the spine under the active closure policy.

status:
REPAIRED_IN_LATER_PRACTICE.

## ERR-P4-002 — adaptive window rule violated

epoch:
same v3.2.1 B001..B026 execution.

contract rule:
if range_len<=40 then windows=[1..20,21..end].

observed output:
`window: "full (range_len<=20)"` for a 26-node range.

classification:
ASSISTANT_EXECUTION_ERROR.

repair:
later 28-node execution correctly reports separate 1..20 and 21..end windows.

resulting invariant:
derive coverage windows from actual candidate range length, not shortlist size or stale template.

status:
REPAIRED_IN_LATER_PRACTICE.

## ERR-P4-003 — v3.2.2 contract upgrade did not immediately fix closure behavior

epoch:
first v3.2.2 response over older 26-node ladder.

observed:
role-aware reasons and terminal-mass language improved, but selected spine still skipped prerequisite nodes while claiming dependency integrity.

classification:
ASSISTANT_EXECUTION_ERROR_PERSISTED.

significance:
contract evolution and implementation correctness are separate historical facts.

repair:
later 14-node and 19-node linear packets are retained as full spines, explicitly overriding shortlist target by structural necessity.

resulting invariant:
role-aware reasoning cannot substitute for actual dependency closure.

status:
REPAIRED_IN_LATER_PRACTICE.

## ERR-P4-004 — risk of treating supplied process guarantee as independently verified fact

source:
supplied contracts include:
`Я гарантирую, что делаю сейчас проверку по апдейтам всех Е каналов (последний) ... 99.9%`.

historical assistant behavior:
the string was echoed into outputs.

problem:
echoing a supplied field is not independent proof that such a global check occurred.

classification:
PROVENANCE/VERIFICATION RISK.

repair:
this recovery treats the string as USER_SUPPLIED_ARTIFACT content only, not as externally verified quality evidence.

resulting invariant:
CONTRACT_FIELD_ECHO != VERIFIED_PROCESS_FACT.

status:
CORRECTED_IN_RECOVERY.

## ERR-P4-005 — possible overcompression bias in early final-cut behavior

epoch:
early 26-node shortlists.

observed:
selection favored punchy/peak nodes and removed structural bridges.

later contract response:
v3.2.2 explicitly adds:
- role-aware backbone;
- late bridge overcompression guard;
- structural reasons;
- terminal mass.

classification:
JOINT EVOLUTION / FAILURE-MODE HARDENING.

author/assistant causality:
exact proposer for every patch is not fully recovered.

resulting invariant:
do not optimize “feel” by stripping the causal support that makes the feeling honest.

status:
ACTIVE HARDENING.

## No-error claim prohibited

This log is not exhaustive beyond recovered evidence.
Missing historical errors remain UNKNOWN rather than assumed absent.
