# D1 — Performance / Comfort / Anti-Boredom Guard

**Project:** ELYXION  
**Channel ID:** `D1_PERFORMANCE_COMFORT_AND_ANTI_BOREDOM_GUARD`  
**Owner role:** `D1_Performance_Comfort_AntiBoredom_Guard_Lead`  
**Recovery status:** HISTORICAL RECOVERY, not a new spec  
**Current strongest-known contract:** `ELYX_D1_CHANNEL_SPEC_V2_4_MASTER` / `2.4.0`  
**Current route:** D-line only, D0 + runtime evidence → D1 → D2/D3/D4/D5/D6  
**Runtime implementation:** NOT EVIDENCED  
**GitHub status before this recovery:** no D1 files or D1 commits found on `main`

This directory reconstructs the real D1 channel history without pretending that the current v2.4 contract existed from the beginning.

## Evidence hierarchy used

1. direct user messages in the D1 conversation;
2. exact user-supplied artifacts;
3. Project/past-conversation recovery with timestamps;
4. GitHub repository evidence;
5. later cross-channel references;
6. assistant outputs;
7. inference only when explicitly labelled.

## Provenance vocabulary

- `AUTHOR_RAW`
- `AUTHOR_CONFIRMED`
- `AUTHOR_DECISION`
- `USER_SUPPLIED_ARTIFACT`
- `ASSISTANT_PROPOSAL`
- `ASSISTANT_INTERPRETATION`
- `JOINT_ITERATION`
- `RECOVERED_FROM_LATER_REFERENCE`
- `GITHUB_ARTIFACT`
- `UNKNOWN_ORIGIN`

Supplied by the user does **not** prove original authorship.

## Recovery headline

The strongest supported lineage is:

`pre-D1 context`
→ `v2.0 (partially recovered; assistant-generated artifact)`
→ `v2.1 (exactly recovered)`
→ `v2.2 (exactly recovered)`
→ `v2.3 (existence proven, content not recovered)`
→ `v2.4 (exactly recovered; current strongest-known)`

The largest architectural reversal is real and explicit:

**historical mixed E/D integration → current D-line-only architecture with zero E-channel dependencies.**

See the other files for source binding, decisions, errors, routes, unknowns, and confidence ceilings.
