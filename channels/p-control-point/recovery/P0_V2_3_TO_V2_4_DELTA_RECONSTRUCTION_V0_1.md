# P0_V2_3_TO_V2_4_DELTA_RECONSTRUCTION_V0_1

Status: `STRUCTURAL_DELTA_RECOVERED / INTENT_CAUSE_UNRESOLVED`

Scope:

compare the last recovered P0 route with explicit `-P1` against the first recovered P0 route with `NO_-P1`.

## 1. Before — P0 v2.3

Route:

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

P0 emitted:

- `minus_p1_input`
- `p1_input`
- `p2_input`
- `p3_input`
- `p4_input`

Historical `-P1` role:

`reality_skeleton_causal_chain`

Historical `-P1` constraints included:

- strict realism;
- causal traceability;
- no fake certainty;
- uncertainty marking;
- no gameplay/UI;
- no lore/personification;
- no magic;
- no code output;
- reproducible seed behavior.

## 2. After — P0 v2.4

Route:

`P0 -> P1 -> P2 -> P3 -> P4`

Structural removals:

- `-P1` route node removed from P0 routing;
- `minus_p1_input` removed from normalized inputs.

Structural continuation:

- P1 remains immediately downstream of P0;
- P2/P3/P4 remain downstream;
- canonical-route discipline remains.

## 3. Important function-migration signal

Recovered v2.4 P1-input constraints contain substantial reality/causal safeguards:

- strict realism;
- continuity / anti-jump;
- parent/source binding;
- filter or bottleneck;
- observable anchor;
- rejected alternatives + why;
- stabilization reason;
- uncertainty labels;
- no UI;
- no lore;
- no mechanics.

These overlap materially with responsibilities previously associated with the historical `-P1` reality-skeleton layer.

## 4. Classification

This supports:

`FUNCTION_MIGRATION_SIGNAL = STRONG`

It does **not** yet support:

`FORMAL_ABSORPTION = TRUE`

Why:

- the fields may have been moved into P1 input while preserving a conceptual `-P1` layer elsewhere;
- P1 may have inherited only part of the function;
- the route may have been task-specific;
- the author may have temporarily bypassed a layer without deleting it;
- no explicit owner rationale / supersession statement has been recovered.

## 5. Function-by-function provisional mapping

| Historical -P1 responsibility | Later location signal | Status |
|---|---|---|
| strict realism | P0 v2.4 p1_input | MIGRATION_SIGNAL |
| causal continuity | P1 mission + p1_input | MIGRATION_SIGNAL |
| no fake certainty | uncertainty labels in downstream constraints | PARTIAL_SIGNAL |
| uncertainty marking | p1_input / P1 guards | MIGRATION_SIGNAL |
| source binding | p1_input / P1 guards | MIGRATION_SIGNAL |
| bottleneck/filter reasoning | p1_input | MIGRATION_SIGNAL |
| observable anchor | p1_input | MIGRATION_SIGNAL |
| rejected alternatives | p1_input | MIGRATION_SIGNAL |
| stabilization reason | p1_input / P1 stabilized-state model | MIGRATION_SIGNAL |
| no UI/lore | P0/P1 downstream guards | MIGRATION_SIGNAL |
| no magic | not yet re-proved in exact v2.4 delta | UNKNOWN |
| reproducible seed behavior | later P1 seed semantics exist, exact migration not proved | PARTIAL_SIGNAL |

## 6. First material architectural finding

The `NO_-P1` change did not obviously correspond to simple removal of all former `-P1` safeguards.

A substantial subset reappears in the direct P0→P1 contract boundary.

This makes the following hypothesis plausible but unconfirmed:

`-P1 function was partly redistributed into P0/P1 boundary contracts rather than simply erased.`

Classification:

`CANDIDATE_EXPLANATION_ONLY`

## 7. New failure guard

`FUNCTION_DISAPPEARANCE_ASSUMPTION`

Do not assume a removed route node means its function disappeared.

Also:

`FUNCTION_MIGRATION_EQUALS_RENAME`

Do not assume migrated fields prove the old channel was renamed.

## 8. Next object

`MINUS_P1_FUNCTIONAL_MIGRATION_MATRIX_V0_1`

Goal:

map every recovered historical `-P1` function to:

- later P0;
- P0→P1 boundary;
- later P1;
- later downstream channel;
- LOST;
- UNKNOWN.

No function may be marked LOST unless all plausible later locations are checked.
