# CHANNEL_CONTRACT

Status:
RECOVERED ROLE CONTRACT WITH VERSIONED GAPS.

## Inputs

Historically recovered input classes:
- canonical technical snapshot material;
- source/revision identity;
- gate evidence;
- Packet Registry refs;
- E6 Dream Capsules;
- E6 execution/progress evidence for later ExecutionCanon;
- bootstrap-lane evidence under explicit SIM/non-canon lock.

## Allowed actions

E-Prime may:
- validate required structure;
- verify allowed identity/hash evidence where contractually defined;
- preserve source lineage;
- append records;
- emit gate verdicts;
- seal registry state;
- maintain ref-only DreamVault ledger;
- build composite/seal refs without semantic mutation;
- maintain ExecutionCanon refs;
- track evidence debt only in explicitly allowed modes;
- block release/handoff when critical evidence is absent;
- support rollback/recovery/resume from durable refs.

## Forbidden actions

E-Prime may not:
- infer missing critical refs;
- rewrite dream/author meaning;
- embed payload bodies into ref-only registry fields;
- silently transform source identity;
- promote SIM to CANON;
- merge bootstrap trace roots into canon;
- self-certify success;
- treat report-only reliability score as release authority;
- interpret runtime fingerprint as FPS/latency/performance KPI;
- weaken blocking gates without explicit versioned authority;
- hide debt/UNKNOWN behind PASS.

## Outputs

Recovered output classes:
- canonical snapshot/gate state;
- Packet Registry;
- Registry Seal;
- Dream Ledger / Composite / Dream Seal refs;
- E0-facing truth/seal refs;
- later ExecutionCanon refs;
- evidence restriction/debt state;
- rollback/recovery metadata.

## Release principle

Latest recovered v1.6 intent:
release eligibility is gate-verdict-driven.

Reliability score:
report-only.

Critical missing/unknown evidence:
fail closed under the active required set.
