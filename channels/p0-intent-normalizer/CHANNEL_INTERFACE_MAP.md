# CHANNEL_INTERFACE_MAP

## Historical route family A — v2.3

`AUTHOR_TEXT -> P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

P0 output interfaces:
- `minus_p1_input`
- `p1_input`
- `p2_input`
- `p3_input`
- `p4_input`

Status: `HISTORICALLY_ACTIVE`

## Historical route family B — v2.4/v2.6

`AUTHOR_TEXT -> P0 -> P1 -> P2 -> P3 -> P4`

P0 output interfaces:
- `p1_input`
- `p2_input`
- `p3_input`
- `p4_input`

Status: `HISTORICALLY_ACTIVE / LATEST_STRONGLY_RECOVERED_P0_ROUTE`

## Current global route

`HOLD_UNRESOLVED`

Neither route A nor route B is frozen as current global P-system truth.

## Interface semantics

### P0 -> P1
P0 hands normalized intent plus scope/guards/causal requirements.

### P0 -> P2/P3/P4
Recovered specs contain pre-shaped downstream inputs/references, but actual downstream execution still depends on upstream artifacts/refs becoming real.

P0 is therefore a router/normalizer, not evidence that P2/P3/P4 may execute before P1/P2 outputs exist.

### P ↔ A

No direct P0→A packet is strongly recovered.

Downstream P2/A-bridge evidence exists in historical conversation context, but is outside P0's own recovered interface authority.

## Forbidden interface inference

Do not infer:
- removed node = removed function;
- similar fields = renamed channel;
- user-supplied artifact = owner-authored artifact;
- later output schema = formal channel spec.
