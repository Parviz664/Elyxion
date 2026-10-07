# P0_CONTRACT_LINEAGE_PASS_V0_1

Status: `LINEAGE_PARTIALLY_RECOVERED`

Target: `P0`

Purpose:

recover P0's role evolution independently of the unresolved current `-P1` routing decision.

## 1. Stable P0 identity across recovered versions

Recovered channel family:

`ELYX_P0_INTENT_NORMALIZER`

Stable mission theme:

`author intent -> strict structured/JSON downstream input`

Stable boundary theme:

P0 normalizes and routes intent; it is not the place for UI, lore, magic, implementation code, or uncontrolled content invention.

## 2. P0 v2.3

Recovered identifier:

`ELYX_P0_INTENT_NORMALIZER_v2.3`

Recovered route:

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

Recovered downstream packets:

- `minus_p1_input`
- `p1_input`
- `p2_input`
- `p3_input`
- `p4_input`

Recovered architectural meaning:

P0 acts as the front normalization gateway and explicitly prepares both `-P1` and later channel inputs.

Provenance class:

`USER_SUPPLIED_CHAT_ARTIFACT`

## 3. P0 v2.4

Recovered identifier:

`ELYX_P0_INTENT_NORMALIZER_v2.4`

Recovered name includes:

`NO_-P1`

Recovered route:

`P0 -> P1 -> P2 -> P3 -> P4`

Recovered downstream packets:

- `p1_input`
- `p2_input`
- `p3_input`
- `p4_input`

`minus_p1_input` is absent.

Recovered guards include:

- JSON-only routing;
- no UI/lore/magic/code;
- strict realism;
- canonical routing;
- uncertainty discipline;
- P5 disabled by author.

Recovered P1-boundary detail:

P1 input now carries strong causal/reality requirements such as continuity/anti-jump, parent/source, filter/bottleneck, observable anchor, rejected alternatives, stabilization reason, and uncertainty labels.

Provenance class:

`USER_SUPPLIED_CHAT_ARTIFACT`

## 4. P0 v2.5

Exact v2.5 artifact:

`NOT_RECOVERED`

No current evidence is sufficient to reconstruct its content.

Important:

do not infer v2.5 fields merely because v2.6 supersedes it.

## 5. P0 v2.6

Recovered identifier:

`ELYX_P0_INTENT_NORMALIZER_v2.6`

Recovered route remains:

`P0 -> P1 -> P2 -> P3 -> P4`

Recovered:

- `NO_-P1`
- `no_-P1_enforced: true`
- no `minus_p1_input`
- `range_semantics = index_range`
- default range behavior around the working ladder bounds
- trace-full autopatch behavior
- auto-fixes require explicit assumption/autopatch logging.

Recovered supersession field:

`supersedes_semver: ["2.5.0"]`

This proves:

`v2.6 supersedes v2.5 semver`

It does **not** prove the content of v2.5.

Provenance class:

`USER_SUPPLIED_CHAT_ARTIFACT`

Artifact-origin nuance:

at least some recovered later artifacts may have been assistant-generated earlier and then supplied/adopted by the owner; therefore authorship is not silently attributed.

## 6. P0 lineage delta

### Stable across v2.3 -> v2.6

- intent normalization;
- strict downstream structure;
- routing discipline;
- anti-invention boundaries;
- no uncontrolled UI/lore/code generation;
- handoff into later P-channels.

### Material route change by v2.4

`-P1` removed from the P0 route.

### Material contract growth by v2.6

P0 gains stronger range semantics and traceable autopatch behavior.

## 7. Missing lineage links

Not recovered:

- explicit `v2.4 supersedes v2.3` field;
- exact v2.5 artifact;
- explicit owner rationale for `NO_-P1`;
- whether `NO_-P1` was global or task-family-local;
- current October P0 route authority.

## 8. Safe current P0 statement

Allowed:

`P0 is historically a front intent-normalization/routing channel whose recovered route changed from including -P1 in v2.3 to NO_-P1 by v2.4/v2.6.`

Not allowed:

`Current P0 definitely routes directly to P1.`

Reason:

October owner Decision C keeps the current route unresolved.

## 9. P0 current status

`ROLE_CORE = STRONGLY_RECOVERED`

`VERSION_LINEAGE = PARTIALLY_RECOVERED`

`CURRENT_ROUTE_AUTHORITY = HOLD_UNRESOLVED`

`IMPLEMENTATION_STATUS = BLOCKED_AT_DISPUTED_ROUTE_BOUNDARY`

## 10. Next object

`P1_CONTRACT_LINEAGE_PASS_V0_1`

Goal:

recover P1 v3.2.1 -> v3.2.2 role evolution and determine exactly which reality/causality responsibilities are native P1 responsibilities versus boundary guards inherited from P0.
