# CHANNEL_CONTRACT

Status: `RECOVERED_CONTRACT_FAMILY`

This document records the strongest common contract across recovered P0 versions. It does not erase version-specific differences.

## Stable contract

Input:
- author intent text;
- optional bounded overrides.

Transformation:
- normalize intent;
- mark assumptions/uncertainty;
- set or validate downstream routing inputs;
- preserve route discipline;
- do not become the downstream content generator.

Output:
- one structured artifact;
- JSON-only in recovered formal contracts;
- downstream packet(s);
- route and validation state.

## Stable prohibitions

Recovered across the formal family:
- no free world generation;
- no lore/personification invention;
- no magic invention;
- no code output;
- no fake certainty;
- no uncontrolled route mutation.

## v2.3 contract-specific route

`P0 -> -P1 -> P1 -> P2 -> P3 -> P4`

Includes:
`minus_p1_input`

## v2.4 contract-specific route

`P0 -> P1 -> P2 -> P3 -> P4`

Channel name explicitly includes `NO_-P1`.

`minus_p1_input` removed.

P5 disabled.

## v2.6 contract-specific additions

- `range_semantics = index_range` only;
- default first batch `1..80`;
- count hints live in `output_size_hint` / `target_step_count_hint`;
- invalid/legacy range semantics trigger auto-fix;
- auto-fix requires assumption + autopatch log;
- legacy range intent may be echoed read-only in `legacy_range_hint`;
- missing trace after auto-fix is failure.

## Supplied v2.7 output-level patch

Recovered only as a user-supplied output artifact.

Observed patch ideas:
- stale thematic scope may be treated as a legacy misroute when it directly contradicts raw author text;
- mechanics may be extracted at meaning/surface level while tutorial/UI walkthrough remains forbidden;
- `dream_loss_tolerance = ZERO_LOSS_REQUIRED`;
- `no_silent_fixes = true`.

Caution:
the supplied artifact's `autopatch_log` schema deviates from the v2.6 declared schema in some fields/enums, and its binding still points to v2.6.

Therefore status:
`WORKING_OUTPUT_PATCH / FORMAL_SPEC_NOT_RECOVERED`.
