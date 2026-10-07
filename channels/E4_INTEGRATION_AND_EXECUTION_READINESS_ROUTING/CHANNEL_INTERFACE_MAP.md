# Interface map

## Current v2.1 inbound interfaces

### E0
Input: locked canon handle only.  
Authority relation: E0 is sole truth binder; E4 echo/equality only.  
Failure: missing/incomplete handle => BLOCK.

### D0
Input: invariant freeze packet.  
Use: safety/invariant lint.  
E4 cannot override.

### D1
Input: guard packet.  
Use: comfort/overload/safety clearance.  
E4 cannot override.

### E1
Input: constrained skeleton + dependency graph.  
Use: dependency reachability, route structure, rollback anchoring.  
E4 cannot author/replace E1 skeleton.

### E2
Inputs: engine contract map + affordance map.  
Use: contract refs, precise UI/command/document anchors.  
E4 cannot silently invent missing affordances.

### E3
Input: one Production Bundle primary path.  
Use: route semantic backbone.  
E4 cannot re-run variant selection or rewrite primary semantics.

### D2/D3/D4
Optional non-binding alignment sources in v2.1.

## Current outbound interfaces

### E5
Primary consumer.

E5 receives a single route and actionability scaffolding. E5 must not choose architecture.

### D4
Optional player-impact/strain/awe annotations.

### E3/E2/E1/D1 feedback
Non-mutating diagnostics:
- actionability gaps;
- missing affordance refs;
- contract granularity gaps;
- dependency/guard hotspots;
- closure blockers.

## Historical v1.1 interfaces

Primary upstream pair:
E3 + D3.

Historical downstream:
E5 + D4 plus feedback to E1/D1 and E3/D3.

## Interface ownership rule

A reference may be carried through E4 without E4 owning the semantic authority of the referenced subsystem.
