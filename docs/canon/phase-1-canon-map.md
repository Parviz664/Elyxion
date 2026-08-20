# Elyxion Phase 1 canon map

- Status: ACTIVE SOURCE-OF-TRUTH MAP
- Scope: Cell Stage, Phase 1
- Rule: user-stated meaning outranks implementation convenience and prior
  assistant interpretation.

This map separates the creator's confirmed Phase 1 from prototype constants,
tuning hypotheses, and preserved experiments. A lower-status item must never be
promoted to canon without explicit creator confirmation.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| `USER_STATED_CANON` | Meaning or rule directly established by the creator. |
| `USER_APPROVED_PROTOTYPE_RULE` | Exact rule approved for a small prototype; it is not automatically final gameplay. |
| `PROVISIONAL_TUNING` | Number or formula retained for testing, not asserted as optimal or scientific fact. |
| `EXPERIMENTAL_CANDIDATE` | Reversible implementation or authored scene that may inform canon but cannot define it. |
| `UNRESOLVED` | A creator decision or evidence is still required. |

## USER_STATED_CANON

### Purpose

Phase 1 is the first biography of the cell. The player learns to hold life,
open the membrane to the environment, survive the consequences of that risk,
restore rhythm, and leave a persistent evolutionary trace.

### Causal spine

```text
manual breathing / rhythm
-> sufficient internal stability
-> timed membrane intake
-> friendly + hostile particle composition inside
-> overload severity
-> recovery through the same Elyxionpad language
-> delayed friendly-particle activation
-> partial breathing automation
-> Phase 2 entry carrying the Phase 1 result
```

The order is part of the meaning. Friendly particles do not provide an instant
reward: they are initially quiet and become useful only after the player has
restored rhythm. Hostile particles act quickly. Benefit is delayed; harm is
immediate.

### Player agency

- The player manually supports the membrane's breathing/rhythm before it can
  become partially automated.
- The player chooses when and how long to open the membrane to the particle
  flow.
- Intake cannot be perfectly clean; the meaningful decision is how much risk
  to accept, not how to eliminate all risk.
- The same Elyxionpad interaction language is used for ordinary rhythm and for
  recovery under pressure. Recovery is not a separate healing button.
- Mature play means reading the state early and responding accurately, not
  rapidly spamming input.

### Separate state axes

The implementation must not collapse different meanings into one state enum.

1. Membrane life mode: `Stable`, `Evolving`, and
   `Deteriorating/Destroying` (same rollback/degradation meaning; the final
   English display label remains unresolved).
2. Overload severity: normal, light pain, pressure overload, heavy overload,
   and critical collapse.
3. Breathing mastery: manual, partially automated, and any later automation
   state unlocked by the game.

### Project boundary

WhiteLine and Elyxion are independent projects. Elyxion cannot require
WhiteLine scores, tiers, or runtime availability.

## USER_APPROVED_PROTOTYPE_RULE

Friendly Points Prototype v0.1 / TASK 001 intentionally proves only:

- membrane scale starts at `2.0`;
- three absorbed Friendly Points change scale to `3.0`;
- five absorbed Friendly Points change scale to `5.0`;
- at five points, the visible breathing interval changes from `2s` to `3s`;
- slight autonomous membrane movement after five points is allowed but was not
  required by TASK 001.

These are exact prototype acceptance values. They do not replace the longer
manual-breathing cadence or the full Phase 1 automation model.

## PROVISIONAL_TUNING

The following design draft is preserved for playtesting but is not yet proven
optimal:

- initial manual rhythm around `5-6s`, later `7-8s`, and a Phase 1 ceiling near
  `12s`;
- a good intake window around `1.5-2.8s`, with longer openings carrying more
  risk;
- `P1 Evolution Score` weights of rhythm `40%`, intake `25%`, particle
  composition `20%`, and recovery `15%`;
- `Breath Interval = 5.5 + P1 Evolution Score * 0.65`;
- the current overload boundaries and recovery-cycle counts from the Phase 1
  Core Spec draft.

No document or source code may describe these values as scientifically exact.
They require instrumentation and playtesting.

## EXPERIMENTAL_CANDIDATE

The existing deterministic Red/Crimson Pressure Node simulation is preserved as
an experiment. Its confirmed visual ideas can remain useful, but these exact
implementation choices are not Phase 1 canon:

- a fixed topology of exactly one internal Friendly Particle and one enemy;
- signal intensities `18 / 42 / 78 / 28`;
- a `31s` seven-beat first-contact score;
- `100`-point integrity and energy scales;
- exposure thresholds, automatic defense strategies, and a `25%` mitigation
  cap;
- technical states `stable / alert / defense / recovery` as a replacement for
  the separate canonical state axes.

The visual identity of a translucent crimson node with three red-orange cores,
its pressure-like impact, a fragile semi-transparent membrane, disturbed
breathing, and green particles beginning to recognize danger is preserved as a
creator-confirmed scene direction. Exact timing, numbers, and phase placement
remain outside canon.

## UNRESOLVED

- Whether the Red/Crimson Pressure Node encounter belongs in late Phase 1,
  Phase 2, or another transition layer.
- Whether Friendly Points automatically select breathing or the player chooses
  which function to automate.
- The final full-Phase-1 breathing cadence after playtesting.
- Whether the earlier seven-point maximum/overload rule belongs in the first
  playable vertical slice.
- The final English display label for the rollback state:
  `Deteriorating` or `Destroying`.

## Admission rule for future changes

Every new mechanic, formula, timeline, enemy role, or canonical adjective must
state its status. Tests can prove that code matches a chosen rule; they cannot
turn an experimental rule into creator canon.
