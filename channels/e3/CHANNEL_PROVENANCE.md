# CHANNEL_PROVENANCE

Classes:
AUTHOR_RAW
AUTHOR_CONFIRMED
AUTHOR_DECISION
USER_SUPPLIED_ARTIFACT
ASSISTANT_PROPOSAL
ASSISTANT_INTERPRETATION
JOINT_ITERATION
RECOVERED_FROM_LATER_REFERENCE
GITHUB_ARTIFACT
UNKNOWN_ORIGIN

Critical law:
SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR.
ASSISTANT_RATIONALE != AUTHOR_RATIONALE.

## Source index

SRC-CURRENT-001 — user-supplied E3 v1.1 master.
Class: USER_SUPPLIED_ARTIFACT.
Ceiling: HIGH for artifact fields; UNKNOWN for original line-by-line authorship.

SRC-CURRENT-002 — user-supplied D2 v1.1 execution result, E2-VP-20260217-0011.
SRC-CURRENT-003 — assistant E3 v1.1 result from that packet.
Class of 003: ASSISTANT_PROPOSAL / practice execution; not canon authority.

SRC-CURRENT-004/005 — user D2 SIM input + assistant E3 SIM result.
SRC-CURRENT-006/007 — user D2 REF_ONLY input + assistant E3 REF result.

SRC-CURRENT-008 — user-supplied E3 v1.2 master.
SRC-CURRENT-009 — assistant v1.2 BLOCK result.

SRC-CURRENT-010 — user-supplied E3 v2.0 master.
SRC-CURRENT-011 — assistant v2.0 BLOCK result.
SRC-CURRENT-012 — current user self-recovery directive.

SRC-RECOVERED-001 — prior-conversation recovery metadata for 2026-02-16 genesis.
Class: RECOVERED_FROM_LATER_CONTEXT.
Ceiling: MEDIUM/HIGH for event order and recovered phrase fragments; not raw transcript bytes.

SRC-GH-001 — Navigator topology snapshot v0.2.
SRC-GH-002 — E-Prime ARCHIVE_LOCK.json.
SRC-GH-003 — E-Prime archive manifest.
SRC-GH-004 — fresh 2026-10-07 branch inventory/search.
SRC-GH-005 — main base commit 01b97c8edd19fdd59f81de827fb5f4a99861048f.

## Raw transcript ceiling

No full byte-exact historical E3 chat transcript is available through the current repository/tool surface. Therefore this recovery does not claim 100% transcript completeness.
