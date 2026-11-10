# NAV — Cross-Shaft Presence/Absence and Cell Phase Count Contract V0.1

**Status:** CANDIDATE / NAVIGATION-ONLY / NOT CANON / NO EXECUTION AUTHORITY
**Project scope:** Elyxion / Cell Stage. External projects including WhiteLine remain independent.
**Purpose:** Make independently sourced Elyxion shafts jointly queryable without fusing their authorial authority, and allow an evidence-bounded assessment of how many playable phases the cell stage actually needs.

## 1. Unification is an index, not a forced pipeline

Each shaft preserves its own source, branch, owner, version/era, lifecycle status, and authority ceiling. Navigator indexes objects, claims, relations, explicit absence constraints, unknowns and conflicts.

Conceptual path:

`RAW author intent -> preservation -> separately evidenced P/A/E/D + gameplay artifacts -> shared evidence graph -> phase-boundary assessment -> creator decision -> separately authorized canon/implementation`

This does **not** assert a mandatory execution order P->A->E->D. Nor does Navigator build or impersonate the already-existing Global C0.

## 2. Epistemic states

Every proposition must carry a **scope** and a **source**.

- `PRESENT_DOCUMENTED`: a positive assertion supported by an exact named source.
- `PRESENT_AUTHOR_DECLARED`: creator stated it; whether implemented remains separate.
- `EXPLICITLY_ABSENT_OR_FORBIDDEN`: source positively forbids or states absence **within its named scope**.
- `NOT_OBSERVED_IN_SCOPED_SEARCH`: search did not find evidence. This is **not** proof of absence.
- `UNKNOWN`: no justified conclusion yet.
- `CONFLICTING_EVIDENCE`: observations disagree; neither is silently selected.
- `CONDITIONAL`: relation or capability requires explicit condition.
- `HISTORICAL`: supported for a named earlier era/version.
- `CANDIDATE`: reversible research hypothesis, not canon.

No 'unknown = absent' inference; no 'not in GitHub = does not exist' inference; no 'absence of evidence = prohibition' inference.

## 3. Cross-shaft claim record (minimum)

`claim_id, object_id, project_id, source_locator, source_version_or_era, asserted_fact_or_absence, epistemic_state, scope, exact_evidence_refs, evidence_freshness, relation_to_other_claims, authority_ceiling, open_unknowns, supersession_or_condition`.

New cross-shaft links require evidence at the endpoints as appropriate. Local edges must not silently compose into a global route. Explicit absence may block a proposed transition **only if its scope applies**.

## 4. What counts as a Cell Stage phase?

A **playable phase** is not automatically a membrane mode, severity value, animation beat, subsystem, or numerical progression level.

For each proposed phase require:

1. `entry_trigger` — what changes to begin it;
2. `player_agency` — what the player can decide/do;
3. `new_causal_capability_or_constraint` — what is meaningfully different;
4. `persistent_consequence` — what carries forward;
5. `exit_or_transition_contract` — what leads to the next phase;
6. `evidence_and_epistemic_state` — what is creator-established vs candidate;
7. `failure_modes_and_test` — how the distinction could be falsified in prototype/playtest.

Do not count a new phase simply because a new file, animation, particle type, enemy or label appears. Distinct changes can occur within a single phase.

## 5. Current evidence ceiling

Direct repository source:

`agent/phase1-scaffold:docs/canon/phase-1-canon-map.md`

It documents the Phase 1 causal spine:

`manual breathing/rhythm -> stability -> timed membrane intake -> mixed friendly/hostile particles -> overload -> recovery -> delayed friendly activation -> partial automation -> Phase 2 entry`

It establishes the Phase 1 -> Phase 2 transition, **not a final numeric total for every phase in Cell Stage**.

The canon map separately lists:

- three membrane life modes (`Stable`, `Evolving`, `Deteriorating/Destroying`);
- five overload severity categories;
- breathing mastery states.

These are **independent axes**, not evidence for three or five playable phases.

Long-run creator working context has referred to **five Cell Stage phases**. Preserve `5` as a **working target / CHAT_CONTEXT**, not as a repository-verified final phase count. Phases 2–5 must not be invented from this number.

Known:

- Phase 1 causal identity is directly documented.
- Phase 2 entry is explicitly referenced.
- Phase 2–5 detailed phase identity and exact exit boundaries are **NOT VERIFIED BY THE SOURCES READ HERE**.
- Final Cell Stage playable phase count remains **UNRESOLVED**, with working target `5`.

## 6. Counting procedure

`collect source-linked candidate phases -> deduplicate aliases by provenance -> compare each adjacent transition -> inspect explicit absences/conditions/conflicts -> group events that do not create a distinct playable phase -> report provisional count and confidence/evidence ceilings -> creator authorizes canonical count`

Output must have separate fields:

- `creator_working_target_count` (currently 5 based on chat context);
- `repository_verified_distinct_phase_count` (do not assign from a Phase 1-only spec);
- `explicitly_named_phase_entries` (Phase 1, Phase 2 entry);
- `candidate_phase_count`;
- `count_conflicts_and_unknowns`;
- `canonically_authorized_phase_count` (UNKNOWN until separately evidenced).

The pipeline must permit a result such as **five planned, one deeply documented, transition to two documented, final count unresolved** without treating that as failure.

## 7. First falsification cases

- No source for Phase 4 -> output UNKNOWN, not ABSENT.
- A source forbids instant Friendly help before recovery -> record scoped FORBIDDEN, not a missing mechanic.
- Three membrane modes -> do not infer three phases.
- Five overload severities -> do not infer five phases.
- Seven causal beats -> do not infer seven phases.
- A new prototype implements an enemy -> do not create a new canon phase.
- Different eras disagree about A/E routing -> preserve temporal tension, not a single route.
- WhiteLine unavailability -> must not block Elyxion Cell Stage progression.
- Existing Global C0 -> no reimplementation, authority assumption or invented handoff.

## 8. Next evidentiary frontier

Recover creator-backed phase identities and transition conditions for Cell Stage Phase 2 onward; keep all missing portions UNKNOWN until found. Evaluate whether the working five-phase partition covers all distinct player-capability transitions without artificial splitting or meaning loss.

**This is a navigation/research contract only. No phase was canonized or implemented by this artifact.**
