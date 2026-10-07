# CHANNEL_ERROR_CORRECTION_LOG

## ERR-A3-001 — early evidence overclaim

Historical assistant behavior:
after an A2 payload was supplied under the v1.0-era contract, PASS_WITH_CONSTRAINTS was emitted although the independent E-Prime packet and cryptographic proof were absent.

Recovery classification:
ASSISTANT_INTERPRETATION / execution error evidence, not owner canon.

Later v1.1 behavior:
one sealed A2+E-Prime bundle became mandatory and missing proof caused BLOCK.

Direct causal claim that v1.1 was created because of this exact execution is UNKNOWN.

## ERR-A3-002 — hash friction

v1.2 explicitly moved SHA-256 computation into A3 when raw payloads were available.
Artifact change-intent describes operator-friction reduction.

## ERR-A3-003 — E-Prime role reversal

v1.0–v1.2:
E-Prime lock validation inside A3.

v1.3 onward:
E-Prime forbidden in A3; later bound in E0 from E6/E-lane.

This is a real architectural reversal.

## ERR-A3-004 — first v1.3 numeric inconsistency

First v1.3 artifact contains both:
guarantee_percent = 99.9
and
dream_loss_probability_percent = 0.00001.

They are not mathematical complements.

The later same-semver v1.3 snapshot changes to a bounded fidelity-cap model and explicitly avoids an absolute 100% promise.

## ERR-A3-005 — same-semver version drift

Two materially different v1.3.0 artifacts exist.

No historical semver repair was recovered.
Both snapshots are preserved separately.

## ERR-A3-006 — strict one-root behavior

v1.4 BLOCKed a V7 submission containing JSON plus external prose.

This follows the one-root/no-free-text contract and is preserved as a UX/strictness event, not a semantic rejection of V7.

## ERR-A3-007 — possible v2.2 legacy-class tension

A later assistant execution assigned planning_only / blocked_carrier_only / not_bind_ready to a legacy A2 carrier because adult A2 basis blocks were missing.

v2.2 simultaneously forbids A3 from re-judging lawful status.

Whether that conservative classification was fully lawful normalization or role overreach is UNKNOWN.
It must not be promoted to owner verdict.

## ERR-A3-008 — timestamp evidence risk

created_at_utc values generated inside assistant packets are not treated as independent chronology evidence.
