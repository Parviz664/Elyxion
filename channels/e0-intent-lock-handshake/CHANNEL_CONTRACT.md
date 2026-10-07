# CHANNEL_CONTRACT

Status: STRONGEST_KNOWN_CURRENT_CONTRACT_WITH_GAPS
Reference: ELYX_E0_CHANNEL_SPEC_V1_5_MASTER
This is recovery, not a new v1.6 design.

## Bind condition
Both source sides must be present and valid.

KERNEL:
E6_KERNEL_BUNDLE_REF_ONLY with lock_anchor_id, trace_root_id, packet_registry_ref, registry_seal_ref.

DREAM:
A3 release bundle carrying dream seal plus required carry/manifest material.

## No-inference
No missing registry/seal/A3 evidence may be guessed.
Missing critical lock input => BLOCK.

## Non-mutation
E0 binds refs and permissions. It does not rewrite dream text.

## Planning dispatch
Distinct from runtime promotion.
Recovered v1.5 planning surface:
E1, E2, E3, D1, D2, D3, D4, E4.

Mode:
BOOTSTRAP_LIMITED.

Forbidden before promotion:
real_build, real_packaging, real_test_execution, production_release, unsigned_snapshot_promotion.

## Runtime promotion
Recovered v1.5 runtime route:
E5 / E6 stage after closure.

Requires:
runtime bind proof, computed/stable hash evidence or equivalent contract satisfaction, output_contract_hash, result_evidence_hash, trace_id, no unresolved policy conflict/drift incident.

## Active A3 compatibility gap
v1.5 a3_ingest_contract explicitly lists:
ELYX_A3_RELEASE_BUNDLE_V1_4_OR_HIGHER

Later supplied:
ELYX_A3_PRE_E0_RELEASE_BUNDLE_V2_2

Observed E0 evaluation BLOCKed this as unaccepted type.
No later owner-supplied E0 patch is recovered.

## Active E-Prime floor gap
v1.5 declares requires_eprime_spec_min=1.3.0.
Current conversation explicitly supplies E-Prime v1.2.1, not an exact v1.3 technical-kernel master.

Classification:
UNVERIFIED_COMPATIBILITY_FLOOR.
Do not assume v1.3 exists.
