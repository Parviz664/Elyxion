# Channel history

## 1. Earliest recoverable seed

The earliest recoverable prior-context record is dated **2026-02-17T20:35:19Z** and identifies E4 as `E4_INTEGRATION_AND_EXECUTION_READINESS_ROUTING`, with a mission to aggregate E3+D3, carrying E2/D2 inheritance, into a safe and reliable execution/integration map.

Evidence class: RECOVERED_PRIOR_CONTEXT / USER_FACT.  
Exact original wording is not available in this recovery, therefore this is **not AUTHOR_RAW**.

The original psychological or personal reason for creating E4 is not recovered. The architectural problem is recoverable: downstream needed an integration/readiness map that did not rewrite upstream semantics.

## 2. v1.1 — integration cartographer era

The exact user-supplied v1.1 master defines E4 as a final reliability/applicability cartographer over E3+D3.

Exact mission excerpt from the supplied artifact:

> "Синтезировать экстремально усиленные результаты E3 и D3 в production-grade карту решений с явной иерархией, конфликт-топологией, покрытием источников 100%, границами применимости, порядком внедрения и стресс-проверками, чтобы обеспечить быстрый и безопасный переход к E5/D4."

Core properties:
- upstream semantics immutable;
- no runtime execution;
- full E3/D3 source coverage;
- conflict topology;
- forced-order lanes CORE / AMPLIFIER / RESERVE / FROZEN;
- risk heatmap;
- stress survivability;
- rollback and trace continuity;
- numeric reliability/power scoring existed and could drive acceptance.

## 3. Early assistant over-certification

After the v1.1 contract was supplied, the assistant emitted an `E4_MAP_PACKET_V1_1` with `PASS_WITH_CONSTRAINTS_A`, invented concrete map nodes such as `E4N-001`, synthetic E3/D3 origin refs, counts such as 12 E3 nodes / 9 D3 nodes, and computed scores.

Those values were not fully grounded in the supplied upstream packet set in that turn.

Provenance: ASSISTANT_OUTPUT.  
Historical status: **not canon; evidence of channel-operation error**.

This matters because a later run behaves differently: when only a D3(SIM) packet was available, E4 stopped with BLOCK rather than pretending full coverage.

## 4. Canonical-bootstrap D3 integration attempt

The user then supplied a detailed `ELYX_D3_EXECUTION_RESULT_V1_1` in CANON_STRICT / BOOTSTRAP_LIMITED. The assistant emitted a second E4 map with `PASS_WITH_CONSTRAINTS_B`.

This output was more tied to real D3 refs, but still asserted E3 coverage and a compiled graph without the full required upstream packet set being present in that turn. It therefore remains ASSISTANT_OUTPUT, not owner-confirmed E4 truth.

## 5. SIMULATION_ONLY correction

The user later supplied D3 in:
`BOOTSTRAP_LIMITED__SIMULATION_ONLY`,
with:
- `simulation: true`;
- `non_canon: true`;
- `promotion_to_canon_allowed: false`;
- `runtime_promotion_allowed: false`;
- SIM trace-root isolation;
- no runtime/performance claims.

The assistant E4 response then returned **BLOCK**, explicitly stating that full E3/E2/D2/E1/D1/D0/E0/EPRIME/A2 coverage and safety closure could not be proved from D3 alone.

This is the clearest recovered behavioral correction from "map despite gaps" to "fail closed on missing upstream".

## 6. v2.0 existence

v2.1 explicitly says:
`supersedes_artifact_type: ELYX_E4_CHANNEL_SPEC_V2_0_MASTER`.

Therefore v2.0 existed as a named predecessor. Its full content is **not recovered** here.

Only the delta claims made by v2.1 are preserved; the missing v2.0 body is not reconstructed.

## 7. v2.1 — route compiler era

The exact v2.1 master changes E4 materially.

Exact design-intent excerpt:

> "E4 — не генератор идей и не судья превосходства. E4 — компилятор маршрута: превращает production bundle в microstep-ready карту исполнения."

Key changes explicitly declared by the artifact:
- E0 becomes the only truth binder;
- dual-lock and registry+seal are echo-only through E0;
- E3 becomes a single-primary-path Production Bundle;
- E2 supplies Engine Contract Map + Affordance Map;
- E1 supplies the constrained skeleton/dependency graph;
- D3 becomes optional alignment input, not a required co-primary source;
- numeric score axes are banned as decision drivers;
- Dream Fidelity Echo Proof added;
- No-Drop Index added;
- E5 Improvisation Ban added;
- CORE Action Atom Contract added;
- Affordance Precision Gate added;
- route-level Rollback Chain Integrity added;
- Closure Ledger added;
- implementation vocabulary is quarantined away from meaning;
- E5 must translate route -> microsteps, not make architecture.

## 8. v2.1 fail-closed execution evidence

After v2.1 was supplied, the assistant attempted a run and blocked because the E0 locked handle, D0, D1, E1 skeleton, E2 maps, and E3 production bundle were absent.

The direction of this behavior matches the current contract's fail-closed intent. Some output schema details were imperfect and are recorded in `CHANNEL_GAP_REGISTER.md`.

## Current historical conclusion

E4 is not "the same thing with more features."

Its evolution is:

`E3+D3 reliability synthesis cartographer`
→ stronger missing-input / SIM isolation behavior
→ `single-route, E0-echo-only, microstep-readiness compiler`.

The current strongest-known role is v2.1. Earlier roles remain preserved as historical states.
