# CHANNEL PROVENANCE

## Source classes

### P1 — Direct D1 conversation RAW
Highest available evidence for author commands.

Recovered examples:

- `AUTHOR_RAW`: "принимаете роль эту"
- `AUTHOR_RAW`: "Работать строго по контракту Д1!"
- `AUTHOR_RAW`: "История канала является частью архитектуры канала."
- the current full recovery instruction.

### P2 — User-supplied D1 artifacts
Exact text is available in the conversation, but original authorship is not assumed.

- `ELYX_D1_CHANNEL_SPEC_V2_1_MASTER`
- `ELYX_D1_CHANNEL_SPEC_V2_2_MASTER`
- `ELYX_D1_CHANNEL_SPEC_V2_4_MASTER`
- E1 handoff/simulation/kernel packets supplied to D1

Provenance label: `USER_SUPPLIED_ARTIFACT`.

### P3 — Prior-conversation recovery
Used to recover timestamps and existence facts not visible from the current turn metadata.

Key recovered timestamps:

- 2026-02-16T11:57:24Z — assistant D1 v2.0 artifact
- 2026-02-16T21:21:28Z — user supplies v2.1
- 2026-02-17T21:42:36Z — user supplies v2.2
- 2026-02-17T22:51:01Z — exact user command "Работать строго по контракту Д1!"
- 2026-02-18T09:40:40Z — simulation lane packet
- 2026-02-18T21:15:24Z — kernel compatibility packet
- 2026-02-26T20:08:21Z — user supplies v2.4

This source is weaker than direct RAW for semantic content.

### P4 — Later cross-channel references

Used only to prove relations/existence, never to synthesize missing D1 content.

Examples:

- D2 later requires `D1_GUARD_PACKET_V2_3_OR_HIGHER`;
- D2 v1.3 later references `D1_DLINE_ONLY_V2_4`;
- D3 v1.3 references D1 guard envelope in D-line-only routing;
- D4 v1.2 requires `D1_GUARD_PACKET_V2_4_DLINE_OR_HIGHER`.

### P5 — GitHub archaeology

Fresh repository findings on 2026-10-07:

- repository: `Parviz664/Elyxion`;
- default branch: `main`;
- code search on main for D1 master/id/seal terms returned no D1 hits;
- commit search for "D1" returned no hits;
- branch searches returned no D1 branch before this recovery;
- main contained `docs/channels/ECO-SYSTEMS-ELYXION.md`, but no D1 durable document;
- existing channel recovery branches (P0/P1/P3 etc.) demonstrate a separate `channels/` recovery pattern.

### P6 — Assistant outputs

Assistant release reports/ACKs are preserved as historical behavior, not automatically as channel truth.

They are specifically audited for schema drift, invented metrics, and enum violations in `CHANNEL_ERRORS_AND_CORRECTIONS.md`.

## Critical provenance rule

`USER_SUPPLIED_ARTIFACT != AUTHOR_RAW`

and

`ASSISTANT_RATIONALE != AUTHOR_RATIONALE`.

When an explicit reason is absent:

`reason_explicit = false`  
`reason = UNKNOWN`
