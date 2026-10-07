# CHANNEL_PROVENANCE

## Provenance law

SUPPLIED_BY_AUTHOR != AUTHORED_BY_AUTHOR.

A user-pasted JSON contract proves:
the author supplied that artifact in the conversation.

It does not prove:
the author personally wrote every line.

Therefore the full v3.1.1 and v3.2.0 specs are classified:
USER_SUPPLIED_ARTIFACT
with artifact_origin = UNKNOWN_OR_JOINT unless separately proven.

## Evidence classes used

AUTHOR_RAW
Direct user wording not merely pasted artifact text.

AUTHOR_CONFIRMED
Explicit user confirmation of a previously proposed element.

AUTHOR_DECISION
Explicit user selection among options or explicit freeze.

USER_SUPPLIED_ARTIFACT
Artifact supplied in a user message; authorship not inferred.

ASSISTANT_PROPOSAL
Assistant-generated proposed design or rationale.

ASSISTANT_INTERPRETATION
Assistant explanation not owner-confirmed as a decision.

JOINT_ITERATION
Only used where both sides' contribution is demonstrable.

RECOVERED_FROM_LATER_REFERENCE
Later artifact proves existence/reference but not full earlier content.

GITHUB_ARTIFACT
Durable repository evidence.

UNKNOWN_ORIGIN
Used when authorship cannot be established.

## Current-channel artifact provenance

### P3 v3.1.1 spec
supplied_by:
user.
artifact_origin:
UNKNOWN_OR_JOINT.
owner_acceptance_status:
strong working-contract evidence because it was supplied as active channel_spec and used downstream.
evidence_class:
USER_SUPPLIED_ARTIFACT.

### P3 v3.2.0 spec
supplied_by:
user.
artifact_origin:
UNKNOWN_OR_JOINT.
owner_acceptance_status:
strong working-contract evidence; explicitly supersedes 3.1.1 and is used by current execution.
evidence_class:
USER_SUPPLIED_ARTIFACT.

### P2 packets
supplied_by:
user.
artifact_origin:
UNKNOWN_OR_JOINT.
use_in_this_recovery:
practice/input evidence only, not proof of P3 authorship.

### actual P3 rendered output before this recovery
supplied_by:
assistant in current conversation.
artifact_origin:
ASSISTANT_OUTPUT.
use:
implementation-in-chat evidence, not owner-authored contract.

## Prior-conversation recovered direct user constraints

Recovered through personal-context retrieval:
- P3 = final_text_renderer_patch_safe.
- P2 does not finalize artistic text; P3 does.
- route P0 -> P1 -> P2 -> P3 -> P4 in March working state.
- strict realism / patch-safe / proof-block constraints.

These are classified:
RECOVERED_FROM_PRIOR_CONVERSATION.
Where exact byte-level transcript is unavailable in this branch, they are not promoted to immutable AUTHOR_RAW quote status without qualification.

## GitHub provenance

P3_CONTRACT_RECOVERY_PASS_V0_1.md:
GITHUB_ARTIFACT.
Commit:
d929e8e503ff, 2026-10-06T03:02:35Z.

P_SYSTEM_ROUTE_AUTHORITY_TIMELINE_V0_1.md:
GITHUB_ARTIFACT.

P_CHANNEL_REGISTRY_V0_2.yaml:
GITHUB_ARTIFACT.

SOURCE_PROVENANCE_CORRECTION_V0_1.md:
GITHUB_ARTIFACT.
It explicitly corrects earlier overclaim from owner-supplied to owner-authored.

## Provenance prohibitions

Never say:
- "the author wrote the whole v3.2 spec" unless proven;
- "assistant rationale is author rationale";
- "later v3.2 content existed in v3.1.0";
- "October recovery knew the full schema" when it explicitly did not;
- "P3 PASS means owner-confirmed canon".
