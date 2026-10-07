# CHANNEL_PROVENANCE — evidence register

## Source hierarchy used

1. exact current-channel user messages;
2. exact user-supplied artifacts in current channel;
3. Project/Library artifacts;
4. GitHub evidence;
5. owner confirmations/decisions from recovered conversations;
6. later references;
7. assistant outputs;
8. summaries/recovered context;
9. inference.

Inference never closes a gap.

## Evidence register

### SRC-CURR-V22
**Class:** USER_SUPPLIED_ARTIFACT  
**Content:** full `ELYX_A0_LAW_v2.2_ZERO_MANUAL_STABLE_GATEWAY` pasted in this channel.  
**Authorship:** UNKNOWN. Supplied by owner does not prove authored by owner.  
**Evidence ceiling:** 1.00 for what the pasted artifact says; lower for who originally wrote it.

### SRC-CURR-V30
**Class:** USER_SUPPLIED_ARTIFACT  
**Content:** full `ELYX_A0_LAW_v3.0_COPY_PASTE_PROOF_GATEWAY` pasted in this channel.  
**Authorship:** UNKNOWN.  
**Evidence ceiling:** 1.00 for artifact text.

### SRC-REC-V22-DATE
**Class:** recovered conversation context  
**Fact:** earliest recovered v2.2 occurrence 2026-02-12T22:25:30Z.  
**Evidence ceiling:** 0.90; this is a recovered occurrence, not guaranteed original creation time.

### SRC-REC-V30-DATE
**Class:** recovered conversation context  
**Fact:** earliest recovered exact v3.0 occurrence 2026-03-02T11:39:52Z.  
**Evidence ceiling:** 0.90.

### SRC-REC-V41
**Class:** USER_SUPPLIED_ARTIFACT occurrence recovered from prior conversation context.  
**Date:** 2026-03-09T09:54:40Z.  
**Known:** law ID, supersession, CRYSTAL_CARRY role, adult/legacy route, E0 readiness classes, sacred carry categories.  
**Full exact artifact:** unavailable in this pass.  
**Evidence ceiling:** 0.80–0.90 per individual recovered fact; 0 for unknown omitted fields.

### SRC-REC-V40
**Class:** RECOVERED_FROM_LATER_REFERENCE.  
**Known only:** law ID `ELYX_A0_LAW_v4.0_POST_A_ULTRA_CRYSTAL_CARRY_GATE` and existence via v4.1 supersession.  
**Evidence ceiling:** 0.95 for existence/name; 0 for unrecovered contents.

### SRC-A0-EARLY-RAW
**Class:** AUTHOR_RAW / AUTHOR_CONFIRMED from later conversations.  
**Exact fragment:** "А0 усилятор!"  
**Later owner description:** RAW → 30 variants; no execute/canonize/argue.  
**Evidence ceiling:** 0.95 for existence/function; lower for original date.

### SRC-A0-EARLY-SPEC
**Class:** RECOVERED_FROM_LATER_REFERENCE.  
**Spec ID:** `ELYX_A0_IDEA_AMPLIFIER_SPEC_V1_0`.  
**Original date later referenced as:** 2026-02-04.  
**Exact original artifact:** not recovered.  
**Evidence ceiling:** 0.75.

### SRC-LIB-RAW
**Class:** Project/Library artifact.  
**Files inspected:** Elyxion PRRS RAW archives / Master RAW Map and A0-related search results.  
**Use:** supports the existence of the 30-variant amplification workflow and strict source hierarchy, but does not prove A0_ORCHESTRATOR lineage.

### SRC-GH-MAIN-20261007
**Class:** GITHUB_ARTIFACT.  
**Main head inspected:** `01b97c8edd19fdd59f81de827fb5f4a99861048f`.  
**Finding:** direct GitHub code search and commit search returned no A0 law IDs/names before this recovery branch.  
**Evidence ceiling:** 0.70 for "not found by available search"; absence of hit is not proof of global absence.

## Provenance law

Never transform:
- USER_SUPPLIED_ARTIFACT → AUTHOR_RAW;
- ASSISTANT_RATIONALE → AUTHOR_RATIONALE;
- later summary → exact earlier wording;
- existence reference → reconstructed version contents.
