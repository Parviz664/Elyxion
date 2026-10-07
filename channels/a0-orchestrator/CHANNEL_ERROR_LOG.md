# CHANNEL_ERROR_LOG — A0_ORCHESTRATOR

Errors are preserved as historical evidence. An assistant execution mistake is not the same thing as a defect in the supplied law.

## ERR-A0-001 — early amplifier lost independent-variant form

Era: early A0 Meaning Amplifier, recovered later in 2026-08 discussion.

Observed later audit: a requested set of 30 independent variants had collapsed toward one multi-point design document.

Recovery consequence:
- generator is not an executor;
- exact-30 and independence became explicit guards;
- this belongs to the early Meaning Amplifier namespace, whose direct lineage to A0_ORCHESTRATOR remains UNKNOWN.

## ERR-A0-100 — v2.2 execution did not provide real SHA-256 evidence

The v2.2 supplied law says deterministic patching plus hash evidence is mandatory and names sha256_before / sha256_after in its fingerprint.

Assistant executions returned values such as:
`not_computed_in_chat_context`

That is not a SHA-256 digest.

Verdict: IMPLEMENTATION NONCOMPLIANCE. The law itself remains preserved unchanged.

## ERR-A0-200 — false schema-collision warning during v3.0 validation

When v3.0 was first validated in this channel, the assistant warned that `copy_paste_payload_chunks` was blocked by `additionalProperties=false` because it was absent from `required`.

That warning was wrong:
- `copy_paste_payload_chunks` is explicitly declared in `properties`;
- a declared property may be optional;
- `additionalProperties=false` blocks undeclared properties, not optional declared ones.

Resulting invariant:
schema validation must distinguish ALLOWED from REQUIRED.

## ERR-A0-210 — source artifact identity contaminated by processor law

During a v3.0 P5 example, the source P5 artifact did not itself contain an A0 law ID, yet assistant output populated `law_id_if_present` with the active v3.0 A0 law.

That mixes:
- source-artifact identity;
- processor/runtime identity.

Repair rule:
active A0 law belongs in processing/source-trace metadata, not in a source field named "if present".

## AMB-A0-220 — canon_spec projection under-specified

Assistant executions wrapped P5 content inside a newly constructed `canon_spec` in CANON_BINDING_PACKET_V2.

The law simultaneously says:
- A0 may extract allowlisted canon-safe blocks into a binding packet;
- do not inject new canon fields.

For a P packet that has no existing `canon_spec`, the precise legal projection shape is not fully recovered.

Verdict: OPEN CONTRACT AMBIGUITY, not silently classified as valid or invalid.

## ERR/UNC-A0-230 — exact-looking metadata without demonstrated calculation

Some assistant examples emitted exact-looking `len_chars` values while admitting hashes were not computed.

This recovery cannot prove whether every length was actually calculated.

Status: UNCERTAIN IMPLEMENTATION EVIDENCE. Do not use those lengths as historical proof.

## Durable rule

Contract artifact, runtime execution, and later assistant explanation are three separate evidence layers. They must never overwrite each other.
