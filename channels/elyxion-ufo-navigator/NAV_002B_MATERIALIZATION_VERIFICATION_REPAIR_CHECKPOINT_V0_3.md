# NAV-002B — Materialization / Verification / Targeted Repair Checkpoint V0.3

**Status:** CANDIDATE / DURABLE IMPLEMENTATION + SYNCHRONOUS PASS  
**Authority:** NAVIGATION-ONLY  
**Repository:** `Parviz664/Elyxion`  
**Validation base Navigator head:** `1fc149d5035939057a1e6e5f417874e117431e4b`

## Global C0 boundary

Global C0 already exists by explicit creator declaration.

Navigator still does **not** build, rebuild, duplicate, replace, or define Global C0 internals.

Current state:

- existence = `AUTHOR_DECLARED_EXISTS`
- durable/repository location = `UNKNOWN`
- Navigator Global C0 authority = `NONE`

## Current substrate counts

- observed objects: **7**
- discovery targets: **6**
- confirmed relations: **8**
- unresolved relations: **5**
- open collisions: **1**
- freshness bindings: **21**
- evidence identities: **20**
- claims: **13**
- materialization receipts: **6**
- semantic verification receipts: **7**

## New durable materialization layer

Implemented:

- `NAV_MATERIALIZATION_RECEIPT_SCHEMA_V0_1.json`
- `NAV_MATERIALIZATION_RECEIPTS_V0_1.json`
- `tools/materialize_evidence.py`
- `tools/test_materialize_evidence.py`

Materialization receipt proves exact-source retrieval/integrity, **not claim truth**.

Observed exact-source receipts include:

- Eco-Systems source;
- E-Prime archive lock;
- E-Prime archive manifest;
- Global C0 author declaration registry;
- Global C0 non-duplication boundary;
- Creator Reality Stabilizer governance law.

Source bodies are not durably duplicated by default.

## Semantic verification layer

Implemented:

- `NAV_CLAIM_VERIFICATION_RECEIPT_SCHEMA_V0_1.json`
- `NAV_CLAIM_VERIFICATION_RECEIPTS_V0_1.json`
- `NAV_CLAIM_EVIDENCE_SUFFICIENCY_POLICY_V0_1.json`
- `tools/check_claim_sufficiency.py`
- `tools/test_receipt_and_repair.py`

Key law:

`materialized source != verified claim`

Semantic verification is a separate receipt.

### Current verified control claims

Eco one-hop pack:

1. `CLAIM_GLOBAL_C0_EXISTS` → `SUPPORTED_AT_DECLARED_LEVEL`
2. `CLAIM_NAV_MUST_NOT_BUILD_GLOBAL_C0` → `SUPPORTED_AT_DECLARED_LEVEL`
3. `CLAIM_ECO_SYSTEMS_ROLE` → `SUPPORTED_WITH_LIMITS`
4. `CLAIM_EPRIME_CHAT_TRANSCRIPTS_ONLY` → `SUPPORTED_WITH_LIMITS`
5. `CLAIM_ECOSYS_EPRIME_SCOPE_COLLISION_OPEN` → `SUPPORTED_WITH_LIMITS`

Navigator zero-hop pack:

1. `CLAIM_GLOBAL_C0_EXISTS` → `SUPPORTED_AT_DECLARED_LEVEL`
2. `CLAIM_NAV_MUST_NOT_BUILD_GLOBAL_C0` → `SUPPORTED_AT_DECLARED_LEVEL`
3. `CLAIM_NAV_NO_GLOBAL_C0_AUTHORITY` → `SUPPORTED_WITH_LIMITS`
4. `CLAIM_REALITY_STABILIZER_SCOPE` → `SUPPORTED_WITH_LIMITS`

Synchronous coverage:

- Eco = **5/5 sufficient**
- Navigator zero-hop = **4/4 sufficient**

Result:

`PASS`

No AUTHOR_DECLARED claim is promoted to independent FACT.

## Collision verification

For:

`COL_ECOSYS_EPRIME_SCOPE_001`

M2 materialization read:

- Eco-Systems source;
- E-Prime `ARCHIVE_LOCK.json`;
- E-Prime `ARCHIVE_MANIFEST.json`.

Observed:

- Eco-Systems describes E-Prime as a broad durable-reality / recovery interface;
- E-Prime lock says `purpose = CHAT_TRANSCRIPTS_ONLY`;
- E-Prime manifest says `archive_scope = THIS_EPRIME_CHAT_TRANSCRIPT_ONLY`.

Verdict:

`SUPPORTED_WITH_LIMITS`

This supports a real unresolved scope mismatch.

It does **not** establish which description has higher authority or whether the documents describe different layers/times.

Navigator must not auto-resolve it.

## Evidence sufficiency proof

Observed synthetic checks:

- full M2 collision set → `SUFFICIENT`
- one-sided collision set → `INSUFFICIENT_EVIDENCE`
- Global C0 author claim with author-declaration receipt → `SUFFICIENT` at declared level
- same claim without author source → `INSUFFICIENT_EVIDENCE`
- exact Eco role evidence → `SUFFICIENT`

## Targeted repair

Implemented:

- `NAV_CONTEXT_PACK_REPAIR_POLICY_V0_1.json`
- `tools/plan_context_pack_repair.py`
- `tools/test_context_pack_repair.py`

Repair laws:

- source head changed + used blob unchanged → `REVALIDATED_UNCHANGED`
- used blob changed → rematerialize only changed evidence
- reverify only dependent claims
- fresh supporting evidence can be reused
- unrelated claims remain untouched
- global replay default = false
- repair creates a new pack fingerprint

Observed repair scope examples:

- E-Prime lock changed → reverify only E-Prime role + Eco/E-Prime collision
- Global C0 author declaration changed → reverify only Global C0 existence + Navigator non-build claim
- unrelated evidence changes do not require global replay

## Verification-aware Global C0 handoff

Current schema:

`NAV_GLOBAL_C0_HANDOFF_SCHEMA_V0_2.json`

Builder:

`tools/build_global_c0_handoff.py`

Handoff readiness now depends on:

1. pack freshness;
2. sufficient verification for critical claims;
3. collision multi-side evidence;
4. AUTHOR_DECLARED claims remaining at declared epistemic level.

Readiness values:

- `READY_FOR_GLOBAL_C0_REVIEW`
- `BLOCKED_FRESHNESS`
- `BLOCKED_EVIDENCE`

Current synchronous mirror:

- Eco one-hop verification coverage = **1.0**
- Navigator zero-hop verification coverage = **1.0**
- critical failures = **0**

## Cold-start export

Implemented:

- `tools/build_global_c0_cold_start_export.py`
- `tests/NAV_GLOBAL_C0_COLD_START_EXPORT_EXPECTATIONS_V0_1.json`
- `tools/test_global_c0_cold_start_export.py`

Export intentionally contains a bounded startup envelope:

- producer / consumer boundary;
- pack fingerprint;
- counts and risk;
- verification summary;
- verified claims + limits;
- unresolved relation IDs;
- collision IDs;
- discovery boundary IDs;
- targeted-repair contract;
- handoff readiness.

It does not define Global C0 internal architecture.

## Current source heads

At checkpoint validation:

- `main` = `848859284af4d97dafd8dfde1b2a847acdd44cc2`
- `E-Prime` = `061c74cb8898cf9be23586feec1c680ea48e6f44`
- `agent/phase1-scaffold` = `4f3b5c53849a992e282f85a8345b637e4b06d9d1`
- `channel/p-control-point-v0.1` = `4c7183356699a53d081e40b3d5d28cb362d6dbcf`

External heads match the current Navigator freshness policy.

## Validation evidence

During this pass:

- exact-source read-side materialization executed successfully;
- local staged receipt/repair bundle passed: `PASS receipts=5 verifications=2 targeted_repair_cases=2`;
- current durable registries were fresh-read and produced:
  - Eco = 5/5 sufficient;
  - Navigator zero-hop = 4/4 sufficient;
  - overall synchronous verdict = `PASS`.

GitHub Actions workflow now gates:

- substrate validation;
- bounded slices;
- claim-aware packs;
- targeted pack invalidation;
- evidence materialization;
- receipt/sufficiency verification;
- targeted repair planner;
- verification-aware existing Global C0 handoff;
- cold-start export;
- upstream freshness.

No GitHub Actions run was observed through the connector at checkpoint time.

Therefore this checkpoint does **not** claim CI PASS.

## Current frontier

`NAV-002B — Evidence Index + Context Pack Assembly`

State:

`ACTIVE_CANDIDATE / MATERIALIZED + SEMANTICALLY VERIFIED + TARGETED-REPAIRABLE + EXPORTABLE`

## Candidate next work

- materialization receipts for more high-value claims on demand rather than bulk-reading Elyxion;
- verification dependency graph / reverse claim impact index;
- handoff failure-mode falsification (`BLOCKED_EVIDENCE`, `BLOCKED_FRESHNESS`);
- first broader multi-surface cold-start benchmark;
- continue discovery of missing durable Elyxion surfaces;
- never construct Global C0.
