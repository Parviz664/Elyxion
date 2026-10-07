# Channel timeline

| Event | Time | Evidence | Before | Event / change | After | Status |
|---|---|---|---|---|---|---|
| T0 | 2026-02-17T20:35:19Z | RECOVERED_PRIOR_CONTEXT / USER_FACT | E4 origin not recovered | E4 ID and E3+D3 integration mission recorded | E4 exists as integration/readiness cartographer | RECOVERED_FACT |
| T1 | 2026-02-17T21:01:35Z | RECOVERED_PRIOR_CONTEXT / PRIOR_ASSISTANT_OUTPUT | early E4 | Assistant describes v1.1 additions: coverage proof, conflict topology, lanes, stress, rollback, trace | v1.1 feature set visible | ASSISTANT_EVIDENCE |
| T2 | ORDER_KNOWN_TIME_UNKNOWN | DIRECT current user message + USER_SUPPLIED_ARTIFACT | E4 v1.x | User says "Работать строго по контракту Е4!!" and supplies `ELYX_E4_CHANNEL_SPEC_V1_1_MASTER` | v1.1 is governing contract for that turn | AUTHOR_DECISION about strict use; artifact authorship UNKNOWN |
| T3 | ORDER_KNOWN_TIME_UNKNOWN | ASSISTANT_OUTPUT | exact v1.1 spec present | Assistant emits `E4_MAP_PACKET_V1_1` PWC-A with synthetic nodes/scores | candidate execution output exists | NON_CANON / OVERREACH |
| T4 | 2026-02-17T21:34:16Z | RECOVERED_PRIOR_CONTEXT / USER_FACT | E4 integrated locally | E0 v1.3 adds E4 as required sync target | E4 becomes explicit downstream target of E0 routing | RECOVERED_FACT |
| T5 | ORDER_KNOWN_TIME_UNKNOWN | DIRECT current user artifact | D3 available | User supplies canonical-bootstrap D3 v1.1 | E4 has stronger D3 evidence | USER_SUPPLIED_ARTIFACT |
| T6 | ORDER_KNOWN_TIME_UNKNOWN | ASSISTANT_OUTPUT | D3 canonical packet present | Assistant emits E4 PWC-B map | still not fully grounded in complete required sources | NON_CANON |
| T7 | 2026-02-18T09:35:16Z | RECOVERED_PRIOR_CONTEXT / USER_FACT | bootstrap route | Stack transitions to SIMULATION_ONLY: no canon promotion, no runtime claims | E4 route inherits SIM isolation | RECOVERED_FACT |
| T8 | ORDER_KNOWN_TIME_UNKNOWN | DIRECT current user artifact | SIM route active | User supplies D3(SIM) with non-canon/no-merge locks | E4 must respect SIM-only boundary | USER_SUPPLIED_ARTIFACT |
| T9 | ORDER_KNOWN_TIME_UNKNOWN | ASSISTANT_OUTPUT | only D3(SIM) present | E4 returns BLOCK for missing full upstream | fail-closed behavior becomes visible | CORRECTION |
| T10 | BEFORE/AT 2026-03-03, exact time unknown | USER_SUPPLIED_ARTIFACT v2.1 metadata | v1.x lineage; v2.0 existed | v2.1 says it supersedes `ELYX_E4_CHANNEL_SPEC_V2_0_MASTER` | v2.0 existence proven, body absent | REFERRED_TO_ONLY |
| T11 | artifact patch id contains 20260303-02 | USER_SUPPLIED_ARTIFACT | v2.0 predecessor | v2.1 Route-Compiler master supplied | E4 authority narrowed/recomposed | EXACT_VERSION_RECOVERED |
| T12 | ORDER_KNOWN_TIME_UNKNOWN | ASSISTANT_OUTPUT | v2.1 current | Missing upstream causes block and closure list | E4 run remains not handoff-ready | CURRENT EXECUTION EVIDENCE |
| T13 | 2026-10-07 | GITHUB_ARTIFACT | repo had no E4 recovery docs found on main | Recovery branch created | durable recovery starts without rewriting main | IMPLEMENTATION |

## Timestamp rule

Dates embedded in artifact IDs are treated as artifact metadata, not silently upgraded to exact conversation timestamps. Where exact chat time is unavailable, this file uses `ORDER_KNOWN_TIME_UNKNOWN`.
