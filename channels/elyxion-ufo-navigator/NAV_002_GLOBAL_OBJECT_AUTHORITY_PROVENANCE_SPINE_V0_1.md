# NAV-002 — Global Object / Authority / Provenance Spine V0.1

**Status:** CANDIDATE  
**Authority:** NAVIGATION-ONLY  
**Canon authority:** NONE  
**Execution authority:** NONE  
**Global C0 authority:** NONE  
**Repository:** `Parviz664/Elyxion`  
**Branch:** `channel/elyxion-ufo-navigator-v0.1`

## Why NAV-002 exists

NAV-001 answered the first repository-level question:

> What GitHub-visible surfaces exist right now?

NAV-002 begins answering the harder future Global C0 question:

> What exactly is each thing, where did it come from, what authority does it have, what evidence supports it, what does it connect to, and what remains unknown?

The goal is not to load the whole of Elyxion into one giant prompt.

The goal is to make Elyxion **addressable, recoverable, evidence-linked, and safely traversable**.

## Core design law

**Global C0 must not depend on remembering all of Elyxion. It must be able to recover the correct part of Elyxion from durable, typed, provenance-linked objects.**

The intended recovery ladder is:

```text
GLOBAL MAP
   ↓
OBJECT REGISTRY
   ↓
OBJECT RECORD
   ↓
RELATION / AUTHORITY / STATUS
   ↓
EVIDENCE POINTER
   ↓
SOURCE ARTIFACT
   ↓
RAW SOURCE when available
```

Every higher layer must remain traceable downward.

## Critical separation of axes

A single overloaded `status` field is forbidden as the long-term model.

NAV-002 separates at least four axes:

### 1. Semantic / lifecycle status
What kind of state the object itself is in.

Candidate values begin with:
- RAW
- CANDIDATE
- CANON
- EXPERIMENTAL
- FROZEN
- DEPRECATED
- UNKNOWN

This vocabulary remains extensible. Use only evidence-supported values.

### 2. Evidence state
How strongly the Navigator has actually observed the object.

Candidate values:
- DIRECTLY_OBSERVED
- REFERENCED_NOT_INSPECTED
- NOT_OBSERVED
- UNKNOWN

### 3. Authority
What this object or surface is allowed to decide or do.

Authority must be explicit and typed. Unknown authority stays UNKNOWN.

Examples of authority dimensions:
- navigation
- canon
- execution
- archive
- routing
- implementation
- author_selection

An object can have authority in one dimension and none in another.

### 4. Readiness
Whether an object is usable for its next intended handoff.

Candidate values:
- READY
- PARTIAL
- BLOCKED
- HOLD
- NOT_APPLICABLE
- UNKNOWN

These axes must never be silently collapsed into one another.

## Object model

Every Navigator object should eventually expose:

- `id`
- `object_type`
- `title`
- `locations`
- `semantic_status`
- `evidence_state`
- `authority`
- `readiness`
- `provenance`
- `relations`
- `blockers`
- `conflicts`
- `unknowns`
- `evidence`
- `last_verified`

Optional future fields may include:
- aliases
- version
- parent
- children
- owner
- handoff_contract
- supersedes
- superseded_by
- freshness_policy
- verification_tests

The schema is intentionally versioned. V0.1 is not frozen canon.

## Object types

Initial candidate object types:

- REPOSITORY
- BRANCH
- CHANNEL
- ARTIFACT
- CONTRACT
- DECISION
- HANDOFF
- CONCEPT
- IMPLEMENTATION_SURFACE
- ARCHIVE_SURFACE
- FRONTIER
- TEST
- UNKNOWN_OBJECT

These types describe navigation objects, not gameplay ontology.

## Provenance law

Every non-trivial claim should be able to answer:

1. **Where was this observed?**
2. **What exact artifact supports it?**
3. **Was it directly stated or inferred?**
4. **Who/what had authority at that point?**
5. **What is still unknown?**

Inference must be marked as inference.

Absence of evidence must never be converted into non-existence.

## Authority law

Navigator may record authority but may not grant itself authority.

For any object:

```text
authority.claimed
authority.evidence
authority.scope
```

must be distinguishable.

A future C0 must not infer canon authority from:
- branch ownership;
- implementation existence;
- document polish;
- test coverage;
- recency;
- Navigator classification.

## Relation law

Relationships are first-class objects/edges, not prose assumptions.

Initial relation kinds may include:

- CONTAINS
- REFERENCES
- DERIVED_FROM
- IMPLEMENTS
- ARCHIVES
- ROUTES_TO
- HANDS_OFF_TO
- DEPENDS_ON
- SUPERSEDES
- CONFLICTS_WITH
- UNKNOWN_RELATION

A relation may exist with `confidence = UNKNOWN` only if the uncertainty itself is useful and explicitly represented.

No relation is created merely because two artifacts look similar.

## Query / recovery model for future Global C0

Global C0 should recover information progressively:

### Level 0 — Global orientation
"What systems exist and where?"

### Level 1 — Object selection
"Which objects are relevant to this question?"

### Level 2 — Authority + status
"What can each object legitimately tell me?"

### Level 3 — Relation traversal
"What upstream/downstream objects matter?"

### Level 4 — Evidence drill-down
"What exact files/records support the answer?"

### Level 5 — RAW drill-down
"When fidelity matters, recover the raw source rather than trusting summaries."

This prevents the entire project from needing to fit in a single context window.

## Anti-collapse invariants

1. RAW never becomes CANON through Navigator classification.
2. CANDIDATE never becomes CANON without explicit author/canon authority evidence.
3. IMPLEMENTED does not imply CANON.
4. TESTED does not imply CANON.
5. RECENT does not imply authoritative.
6. ABSENT_FROM_GITHUB does not imply DOES_NOT_EXIST.
7. Similar names do not prove identity.
8. Similar functions do not prove lineage.
9. A summary does not replace a raw source when raw fidelity is required.
10. UNKNOWN must survive traversal without being auto-filled.
11. Authority must be scoped.
12. Every Global C0 answer should be able to descend to evidence for material claims.

## V0.1 implementation scope

NAV-002 V0.1 will implement only the infrastructure needed to represent the currently observed NAV-001 surfaces safely.

IN:
- machine-readable object schema;
- machine-readable object registry;
- explicit authority/status/readiness separation;
- evidence pointers;
- relation representation;
- validator for structural invariants;
- frontier tracking.

OUT:
- importing all historical chats;
- inventing A/E channel objects not yet recovered;
- declaring project-wide completeness;
- building Global C0 itself;
- gameplay canon decisions;
- resolving P route disputes.

## Initial seed objects

The first registry is allowed to contain only objects directly supported by NAV-001 evidence:

- `main`
- `E-Prime`
- `agent/phase1-scaffold`
- `channel/p-control-point-v0.1`
- `channel/elyxion-ufo-navigator-v0.1`

Unknown A/E/0.0.1.x/Global-C0 surfaces remain represented as unresolved discovery targets rather than fabricated objects.

## NAV-002 success condition

NAV-002 V0.1 is successful when:

- a schema exists;
- a registry exists;
- all five currently observed surfaces can be represented without semantic collapse;
- evidence pointers are present;
- authority is explicit or UNKNOWN;
- unresolved discovery targets remain unresolved;
- a validator can reject structural violations;
- no object is promoted to CANON by the Navigator.

This is not a claim that Elyxion is globally mapped.

It is the first durable substrate from which global mapping can safely grow.
