# ADR 0001: Engine-agnostic Phase 1 core

- Status: Accepted
- Date: 2026-08-04

## Context

Elyxion will eventually need a visual environment, but its first systems are
rules: pressure, response, cost, recovery, and learning. Binding those rules to
Unity, Godot, or a browser now would make engine decisions shape the domain
before the domain is understood.

## Decision

Build Phase 1 as strict TypeScript modules with no runtime dependencies. Keep
rendering, storage, input, and networking outside the core. Use deterministic
signals and Node's built-in test runner to prove the complete loop.

TypeScript is a reference implementation, not a permanent engine commitment.
Its contracts are intended to be portable to another runtime later.

## Consequences

- System boundaries and event shapes can evolve quickly and safely.
- Scenarios are reproducible and inexpensive to test.
- A future engine adapter will translate contracts instead of reimplementing
  domain rules.
- There is no visual demonstration in this phase.
- If another runtime becomes canonical, the reference core may be ported.

