# CHANNEL ROUTE HISTORY

| Route | Era | Evidence | Status |
|---|---|---|---|
| E-Prime → D1 | v2.1 | v2.1 dependencies_inbound | SUPERSEDED |
| E0 → D1 | v2.1/v2.2 | exact masters | SUPERSEDED |
| D0 → D1 | v2.1 onward | exact masters | ACTIVE, role changed |
| E1 → D1 | v2.2 | exact v2.2 + supplied E1 execution packet | SUPERSEDED |
| D1 → E1 | v2.1/v2.2 | exact masters | SUPERSEDED |
| D1 → D2 | v2.1/v2.2/v2.4 | exact masters | ACTIVE |
| D1 → D3 | v2.1/v2.2/v2.4 | exact masters | ACTIVE |
| D1 → D4 | v2.1/v2.2/v2.4 | exact masters | ACTIVE |
| D1 → E4 | v2.2 alignment/export | exact v2.2 | SUPERSEDED |
| D1 → D5 | v2.4 | exact master | ACTIVE |
| D1 → D6 | v2.4 | exact master | ACTIVE |
| Runtime evidence → D1 | v2.4 | exact dependencies_inbound | ACTIVE |
| D Registry/Seal → D1 gate | v2.4 | exact contract | ACTIVE |
| SIM EPrime/E1 lane → D1 | v2.2 operational episode | supplied simulation packet | HISTORICAL |
| CANON EPrime kernel ref-only → D1 compat ACK | v2.2 episode | supplied kernel packet + assistant ACK | HISTORICAL / NOT CURRENT |

## Historical route 1 — v2.1

```
E-Prime ─┐
E0 ──────┼→ D1 → E1
D0 ──────┘     ├→ D2
               ├→ D3
               └→ D4
```

## Historical route 2 — v2.2

```
E-Prime ─┐
E0 ──────┤
D0 ──────┼→ D1 ↔ E1
E1 ──────┘     ├→ D2
               ├→ D3
               ├→ D4
               └→ E4 integration checks
```

## Current route — v2.4

```
D0 + D Registry/Seal + runtime evidence
                  ↓
                 D1
        ┌─────────┼─────────┬─────────┬─────────┐
        ↓         ↓         ↓         ↓         ↓
       D2        D3        D4        D5        D6
```

## P ↔ A

No direct P/A relation was recovered for D1.

Status: `UNKNOWN / NOT APPLICABLE ON CURRENT EVIDENCE`.

This is intentionally not filled with a modern global pipeline assumption.
