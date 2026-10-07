# NAV-002B — Verification Dependency + Handoff Falsification Checkpoint V0.4

**Status:** CANDIDATE / SYNCHRONOUS MIRROR PASS  
**Authority:** NAVIGATION-ONLY  
**Project:** Elyxion

## Global C0 boundary remains unchanged

Global C0 already exists by creator declaration.

Navigator:

- does not build it;
- does not duplicate it;
- does not define its internals;
- does not infer its durable location.

Current durable location remains:

`UNKNOWN`

## New verification dependency index

Implemented:

- `NAV_VERIFICATION_DEPENDENCY_INDEX_V0_1.json`
- `tools/build_verification_dependency_index.py`
- `tools/test_verification_dependency_index.py`

Status:

`DERIVED_CACHE / NOT AUTHORITY`

Current index spans:

- evidence identities = **20**
- claims = **13**
- materialization receipts = **6**
- semantic verification receipts = **7**

Examples:

`EVID_EPRIME_LOCK`
→ `CLAIM_EPRIME_CHAT_TRANSCRIPTS_ONLY`
→ `CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN`

`EVID_AUTHOR_GLOBAL_C0_EXISTS`
→ `CLAIM_GLOBAL_C0_EXISTS`
→ `CLAIM_NAV_MUST_NOT_BUILD_GLOBAL_C0`

`MAT_ECO_SYSTEMS_M2_2026_10_07`
→ `CLAIM_ECO_SYSTEMS_ROLE`
→ `CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN`

The index is only a regeneration cache. Truth remains in Evidence Index / Claim Index / receipt registries.

## Handoff blocking falsification

Implemented:

- readiness helper inside `tools/build_global_c0_handoff.py`
- `tools/test_global_c0_handoff_blocking.py`

Expected behavior:

1. fresh + no critical evidence failures  
   → `READY_FOR_GLOBAL_C0_REVIEW`

2. stale pack  
   → `BLOCKED_FRESHNESS`

3. unknown freshness  
   → `BLOCKED_FRESHNESS`

4. fresh pack + critical claim insufficient  
   → `BLOCKED_EVIDENCE`

5. stale pack + critical claim insufficient  
   → `BLOCKED_FRESHNESS` first

Synchronous mirror result:

**5/5 PASS**

This prevents freshness/evidence failures from silently producing READY.

## Verification-aware handoff state

Current handoff schema:

`NAV_GLOBAL_C0_HANDOFF_SCHEMA_V0_2.json`

Control coverage:

### Eco one-hop
- selected claims: **5**
- sufficient claims: **5**
- coverage: **1.0**
- critical failures: **0**

### Navigator zero-hop
- selected claims: **4**
- sufficient claims: **4**
- coverage: **1.0**
- critical failures: **0**

Author-declared Global C0 claims remain at:

`SUPPORTED_AT_DECLARED_LEVEL`

Collision remains:

`SUPPORTED_WITH_LIMITS`

No epistemic promotion occurred.

## Repair blast-radius proof

Current targeted repair logic + reverse index establishes:

- E-Prime lock changes → only E-Prime role + Eco/E-Prime collision claims require reverification;
- Global C0 author declaration changes → only Global C0 existence + Navigator non-build claims require reverification;
- Eco source changes → only Eco role + Eco/E-Prime collision claims require reverification;
- head-only change with identical used blob → semantic verification may be preserved;
- unrelated source changes do not require global replay.

## CI gate

GitHub Actions workflow now includes:

- substrate validator;
- bounded context slices;
- claim-aware packs;
- targeted pack invalidation;
- evidence materializer;
- receipt/sufficiency tests;
- targeted repair planner;
- verification dependency index regeneration;
- verification-aware Global C0 handoff;
- handoff blocking falsification;
- cold-start export;
- upstream freshness.

No execution PASS has yet been observed through the connector.

## Current state

`NAV-002B — ACTIVE_CANDIDATE / VERIFIED + REPAIRABLE + FALSIFIABLE HANDOFF SUBSTRATE`

## Next candidate work

- broader multi-surface cold-start benchmark;
- evidence-budget / pack-size pressure tests;
- discover more missing durable Elyxion surfaces;
- only materialize evidence demanded by a concrete question;
- never construct Global C0.
