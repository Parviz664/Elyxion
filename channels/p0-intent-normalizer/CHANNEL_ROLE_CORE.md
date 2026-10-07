# CHANNEL_ROLE_CORE

Status: `RECOVERED_ROLE_CORE_STRONG / CURRENT_ROUTE_HOLD`

## Mission

Receive author intent and emit a strict, routable, machine-readable P-chain input without inventing world content.

## What P0 receives

Historically recovered:
- `raw_author_text`, one-line preferred;
- optional overrides;
- project anchor;
- scope/stage-scope controls;
- output-size hints;
- branching/style/universe-mode controls in some versions.

Observed later practice:
- long raw author material was supplied, not only one line;
- P0 extracted a dominant core intent from longer material.

Exact authority to discard the rest as noise is historically present in contracts, but carries a known drift risk.

## What P0 may do

Recovered authority:
- normalize author intent;
- set contract defaults;
- resolve a stage scope according to the active version;
- emit assumptions;
- emit blocking questions under bounded conditions;
- construct downstream input packets;
- construct a canonical routing plan for that historical contract;
- validate route/format/hard-rule flags;
- in v2.6, auto-fix range/semantics/task-id errors only with trace-full logging.

## What P0 may never do

Strongly recovered:
- generate the world as its own creative authority;
- explain the subject instead of routing it;
- write implementation code;
- invent lore/personification;
- invent magic;
- fake certainty;
- silently skip route nodes required by the active historical contract;
- silently rewrite unknowns;
- claim canon authority.

## Current route authority limit

P0's latest strongly recovered local route is the NO_-P1 route from v2.4/v2.6.

However the current global P-route is `HOLD_UNRESOLVED` by owner Decision C (2026-10-06).

Therefore P0 itself may not resolve the current global `P0/-P1/P1` boundary.

## What P0 outputs

Recovered v2.4/v2.6 core:
- `intent_digest`
- `assumptions`
- `blocking_questions`
- `normalized_inputs.p1_input`
- `normalized_inputs.p2_input`
- `normalized_inputs.p3_input`
- `normalized_inputs.p4_input`
- `routing_plan`
- `validation_flags`
- optional `process_guarantee`

v2.6 adds:
- `autopatch_log`
- `legacy_range_hint`
- index-range-only semantics.

Historical v2.3 additionally emitted:
- `minus_p1_input`

## Canon authority

`NONE`

P0 can normalize or route an author's intent. It cannot promote RAW/candidate material to canon merely because it is structured.

## Uncertainty behavior

Recovered:
- uncertainty must be preserved downstream;
- fake certainty is forbidden;
- later tasks used `plausible/speculative/unknown` labels.

## Implementation status

Documentation/recovery: strong enough to preserve.

Runtime/global routing implementation: blocked at disputed `P0/-P1/P1` route boundary until a later owner decision.
