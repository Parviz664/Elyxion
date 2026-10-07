# CHANNEL INTERFACE MAP

## CURRENT — v2.4

### Inbound

```
D0
 ├─ immutable core
 ├─ allowed adaptation zones
 ├─ non-mutable constraints
 ├─ D sync seed
 ├─ D_PACKET_REGISTRY_REF
 └─ D_REGISTRY_SEAL_REF
        ↓
       D1
        ↑
Runtime evidence
 ├─ real-device metrics
 ├─ funnel/session snapshot
 ├─ crash/hang snapshot
 └─ thermal/battery snapshot
```

### Outbound

```
D1
 ├─→ D2 onboarding optimizer
 ├─→ D3 telemetry brain
 ├─→ D4 experiment orchestrator
 ├─→ D5 audio feel truth guard
 └─→ D6 visual feel truth guard
```

## Current D2 requirements from D1

- release gate pass or non-critical pass-with-warnings;
- onboarding frame-pacing pass;
- onboarding input-latency pass;
- segment-state baselines;
- critical-cluster report;
- locked-context consistency pass;
- D Registry/Seal verified.

## Current D3 receives

- metric schema;
- segment-fairness fields;
- harm fields;
- uncertainty fields;
- anti-boredom fields;
- fidelity fields;
- locked-context fields;
- Registry/Seal fields.

## Current D4 requires

- non-degraded baseline;
- fairness constraints;
- harm constraints;
- intervention guards;
- rarity/recovery registry;
- Registry/Seal verified.

## Current D5/D6 receives

D5:
- audio psychophysiology constraints;
- dynamic silence budget.

D6:
- visual density budget;
- motion discomfort constraints.

## HISTORICAL — v2.1

Inbound:

`E-Prime + E0 + D0 → D1`

Outbound:

`D1 → E1 + D2 + D3 + D4`

## HISTORICAL — v2.2

Inbound:

`E-Prime + E0 + D0 + E1 → D1`

Outbound:

`D1 → E1 + D2 + D3 + D4 + E4-related integration checks`

The apparent E1 inbound/outbound relation is preserved as specified rather than "cleaned up" into a prettier pipeline.

## Route-status warning

Do not use the historical E routes as current dependencies.

Do not retroactively erase them from history either.
