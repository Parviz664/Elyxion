# CHANNEL_PROVENANCE

## Classes

AUTHOR_RAW
AUTHOR_CONFIRMED
AUTHOR_DECISION
USER_SUPPLIED_ARTIFACT
ASSISTANT_PROPOSAL
ASSISTANT_INTERPRETATION
JOINT_ITERATION
RECOVERED_FROM_LATER_REFERENCE
GITHUB_ARTIFACT
UNKNOWN_ORIGIN

## Critical law

SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR.

The user pasted multiple large A3 JSON contracts.
Those are USER_SUPPLIED_ARTIFACT.
Their line-by-line original authorship is UNKNOWN unless separately established.

Operational adoption is stronger:
the user explicitly instructed this channel to work strictly by A3 contract and repeatedly supplied superseding contracts.
Therefore active-contract status is AUTHOR_CONFIRMED even where textual authorship is unknown.

## Highest-grade direct evidence

1. Current conversation: full user-supplied A3 v1.0, v1.1, v1.2, two v1.3 snapshots, v1.4 and v2.2.
2. Current conversation: actual assistant executions showing BLOCK/PASS_WITH_CONSTRAINTS behavior.
3. Recovered prior-user facts: dated route/version anchors.
4. GitHub: repository topology and absence of A3 docs on main before this recovery.
5. Later v2.2 references: proof of v2.0/v2.1 lineage, not full missing bodies.

## Author RAW recovered

Direct historical activation:
“Работать строго по контракту А3!”

Current archaeology request is also AUTHOR_RAW but is recovery instruction rather than historical channel-role content.

No earlier pre-v1.0 author wording is recovered with sufficient confidence.

## Assistant evidence

Assistant outputs are evidence of historical behavior and mistakes, not owner canon.

Example:
the early PASS_WITH_CONSTRAINTS after only A2 was supplied does not prove that v1.0 allowed missing E-Prime.

## Timestamp discipline

Generated created_at_utc values inside assistant packets are not independent timestamps.

Dates from recovered prior conversation context are labeled RECOVERED_FROM_LATER_REFERENCE unless exact raw is present.

## GitHub evidence

Before this recovery, searches on main for A3 law IDs/current identifiers returned no A3 channel artifacts.

Existing P0/P1/P3 recovery branches were used as structural precedent only. They are not A3 historical-content evidence.
