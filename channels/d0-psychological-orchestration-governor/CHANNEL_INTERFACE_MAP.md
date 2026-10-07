# CHANNEL INTERFACE MAP

## v1.0
IN:
- E_PRIME_UE55_CANONICAL_TRUTH_KERNEL
- E0_INTENT_LOCK_AND_HANDSHAKE_GATE
- E0 decision/envelope/constraints/risk
- A2 systems map

OUT:
- D0 invariant freeze
- latent pressure map
- allowed adaptation zones
- E1 task packet
- D1 psych guard packet
- E2 option search brief

## v1.1
Adds:
- E0 sync seed
- psycho-operational seed fields
- E4/D4 alignment awareness
- stronger cross-packet requirements

## v1.2
Adds required ingress:
- EPRIME_PACKET_REGISTRY_REF
- EPRIME_REGISTRY_SEAL_REF
- E0 v1.4+
- no-inference echo

Still outputs to:
E1 / D1 / E2.

## v2.0
IN:
- D_BASELINE_PACKET_REF
- D_BASELINE_PACKET_HASH
- D_PACKET_REGISTRY_REF
- D_REGISTRY_SEAL_REF
- D_SYNC_SEED_PACKET
- segment_registry
- optional runtime/proxy signals

OUT concretely declared:
- D1 task
- D2 task
- D3 task
- D4 task
- D8 task

No E-channel interface remains in current strongest-known spec.

Unresolved:
D5/D6/D7/D9/D10 current interface.
