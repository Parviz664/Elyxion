# MINUS_P1_RATIONALE_RECOVERY_PASS_V0_1

Status: `OWNER_RATIONALE_NOT_RECOVERED`

Target question:

Why did P0 v2.4 move from

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

to

`P0 -> P1 -> P2 -> P3 -> P4`?

## 1. Owner-origin evidence recovered

Direct owner artifacts clearly establish:

- `NO_-P1` in P0 v2.4 naming;
- canonical direct routing P0→P1→P2→P3→P4;
- later `no_-P1_enforced: true`;
- continuation of this route into P0 v2.6.

## 2. Owner-origin rationale not recovered

No direct owner statement has been recovered that says the route changed because:

- `-P1` was redundant;
- `-P1` was too slow;
- `-P1` caused friction;
- P1 absorbed it;
- P0 absorbed it;
- its function was intentionally deleted;
- its function was temporarily bypassed;
- its function was moved elsewhere.

Therefore all of those explanations remain non-authoritative unless separately proven.

## 3. Quarantined assistant-origin rationale

Historical assistant commentary suggested that removing `-P1` could:

- reduce friction / steps;
- reduce focus loss;
- reduce repeated input polishing;
- reach P1–P4 faster.

Classification:

`ASSISTANT_INTERPRETATION_ONLY`

This rationale MUST NOT be promoted to owner intent or architectural history.

## 4. Safe statement

Allowed:

`The owner changed P0 routing to NO_-P1 by v2.4; the direct owner rationale for that change has not yet been recovered.`

Forbidden:

`-P1 was removed because it was redundant / inefficient / absorbed by P1.`

## 5. Control consequence

Add failure class:

`ASSISTANT_RATIONALE_PROMOTION`

Trigger:

an assistant-origin explanation is later treated as if the owner had said or decided it.

## 6. Next dependency

The missing rationale cannot be filled by interpretation.

Continue with structural delta analysis only:

`P0_V2_3_TO_V2_4_DELTA_RECONSTRUCTION_V0_1`

Goal:

determine what functions moved, disappeared, or reappeared downstream without claiming why.
