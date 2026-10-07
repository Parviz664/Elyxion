# CHANNEL_BOUNDARIES

## Hard boundaries recovered

### 1. No UI
No HUD, bars, markers, tutorial overlays, progress UI logic.

### 2. Anti-domino
Explicit module boundaries, versioned contracts, rollback and regression tests; no hidden cross-module side effects.

### 3. Determinism
Same seed + same player actions must produce same logic outcome within declared tolerance. Randomness must be seeded and ordered.

### 4. Vertical-slice first
A1 must not expand into infinite architecture. It defines the smallest buildable proof and extension points.

### 5. Source-binding / assumptions
Uncertainty cannot be silently filled. Missing source integrity produces WARN or FAIL according to contract.

### 6. Canon boundary
A1 translates canon/vision into architecture; A1 output does not itself become owner canon.

### 7. DreamVault no-inference (v3.2+)
Refs are echo-only. Missing fields remain null. Hashes are never synthesized.

### 8. Role integrity (v3.2+)
A1 may provide informational alignment hints but must not emit E-Prime-owned artifact families.

### 9. Meaning cleanroom (v3.3+)
A2-facing meaning view must contain zero denylisted engine/build tokens. Implementation detail is isolated.

## Neighbor boundaries

- `A_MINUS_1 / A_ULTRA`: vision translation / hard guard upstream; not A1.
- `A0`: routing/ingest gateway; not A1.
- `P1`: causal/reality map planner; may hand compact material toward A1; not A1.
- `P5`: feel/truth compression; not A1.
- `A2`: downstream consumer/next agent; A1 prepares, A2 consumes.
- `E-Prime`: durability/archive/reality layer; A1 can align but not emit its artifacts.

## Current unresolved contract tension

v3.3 says build nouns are forced into `implementation_lane_v1`, but the append-only legacy required schema still contains top-level `variants[*].systems_used` and related implementation-bearing fields.

The observed assistant outputs preserve both for compatibility. Whether this duplication is the intended final interpretation is not owner-resolved in the recovered evidence.

Status: `CONTRACT_INTERNAL_TENSION / HOLD`.
