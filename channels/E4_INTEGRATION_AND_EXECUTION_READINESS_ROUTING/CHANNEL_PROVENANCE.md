# Provenance and evidence register

## Provenance law

`SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR`.

The user pasted both master contracts, so they are `USER_SUPPLIED_ARTIFACT`. This recovery does not claim the user personally authored every contract line unless direct evidence says so.

`ASSISTANT_RATIONALE != AUTHOR_RATIONALE`.

## Source register

### SRC-E4-001
Type: DIRECT_USER_MESSAGE  
Content: "Работать строго по контракту Е4!!" followed by the v1.1 master.  
Provenance: AUTHOR_RAW for the command; USER_SUPPLIED_ARTIFACT for the JSON.  
Evidence ceiling: VERY_HIGH for the command and artifact-as-supplied; UNKNOWN for original artifact authorship.

### SRC-E4-002
Type: ASSISTANT_OUTPUT  
Content: first `E4_MAP_PACKET_V1_1`, PWC-A, synthetic E4N nodes and numeric scores.  
Evidence ceiling: HIGH that the assistant emitted it; LOW as architectural truth.

### SRC-E4-003
Type: USER_SUPPLIED_ARTIFACT  
Content: canonical/bootstrap `ELYX_D3_EXECUTION_RESULT_V1_1`.  
Evidence ceiling: VERY_HIGH as supplied input; original authorship UNKNOWN.

### SRC-E4-004
Type: ASSISTANT_OUTPUT  
Content: E4 map PWC-B over canonical D3.  
Evidence ceiling: HIGH as historical assistant behavior; LOW/MEDIUM as validated route truth.

### SRC-E4-005
Type: USER_SUPPLIED_ARTIFACT  
Content: D3 `BOOTSTRAP_LIMITED__SIMULATION_ONLY` packet.  
Evidence ceiling: VERY_HIGH as supplied input.

### SRC-E4-006
Type: ASSISTANT_OUTPUT  
Content: E4 BLOCK(SIM) due missing required upstream.  
Evidence ceiling: HIGH as historical behavior; MEDIUM/HIGH as contract-consistent correction.

### SRC-E4-007
Type: USER_SUPPLIED_ARTIFACT  
Content: `ELYX_E4_CHANNEL_SPEC_V2_1_MASTER`.  
Evidence ceiling: VERY_HIGH as supplied contract; original authorship UNKNOWN.

### SRC-E4-008
Type: ASSISTANT_OUTPUT  
Content: v2.1 missing-input BLOCK/incident-style packet.  
Evidence ceiling: HIGH as assistant behavior; not automatically a schema-valid canonical packet.

### SRC-E4-009
Type: DIRECT_USER_MESSAGE
Content: present self-recovery mandate beginning "Ты — текущий канал Elyxion..." and absolute no-invention rule.  
Provenance: AUTHOR_RAW.  
Evidence ceiling: VERY_HIGH for recovery process rules; not evidence of E4's historical role before this recovery.

### SRC-CTX-001
Type: RECOVERED_PRIOR_CONTEXT / USER_FACT  
Timestamp: 2026-02-17T20:35:19Z.  
Content: E4 ID and early E3+D3 integration mission.  
Evidence ceiling: MEDIUM/HIGH; exact raw wording unavailable.

### SRC-CTX-002
Type: RECOVERED_PRIOR_CONTEXT / USER_FACT  
Timestamp: 2026-02-17T21:34:16Z.  
Content: E0 v1.3 adds E4 as required sync target and minimum E4 spec 1.0.0.  
Evidence ceiling: MEDIUM/HIGH.

### SRC-CTX-003
Type: RECOVERED_PRIOR_CONTEXT / USER_FACT  
Timestamp: 2026-02-18T09:35:16Z.  
Content: SIMULATION_ONLY transition; no runtime/canon promotion.  
Evidence ceiling: MEDIUM/HIGH and corroborated by SRC-E4-005.

### SRC-GH-001
Type: GITHUB_ARTIFACT  
Observed: 2026-10-07 before this recovery write.  
Repository: `Parviz664/Elyxion`, main.  
Observation: code search returned no E4 technical ID / Route-Compiler contract artifacts. Main README indexed Eco-Systems Elyxion, not E4.  
Evidence ceiling: HIGH for repository state visible through the connector at recovery time.

### SRC-GH-002
Type: GITHUB_ARTIFACT  
Observed: 2026-10-07.  
Existing recovery branch names included P0/P1/P3 channel-recovery branches; no E4 recovery branch existed before this write.  
Evidence ceiling: HIGH for observed branch search.

## Source priority used

1. direct user messages in this channel;
2. user-supplied historical artifacts;
3. Project/GitHub artifacts;
4. confirmed user decisions;
5. recovered prior context;
6. assistant outputs;
7. inference.

No inference is upgraded to fact.
