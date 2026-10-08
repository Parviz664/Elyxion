# NAV-002B — O2 Relation Recovery Batch 04 Checkpoint V0.12

**Status:** CANDIDATE / O1 COMPLETE / O2 BATCHES 01-04 VERIFIED / A-ROUTE TENSION OPEN  
**Authority:** NAVIGATION-ONLY  
**Project:** Elyxion

## Non-negotiable Global C0 boundary

Global C0 already exists by explicit creator declaration.

Navigator does not build, duplicate, define, locate, or acquire authority over Global C0.

Durable/repository location remains:

`UNKNOWN`

## Current durable substrate

- repository branches: **31**
- branches mapped: **31/31**
- observed objects: **33**
- normalized OBJECT claim coverage: **33/33**
- evidence identities: **72**
- freshness sources: **31**
- freshness dependencies: **96**
- confirmed current base relations: **57**
- unresolved base relations: **5**
- open legacy collision records: **1**
- indexed claims: **40**
- broad selected claims: **36**
- materialization receipts: **61**
- semantic claim verification receipts: **36**

## O2 aggregate state

Current progress:

`NAV_O2_RELATION_PROGRESS_V0_4.json`

Counts:

- assertions: **25**
- verified assertions: **25**
- promoted current-local relations: **23**
- verified conditional relations not promoted: **1**
- verified historical relations not promoted: **1**
- open O2 relation tensions: **1**
- current base confirmed relations: **57**
- current base unresolved relations: **5**

Known total relation universe:

`UNKNOWN`

Therefore:

`O2 completion percentage = NOT COMPUTABLE`

Current relation/authority readiness:

`PARTIAL_VERIFIED_LOCAL_RELATIONS`

## Batch 04 — A0 v4.1 source-declared interfaces

The latest-known A0 v4.1 recovery is partial but directly preserves the A0 boundary:

`P -> A_ULTRA -> A0 -> E0`

The full exact v4.1 artifact/schema remains unrecovered.

### A0 declares interface with A-Ultra

Current base relation:

`A0_ORCHESTRATOR DECLARES_INTERFACE_WITH A_ULTRA`

Scope:

`A0_v4_1_LATEST_KNOWN_PARTIAL`

Evidence ceiling:

source-side declaration only.

Known:

- A0 v4.1 is post-A-Ultra crystal carry;
- A_ULTRA is directly upstream in A0's recovered adult route;
- A0 must not redo meaning/crystallization.

Unknown:

- exact v4.1 ingress schema;
- exact target-side A-Ultra transport acceptance contract;
- whether a mandatory full-output handoff exists.

### A0 declares interface with E0

Current base relation:

`A0_ORCHESTRATOR DECLARES_INTERFACE_WITH E0`

Scope:

`A0_v4_1_LATEST_KNOWN_PARTIAL`

Known:

- A0 v4.1 is E0-aligned;
- E0 is A0's declared adult downstream;
- A0 exposes recovered readiness classes:
  - READY_FOR_E0
  - READY_FOR_E0_WITH_CONSTRAINTS
  - BLOCKED_FOR_E0

Unknown:

- the full exact A0 v4.1 schema;
- E0-side matching acceptance contract;
- whether E0 receives the A0 object directly, via another carrier, or under a profile not fully recovered.

Critical law:

`DECLARES_INTERFACE_WITH != HANDS_OFF_TO`

No current relation:

`A0 HANDS_OFF_TO E0`

has been established.

## Open A-route temporal/profile tension

Registry:

`NAV_O2_RELATION_TENSIONS_V0_1.json`

Tension:

`O2_TENSION_A0_V41_A3_E0_TEMPORAL_SCOPE`

State:

`OPEN_TEMPORAL_SCOPE_RECONCILIATION`

Observed simultaneously:

1. A0 v4.1 partial recovery:
   `P -> A_ULTRA -> A0 -> E0`
   and A1/A2/A3 are legacy compatibility/recovery;

2. A3 v2.2 current-strongest recovery:
   A2 verdict intake -> sealed handoff bundle -> E0;

3. E0 v1.5 current-strongest recovery:
   bind kernel truth + dream seal from A3.

This is **not yet a proven contradiction**.

Possible explanations remain unresolved:

- different project eras;
- different operating profiles;
- A0 carrying/wrapping an A3-derived seal;
- later supersession not fully recovered;
- an incomplete source set.

Navigator chooses none without evidence.

## Current/historical A separation

Current promoted A-family relations include:

- A-Ultra DECLARES_INTERFACE_WITH A1
- A1 HANDS_OFF_TO A2
- A2 HANDS_OFF_TO A3
- A2 HANDS_OFF_TO E3.5
- A3 HANDS_OFF_TO E0
- A0 DECLARES_INTERFACE_WITH A-Ultra
- A0 DECLARES_INTERFACE_WITH E0

Historical-only:

- A0 HANDS_OFF_TO A1 under v3.0

The historical v3.0 edge is not in current base traversal.

The early A0 Meaning Amplifier -> A0_ORCHESTRATOR lineage remains:

`UNKNOWN`

## Previous O2 guards still active

### P

- P2 -> P3 current local
- P3 -> P4 current local
- P4 -> P5 conditional only
- P5 disabled by default
- global P route remains HOLD_UNRESOLVED

### E

Verified current-local seams include:

- E0 -> E1
- E1 -> E2
- E2 -> E3
- E3 -> E4
- E3.5 -> E4

Local seams do not automatically compose into a complete E pipeline.

### D

Current D evidence remains a dependency graph:

- D1 DEPENDS_ON D0
- D2 DEPENDS_ON D0
- D2 DEPENDS_ON D1
- D3 DEPENDS_ON D0
- D3 DEPENDS_ON D1
- D3 DEPENDS_ON D2
- D4 DEPENDS_ON D1
- D4 DEPENDS_ON D2
- D3 -> D4 HANDS_OFF_TO

It is not rewritten as:

`D0 -> D1 -> D2 -> D3 -> D4`

## Sector / cold-start state

Current sector catalog:

`NAV_SECTOR_CATALOG_V0_11.json`

Global O2 counters:

- current promoted local relations: **23**
- conditional verified assertions: **1**
- historical verified assertions: **1**
- source-declared interfaces: **2**

O0 preserves these counters while loading:

- individual evidence identities: **0**
- exact source bodies: **0**
- full history replay: **false**

Readiness axes:

- topology = `READY_TOPOLOGY_ORIENTATION`
- normalized object semantics = `READY_NORMALIZED_SEMANTIC_COVERAGE`
- relation/authority = `PARTIAL_VERIFIED_LOCAL_RELATIONS`
- global semantic completeness = `NOT_PROVEN`

## Targeted repair

Current O2 dependency cache:

`NAV_O2_RELATION_DEPENDENCY_INDEX_V0_4.json`

Builder:

`tools/build_o2_relation_dependency_index.py`

Regression:

`tools/test_o2_relation_dependency_index.py`

Accounting:

- assertions: **25**
- verifications: **25**
- current promoted: **23**
- conditional without current edge: **1**
- historical without current edge: **1**

Repair law:

`changed exact evidence -> invalidate dependent assertions/verifications/relations only`

Repair must never upgrade:

`DECLARES_INTERFACE_WITH -> HANDS_OFF_TO`

without new evidence.

## Validation posture

CI now gates:

- all six O1 batches;
- O2 Batch 01;
- O2 Batch 02;
- O2 Batch 03;
- O2 Batch 04;
- O2 dependency index regeneration;
- O0 and broad orientation;
- freshness and substrate integrity.

Do not claim GitHub Actions PASS until a completed run is directly observed.

## Current frontier

`O2_RELATION_AUTHORITY_RECOVERY`

State:

`ACTIVE / BATCHES_01_04_VERIFIED / TARGET_ACCEPTANCE_AND_TEMPORAL_SCOPE_OPEN`

## Next evidence-first work

The next high-value step is **not** another inferred route.

Recover target-side evidence for the A0 v4.1 interfaces:

1. search E0 recovery for any A0 / crystal-carry / READY_FOR_E0 acceptance language;
2. search A-Ultra recovery for explicit A0 transport/downstream semantics beyond tone/DreamVault boundaries;
3. recover any stronger/full v4.1 A0 artifact if it exists outside current branch;
4. compare dates/version/profile markers across A0 v4.1, A3 v2.2 and E0 v1.5.

Possible outcomes must remain separate:

- target acceptance proven;
- different era/profile proven;
- explicit supersession proven;
- coexistence proven;
- unresolved remains unresolved.

No Global C0 relation is changed here.
