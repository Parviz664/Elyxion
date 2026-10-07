# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-1 — decorative certainty risk
Historical E-Prime discussions sometimes used very high percentage/reliability targets.

Correction:
a target is not measured evidence.
v1.6 explicitly moves reliability score toward report-only release semantics.

Invariant:
no numerical score alone authorizes release.

## ERR-2 — ref-only notes bypass
v1.4 audit found that registry notes could undermine ref-only intent.

Correction:
notes require strict policy/size/content constraints.

Invariant:
metadata must not become hidden payload transport.

## ERR-3 — underdefined DreamVault hash serialization
v1.4 hash-chain logic did not fully define canonical serialization.

Correction path:
explicit canonicalization was recommended.

Invariant:
a hash claim without byte/canonicalization definition is incomplete.

## ERR-4 — scm_revision portability
v1.4 audit identified missing VCS-neutral revision identity.

Correction path:
restore neutral scm_revision semantics.

## ERR-5 — Gate_10 weakening
v1.6 changed Gate_10 toward report-only behavior while earlier global semantics treated gate failure as blocking.

Correction:
do not treat this as harmless until precedence/consumer invariant is explicit.

Invariant:
release authority cannot be weakened silently.

## ERR-6 — append-only lineage overclaim
Later master documents omitted fields present in earlier hardening.

Correction:
treat monotonic preservation as unproved unless inheritance/supersession semantics are explicit.

## ERR-7 — hash-chain authenticity overclaim
A hash chain may prove continuity/integrity relative to a trusted anchor, not authorship/authenticity by itself.

Invariant:
consistency proof != external authenticity proof.

## ERR-8 — archive/channel name collision
On 2026-10-07 a GitHub branch named E-Prime was created for Chat Archive.

Correction:
separate namespace and recovery branch for architectural E-Prime.

Invariant:
same name != same operational object.
