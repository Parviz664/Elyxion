# ADR 0002: Elyxion and WhiteLine remain separate projects

- Status: Accepted
- Date: 2026-08-05

## Context

An early scaffold placed WhiteLine's 0-100 score and M0-M3 maturity tiers inside
Elyxion and used them to control membrane defense. That made one project a module
of the other and blurred their different purposes.

Elyxion is an emotional-visual evolutionary game universe. WhiteLine is an
intellectual system built around evidenced reaction quality. Both must stand on
their own.

## Decision

- Remove WhiteLine scores, tiers, learning code, and terminology from the
  Elyxion domain core.
- Give Elyxion its own biological state: membrane integrity, energy, pressure
  recognition, and subtle internal support.
- Keep any future Elyxion-WhiteLine exchange outside both cores behind an
  explicit adapter or event contract.
- Never require WhiteLine for Elyxion gameplay or require Elyxion for WhiteLine.

## Consequences

- Elyxion can evolve and ship independently.
- WhiteLine's meaning cannot accidentally become a game power score.
- The Phase 1 loop now describes the actual living scene instead of borrowing
  another project's maturity model.
- A future AI amplifier can translate between projects without owning either.
