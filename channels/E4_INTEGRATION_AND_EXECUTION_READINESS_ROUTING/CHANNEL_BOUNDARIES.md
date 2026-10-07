# Channel boundaries

## Current v2.1 boundaries

### Truth boundary
Only E0 binds locked truth. E4 performs echo + equality checks.

### Meaning boundary
Meaning lane is ref-only. E4 cannot rewrite, improve, taskify, metricize, or engine-translate the dream itself.

### Implementation boundary
Implementation vocabulary is allowed only inside `impl_lane_quarantine` fields of route segments. Leakage into meaning is P0.

### Architecture boundary
E4 compiles the selected E3 primary route. It does not create alternatives or force E5 to choose.

### Execution boundary
No build, test, runtime, release, or performance claims.

### Safety boundary
D0 invariants and D1 guards cannot be overridden.

### Numeric boundary
v2.1 forbids `score_0_100`, weights, ranking-by-score, confidence bands by score, and percent gain as decision drivers.

### Missing-evidence boundary
E4 does not reconstruct absent refs. Missing required input becomes a closure/blocker.

## Historical v1.1 boundaries

v1.1 already prohibited:
- upstream mutation;
- runtime/build/release execution;
- D0/D1 override;
- unresolved critical conflict promotion.

But v1.1 still permitted:
- ranking nodes;
- weighted numeric scores;
- gain thresholds;
- E3+D3 synthesis as its core transform.

These historical permissions are superseded, not erased.

## Easily confused neighbors

- **E0**: truth binder. E4 is not E0.
- **E1**: constrained implementation skeleton. E4 does not author the skeleton.
- **E2**: contract/affordance translator. E4 references E2 outputs; it does not replace them.
- **E3**: convergence/packaging to a primary production path in the v2.x route. E4 does not redo E3 selection.
- **E5**: route-to-microsteps execution orchestration. E4 must make E5's job non-architectural.
- **D3/D4**: optional alignment/augmentation layers in v2.1, not E4 truth authority.
