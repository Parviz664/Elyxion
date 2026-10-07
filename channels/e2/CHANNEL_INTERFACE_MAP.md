# CHANNEL_INTERFACE_MAP

## Historical interfaces

### v1.x
**Inbound**
- E-Prime canonical truth kernel
- E0 decision/constraint packet
- D0 invariant freeze
- E1 execution draft/dependency graph
- D1 guard/harm/comfort packets
- A2 systems map / intent

**Outbound**
- E2 variant packet
- recommended path
- tradeoff/risk/assumption/rollback matrices
- E3 handoff
- feedback to E1/D1/E0

### v2.1
**Inbound**
- E0 locked canon handle
- E1 skeleton + dependency graph
- D0 invariant freeze
- D1 guard
- A2 handshake / A3 refs via E0

**Outbound**
- Engine Contract Map
- Microstep Affordance Map
- Fidelity Proof Summary
- Primary Path Handle
- E3 + E5 handoffs

### v2.2
Recovered direction:
- E0/E1 authoritative upstream
- E2 translated engine contract / bounded routes
- E3 primary downstream
- no build/runtime/action authority.

### v2.3 strongest-known
**Inbound core**
- E0 root/bind context
- E1 lawful constrained skeleton

**Outbound core**
- `E2_ENGINE_CONTRACT_TRANSLATION_PACKET_V3`
- bounded `route_space`
- `translation_maturity`
- E3 handoff

**Non-core / overlay**
- D-family and E5-affordance concerns are no longer identity-bearing E2 core.

## Interface invariant

E2 may transform **representation into engine-contract space**, but may not transform **authority ownership**.
