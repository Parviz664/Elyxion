# CHANNEL GAP REGISTER

| Gap ID | Gap | Why it matters | Evidence ceiling | Status |
|---|---|---|---|---|
| GAP-D1-001 | exact user message that originally requested creation of D1 | prevents claiming a false origin story | LOW-MEDIUM | OPEN |
| GAP-D1-002 | full body of `ELYX_D1_CHANNEL_SPEC_V2_0_MASTER` | v2.0 known only partially | MEDIUM | OPEN |
| GAP-D1-003 | full body of `ELYX_D1_CHANNEL_SPEC_V2_3_MASTER` | prevents reconstructing missing transition | HIGH for existence, NONE for body | OPEN |
| GAP-D1-004 | proof of original authorship of v2.1/v2.2/v2.4 JSON | user supplied != user authored | UNKNOWN | OPEN |
| GAP-D1-005 | trusted current D0 packet matching v2.4 locked values | required for current gate execution | NONE in recovery inputs | OPEN |
| GAP-D1-006 | `D_PACKET_REGISTRY_REF` + trusted `D_REGISTRY_SEAL_REF` | mandatory current no-inference gate | NONE in recovery inputs | OPEN |
| GAP-D1-007 | real-device runtime metrics satisfying current sampling plan | needed for comfort/uncertainty gates | NONE | OPEN |
| GAP-D1-008 | current D implementation fidelity report | needed for >=99.3 fidelity gate | NONE | OPEN |
| GAP-D1-009 | evidence that v2.4 was implemented in game/runtime code | separates contract from implementation | NONE | OPEN |
| GAP-D1-010 | exact D1 raw transcript export | would allow byte-level source archive/hash | NOT AVAILABLE IN THIS RECOVERY | OPEN |
| GAP-D1-011 | exact semantic content of any version before v2.0 | first detectable D1 artifact is v2.0 | NONE | OPEN |
| GAP-D1-012 | direct P/A relationship | user explicitly asked to recover if real; none found | NONE | OPEN |

## Important non-gap

The historical E-channel topology is **not** a gap: it is exactly recovered in v2.1/v2.2.

The current zero-E topology is also exactly recovered in v2.4.

The uncertainty is the missing v2.3 body, not whether the reversal existed.
