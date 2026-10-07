# CHANNEL CONTRACT — CURRENT STRONGEST-KNOWN

Law:
`ELYX_A2_LAW_v1.6.2_FIDELITY_GUARANTEE_FEEL_ANCHORS_QUARANTINE_SPLIT_DV_OPTIONAL`

Status: CURRENT STRONGEST-KNOWN CONTRACTED LAW.
Historical wording source: USER_SUPPLIED_ARTIFACT; original authorship of every law sentence is not assumed.

## Input contract

- one upstream artifact only,
- no questions by default,
- no manual repair loop,
- resolve mode from A0/binding/A1/fallback,
- prefer canon-bearing source,
- do not invent missing DreamVault/root fields.

## Core transformation

Input canon-bearing statements
→ trace index
→ stable systems
→ typed dependencies
→ invariants
→ open questions/non-goals
→ domino guard
→ conflict report
→ compact handoff
→ proof/judge/quarantine/feel-anchor blocks
→ export packet.

## Delta policy

Allowed:
- ADD_SYSTEM
- ADD_DEPENDENCY
- ADD_INVARIANT
- ADD_OPEN_QUESTION
- TIGHTEN_SCOPE_OUT
- ADD_TRACE
- ADD_FEEL_ANCHOR_REF_ONLY

Forbidden:
- WEAKEN_INVARIANT
- REMOVE_INVARIANT
- RENAME_SYSTEM_ID
- ADD_MECHANIC
- ADD_LORE_CAUSE
- ADD_IMPLEMENTATION
- ADD_METRICS_UI_OBJECTIVES
- AUTO_RESOLVE_CONFLICT

## DreamVault

Present:
- echo immutable ID/hash/ref,
- never rewrite/normalize raw author dream.

Missing:
- WARN,
- do not invent,
- do not set core_intent_preserved=false merely because it is missing,
- fidelity audit cap is limited.

## Fidelity model

Policy cap, not measured accuracy.

Recovered caps:
- 99.9 maximum when all listed conditions are met and DreamVault is PRESENT,
- 97.0 when other conditions are met but DreamVault is missing,
- 92.0 when trace coverage is below 1,
- 85.0 under semantic suspicion or judge disagreement.

## Semantic judges

Contract requires two independent semantic judgments.

Strict rules:
- either judge forbidden shift => FAIL,
- disagreement => WARN + author_review_required,
- meaning-shift suspicion => WARN + author_review_required,
- beautification that may flatten meaning => suspicion unless trace-preserving proof exists.

Historical execution caveat:
No durable evidence currently proves that past outputs called two distinct model endpoints or independently seeded judges. Mechanism is CONTRACTED but not VERIFIED.

## Quarantine

v1.6.2 classes:
- LEAK_CANON_RISK
- IMPLEMENTATION_VOCAB
- UNKNOWN_LEAK_RISK

Quarantine is preservation outside the clean main map, not deletion and not canon promotion.

## Feel anchors

REF-ONLY:
- exact substring/quote from canon-bearing source,
- trace-bound,
- no paraphrase,
- no "better wording".

## Export

On PASS/WARN:
- emit exact `A2_SYSTEMS_MAP_V4`,
- emit E3.5 manifest with explicit refs,
- emit A3 handoff reference,
- no substitute payload.

## Unresolved contract tension

The anti-leak token list includes terms that can also occur inside source-grounded negative constraints.
The law says token-hit generated statements are quarantined and the main map stays clean.
Historical assistant outputs sometimes kept such negative constraints in the main map while claiming the leak gate passed.

No recovered exception resolves this.
Status: OPEN_GAP, do not silently normalize.
