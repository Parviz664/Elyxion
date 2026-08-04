# Glossary

| Term | Meaning in Phase 1 |
| --- | --- |
| Elyxion Core | Orchestrator that owns simulation time, resolution order, and immutable encounter history. |
| Membrane | Protective boundary that converts a threat signal into an automatic defense action. |
| WhiteLine | Maturity and learning system represented by a score from 0 to 100. |
| Red Pressure Node | Canonical external threat source for Phase 1. It emits signals only. |
| ThreatSignal | Immutable observation of source, tick, pressure intensity, and pattern. |
| DefenseAction | Membrane decision containing state, strategy, mitigation rate, and energy cost. |
| Outcome | Resolved record of prevented pressure, residual pressure, cost, and maturity change. |
| Tick | Monotonically increasing simulation step controlled by Elyxion Core. |

## WhiteLine maturity

The initial thresholds are working defaults, not final lore or balance.

| Tier | Score | Phase 1 interpretation |
| --- | ---: | --- |
| M0 | 0-24 | Reactive: recognizes pressure but has limited protection. |
| M1 | 25-49 | Stabilizing: responds more consistently. |
| M2 | 50-74 | Adaptive: can use learned defense strategies. |
| M3 | 75-100 | Integrated: strong mitigation with lower relative cost. |

## Membrane states

| State | Meaning |
| --- | --- |
| `stable` | Pressure is below the alert threshold. |
| `alert` | Pressure is meaningful; the Membrane braces. |
| `defense` | Pressure is severe; active mitigation is required. |
| `recovery` | The response was resolved and the system is integrating the outcome. |

