# P_CONTROL_POINT_V0_2_GAP_REGISTER

Status: `ACTIVE / SOURCE-GROUNDED`

Purpose:

make every remaining P Control Point uncertainty visible, ranked by what it blocks.

This register does not erase UNKNOWNs. It tells us which UNKNOWNs matter now.

## Priority classes

- `G0 BLOCKER` — unsafe to freeze or implement across the affected boundary.
- `G1 HIGH` — does not block the whole control point, but blocks a complete channel contract or strong historical claim.
- `G2 MEDIUM` — affects completeness/version archaeology, not the recovered role spine.
- `G3 LOW` — useful historical completeness only.

## G0 — current-route authority

### GAP-G0-001 — current -P1 routing unresolved

Known historical route A:

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

Known later route B:

`P0 -> P1 -> P2 -> P3 -> P4`

Current owner decision:

`C / HOLD_UNRESOLVED`

Impact:

- blocks current-route freeze across P0/-P1/P1;
- blocks current runtime implementation across that boundary;
- does **not** block recovery of P0..P4 roles.

Closure condition:

a later explicit owner decision A/B/new design, or stronger source evidence followed by owner confirmation.

Status:

`INTENTIONALLY_OPEN`

## G1 — source/provenance gaps

### GAP-G1-001 — original ELYX_-P1_INPUT_V1 bytes not recovered

Impact:

prevents global proof that every historical -P1 field/function has been recovered.

Current mitigation:

bounded functional no-drop proof over the recovered function set.

Status:

`OPEN / NON-BLOCKING_FOR_ROLE_SPINE`

### GAP-G1-002 — exact P0 v2.5 artifact not recovered

Known:

P0 v2.6 records `supersedes_semver: ["2.5.0"]`.

Unknown:

exact v2.5 content.

Impact:

version lineage has a hole.

Status:

`OPEN / HISTORICAL_LINEAGE`

### GAP-G1-003 — owner rationale for NO_-P1 not recovered

Known:

route changed by P0 v2.4.

Unknown:

why.

Impact:

we may state the route changed; we may not state the author's reason.

Status:

`OPEN / RATIONALE_QUARANTINED`

## G1 — channel contract gaps

### GAP-G1-004 — P3 full output schema not recovered

Known:

- P3 input identity;
- render role;
- P3 rendered packet identity;
- P4 downstream binding;
- anti-drift locks.

Unknown:

complete output fields/schema.

Impact:

blocks exact executable/schema-level P3 contract.

Status:

`OPEN`

### GAP-G1-005 — P3 generic split/merge semantics not recovered

Impact:

must not infer split/merge authority from P2 or P4.

Status:

`OPEN`

### GAP-G1-006 — P4 full version lineage incomplete

Known:

P4 v3.2 family and later working packets.

Unknown:

complete earlier/later supersession chain.

Impact:

does not block role-core understanding; blocks full lineage claim.

Status:

`OPEN`

## G2 — version completeness

### GAP-G2-001 — P2 v3.2.1 -> v3.5.0 intermediate lineage incomplete

Known endpoints:

- v3.2.1 role/core;
- later v3.5.0 working architecture.

Unknown:

full v3.3/v3.4 transition chain.

Status:

`OPEN / NON-BLOCKING`

### GAP-G2-002 — P3 complete version lineage incomplete

Status:

`OPEN / NON-BLOCKING`

### GAP-G2-003 — exact universal P4 shortlist cardinality/reserve semantics not proved

Reason:

task-specific packets may differ.

Status:

`OPEN / MUST_REMAIN_TASK-SCOPED`

## G2 — provenance fidelity

### GAP-G2-004 — chat artifact authorship can be mixed

A user-supplied artifact is not automatically user-authored line by line.

Mitigation already active:

- `SUPPLIED_BY` != `AUTHORED_BY`;
- provenance overclaim failure class;
- owner decisions separated from supplied specs.

Status:

`MITIGATED / CONTINUOUS_GUARD`

## G2 — original P-channel order wording

### GAP-G2-005 — August RAW textual order remains semantically unresolved

RAW lists:

`минус P1, P0, P1, P2, P3, P4`

The archive itself refuses to silently interpret this as an executable route.

Status:

`PRESERVED_UNKNOWN`

This gap must not be "closed" merely for neatness.

## G3 — completeness-only gaps

### GAP-G3-001 — every historic packet/schema instance not archived

Impact:

historical completeness only.

### GAP-G3-002 — every assistant explanation around P-channel evolution not classified

Impact:

low, provided no assistant rationale is promoted to owner intent.

## Current gap summary

- G0 blockers: `1`
- G1 high gaps: `6`
- G2 medium gaps: `5`
- G3 low gaps: `2`

## What is already strong enough

The following do **not** need these gaps closed to remain valid:

- P-channels answer `как собрано`;
- P-channels are work/AI architecture, not automatically gameplay systems;
- RAW must remain immutable;
- P0 role core;
- P1 role core;
- P2 role core;
- P3 role core;
- P4 role core;
- no-invent/no-drop authority;
- provenance separation;
- author-control boundary;
- no automatic canonization;
- current Decision C HOLD.

## Safe-use envelope

Until G0 is resolved:

Allowed:

- architecture recovery;
- documentation;
- source mapping;
- historical comparison;
- per-channel role analysis;
- non-mutating test/falsification;
- downstream design proposals clearly marked CANDIDATE.

Blocked:

- declaring a current global P route;
- runtime implementation through P0/-P1/P1;
- deleting -P1 from history;
- reactivating -P1 as current without owner decision;
- treating migrated function as formal rename;
- merging unresolved evidence into a cleaner false history.

## Next object

`P_CONTROL_POINT_INVARIANTS_V0_1`

Goal:

turn the recovered anti-drift laws into machine-readable invariants and falsification tests.
