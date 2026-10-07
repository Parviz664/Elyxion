# CHANNEL_CONTRACT

## Current exact contract anchor

payload:
`ELYX_P4_SPEC_V3_2_2`

semver:
`3.2.2`

channel_id:
`ELYX_P4_FEEL_POTENTIAL_ENGINE_v3.2`

status in supplied artifact:
`active`

change_policy:
`append_only`

id_freeze:
true.

rollback:
`revert_to_last_passed_version`.

## Compatibility

Supplied 3.2.2 artifact states compatibility with:
- `ELYX_P4_INPUT_V3_1`;
- `ELYX_P4_INPUT_V3_2`.

Primary current inputs_contract payload is named:
`ELYX_P4_INPUT_V3_2_2`.

This recovery does not reinterpret that naming relationship.

Output:
`ELYX_P4_FILTER_SHORTLIST_PACKET_V3_2_2`.

## Hard constraints recovered

- no gameplay mechanics;
- no UI numbers as world system;
- no progression systems;
- no tech trees/catalogs;
- no formulas/world parameters;
- no lore injection;
- no species/factions/cultures;
- no personified observer;
- causal output;
- uncertainty must stay labeled;
- canon IDs only;
- strict P3 order;
- never rewrite candidate text;
- never invent items;
- dependency closure required;
- meta nodes excluded from spine by default;
- scores are editorial only;
- no score as truth;
- role discipline required;
- late bridge guard required;
- structural reasons required;
- terminal mass check required.

## Preflight

Recovered checks:
- B### candidate format;
- B### dependency format;
- dependency existence;
- no future dependency violation;
- source order monotonicity;
- banned-pattern scan.

Fail-fast is required.

## Selection engine current phase order

1. preflight validation;
2. candidate scoring;
3. dependency closure;
4. role tagging;
5. order-safe selection;
6. observables-first coverage repair;
7. no-guess duplicate trim;
8. late-bridge retention check;
9. meta trim / handoff pack.

## Scoring truth boundary

Weights/numbers:
- internal heuristic only;
- not player-visible;
- not a world model;
- not a simulation metric;
- not truth.

Tie-break order in current supplied contract prioritizes:
1. dependency function;
2. bridge necessity;
3. causal pressure;
4. causal click;
5. unknownness;
6. lower selected overlap;
7. earlier source index.

## Current route policy

If P5 disabled:
never recommend P5 by default.

Default next:
- P3 patch if problem is wording/observability sharpness;
- P2 expand if problem is bridge mass/support.

Other current next options:
- A_ULTRA;
- A0.

These options are route recommendations, not proof of automatic direct consumption.

## Owner boundary

Default:
`selection_mode = author_selects_ids_only`.

Interpretation supported by P Control Point recovery:
P4 may recommend/score/filter, but does not silently convert selection into owner canon.
