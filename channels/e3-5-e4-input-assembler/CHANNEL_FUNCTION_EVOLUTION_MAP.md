# CHANNEL_FUNCTION_EVOLUTION_MAP

## STATE_0 — creation seed

name:
E3.5, full technical name created by assistant immediately after user command.

version:
pre-v1.0 body not recovered.

mission:
engineering assembler for E4 required sources.

transformation authority:
partially unknown.

implementation status:
assistant-created concept.

delta to STATE_1:
formal v1.0 manifest and proof template supplied.

## STATE_1 — v1.0 assembler template

mission:
assemble full required_sources for E4 and prove no-drop coverage.

inputs:
10 required sources + optional sources + possible waivers.

authority:
reference/assembly plus coverage metadata.

forbidden:
source mutation, SIM->CANON merge, runtime claims.

lane:
single SIMULATION_ONLY.

output:
E4_REQUIRED_SOURCES_BUNDLE_V1 + coverage proof.

weakness exposed in practice:
assistant execution invented/assumed refs and unsigned waivers.

delta to STATE_2:
explicit ref-only/no-reserialization/no-shadow discipline.

## STATE_2 — v1.1 REF_ONLY_STRICT

mission:
same assembly goal with far less semantic authority.

inputs:
same families under explicit E4 source contract.

authority:
refs/index/proof only.

forbidden strengthened:
no compacting, no aggregation, no reserialization.

type policy:
exact match.

modes:
strict or partial-with-waivers.

delta to STATE_3:
formal guarantee scope and missing-input BLOCK-class elimination.

## STATE_3 — v1.2 scoped proof boundary

mission:
prove exactly what E3.5 can eliminate for E4.

new functions:
contract sync guard;
strict ref integrity proof;
E4_BLOCK_CLASS_ELIMINATION_MAP.

new non-guarantee:
E4_TOTAL_PASS explicitly excluded.

lane:
still SIM single-root.

delta to STATE_4:
real BOOTSTRAP dual-root inputs expose lane-model insufficiency.

## STATE_4 — v1.3 multi-lane ref proof

mission:
preserve ref-only assembly while supporting either:
SIM single-root
or
BOOTSTRAP dual-root/no-merge.

new authority:
validate root_binding and dual-root integrity.

new prohibition:
cross-root stitching.

delta to STATE_5:
harder registry/type/injection/seal proof surface.

## STATE_5 — v1.4 hardened assembler

mission:
10/10 refs + proofability with reduced false type-version blocking while preserving no-drop.

new structures:
MIN_VERSION_SAME_MAJOR;
registry/seal presence proof;
anti-injection;
deterministic hashes;
bundle V1_1.

current evidence state:
latest user-supplied spec.

implementation state:
contract exists; no recovered real 10/10 PASS execution.

## Proposed STATE_6 — v1.4.1

origin:
assistant review only.

status:
NOT ADOPTED / HOLD.

Do not merge into current state.
