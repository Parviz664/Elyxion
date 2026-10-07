# CHANNEL_PROVENANCE

## Provenance law

`SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR`

`ASSISTANT_RATIONALE != AUTHOR_RATIONALE`

Inference never upgrades itself to fact.

## Evidence register

### EV-AU-001
Source: `raw-evidence/EV_AU_001_V4_2_LAW_USER_SUPPLIED.json`  
Class: `USER_SUPPLIED_ARTIFACT`  
Supports: exact v4.2 law, mission, inputs/outputs, modes, source precedence, A0 handoff.  
Authorship ceiling: supplied by owner; line-by-line authorship not proven.

### EV-AU-002
Source: `raw-evidence/EV_AU_002_V4_3_LAW_USER_SUPPLIED.json`  
Class: `USER_SUPPLIED_ARTIFACT`  
Supports: exact v4.3 law, rename, DreamVault, transport envelope, dual anchor, safety locks, constraints, D echo.  
Authorship ceiling: supplied by owner; line-by-line authorship not proven.

### EV-AU-003
Source: recovered past-chat index, 2026-02-26.  
Class: `USER_SUPPLIED_CHAT_ARTIFACT / RECOVERED_FROM_CONVERSATION_INDEX`  
Supports: A0 v2.2 P5 gateway to A_MINUS_1 and v4.2 operational task evidence.  
Ceiling: strong event-level recovery; raw transcript not archived here.

### EV-AU-004
Source: recovered past-chat index, 2026-03-02.  
Class: `USER_SUPPLIED_CHAT_ARTIFACT / RECOVERED_FROM_CONVERSATION_INDEX`  
Supports: A0 v3.0 copy-paste gateway; A_MINUS_1 Vision Artifact handling; unknown routing.

### EV-AU-005
Source: recovered past-chat index, 2026-03-09.  
Class: `USER_SUPPLIED_CHAT_ARTIFACT / RECOVERED_FROM_CONVERSATION_INDEX`  
Supports: A0 v4.1 adult route `P → A_ULTRA → A0 → E0`.

### EV-AU-006
Source: current recovery conversation, user-supplied P4 packet.  
Class: `USER_SUPPLIED_ARTIFACT`  
Supports: task-local `p5_enabled_by_author=false`; P4 lists A_ULTRA as next option; P2 expand recommendation.

### EV-AU-007
Source: current/recovered assistant runtime outputs.  
Class: `ASSISTANT_RUNTIME_OUTPUT`  
Supports: observed behavior only, including direct P4 falling into UNKNOWN_JSON/WARN and initial v4.3 resolver mismatch.  
Cannot prove: author intent or canonical topology.

### EV-AU-008
Source: `channel/elyxion-ufo-navigator-v0.1:channels/elyxion-ufo-navigator/NAV_001_REPOSITORY_TOPOLOGY_SNAPSHOT_V0_2.md`  
Class: `GITHUB_ARTIFACT / NAVIGATION_EVIDENCE`  
Supports: A-channel surface was not observed in GitHub at that recovery point.

### EV-AU-009
Source: fresh GitHub branch inventory immediately before current write.  
Class: `GITHUB_OBSERVATION`  
Supports: no pre-existing A-Ultra recovery branch/file before this recovery.

### EV-AU-010
Source: Project file `ELYXION_PRRS_RAW_0.0.0.2.md`.  
Class: `PERSISTENT_RAW_FILE`  
Supports: broader P-channel architecture vocabulary/context.  
Does not prove: A-Ultra origin.

## Authority order used

1. exact AUTHOR_RAW / explicit author decision;
2. exact user-supplied artifacts;
3. persistent Project files;
4. GitHub artifacts;
5. recovered conversation index;
6. assistant runtime outputs;
7. inference.

No standalone A-Ultra AUTHOR_RAW origin statement was recovered.
