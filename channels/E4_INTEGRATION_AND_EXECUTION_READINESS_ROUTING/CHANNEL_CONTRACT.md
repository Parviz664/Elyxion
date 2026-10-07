# Channel contract recovery

This file does not synthesize a new contract. It records the exact strongest recovered contract states.

## Contract state A — v1.1

Artifact: `ELYX_E4_CHANNEL_SPEC_V1_1_MASTER`  
Recovery class: EXACT_VERSION_RECOVERED  
Status inside artifact: PASS  
Mode: CANON_STRICT

### Exact purpose excerpt

> "Взять полный усиленный контур E3+D3 (с наследием E2/D2), ничего не обнуляя и не размывая, и собрать единую карту безопасной силы: максимально надежную, трассируемую, применимую и готовую к downstream-интеграции без канонического дрейфа и без runtime-исполнения."

### Exact design-intent excerpt

> "E4 — не генератор новых идей и не переписыватель предыдущих слоев. E4 — финальный картограф надежности и применимости..."

### Core v1.1 authority

Allowed:
- ingest E3+D3;
- prove coverage;
- build unified decision map;
- resolve conflict topology;
- rank nodes;
- emit `E4_MAP_PACKET_V1_1`.

Forbidden:
- mutate upstream;
- build/test/runtime/release;
- override D0/D1;
- promote unresolved/untraceable nodes.

### v1.1 decision mechanics

v1.1 explicitly included a numeric scoring model with weighted subscores and acceptance thresholds. This is historically real and later superseded.

## Contract state B — v2.0

Artifact named by v2.1:
`ELYX_E4_CHANNEL_SPEC_V2_0_MASTER`

Recovery class: REFERRED_TO_ONLY.  
Content: NOT_RECOVERED.

Do not reconstruct v2.0 from v2.1.

## Contract state C — v2.1

Artifact: `ELYX_E4_CHANNEL_SPEC_V2_1_MASTER`  
Recovery class: EXACT_VERSION_RECOVERED  
Mode: CANON_STRICT

### Exact purpose excerpt

> "Скомпилировать E3 Production Bundle (один primary path) + E2 Engine Contract Map/Affordance Map + E1 Skeleton в единую route-карту для E5: без дрейфа мечты, без runtime-исполнения, с 100% source coverage (no silent drop)..."

### Exact design-intent excerpt

> "E4 — не генератор идей и не судья превосходства. E4 — компилятор маршрута..."

### v2.1 critical contract changes

- `E4_E0_TRUTH_BINDER_ONLY_V1`
- `E4_NUMERIC_AXIS_BAN_V1`
- `E4_DREAM_FIDELITY_ECHO_PROOF_V1`
- `E4_NO_DROP_INDEX_V1`
- `E4_E5_IMPROV_BAN_V1`
- `E4_ACTION_ATOM_CONTRACT_V1`
- `E4_AFFORDANCE_PRECISION_GATE_V1`
- `E4_ROLLBACK_CHAIN_INTEGRITY_V1`
- `E4_CLOSURE_LEDGER_V1`
- `E4_MICROSTEP_READINESS_COMPILER_V1`

### Current authority ceiling

E4 may compile and govern route readiness. It may not:
- become another E0;
- make meaning;
- choose architecture on E5's behalf;
- execute runtime;
- invent missing proof.

Missing required input is a reason to stop, freeze, or emit closure—not a license to fill gaps.
