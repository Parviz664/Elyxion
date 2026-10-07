# EVIDENCE_INDEX

## Current-conversation primary sequence

CONV-A3-01
User supplies ELYX_A3_CHANNEL_SPEC_V1_0_MASTER and says:
“Работать строго по контракту А3!”
Class: AUTHOR_RAW for the command; USER_SUPPLIED_ARTIFACT for JSON.

CONV-A3-02
Assistant initial v1.0 BLOCK due missing A2/E-Prime.
Class: ASSISTANT_INTERPRETATION / execution evidence.

CONV-A3-03
User supplies first A2 systems-map payload.
Class: USER_SUPPLIED_ARTIFACT.

CONV-A3-04
Assistant emits PASS_WITH_CONSTRAINTS despite independent E-Prime/hash gaps.
Class: ASSISTANT_INTERPRETATION / error evidence.

CONV-A3-05
User supplies ELYX_A3_CHANNEL_SPEC_V1_1_MASTER.
Class: USER_SUPPLIED_ARTIFACT.

CONV-A3-06
Under v1.1 an A2-only payload is BLOCKed because sealed A2+E-Prime bundle is absent.
Class: execution evidence.

CONV-A3-07
User supplies ELYX_A3_CHANNEL_SPEC_V1_2_MASTER.
Class: USER_SUPPLIED_ARTIFACT.

CONV-A3-08
A2-only payload remains BLOCKed because v1.2 still requires A2+EPRIME bundle.
Class: execution evidence.

CONV-A3-09
User supplies first ELYX_A3_CHANNEL_SPEC_V1_3_MASTER.
Key: A-only, E-Prime removed, full canon carry.
Class: USER_SUPPLIED_ARTIFACT.

CONV-A3-10
User supplies second materially different v1.3 master with same semver.
Key: bounded fidelity cap + no-drop.
Class: USER_SUPPLIED_ARTIFACT.

CONV-A3-11
User supplies ELYX_A3_CHANNEL_SPEC_V1_4_MASTER.
Key: dual ingest and A2-only fast path.
Class: USER_SUPPLIED_ARTIFACT.

CONV-A3-12
V8 A2-only input receives PASS_WITH_CONSTRAINTS.
Class: execution evidence.

CONV-A3-13
V7 JSON plus external prose receives one-root BLOCK.
Class: execution evidence.

CONV-A3-14
WaterOnly B001→B019 A2 receives PASS_WITH_CONSTRAINTS.
Class: execution evidence.

CONV-A3-15
User supplies ELYX_A3_CHANNEL_SPEC_V2_2_MASTER.
Key: current strongest-known role.
Class: USER_SUPPLIED_ARTIFACT.

CONV-A3-16
WaterOnly legacy A2 receives LEGACY_COMPAT sealed handoff.
Generated downstream classes are assistant execution evidence, not owner verdict.

CONV-A3-17
Current user requests full channel archaeology and GitHub preservation.
Class: AUTHOR_RAW recovery instruction.

## Dated recovered-context anchors

CTX-A3-2026-02-17:
user v1.0 strict immutable A2→E0 packaging.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-02-18:
user route fact A3 is last A-channel; A2→A3→E0.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-02-20:
user v1.1 one sealed A2+E-Prime bundle.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-03-02-0823:
user v1.2.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-03-02-0837:
user first v1.3 A-only edition.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-03-02-0956:
user second v1.3 hardening; exact seconds unknown.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-03-02-1005:
user v1.4 dual ingest.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-03-09-1635:
user v2.0 law ID/role.
Class: RECOVERED_FROM_LATER_REFERENCE.

CTX-A3-2026-03-11:
user v2.2.
Class: RECOVERED_FROM_LATER_REFERENCE plus full current artifact.

## GitHub evidence

GH-A3-01:
Parviz664/Elyxion main head before recovery:
01b97c8edd19fdd59f81de827fb5f4a99861048f.

GH-A3-02:
main searches for A3_PRE_E0_LAWFUL_HANDOFF_SEAL_COMPILER and ELYX_A3_LAW returned no A3 artifacts.

GH-A3-03:
existing P0/P1/P3 channel recovery branches provide repository-process precedent only; they are not A3 historical-content evidence.
