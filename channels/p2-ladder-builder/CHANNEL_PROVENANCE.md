# CHANNEL_PROVENANCE

## Provenance law

`SUPPLIED_BY_AUTHOR != NECESSARILY AUTHORED_BY_AUTHOR`.

A pasted contract is recorded as `USER_SUPPLIED_ARTIFACT` unless authorship is independently proved.

`ASSISTANT_RATIONALE != AUTHOR_RATIONALE`.

If the author did not state why a version/decision changed:
`reason = UNKNOWN`.

## Evidence classes used here

### AUTHOR_RAW
Direct user prose.
Examples:
- current: `Работать строго в режиме П2!!!`
- 2026-03-11: `Полный путь B001→B019 ощущается как неделимая причинная лестница, а не как набор заменяемых эпизодов.`
- current recovery law: `История канала является частью архитектуры канала.`

### USER_SUPPLIED_ARTIFACT
Pasted specs/packets:
- ELYX_P2_SPEC_V3_2_1;
- ELYX_P2_SPEC_V3_3_0;
- recovered/supplied v3.4 artifact;
- ELYX_P2_SPEC_V3_5_0;
- P1 packets used as P2 inputs.

Authorship of their exact wording is not assumed.

### ASSISTANT_EXECUTION
Generated ladder packets, diagnostics and prior interpretations.
Useful as practice evidence, lower authority than contract/source.

### GITHUB_ARTIFACT
Durable neighbor/control recovery:
- channel/p-control-point-v0.1;
- channel/p1-map-planner-recovery-v0.1;
- channel/p3-final-text-renderer-recovery-v0.1.

### RECOVERED_FROM_LATER_REFERENCE
Used when later versions prove predecessor existence but not content.

## Source refs

GITHUB:
- channels/p-control-point/P_SYSTEM_ROUTE_AUTHORITY_TIMELINE_V0_1.md
- channels/p-control-point/P_CHAIN_ROLE_SPINE_CROSSCHECK_V0_1.md
- channels/p-control-point/P_CHANNEL_REGISTRY_V0_2.yaml
- P1 CHANNEL_ROUTE_HISTORY / INTERFACE_MAP / VERSION_LINEAGE / HISTORY
- P3 CHANNEL_ROUTE_HISTORY / INTERFACE_MAP / VERSION_LINEAGE / HISTORY

CHAT:
- 2026-03-05T08:07:14Z P2 v3.2.1 supplied artifact
- 2026-03-06T14:21:48Z P2 v3.3.0 supplied artifact
- 2026-03-06 v3.4.0 recovered supplied artifact context
- 2026-03-06T20:09:46Z P2 v3.5.0 supplied artifact
- current conversation full v3.5 re-supply and strict-P2 instruction

## Evidence ceiling

No claim in this recovery should exceed the class above.
Inferences are labeled and never promoted to recovered fact.
