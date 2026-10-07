# RECOVERY_ASSERTIONS

These are archaeology invariants, not runtime tests.

RA-001:
v1.0 must not be described as A-only.
Expected: E-Prime lock is part of A3 upstream validation.

RA-002:
v1.3 must preserve the E-Prime reversal.
Expected: E-Prime forbidden inside A3 and later bound at E0 from E6/E-lane.

RA-003:
v1.3 snapshot A and snapshot B remain separate despite same semver.

RA-004:
v1.4 preserves A2_ONLY_SEAL and FULL_CANON_CARRY dual ingest.

RA-005:
v2.2 must not be projected backward onto v1.x.

RA-006:
current role must not claim admissibility authority.

RA-007:
current role must not claim bind legality.

RA-008:
missing v2.1 body remains UNKNOWN.

RA-009:
assistant PASS packets are not owner canon.

RA-010:
assistant-generated packet timestamps are not chronology truth.

RA-011:
current A3 must not ingest or validate E-Prime.

RA-012:
current output is a pre-E0 sealed lawful carrier, not runtime plan.

RA-013:
early evidence-overclaim execution remains visible in error history.

RA-014:
first v1.3 numeric inconsistency remains visible.

RA-015:
recovery status remains PASS_WITH_GAPS unless new primary evidence closes origin/version/runtime gaps.
