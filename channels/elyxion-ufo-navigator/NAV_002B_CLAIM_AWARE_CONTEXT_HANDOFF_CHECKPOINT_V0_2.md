# NAV-002B — Claim-Aware Fingerprinted Context + Global C0 Handoff Checkpoint V0.2

**Status:** CANDIDATE / SYNCHRONOUS MIRROR PASS
**Authority:** NAVIGATION-ONLY
**Validation base Navigator head:** `168d45dd68d70cc6e6196227c2a8dea6036943b5`

## Hard boundary

Global C0 already exists by explicit creator declaration.

Navigator does not build, rebuild, duplicate, or replace Global C0.

Current representation:

- existence = `AUTHOR_DECLARED_EXISTS`
- repository/durable location = `UNKNOWN`
- Navigator Global C0 authority = `NONE`
- construction performed by Navigator = `false`

## Current substrate counts

- observed objects: **7**
- discovery targets: **6**
- confirmed relations: **8**
- unresolved relations: **5**
- open collisions: **1**
- freshness bindings: **21**
- evidence identities: **20**
- claims: **13**
- author declarations: **1**

## Claim layer

Implemented:

- `NAV_CLAIM_SCHEMA_V0_1.json`
- `NAV_CLAIM_INDEX_V0_1.json`

Each claim carries:

- stable claim ID;
- statement;
- epistemic state;
- subject refs;
- evidence IDs;
- explicit limits;
- materialization hint.

Important separation:

`AUTHOR_DECLARED` is not silently rewritten as GitHub-observed fact.

## Evidence materialization

Implemented:

- `NAV_EVIDENCE_MATERIALIZATION_POLICY_V0_1.json`
- `NAV_CONTEXT_PACK_RISK_POLICY_V0_1.json`

Escalation ladder:

`M0_MANIFEST_ONLY -> M1_EXACT_ARTIFACT -> M2_CONFLICT_SET -> M3_PRIMARY_RAW`

If primary evidence is required but unavailable, correct result is BLOCKED / evidence missing, not invention.

## Fingerprinted context packs

Current pack schema:

`NAV_CONTEXT_PACK_SCHEMA_V0_3.json`

Current builder:

`tools/build_context_pack.py`

A pack now contains:

- bounded object/relation slice;
- discovery boundary;
- unresolved boundary;
- collisions;
- selected claims;
- deduplicated evidence manifest;
- risk band;
- materialization plan;
- source snapshot;
- SHA-256 pack fingerprint;
- freshness/invalidation contract.

The fingerprint is an integrity identity, not semantic truth.

## Targeted pack invalidation

Implemented:

- `NAV_CONTEXT_PACK_INVALIDATION_POLICY_V0_1.json`
- `tools/check_context_pack_staleness.py`
- `tools/test_context_pack_invalidation.py`

Self-hosted Navigator evidence is tracked by exact file blob SHA at pack build.

External evidence is tracked by pinned source head + blob SHA.

Author declarations are tracked through the author-declaration registry blob.

### Synchronous invalidation proof

Observed mirror results:

- baseline Eco pack -> `FRESH`
- simulated `main` change -> `STALE_TARGETED`
- simulated unrelated P-control change -> Eco pack remains `FRESH`
- simulated used self-evidence blob change -> `STALE_TARGETED`
- simulated author-declaration registry change -> `STALE_TARGETED`

Result:

**PASS**

This demonstrates targeted invalidation over used evidence rather than project-wide invalidation.

## Claim-aware context-pack proofs

### CP01 — Eco-Systems one hop

- objects = **3**
- claims = **5**
- evidence identities = **10**
- risk = `HIGH`
- recommended materialization = `M2_CONFLICT_SET`
- freshness = `FRESH`

Reason for HIGH:

the open Eco-Systems / E-Prime scope collision is material to the slice.

Result:

**PASS**

### CP02 — Navigator zero hop

- objects = **1**
- claims = **4**
- evidence identities = **7**
- risk = `ELEVATED`
- recommended materialization = `M1_EXACT_ARTIFACT`
- freshness = `FRESH`

The Global C0 boundary appears as:

- existence = author-declared;
- durable location = UNKNOWN;
- no Global C0 object fabricated.

Result:

**PASS**

## Existing Global C0 handoff envelope

Implemented:

- `NAV_GLOBAL_C0_HANDOFF_SCHEMA_V0_1.json`
- `tools/build_global_c0_handoff.py`
- `tests/NAV_GLOBAL_C0_HANDOFF_EXPECTATIONS_V0_1.json`
- `tools/test_global_c0_handoff.py`

The handoff envelope carries the context pack, fingerprint, freshness, risk, unresolved/collision counts, and non-authority boundary.

It explicitly sets:

- `global_c0_authority = NONE`
- `may_build_global_c0 = false`
- `may_duplicate_global_c0 = false`
- `global_c0_construction_performed = false`
- `global_c0_internal_architecture_defined = false`

### Handoff mirror proof

- `H01_ECO_ONE_HOP` -> PASS
- `H02_NAVIGATOR_ZERO_HOP` -> PASS

Both:

- consumer existence = `AUTHOR_DECLARED_EXISTS`
- consumer location = `UNKNOWN`
- payload kind = `ELYXION_NAV_CONTEXT_PACK`
- freshness = `FRESH`
- build flag = `false`

## Evidence resolution proof

All self-hosted evidence files required by the two current pack cases resolved to concrete Git blob SHAs.

Resolved examples include:

- Navigator topology snapshot;
- Global C0 non-duplication boundary;
- ACTIVATE;
- README;
- NAV-002 object/provenance spine;
- Navigator bootstrap;
- author-declaration registry.

Result:

**PASS**

## Current source heads

At checkpoint validation:

- `main` = `848859284af4d97dafd8dfde1b2a847acdd44cc2`
- `E-Prime` = `061c74cb8898cf9be23586feec1c680ea48e6f44`
- `agent/phase1-scaffold` = `4f3b5c53849a992e282f85a8345b637e4b06d9d1`
- `channel/p-control-point-v0.1` = `4c7183356699a53d081e40b3d5d28cb362d6dbcf`

These match current pinned external freshness state.

Navigator self uses current/self-resolution rules.

## Validation honesty

GitHub Actions workflow is configured for:

- claim-aware substrate validation;
- bounded context slices;
- claim-aware context packs;
- targeted pack invalidation;
- existing Global C0 handoff;
- upstream freshness.

No GitHub Actions run was observed through the connector at checkpoint time.

Two local fresh-clone execution attempts were blocked by container infrastructure rate limiting before tests began.

Therefore this checkpoint claims:

**synchronous GitHub-state mirror PASS**

It does not claim an observed CI execution PASS.

## Current frontier

`NAV-002B — Evidence Index + Context Pack Assembly`

State:

`ACTIVE_CANDIDATE / CLAIM-AWARE FINGERPRINTED PACKS + HANDOFF PROVEN BY MIRROR`

## Next candidate work inside NAV-002B

- actual evidence body materializer with receipts;
- claim verification receipts;
- pack repair after targeted invalidation;
- stronger evidence sufficiency checks;
- cold-start export samples for the existing Global C0 interface;
- continue discovering missing Elyxion surfaces without constructing Global C0.

## Materialization + semantic verification continuation (2026-10-07)

Read-only exact-source materialization was executed for:

- `EVID_ECO_SYSTEMS` — blob `e05e677f9a961d507812380e98002d7af2608304`
- `EVID_EPRIME_LOCK` — blob `c34a95613b8d45324de0e75e15d6459badddc83f`
- `EVID_EPRIME_MANIFEST` — blob `ee67e503591d2af3d9eacadcf1a4627da7906051`
- `EVID_AUTHOR_GLOBAL_C0_EXISTS` — author registry blob `239d9b05da5f6c80b0bc696887b631ac14610b50`
- `EVID_NAV_GLOBAL_C0_BOUNDARY` — blob `04e12e5cbaca729ab93e750f90180c7ab597fe60`

Semantic verification results:

- `CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN` → `SUPPORTED_WITH_LIMITS`
- `CLAIM_GLOBAL_C0_EXISTS` → `SUPPORTED_AT_DECLARED_LEVEL`

The Global C0 claim was deliberately **not promoted** beyond AUTHOR_DECLARED.

Evidence-sufficiency falsification also behaved as intended:

- full M2 collision set → sufficient;
- one-sided collision evidence → insufficient;
- Global C0 author claim with author-declaration source → sufficient at declared level;
- same claim without author-declaration source → insufficient.

A local staged receipt/repair bundle passed:

`PASS receipts=5 verifications=2 targeted_repair_cases=2`

Targeted repair law confirmed:

- branch head changed + used blob unchanged → revalidate snapshot without semantic recheck;
- used evidence blob changed → rematerialize only that evidence and reverify only dependent claims;
- unrelated evidence changes do not trigger global replay.

At the time of this continuation, GitHub read operations worked, while multiple write endpoints returned internal connector errors. Do not claim durable receipt files exist until a later successful write confirms them.
