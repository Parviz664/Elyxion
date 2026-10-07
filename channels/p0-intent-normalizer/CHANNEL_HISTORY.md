# CHANNEL_HISTORY

## Origin problem

A persistent RAW artifact captured on 2026-08-21 preserves the author's explicit problem statement:

> "Каналы P мне нужно, чтобы не было неразберих, слишком много хаоса, большой объем для ИИ."

The same RAW continues:

> "Одна человеческая строка, мечта, запускает конвейер структуры игры."

and:

> "P-каналы — это про как собрано."

This is strong evidence for the conceptual need behind the P-system.

Important chronology limit:
the RAW was captured in August and refers to notes filled on earlier days, but the original note date is not recovered. It cannot be placed before February 2026 as a dated fact.

## First dated P0 contract — 2026-02-12

Recovered:
`ELYX_P0_INTENT_NORMALIZER_v2.3`

Mission:
one human/author line -> strict JSON input for -P1/P1 and canonical route to P4.

Historical route:
`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

Stable early boundaries:
- JSON-only;
- one message / one artifact;
- no world generation;
- no UI/gameplay generation;
- no lore/personification;
- no magic;
- no code;
- uncertainty downstream;
- no fake certainty;
- no route skipping;
- P5 disabled.

## Route transition — 2026-03-05

Recovered:
`ELYX_P0_INTENT_NORMALIZER_v2.4`

Channel name explicitly contains:
`NO_-P1`

New historical route:
`P0 -> P1 -> P2 -> P3 -> P4`

Removed from P0 normalized outputs:
`minus_p1_input`

The structural route change is proven.

The author's explicit reason for removing/bypassing -P1 is not recovered.

## Contract hardening — 2026-03-06

Recovered:
`ELYX_P0_INTENT_NORMALIZER_v2.6`

v2.6 declares:
- append-only from v2.5;
- `range_semantics` only `index_range`;
- count hints must not live in range;
- trace-full autopatch;
- no silent fixes;
- legacy intent may be preserved in `legacy_range_hint`.

This is the strongest fully recovered formal P0 channel spec.

## Later RAW tension — captured 2026-08-21

Persistent RAW again names:

`минус P1, P0, P1, P2, P3, P4`

This does not erase March NO_-P1.

The archive itself marks exact meaning/order unresolved.

Result:
the history contains both route families and they must coexist.

## October archaeology — 2026-10-06

P Control Point recovered the route conflict and function migration.

Owner Decision C:
`HOLD_UNRESOLVED`

This freezes neither historical route as current global truth.

## Current-channel supplied v2.7 output artifact — 2026-10-07

The user supplied an artifact with:

`payload_type = ELYX_P0_OUTPUT_V2_7`

It patches two practical failures:
1. stale scope override conflicting with the actual raw topic;
2. `no_mechanics=true` conflicting with a request to extract mechanics/control meaning.

It adds ideas such as:
- `ZERO_LOSS_REQUIRED`;
- `no_silent_fixes`;
- `SURFACE_ONLY_NO_STEPS`.

But:
- channel_id remains v2.6;
- process binding remains v2.6;
- no v2.7 channel spec is recovered;
- supplied autopatch schema is not fully identical to v2.6's declared schema.

Therefore it is preserved as an output-level evolution artifact, not silently promoted to a formal channel-spec version.

## Historical invariant

The deepest stable identity across recovered history is not a particular route.

It is:

`human author intent -> disciplined structured routing input without uncontrolled invention`.
