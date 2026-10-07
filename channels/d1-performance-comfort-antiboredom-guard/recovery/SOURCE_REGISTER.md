# SOURCE REGISTER

## Direct/current conversation

| ID | Source | Provenance | Evidence class |
|---|---|---|---|
| SRC-D1-CUR-001 | first supplied v2.1 master + "принимаете роль эту" | USER_SUPPLIED_ARTIFACT + AUTHOR_RAW | PRIMARY |
| SRC-D1-CUR-002 | repeated v2.1 master | USER_SUPPLIED_ARTIFACT | PRIMARY |
| SRC-D1-CUR-003 | supplied v2.2 master | USER_SUPPLIED_ARTIFACT | PRIMARY |
| SRC-D1-CUR-004 | "Работать строго по контракту Д1!" + E1 execution result | AUTHOR_RAW + USER_SUPPLIED_ARTIFACT | PRIMARY |
| SRC-D1-CUR-005 | E1 simulation-lane constraint response | USER_SUPPLIED_ARTIFACT | PRIMARY |
| SRC-D1-CUR-006 | duplicate E1 simulation-lane packet | USER_SUPPLIED_ARTIFACT | PRIMARY DUPLICATE |
| SRC-D1-CUR-007 | E1 kernel-update compatibility ACK | USER_SUPPLIED_ARTIFACT | PRIMARY |
| SRC-D1-CUR-008 | supplied v2.4 master | USER_SUPPLIED_ARTIFACT | PRIMARY |
| SRC-D1-CUR-009 | full channel archaeology instruction | AUTHOR_RAW | PRIMARY |

## Prior-conversation recovered refs

| ID | Time | Fact |
|---|---|---|
| SRC-D1-PC-001 | 2026-02-16T11:05:19Z | broader Elyxion human-depth/retention goal |
| SRC-D1-PC-002 | 2026-02-16T11:57:24Z | v2.0 assistant artifact exists; partial properties recovered |
| SRC-D1-PC-003 | 2026-02-16T21:21:28Z | v2.1 user-supplied timestamp |
| SRC-D1-PC-004 | 2026-02-17T21:42:36Z | v2.2 user-supplied timestamp |
| SRC-D1-PC-005 | 2026-02-17T22:51:01Z | exact strict-contract command |
| SRC-D1-PC-006 | 2026-02-18T09:40:40Z | simulation-lane packet |
| SRC-D1-PC-007 | 2026-02-18T21:15:24Z | kernel-update packet |
| SRC-D1-PC-008 | 2026-02-20T11:37:02Z | D2 reference proves D1 v2.3 existed |
| SRC-D1-PC-009 | 2026-02-26T20:08:21Z | v2.4 user-supplied timestamp |

## GitHub refs

| ID | Finding | Status |
|---|---|---|
| SRC-D1-GH-001 | `main` has no detected D1 master/id/seal code-search hits | VERIFIED NEGATIVE |
| SRC-D1-GH-002 | no D1 commit-search hits | VERIFIED NEGATIVE |
| SRC-D1-GH-003 | no D1 branch found before recovery | VERIFIED NEGATIVE |
| SRC-D1-GH-004 | existing P0/P1/P3/channel recovery branches exist | VERIFIED |
| SRC-D1-GH-005 | main `docs/channels/ECO-SYSTEMS-ELYXION.md` exists but is a different channel | VERIFIED |

## Evidence ceilings

- direct current RAW/artifact: HIGH
- prior-conversation timestamp recovery: MEDIUM-HIGH
- later cross-channel reference: MEDIUM for existence/route only
- assistant output: LOW-MEDIUM unless owner-confirmed
- inference: must remain labelled and never close UNKNOWN
