# CHANNEL_PROVENANCE

## Law

SUPPLIED_BY_AUTHOR != AUTHORED_BY_AUTHOR.

The v1.0-v1.4 JSON artifacts were supplied in user messages.
That proves they were intentionally put into the channel and used as working artifacts.
It does not prove who originally drafted every field.

ASSISTANT_RATIONALE != AUTHOR_RATIONALE.

Chronological proximity is not enough to infer motive.

## Evidence classes

AUTHOR_RAW
Direct user wording.

AUTHOR_CONFIRMED
Explicit confirmation of a previously proposed element.

AUTHOR_DECISION
Explicit user instruction/selection.

USER_SUPPLIED_ARTIFACT
Artifact pasted by user; authorship not inferred.

ASSISTANT_PROPOSAL
Assistant-generated proposed change/design.

ASSISTANT_INTERPRETATION
Assistant explanation not owner-confirmed.

JOINT_ITERATION
Only where contribution from both sides is demonstrable.

RECOVERED_FROM_LATER_REFERENCE
Later material proves an earlier element existed but not its full body.

GITHUB_ARTIFACT
Durable repository evidence.

UNKNOWN_ORIGIN
Origin not established.

## Provenance assignments

### Birth command

“хорошо сделай этот Е3.5”
class:
AUTHOR_RAW / AUTHOR_DECISION.
source:
prior-conversation recovery.
timestamp:
2026-02-18T10:16:05Z.

### Strict contract command

“Работать строго по контракту Е3.5!!!”
class:
AUTHOR_RAW / AUTHOR_DECISION.
source:
current conversation.

### v1.0-v1.4 specs

class:
USER_SUPPLIED_ARTIFACT.

artifact_origin:
UNKNOWN_OR_JOINT unless separately proven.

working authority:
strong for reconstructing what the channel was instructed to use at those moments.

### assistant executions

class:
ASSISTANT_OUTPUT.

Use:
evidence of actual in-chat channel behavior, including mistakes.

Never treat an assistant PASS/BLOCK as proof the user's contract itself changed.

### v1.4 review and v1.4.1 patch set

class:
ASSISTANT_PROPOSAL.

owner acceptance:
not recovered.

### E-Prime Packet Registry relationship

class:
RECOVERED_FROM_PRIOR_CONVERSATION / assistant-generated upstream integration artifact.

Use:
historical topology evidence only.

### A2 E3.5-ready export relationship

class:
RECOVERED user-supplied A2 artifact + prior assistant output.

Use:
strong evidence of A2 -> E3.5 interface expectation.

## Evidence strength order used in this recovery

1. exact current-chat user wording;
2. exact current-chat user-supplied artifacts;
3. recovered earlier exact user wording with timestamp;
4. recovered earlier structured artifact facts;
5. GitHub durable state;
6. assistant outputs as behavior/history evidence;
7. inference, explicitly labeled.

## Prohibitions

Do not say:
- the user authored every JSON field;
- v1.4.1 is accepted;
- 10/10 coverage ever passed unless a real PASS artifact is recovered;
- assistant-generated refs prove the source packets existed;
- a later version's field existed in an older version unless directly recovered;
- E3.5 owns E4 conflict/safety decisions.
