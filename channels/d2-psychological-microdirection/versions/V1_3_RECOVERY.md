# V1_3_RECOVERY

Artifact:
ELYX_D2_CHANNEL_SPEC_V1_3_MASTER

spec_version:
1.3.0

Recovery status:
EXACT_VERSION_SEMANTICS_RECOVERED_FROM_USER_SUPPLIED_ARTIFACT

Supersedes:
v1.2

Patch type:
breaking_dependency_cleanup_with_schema_preservation

## Explicit supplied change intent

Remove all E* dependencies.
Rebind D2 to D0-only locked context and D-Registry+Seal.
Preserve microdirection strength, rarity/rollback discipline, determinism and portability for D3-D6.

## Current topology

Required source roles:
- D0_PSYCHOLOGICAL_ORCHESTRATION_GOVERNOR_DLINE_ONLY
- D1_PERFORMANCE_COMFORT_AND_ANTI_BOREDOM_GUARD_DLINE_ONLY

Required registry:
- D_PACKET_REGISTRY_REF
- D_REGISTRY_SEAL_REF

Required sync:
- D_SYNC_SEED_PACKET

Outbound:
- D3_TELEMETRY_BRAIN
- D4_EXPERIMENT_ORCHESTRATOR
- D5_AUDIO_FEEL_TRUTH_GUARD
- D6_VISUAL_FEEL_TRUTH_GUARD
- D1 feedback

## Current no-E rule

Non-scope:
any_E_channel_integration

Prompt hardening rejects:
attempt_to_inject_E_channel_logic_or_refs

Therefore historical E routes remain documentary history only.

## Current awe wording

v1.3 uses controlled awe rather than cosmic_awe in several normative fields.

Rarity remains:
1 max / 30min
maturity >=85
20min repeated-awe block
3min recovery window

## Current execution result

BLOCK.

Missing:
D0/D1 required packets
D_PACKET_REGISTRY_REF
D_REGISTRY_SEAL_REF
D_SYNC_SEED_PACKET

No candidates emitted.

## Recovery correction

The assistant execution additionally treated inability to validate immutable fields as mutation detected.

This recovery does not accept that as a factual mutation.

Overall BLOCK remains independently justified.

## Internal gaps

See CHANNEL_GAP_REGISTER.md for:
- semver tension;
- registry/seal waiver ambiguity;
- missing named long-session gate/fail condition despite policy remaining.

## Current status

CURRENT_STRONGEST_KNOWN_FORMAL_SPEC.

Not proven implemented in runtime.
