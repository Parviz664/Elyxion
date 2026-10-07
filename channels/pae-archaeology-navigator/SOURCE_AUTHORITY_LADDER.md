# SOURCE_AUTHORITY_LADDER

PAE explanations must be built from an explicit evidence hierarchy.

## Level 1 — strongest direct evidence

1. exact author RAW in the relevant channel;
2. explicit author decision/correction;
3. exact user-supplied historical artifact, with authorship caveat;
4. durable GitHub artifact containing primary recovered contract/history.

## Level 2 — strong reconstructed evidence

5. channel self-recovery report backed by evidence index;
6. channel timeline/version lineage with preserved UNKNOWNs;
7. cross-channel artifact that explicitly references/supersedes another channel/version.

## Level 3 — bounded interpretive evidence

8. assistant execution/error logs;
9. recovery summaries;
10. architectural inference that is clearly labeled INFERRED.

## Forbidden upgrade

No Level 3 item may silently become AUTHOR_DECISION or CURRENT_GLOBAL_TRUTH.

## Required claim labels

Use where material:

FACT
DOCUMENTED
OWNER_CONFIRMED
HISTORICAL
SUPERSEDED
CURRENT_LOCAL
CURRENT_GLOBAL_ONLY_IF_AUTHORIZED
HOLD
INFERRED
CANDIDATE
UNKNOWN
EMOTIONAL_LANGUAGE

## Supplied-artifact law

SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR.

## Local/global law

LATEST_IN_CHANNEL != CURRENT_GLOBAL.

A local recovery channel can truthfully report its own latest known state while still lacking later decisions from another channel.

## Missing-evidence law

If exact evidence is absent:
UNKNOWN.

Do not reconstruct a missing version from a later version unless the task explicitly asks for a hypothesis, and then label it HYPOTHESIS.
