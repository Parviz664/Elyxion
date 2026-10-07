# ACTIVATE — Elyxion UFO Navigator 🛸🌍

Use this file as the clean activation entrypoint for a fresh chat.

## Repository
`Parviz664/Elyxion`

## Navigator branch
`channel/elyxion-ufo-navigator-v0.1`

## Non-negotiable Global C0 boundary

The creator explicitly states:

`Global C0 already exists.`

Navigator must not build, rebuild, duplicate, replace, impersonate, or define the internals of Global C0.

Current Navigator representation:

- existence = `AUTHOR_DECLARED_EXISTS`
- durable/repository location = `UNKNOWN`
- Navigator Global C0 authority = `NONE`
- Navigator role = evidence/navigation/recovery substrate only

Read first:

- `NAV_GLOBAL_C0_EXISTENCE_BOUNDARY_V0_1.md`
- `NAV_AUTHOR_DECLARATIONS_V0_1.json`

## Fresh activation procedure

Fresh-read current contracts:

- `README.md`
- `NAV_GLOBAL_C0_EXISTENCE_BOUNDARY_V0_1.md`
- `NAV_AUTHOR_DECLARATIONS_V0_1.json`
- `NAV_OBJECT_SCHEMA_V0_4.json`
- `NAV_OBJECT_REGISTRY_V0_4.json`
- `NAV_RELATION_SCHEMA_V0_3.json`
- `NAV_RELATION_REGISTRY_V0_3.json`
- `NAV_COLLISION_REGISTRY_V0_1.json`
- `NAV_FRESHNESS_POLICY_V0_3.json`
- `NAV_EVIDENCE_SCHEMA_V0_1.json`
- `NAV_EVIDENCE_INDEX_V0_2.json`
- `NAV_CLAIM_SCHEMA_V0_1.json`
- `NAV_CLAIM_INDEX_V0_1.json`
- `NAV_EVIDENCE_MATERIALIZATION_POLICY_V0_1.json`
- `NAV_CONTEXT_PACK_RISK_POLICY_V0_1.json`
- `NAV_CONTEXT_PACK_INVALIDATION_POLICY_V0_1.json`
- `NAV_CONTEXT_PACK_REPAIR_POLICY_V0_1.json`
- `NAV_MATERIALIZATION_RECEIPT_SCHEMA_V0_1.json`
- `NAV_MATERIALIZATION_RECEIPTS_V0_1.json`
- `NAV_CLAIM_VERIFICATION_RECEIPT_SCHEMA_V0_1.json`
- `NAV_CLAIM_VERIFICATION_RECEIPTS_V0_1.json`
- `NAV_CLAIM_EVIDENCE_SUFFICIENCY_POLICY_V0_1.json`
- `NAV_CONTEXT_PACK_SCHEMA_V0_3.json`
- `NAV_GLOBAL_C0_HANDOFF_SCHEMA_V0_2.json`
- `NAV_002B_MATERIALIZATION_VERIFICATION_REPAIR_CHECKPOINT_V0_3.md`

Then:

1. Fresh-recover current branch/source heads.
2. Apply targeted freshness logic before trusting cached packs.
3. Preserve lifecycle status, source-native labels, evidence state, authority, readiness, relation state, collision state, claim epistemics, verification state, and freshness as distinct axes.
4. Never promote RAW/CANDIDATE to CANON without explicit evidenced authority.
5. Never traverse unresolved relations as facts.
6. Never auto-resolve collisions.
7. Never treat an author declaration as independent implementation evidence.
8. Never promote an AUTHOR_DECLARED claim above `SUPPORTED_AT_DECLARED_LEVEL` without independent evidence.
9. Never fill the existing Global C0 durable location without evidence.
10. Never build Global C0.

## Current frontier

`NAV-002B — Evidence Index + Context Pack Assembly`

Parent:

`NAV-002 — Global Object / Authority / Provenance Spine`

State:

`ACTIVE_CANDIDATE / MATERIALIZED + SEMANTICALLY VERIFIED + TARGETED-REPAIRABLE + EXPORTABLE`

## Current durable substrate

- objects = **7**
- discovery targets = **6**
- confirmed relations = **8**
- unresolved relations = **5**
- open collisions = **1**
- freshness bindings = **21**
- evidence identities = **20**
- claims = **13**
- materialization receipts = **6**
- semantic verification receipts = **7**

Implemented:

- typed object / authority / provenance substrate;
- confirmed vs unresolved relation graph;
- collision radar;
- targeted freshness invalidation;
- Evidence Index;
- claim-to-evidence index;
- materialization ladder M0→M3;
- context-pack risk policy;
- bounded claim-aware context packs;
- exact source snapshots;
- SHA-256 pack fingerprint;
- materialization receipt layer;
- semantic claim verification receipts;
- claim-specific evidence sufficiency policy;
- targeted stale-pack invalidation;
- targeted pack repair planner;
- verification-aware existing Global C0 handoff V0.2;
- cold-start export builder;
- compact validators/regression tests;
- GitHub Actions gate.

## Materialization / verification law

`source retrieved != claim verified`

Materialization proves the exact source identity/read.

Semantic verification is a separate receipt.

Current control verification:

### Eco one-hop

- selected claims = 5
- sufficient claims = 5
- verification coverage = **1.0**
- collision = `SUPPORTED_WITH_LIMITS`

### Navigator zero-hop

- selected claims = 4
- sufficient claims = 4
- verification coverage = **1.0**

Global C0 claims remain:

`SUPPORTED_AT_DECLARED_LEVEL`

not independent FACT.

## Targeted repair law

If:

`branch head changed + used blob unchanged`

then:

`REVALIDATED_UNCHANGED`

No semantic recheck is required.

If:

`used evidence blob changed`

then:

`rematerialize changed evidence → reverify dependent claims → reuse fresh supporting evidence → new fingerprint`

Do not replay unrelated Elyxion history.

## Existing Global C0 handoff

Handoff readiness values:

- `READY_FOR_GLOBAL_C0_REVIEW`
- `BLOCKED_FRESHNESS`
- `BLOCKED_EVIDENCE`

Critical claims require sufficient verification before readiness.

Cold-start export contains:

- consumer boundary;
- pack fingerprint;
- risk/materialization;
- verification summary;
- verified claims + limits;
- unresolved/collision/discovery IDs;
- targeted repair contract.

It does not define Global C0 internals.

## Important unresolved surfaces

- 0.0.1.0 through 0.0.1.4 RAW/version surfaces;
- A-channel repository surface;
- E-channel repository surfaces beyond E-Prime;
- existing Global C0 durable/repository surface;
- Tools under Elyxion repository surface;
- Dream / RAW durable surface;
- exact P-to-implementation handoff.

## Open collision

`COL_ECOSYS_EPRIME_SCOPE_001`

Current verification:

`SUPPORTED_WITH_LIMITS`

Observed mismatch:

- Eco-Systems gives E-Prime a broad durable-reality/recovery role;
- E-Prime own lock says `CHAT_TRANSCRIPTS_ONLY`;
- E-Prime manifest says `THIS_EPRIME_CHAT_TRANSCRIPT_ONLY`.

Do not choose a winner automatically.

## Latest evidence level

Current synchronous GitHub-state verification:

`PASS`

Control verification coverage:

- Eco = **5/5**
- Navigator zero-hop = **4/4**

GitHub Actions workflow is configured for the current substrate, but no execution PASS has yet been observed through the connector.

Do not claim CI PASS until observed.

## Next candidate work

- falsify handoff blocking states (`BLOCKED_EVIDENCE`, `BLOCKED_FRESHNESS`);
- build reverse verification-dependency index for larger repair scopes;
- broader multi-surface cold-start benchmark;
- materialize only high-value evidence on demand;
- continue discovering missing durable Elyxion surfaces;
- never construct Global C0.

## Fresh-chat activation phrase

> Activate Elyxion UFO Navigator. Fresh-recover `Parviz664/Elyxion`, branch `channel/elyxion-ufo-navigator-v0.1`, read `ACTIVATE.md`, preserve the existing Global C0 non-duplication boundary, and continue from the current Navigator frontier without inventing missing state.
