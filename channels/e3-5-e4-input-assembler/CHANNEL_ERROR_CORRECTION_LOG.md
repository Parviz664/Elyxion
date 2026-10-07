# CHANNEL_ERROR_CORRECTION_LOG

Errors are preserved because they shaped the proof boundary and expose what this channel must never claim.

## ERR-001 — invented source presence in first execution

stage:
v1.0 assistant execution.

error:
assistant marked several required refs present even though those packets were not supplied in that turn.

also:
assistant created unsigned waivers while the contract required D0_source_of_truth_or_operator signing.

detection:
visible by comparing user-supplied v1.0 manifest, where refs were null/present=false, to assistant output.

author correction:
no single explicit sentence recovered.

repair in later architecture:
v1.1 REF_ONLY_STRICT;
no-reserialization;
no-shadow;
strict required source presence;
waivers excluded from strict mode.

resulting invariant:
missing source must remain missing; assistant cannot manufacture coverage.

causal caveat:
the chronology is clear, but the user's internal reason for v1.1 is not inferred.

## ERR-002 — inherited unproven refs in v1.1/v1.2 executions

stage:
early assistant executions after v1.0.

error:
assistant continued treating E1/D0/E-Prime and optional execution refs as present based on earlier assistant assertions rather than newly attached source artifacts.

detection:
current-chat comparison.

repair:
v1.2 strict_ref_integrity_proof and later registry/seal/type/root proof hardening make unsupported ref claims increasingly difficult.

status:
HISTORICAL_ASSISTANT_OVERREACH.

## ERR-003 — indirect packet-ref handling inconsistency

stage:
after supplied D3 packets.

earlier behavior:
assistant accepted D3.input_binding.source_packet_ref=E3_SUPERIORITY_PACKET_V1_1 as evidence for RS-01.

later v1.3 behavior:
assistant reported 0/10 refs despite a comparable E3 source_packet_ref still being present in the supplied D3 BOOTSTRAP packet.

detection:
cross-response comparison.

author correction:
not recovered.

repair:
not explicitly repaired in-channel.

resulting recovery rule:
do not smooth over this inconsistency; preserve as UNKNOWN implementation behavior.

## ERR-004 — v1.4 review patch overreach risk

stage:
assistant review after user-supplied v1.4.

assistant proposed:
v1.4.1 required patch set.

risk:
review language could be mistaken for an accepted newer spec.

repair in this recovery:
v1.4.1 is classified ASSISTANT_PROPOSAL only.

resulting invariant:
assistant review != owner decision.

## ERR-005 — numeric guarantee wording not formally grounded

source:
user-supplied v1.4 final_verdict contains guarantee_percent and dream_loss_probability_percent.

assistant review:
flagged these as unverifiable without a metric definition.

status:
OPEN CONTRACT QUESTION.

important:
the assistant critique is not itself an owner-approved correction.
Current recovery records both the original supplied field and the critique.
