# CHANNEL_INTERFACE_MAP

## Current strongest-known

### E0 -> E1
Packet:
E0_LOCKED_CANON_BINDING_PACKET_V1_7

Authority:
E0 owns bind/root legality.
E1 only consumes and echoes lawful basis.

### E1 -> E2
Packets:
E1_CONSTRAINED_IMPLEMENTATION_SKELETON_PACKET_V3
E1_TO_E2_ENGINE_CONTRACT_INPUT_V2

E2 responsibility:
engine-contract translation / bounded route expansion.

E1 must not preempt it.

### E1 -> E3
Packet:
E1_TO_E3_WEAK_VISIBILITY_INPUT_V1

Semantics:
visibility only.

Forbidden interpretation:
build-plan co-authority, task injection, DoD/rollback ownership.

## Historical interfaces

### A2 -> E1
v1.0–v1.3:
A2 systems map / immutable intent directly referenced among required inputs.

v1.4+:
no direct operator ingress; A2/A3 refs are carried inside E0 locked handle.

### D0 -> E1
v1.2:
D0_TO_E1_EXECUTION_TASK_PACKET_V1_1 and invariant/adaptation constraints.

v1.4+:
D0 not recovered as direct sole ingress; E0 handle becomes operator input boundary.

### E1 -> D1
v1.0–v1.3:
execution draft, risk, assumptions, constraint bindings, psycho-operational map.

v1.4+:
direct authoring role reduced/removed; D1 may optionally consume skeleton, but D1 seeds/guards come separately from E0/D0.

### E1 -> E0 feedback
v1.2/v1.3:
progress status, pending constraints, trace updates.

Current v1.6 exact feedback interface:
UNKNOWN in this recovery.

## Interface law

An interface existing in one epoch must not be assumed active in another.
