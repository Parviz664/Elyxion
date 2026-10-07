# CHANNEL_BOUNDARIES

## Upstream boundary

P3 owns rendered candidate text.

P4 must treat P3 candidate meaning as immutable unless higher-authority evidence explicitly changes it.

Forbidden seam drift:
`P3 weak line -> P4 rewrites it into a stronger line`.

Allowed:
`P4 flags the line and recommends P3 patch`.

## Dependency boundary

If a selected node depends on B### prerequisites, P4 must include prerequisites or fail/repair selection.

No output may claim `dependency_integrity=true` when required spine dependencies are missing.

This invariant was violated in early historical executions and is now explicitly preserved as a correction.

## Order boundary

P4 never reorders P3 source order.

Any improvement requiring reorder belongs upstream to P3/P2.

## Duplicate boundary

Drop as duplicate only when provable under the supplied no-guess rules.

If similarity is suspected but not proved:
keep as reserve with a flag.

## Uncertainty boundary

`plausible`, `speculative`, `unknown` cannot be silently upgraded.

Late speculative bridges may be structurally necessary and remain in spine with debt visible.

## Score boundary

Scores are editorial priority only.

They are not:
- truth;
- physics;
- world parameters;
- player-visible values.

## Gameplay/world boundary

P4 is an AI work/channel architecture.
Its shortlist, roles, weights and scoring are not automatically systems inside Elyxion gameplay.

Translation to game implementation requires a separate explicit bridge.

## Author boundary

P4 has no canonization authority.

Under `author_selects_ids_only`, owner selection remains a real control point.

## Downstream boundary

P5 is not default and is currently disabled in recovered P-chain authority.

`ready_for_p5` is legacy compatibility only unless explicitly enabled upstream.

A-layer names in P4 handoff are route options, not automatic authority.

## Global-route boundary

The historical -P1 dispute is not P4's authority to resolve.

P4 recovery must remain compatible with both recovered route families until owner authority freezes one.
