# RECOVERY_ASSERTIONS

These are archaeology assertions, not runtime tests.

## Identity assertions
- [x] architectural id is `E_PRIME_UE55_CANONICAL_TRUTH_KERNEL`
- [x] architectural E-Prime is not the Chat Archive branch
- [x] E-Prime is not the game repository

## Lineage assertions
- [x] v1.2.1 role preserved
- [x] v1.3 body marked partial
- [x] v1.4 DreamVault addition preserved
- [x] v1.4.1 marked recommended, not proven installed
- [x] E-Prime v1.5 remains unknown
- [x] v1.6 role preserved
- [x] Bootstrap Lock V2 kept separate from semver lineage

## Authority assertions
- [x] no author-dream ownership
- [x] no E0 bind authority
- [x] no E6 runtime authority
- [x] no SIM→CANON promotion
- [x] no missing-ref inference
- [x] report-only reliability score does not authorize release

## Error/gap assertions
- [x] v1.4 ref-only/notes gap preserved
- [x] DreamVault canonicalization gap preserved
- [x] scm_revision hardening gap preserved
- [x] v1.6 Gate_10 issue preserved
- [x] earlier-hardening-field regression concern preserved

## Cross-channel assertions
- [x] E0 historical direct E-Prime ingress preserved
- [x] registry/seal ingress preserved
- [x] later E6 ref-only kernel-bundle topology preserved
- [x] exact final E-Prime/E6 ownership seam remains unresolved

## Recovery verdict expectation

Expected:
`SELF_RECOVERY_PASS_WITH_GAPS`

A STRONG_PASS would be false while exact v1.3/v1.5/runtime/current seam evidence remains missing.
