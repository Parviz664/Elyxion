# MINUS_P1_CURRENT_STATUS_DECISION_GATE_V0_1

Status: `OWNER_DECISION_REQUIRED`

This gate exists because recovery found real historical architecture change and no authoritative global supersession statement.

The control point must not choose for the owner.

## Recovered facts

1. Historical architecture used:

   `P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

2. P0 v2.3 still emitted `minus_p1_input`.

3. P0 v2.4 and v2.6 used:

   `P0 -> P1 -> P2 -> P3 -> P4`

   with `NO_-P1` / `no_-P1_enforced`.

4. Later P1 carries substantial causal/reality-map responsibility.

5. Functional overlap does not prove that P1 formally absorbed or renamed `-P1`.

6. August RAW still preserves `−P1` in the P-channel vocabulary, but does not settle exact active routing.

## Decision A — latest recovered P0 route becomes current

Current route:

`P0 -> P1 -> P2 -> P3 -> P4`

`-P1` status:

`HISTORICAL / DORMANT / NOT_IN_CURRENT_ROUTE`

Meaning:

- respects the latest strongly recovered P0 v2.4/v2.6 routing;
- does not delete `-P1` history;
- does not claim P1 is a rename of `-P1`;
- current implementation proceeds without a `-P1` runtime node.

This is the strongest choice if the goal is to continue from the latest recovered P0 architecture.

## Decision B — owner explicitly reactivates historical -P1

Current route becomes:

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

`-P1` status:

`REACTIVATED_BY_OWNER`

Meaning:

- this is a new current owner decision;
- it restores the historically recovered dedicated reality-skeleton layer;
- it does **not** pretend P0 v2.4/v2.6 never existed;
- a new versioned `-P1` contract must be built and tested against P1 to prevent duplicate work.

## Decision C — remain unresolved

Current route:

`HOLD`

`-P1` status:

`UNRESOLVED`

Meaning:

- no current P-route is frozen yet;
- continue source recovery / architecture archaeology;
- no implementation proceeds through the disputed boundary.

This is safest when historical fidelity is more important than speed and the owner does not yet want to choose.

## Not currently admissible as recovered truth

The following must not be declared historical/current without a new explicit owner design:

`-P1 -> P0 -> P1 -> P2 -> P3 -> P4`

Although August RAW lists the names in that textual order, the archive explicitly leaves exact meaning/order unresolved.

If the owner wants this architecture now, it must be recorded as a **new design decision**, not as recovered fact.

## Required owner resolution record

Any decision must record:

- selected decision: `A | B | C`;
- date;
- reason in owner's own words;
- whether it is `CURRENT_CONTRACT_DECISION` or temporary;
- what it supersedes operationally;
- what historical material remains preserved;
- next exact object.

No branch history is rewritten.
