# CURRENT_CHAT_SOURCE_REGISTER

This is a source register, not a byte-for-byte transcript archive.

## User-supplied E2 masters present in the current conversation

### E2 v1.0
- artifact: `ELYX_E2_CHANNEL_SPEC_V1_0_MASTER`
- channel_id: `E2_VARIANT_SEARCH_AND_PATH_EXPANSION`
- owner: `E2_Variant_Intelligence_Lead`
- key artifact wording:
  - mission: build strong alternative trajectories, not execute them;
  - output focus includes `alternative paths (not one path)`;
  - min variants 3, max 7;
  - E3 next channel: `E3_DECISION_PACKAGING_AND_DOWNSTREAM_ROUTING`.
- provenance: USER_SUPPLIED_ARTIFACT.

### E2 v1.1
- artifact: `ELYX_E2_CHANNEL_SPEC_V1_1_MASTER`
- adds `E2-G08 cross_packet_locked_consistency`;
- adds `E2-G09 recommendation_confidence_governed`;
- `must_equal_locked_values.kernel_schema_version = 1.0.0`.
- provenance: USER_SUPPLIED_ARTIFACT.

### Exact author command
> Работать строго по контракту Е2.

Provenance: AUTHOR_RAW.

### E2 v1.2
- artifact: `ELYX_E2_CHANNEL_SPEC_V1_2_MASTER`
- patch intent explicitly says synchronization with E0 v1.3 / D0 v1.1 / E1 v1.2 / D1 v2.3 and registry+seal/no-inference hardening.
- `must_equal_locked_values.kernel_schema_version = 1.1.0`.
- registry/seal missing/untrusted/MISSING upstream packet → BLOCK.
- provenance: USER_SUPPLIED_ARTIFACT.

### E2 v2.1
- artifact: `ELYX_E2_CHANNEL_SPEC_V2_1_MASTER`
- exact artifact phrase:
> E2 перестаёт быть «портфелем стратегий» по умолчанию.

- primary outputs:
  - `E2_ENGINE_CONTRACT_MAP_PACKET_V1`
  - `E2_MICROSTEP_AFFORDANCE_MAP_PACKET_V1`
  - `E2_FIDELITY_PROOF_SUMMARY_PACKET_V2_1`
- primary-path max: 1
- optional alt max: 1, fallback-only
- no 0–100 metric axis for selection
- registry+seal echo only via E0 locked handle
- provenance: USER_SUPPLIED_ARTIFACT.

## Assistant-generated E2 operational packets in current conversation

These are historical evidence of attempted operation, **not owner-authored RAW**:
- `ELYX_E2_EXECUTION_RESULT_V1_1` — D1 evidence-closure variants;
- `ELYX_E2_EXECUTION_RESULT_V1_1` — SIM lane variants;
- `ELYX_E2_EXECUTION_RESULT_V1_1` — REF_ONLY kernel compatibility variants;
- `ELYX_E2_EXECUTION_RESULT_V1_2` — registry/seal missing → BLOCK;
- `ELYX_E2_EXECUTION_RESULT_V2_1` — missing dual-lock/skeleton inputs → BLOCK.

## Preservation warning

The current conversation itself remains the higher-fidelity source for the complete pasted JSON bodies. This register does not claim byte equivalence.
