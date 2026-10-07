# CHANNEL_GAP_REGISTER

Status: OPEN_GAPS_PRESERVED.

## G1 — exact v1.3 body
Known:
law id and broad Registry Seal/no-inference role.

Missing:
full exact v1.3 schema/contract body.

Effect:
cannot claim gap-free lineage v1.2.1→v1.4.

## G2 — v1.4.1 acceptance
Known:
hardening patch was recommended.

Missing:
proof that v1.4.1 became accepted canonical master.

Effect:
treat as recommended patch, not installed truth.

## G3 — E-Prime v1.5
Exact E-Prime v1.5 master not recovered.

Effect:
do not infer from E0 v1.5.

## G4 — Gate_10 semantics in v1.6
Recovered audit flags report-only weakening risk.

Effect:
v1.6 cannot be called fully closed without explicit downstream invariant or superseding fix.

## G5 — dropped/restored hardening fields
v1.6 audit identified missing/restoration concerns:
- notes_policy;
- lane_echo;
- scm_revision;
- runtime-signature definition;
- DreamVault hash canonicalization.

Effect:
requires reconciliation against earlier hardening before claiming monotonic append-only preservation.

## G6 — debt precedence
Open historical question:
how raw gate failure vs effective deferred/debt state resolves under v1.6.

Effect:
release semantics need exact precedence.

## G7 — evidence tier/lane distinction
SIM/CANON lane and T0/T1/T2 evidence tier are different dimensions.

Effect:
must not conflate them.

## G8 — E6 Progress Gate semantic validation
Reference presence alone is insufficient unless trace/freshness/meaning is validated.

Effect:
ExecutionCanon integration remains partly open.

## G9 — DreamVault authenticity vs consistency
Hash chain proves internal continuity/tamper evidence only under a trusted root/head.

Effect:
must not overclaim authenticity.

## G10 — source recovery
DreamVault ref-only design depends on retained source capsules/raw source.

Effect:
loss of all source copies prevents full raw recovery.

## G11 — current E-Prime↔E6↔E0 route
Later E0 uses E6 kernel bundle refs.

Effect:
exact current ownership/handoff division needs global reconciliation.

## G12 — runtime implementation
No executable E-Prime runtime implementation has been independently verified in this recovery.

Effect:
contract recovery != coded runtime proof.

## G13 — Chat Archive relation
Chat Archive is storage infrastructure and separate namespace.

Effect:
Global C0 must not merge archive progress with E-Prime channel readiness.
