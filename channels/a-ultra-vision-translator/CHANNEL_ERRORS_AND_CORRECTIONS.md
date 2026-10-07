# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-AU-001 — law artifact treated as runtime vision payload

Observed:
when the v4.2 law itself was pasted, an assistant response processed it as `UNKNOWN_JSON` runtime input and emitted WARN.

Detection:
current archaeology.

Author correction:
NOT RECOVERED.

Repair:
not promoted to invariant; configuration-vs-runtime distinction remains a documented application gap.

## ERR-AU-002 — v4.3 unknown resolver initially applied as v4.2-style behavior

The supplied v4.3 law says:
- UNKNOWN_JSON → `hard_guard_with_dreamvault_only`
- RAW/UNKNOWN may keep DreamVault non-canon enabled.

But the assistant response immediately after the v4.3 law reported:
- mode `hard_guard`
- non_canon false.

This conflicts with the supplied v4.3 resolver.

Later behavioral repair:
a later direct P4-as-UNKNOWN run used `hard_guard_with_dreamvault_only` and non_canon true, matching v4.3 more closely.

Author correction:
not explicit.

Status:
`ASSISTANT_APPLICATION_ERROR → LATER_BEHAVIORAL_REPAIR`.

## ERR-AU-003 — P4 route advertised but not recognized

Observed:
P4 lists A_ULTRA as a next-channel option; v4.3 source types omit P4_PACKET.

Effect:
direct P4 is classified UNKNOWN_JSON and WARN.

Author correction:
not recovered.

Repair:
NONE. Preserved as GAP-AU-003.

## ERR-AU-004 — retroactive topology flattening risk

Wrong reconstruction would describe all history as `P → A_ULTRA → A0 → E0`.

Recovery correction:
preserve the earlier 2026-02-26/03-02 A0↔A_MINUS_1 gateway epoch separately.

Resulting recovery invariant:
routes are epoch-specific.
