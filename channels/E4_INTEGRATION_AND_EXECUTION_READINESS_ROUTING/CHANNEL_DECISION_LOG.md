# Decision timeline

All decisions below distinguish the user's command/selection from the authorship of pasted artifacts.

| ID | Order / date | Question | Options actually evidenced | Selection / state | Provenance | Rationale | Later status |
|---|---|---|---|---|---|---|---|
| E4-DEC-001 | ORDER_KNOWN_TIME_UNKNOWN | What contract governs E4? | v1.1 supplied contract vs unspecified behavior | User: "Работать строго по контракту Е4!!" | DIRECT_USER_MESSAGE / AUTHOR_DECISION | Explicit reason not stated | SUPERSEDED by later v2.1 as strongest-known contract |
| E4-DEC-002 | v1.1 | May E4 rewrite E3/D3 or execute runtime? | rewrite/execute vs synthesis-only | synthesis without upstream rewrite; no build/test/runtime/release | USER_SUPPLIED_ARTIFACT | Contract states reliability + no canon drift | Historical invariant, still ACTIVE in narrowed form |
| E4-DEC-003 | v1.1 | How are nodes organized? | unconstrained map vs forced-order lanes | CORE/AMPLIFIER/RESERVE/FROZEN | USER_SUPPLIED_ARTIFACT | Contracted governance | ACTIVE concept, semantics narrowed in v2.1 |
| E4-DEC-004 | 2026-02-18 transition | Can SIM route promote to canon/runtime? | promotion vs isolated SIM | no canon merge, no promotion, no runtime claims | USER_SUPPLIED_ARTIFACT + RECOVERED_PRIOR_CONTEXT | Explicit SIM hard blocks | HISTORICAL/TEMPORARY lane rule where SIM applies |
| E4-DEC-005 | v2.1 | Who binds truth? | E4 independent verification vs E0-only binder | E0 truth-binder only; E4 echo/equality only | USER_SUPPLIED_ARTIFACT | v2.1 policy explicitly rejects "second E0" | ACTIVE |
| E4-DEC-006 | v2.1 | May numeric scoring drive E4 decisions? | v1.1 score/weights vs gate/closure/trace | numeric axis banned as driver | USER_SUPPLIED_ARTIFACT | Explicit `E4_NUMERIC_AXIS_BAN_V1` | ACTIVE; reverses historical v1.1 decision mechanic |
| E4-DEC-007 | v2.1 | Does E5 choose among alternatives? | route portfolio/A-B-C vs single route | single recommended route; anti-choice | USER_SUPPLIED_ARTIFACT | E5 must not become architect | ACTIVE |
| E4-DEC-008 | v2.1 | What qualifies CORE? | broad readiness vs directly translatable actions | ACTIONABLE + action atoms + affordance refs + stop/verify/rollback/closure | USER_SUPPLIED_ARTIFACT | E5 improvisation ban | ACTIVE |
| E4-DEC-009 | latest recovered run | What happens when required upstream is absent? | guess/fill vs block/closure | BLOCK | ASSISTANT_OUTPUT aligned with v2.1 contract | Missing refs may not be invented | ACTIVE operational behavior |

## Reversals / material changes

### Numeric ranking authority
v1.1: explicit weighted scoring and threshold model.  
v2.1: numeric decision axis is P0-blocked.

Status: **REVERSED/SUPERSEDED**.

### Core source topology
v1.1: E3+D3 are the core synthesis pair.  
v2.1: E3 single production bundle + E2 maps + E1 skeleton + E0/D0/D1 are required; D3 is optional alignment.

Status: **SUPERSEDED topology**.

### Missing-input behavior
Early assistant executions acted as though complete maps could be emitted from partial evidence. Later SIM/v2.1 behavior blocks.

Status: **ASSISTANT_OPERATION CORRECTED**, not an owner-authored design reversal.

## Decisions with unknown rationale

The artifacts often state rules but not the author's personal reason for accepting them. Where no direct author rationale exists, the rationale remains `UNKNOWN`; assistant explanations are not substituted.
