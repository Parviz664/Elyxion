# E3.5 E4 Input Assembler + No-Drop Coverage Proof — channel recovery

Recovery branch: channel/e3-5-input-assembler-recovery-v0.1

Recovery target:
E3_5_E4_INPUT_ASSEMBLER_AND_NO_DROP_COVERAGE_PROOF

Human name recovered:
E3.5 Канал Сборки Входов для E4 + No-Drop Coverage Proof

Strongest currently recovered working specification:
ELYX_E3_5_CHANNEL_SPEC_V1_4_MASTER, status DRAFT_READY_FOR_USE, supplied by the user on 2026-02-20.

Important provenance rule:
SUPPLIED_BY_AUTHOR != AUTHORED_BY_AUTHOR.
The user supplied the v1.0-v1.4 artifacts in conversation. That proves they were used as working channel artifacts; it does not prove the user personally authored every field.

## Strongest recovered identity

E3.5 is a ref-only fan-in assembler and proof boundary immediately before E4.

It does not improve E2/E3/D2/D3 meaning.
It does not solve E4 conflict topology.
It does not promote SIM to CANON.
It does not make runtime/performance claims.

Its own job is narrower:
1. receive the required upstream packet references for E4;
2. validate presence/type/lane/root constraints;
3. build a one-to-one no-drop index;
4. prove or fail to prove input coverage;
5. hand off a bounded bundle to E4 only when the configured proof rules permit it.

## Historical arc

Earliest recovered user command:
“хорошо сделай этот Е3.5”
2026-02-18T10:16:05Z.

Three seconds later an assistant output created the channel as an engineering E4 required-sources assembler.

Evolution:
pre-v1.0 seed
-> v1.0 assembler template
-> v1.1 REF_ONLY_STRICT / no-shadow / exact-type proof
-> v1.2 guarantee scope + E4 missing-input BLOCK-class elimination
-> v1.3 BOOTSTRAP dual-root ref-only support
-> v1.4 registry/seal presence proof + anti-injection + deterministic hashes + MIN_VERSION_SAME_MAJOR

The newest assistant-proposed v1.4.1 patch set is NOT owner-confirmed and is preserved only as an assistant proposal.

## Current evidence ceiling

Recovered strongly:
- channel identity and technical id;
- v1.0-v1.4 supplied specification lineage;
- ref-only/no-mutation boundary;
- SIM single-root and later BOOTSTRAP dual-root/no-merge lane models;
- E4 missing-input/coverage elimination scope;
- 10-key E4 input contract in v1.4;
- several historical assistant errors that motivated stronger proof discipline at least architecturally, though author rationale is not inferred.

Not recovered strongly:
- exact user discussion immediately before “хорошо сделай этот Е3.5”;
- proof that the user personally authored the JSON specs;
- a real 10/10 REF_ONLY_STRICT PASS execution;
- an external/runtime validator implementation;
- owner acceptance of the assistant-proposed v1.4.1 patch;
- a full byte-for-byte archive of every source packet referenced by E3.5.

Recovery status target:
SELF_RECOVERY_PASS_WITH_GAPS.
