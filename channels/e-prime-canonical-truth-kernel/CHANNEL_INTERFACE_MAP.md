# CHANNEL_INTERFACE_MAP

## Upstream classes

### Technical truth inputs
E-Prime historically receives:
- snapshot identity;
- source revision identity;
- deterministic gate evidence;
- packet refs;
- validation/proof refs.

### E6 -> E-Prime
Recovered functions include:
- Dream Capsules for DreamVault;
- execution/progress evidence for ExecutionCanon;
- later kernel-bundle relationship visible through E0 recovery.

Exact final E6 role partition:
NOT FULLY RECOVERED.

### Bootstrap lane
SIM/bootstrap evidence may enter only under explicit non-canon/bootstrap controls.

## Downstream classes

### E-Prime -> E0
Historical progression:
1. direct E-Prime truth packet;
2. registry+seal refs;
3. Dream Seal / truth refs;
4. later E6-carried kernel bundle refs visible at E0.

E-Prime does not own E0 bind authority.

### E-Prime -> recovery/resume
E-Prime provides durable refs, lineage, rollback/recovery identity and later execution-canon state.

## Internal interfaces

### Packet Registry
Ref-only identity index.
Must not become a hidden payload transport.

### Registry Seal
Closes/attests a registry state under no-inference rules.

### DreamVault
E6 capsule refs
→ append-only ledger
→ composite
→ dream seal.

### ExecutionCanon
Later execution-state surface.
Requires E6 Progress Gate in v1.6 family.

### Debt Ledger
Permits explicitly bounded evidence deferral in allowed SOLO_BOOTSTRAP/evidence-tier contexts.
Debt does not disappear by time alone.

## Forbidden interface collapse

Do not collapse:
- registry ref into payload;
- DreamVault into canon authoring;
- ExecutionCanon into runtime executor;
- E-Prime into E0;
- E-Prime into E6;
- E-Prime channel into GitHub Chat Archive.
