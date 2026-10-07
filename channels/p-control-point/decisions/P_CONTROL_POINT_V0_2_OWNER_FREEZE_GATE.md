# P_CONTROL_POINT_V0_2_OWNER_FREEZE_GATE

Status: `OWNER_DECISION_REQUIRED`

Target:

`P_CONTROL_POINT_V0.2_CANDIDATE`

Readiness audit:

`P_CONTROL_POINT_V0_2_FREEZE_READINESS_AUDIT = PASS`

## Decision A — freeze the Control Point with route HOLD

Decision token:

`FREEZE_CONTROL_POINT_V0_2_WITH_ROUTE_HOLD`

Effect:

- accept v0.2 control laws as current durable control-layer contract;
- preserve Decision C / `HOLD_UNRESOLVED`;
- keep all open G0/G1/G2/G3 gaps visible;
- keep `-P1` current routing unresolved;
- do not authorize runtime implementation across P0/-P1/P1;
- keep historical route families intact;
- permit future recovery as append-only v0.2.x / v0.3 changes.

This decision freezes **how uncertainty is governed**, not the uncertain route itself.

## Decision B — keep the Control Point draft

Decision token:

`KEEP_CONTROL_POINT_V0_2_DRAFT`

Effect:

- no freeze;
- PR remains draft;
- recovery may continue before admitting v0.2 as durable control contract.

## Explicitly not available through this gate

This gate cannot:

- select route A;
- select route B;
- reactivate `-P1`;
- delete `-P1`;
- merge P1 and `-P1`;
- canonize Elyxion content.

Those require separate owner decisions.

## Required owner record

The selected token must be preserved verbatim with:

- date;
- decision scope;
- current route state;
- open-gap count/status;
- freeze target;
- next object.

No historical record is rewritten.
