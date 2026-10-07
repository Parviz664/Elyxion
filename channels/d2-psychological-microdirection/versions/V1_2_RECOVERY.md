# V1_2_RECOVERY

Artifact:
ELYX_D2_CHANNEL_SPEC_V1_2_MASTER

spec_version:
1.2.0

Recovery status:
EXACT_VERSION_SEMANTICS_RECOVERED_FROM_USER_SUPPLIED_ARTIFACT

Supersedes:
v1.1

Patch type:
backward_compatible_contract_hardening

## Explicit supplied change intent

Synchronize D2 with newer E0/D0/E1/D1/E2 floors and add registry+seal/no-inference plus anti-injection so psychological enhancement relies only on provably valid inputs.

## New controls

- EPRIME_PACKET_REGISTRY_REF
- EPRIME_REGISTRY_SEAL_REF
- no-inference
- registry/seal verification gate
- prompt-injection hardening
- injection gate
- new risks D2-R009 and D2-R010
- D2_ENHANCEMENT_PACKET_V1_2

## Route

Still E-bound.

Required sources:
E-Prime/E0/D0/E1/D1/E2/A2.

## Behavioral significance

This version changes how missing evidence is handled.

Recovered execution:
registry and seal absent -> BLOCK.

No candidates emitted.

This is a hardening compared with the first v1.1 assistant response.

## Historical status

SUPERSEDED by v1.3.
