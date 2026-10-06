# MINUS_P1_NO_DROP_COVERAGE_PROOF_V0_1

Status: `BOUNDED_PASS_WITH_UNKNOWNS`

Target:

historical `-P1` functional payload across the transition to P0 `NO_-P1`.

This proof is bounded to responsibilities currently recovered from owner-origin artifacts and dated conversation recovery.

It is **not** a proof that every historical `-P1` field has been recovered.

## 1. Coverage classes

- `PRESERVED_EQUIVALENT` — same material responsibility is explicitly present later.
- `PRESERVED_CHANGED_FORM` — responsibility survives but in a structurally different place/form.
- `PARTIAL` — only part of the old responsibility is recovered later.
- `UNKNOWN` — insufficient evidence.
- `MATERIAL_LOSS` — recovered historical responsibility has no later home after bounded search.

## 2. Responsibility ledger

### MP1-F01 — strict realism

Historical: required.

Later: P0/P1 hard guards require strict realism.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F02 — causal traceability

Historical: required.

Later: P1 causal-map contract + linear causal micro-stage order.

Verdict: `PRESERVED_CHANGED_FORM`

### MP1-F03 — no "from nowhere" causal jumps

Historical: project goal / -P1 causal skeleton principle.

Later: P1 conditions→pressure→trigger→micro-transition→stabilized-state chain + anti-jump continuity.

Verdict: `PRESERVED_CHANGED_FORM`

### MP1-F04 — uncertainty must be marked

Historical: explicit downstream rule.

Later: P1 uncertainty labels required; speculative/unknown cannot sole-bridge major blocks.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F05 — no fake certainty

Historical: explicit.

Later: later P0/P1 truth-first / uncertainty guards preserve this requirement.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F06 — no gameplay / no UI

Historical: explicit.

Later: P0/P1 hard guards.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F07 — no lore / personification

Historical: explicit.

Later: P0/P1 hard guards.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F08 — no magic

Historical: explicit.

Later: recovered P0/P1 hard guards include no magic.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F09 — no code output

Historical: explicit.

Later: P0/P1 hard guards include no code.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F10 — deterministic / reproducible seeded behavior

Historical: explicit.

Later: P1 uses seed+linear semantics, deterministic ordering, append-only/id-freeze/rollback behavior.

Verdict: `PRESERVED_CHANGED_FORM`

### MP1-F11 — source binding

Historical: recovered as part of reality-skeleton discipline.

Later: P1/P2 source IDs, source binding, parent/source fields.

Verdict: `PRESERVED_CHANGED_FORM`

### MP1-F12 — filter / bottleneck reasoning

Historical: recovered as part of reality-skeleton step discipline.

Later: direct P0 v2.4 P1-input per-step contract includes filter/bottleneck.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F13 — observable anchor

Historical: recovered as part of reality-skeleton step discipline.

Later: P0 v2.4 P1-input requires observable data-class anchor.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F14 — rejected alternatives + why

Historical: recovered as part of reality-skeleton step discipline.

Later: P0 v2.4 P1-input requires rejected alternatives / reason.

Verdict: `PRESERVED_EQUIVALENT`

### MP1-F15 — stabilization reason

Historical: recovered as part of reality-skeleton step discipline.

Later: P0 v2.4 P1-input requires stabilization reason; P1 has stabilized-state structure.

Verdict: `PRESERVED_CHANGED_FORM`

### MP1-F16 — dedicated standalone reality-skeleton node identity

Historical: explicit `-P1` node exists in route.

Later: P0 v2.4/v2.6 removes that node from route.

Verdict: `PRESERVED_FUNCTIONALLY_BUT_NODE_IDENTITY_REMOVED`

This is not classified as MATERIAL_LOSS because identity and function are separate axes.

## 3. Bounded result

Recovered functional responsibilities checked: `16`

Current classifications:

- `PRESERVED_EQUIVALENT`: MP1-F01, F04, F05, F06, F07, F08, F09, F12, F13, F14
- `PRESERVED_CHANGED_FORM`: MP1-F02, F03, F10, F11, F15
- `PRESERVED_FUNCTIONALLY_BUT_NODE_IDENTITY_REMOVED`: MP1-F16
- `PARTIAL`: none in this bounded set
- `UNKNOWN`: none in this bounded set
- `MATERIAL_LOSS`: none in this bounded set

## 4. Critical caveat

This result proves only:

`NO MATERIAL LOSS FOUND IN THE CURRENTLY RECOVERED FUNCTION SET`

It does **not** prove:

`100% of historical -P1 was preserved`

because the exact full original `ELYX_-P1_INPUT_V1` source bytes are still not recovered in the persistent corpus.

Therefore final status:

`BOUNDED_NO_DROP_PASS`

not:

`GLOBAL_NO_DROP_PROOF`.

## 5. New control law

When a channel/node disappears from routing, the control point must perform two independent checks:

1. `NODE_CONTINUITY`
2. `FUNCTION_CONTINUITY`

A failure in node continuity is not automatically a failure in function continuity.

## 6. Remaining unresolved object

The owner chose Decision C:

`HOLD_UNRESOLVED`

So this bounded pass does not resolve current routing.

It only shows that the historical `NO_-P1` transition appears to have preserved the currently recovered functional payload.

## 7. Next object

`P_SYSTEM_ROUTE_AUTHORITY_TIMELINE_V0_1`

Goal:

construct a single chronological authority timeline from February → March → August → current October HOLD, with every route state, evidence class, owner decision, and unresolved gap visible in one place.

This timeline becomes the recovery spine for all later P-channel contracts.
