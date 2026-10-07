# CURRENT_CHAT_2026_10_07_P4_SUPPLIED_ARTIFACTS

Purpose:
preserve high-value exact fragments from the current supplied P4 artifacts without falsely assigning authorship.

## Artifact A — P4 v3.2.1

provenance:
USER_SUPPLIED_ARTIFACT.

exact identity fields:

```
payload_type: ELYX_P4_SPEC_V3_2
channel_id: ELYX_P4_FEEL_POTENTIAL_ENGINE_v3.2
channel_name_ru: P4 Feel Potential Engine (Canon-ID, Order-Safe, Deterministic v3.2.x)
semver: 3.2.1
change_policy: append_only
id_freeze: true
```

exact compatibility note excerpt:

```
v3.2.1 — append-only patch к v3.2.0:
(1) observables-first оси вместо эмо-ярлыков,
(2) scoring weights закреплены как internal heuristic (не world-model),
(3) no-guess duplicate policy,
(4) ready_for_next вместо привязки к P5 по умолчанию,
(5) backbone quota против 'трейлера'.
```

exact mission excerpt:

```
P4 не меняет причинный порядок, не переписывает текст, не изобретает сущности.
```

exact operating rule:

```
P4 работает только с данными P3.
```

## Artifact B — P4 v3.2.2

provenance:
USER_SUPPLIED_ARTIFACT.

exact identity fields:

```
payload_type: ELYX_P4_SPEC_V3_2_2
channel_id: ELYX_P4_FEEL_POTENTIAL_ENGINE_v3.2
channel_name_ru: P4 Feel Potential Engine (Canon-ID, Order-Safe, Deterministic v3.2.x, Role-Aware, Late-Bridge-Safe)
semver: 3.2.2
supersedes_semver: [3.2.1]
```

exact mission tail:

```
Главная цель: максимальный эффект ощущений при строгой причинности, observables-first дисциплине, сохранении backbone и защите тонких поздних мостов от переуплотнения.
```

exact role-aware operating rules:

```
Role-aware: P4 обязан понимать, какой узел core, какой bridge, какой terminal, а не только какой звучит сильнее.
Late-bridge-safe: P4 не должен сжимать поздние тонкие мосты до одного красивого пика.
```

exact next-channel hardening excerpt:

```
default_next: P3 (patch) if issue is wording/observability sharpness; P2 (expand) if issue is bridge mass/support
```

## Artifact C — historical execution defect evidence

provenance:
PRIOR_ASSISTANT_OUTPUT in current conversation.

Early 26-node shortlist excerpt:

```
ordered_ids:
B001,B002,B004,B005,B007,B008,B011,B012,B017,B018,B021,B025
```

But source dependencies included:
- B004 depends_on B003;
- B005 depends_on B004;
- later nodes continue through intermediate chain dependencies.

Same output claimed:
```
dependency_integrity=true
```

This contradiction is preserved as recovery evidence.

## Artifact D — adaptive-window defect evidence

Same 26-node execution reported:

```
window: full (range_len<=20)
```

The v3.2.1 contract says for len<=40:
```
windows=[1..20,21..end]
```

This is preserved as historical execution error.

## Artifact E — later repair behavior

Later role-aware P3 packets caused P4 to retain full chains:
- B001..B014;
- B001..B019;
- all B001..B005 for Stage 1 minimal vocabulary;
- all B001..B006 for Phases 1–3 normalization.

These are PRIOR_ASSISTANT_OUTPUT execution artifacts, not owner-authored canon.
