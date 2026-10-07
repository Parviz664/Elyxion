# CHANNEL_PROVENANCE

## Provenance law

SUPPLIED_BY_AUTHOR != AUTHORED_BY_AUTHOR.

A JSON spec pasted by the user proves:
the user supplied/selected it for this channel conversation.

It does not prove:
the user personally authored every field.

ASSISTANT_RATIONALE != AUTHOR_RATIONALE.

## Evidence classes used

AUTHOR_RAW:
direct recovered user wording.

AUTHOR_CONFIRMED:
explicit user confirmation.

AUTHOR_DECISION:
explicit user selection/freeze.

USER_SUPPLIED_ARTIFACT:
artifact supplied in a user message; authorship not inferred.

ASSISTANT_PROPOSAL:
assistant-proposed structure/name/rationale.

ASSISTANT_INTERPRETATION:
assistant explanation not owner-confirmed as decision.

ASSISTANT_OUTPUT:
assistant-generated execution packet/result.

RECOVERED_FROM_PRIOR_CONVERSATION:
retrieved historical conversation evidence; lower ceiling than direct current transcript when byte-complete context is unavailable.

RECOVERED_FROM_LATER_REFERENCE:
later artifact proves existence of earlier item but not full earlier content.

GITHUB_ARTIFACT:
repository evidence.

UNKNOWN_ORIGIN:
authorship cannot be established.

## Source register

### SRC-RAW-001
Date:
2026-02-16 23:51:04Z.

Class:
AUTHOR_RAW recovered from prior conversation.

Content fragments:
"Теперь Д3 канал Берет и дополняет ни капли не изменяя содержимое Е3 оставляет его как есть…"
"…находит невозможные решения и от них делает улучшение через свой невозможный фильтр 60% улучшение…"
"…и умудряется даже еще углубиться еще вглубь чтобы на самые невероятные углубления наткнуться."

Confidence:
HIGH for quoted fragments; full surrounding message not archived here.

### SRC-AST-001
Date:
2026-02-16 23:51:05Z.

Class:
ASSISTANT_PROPOSAL.

Recovered phrase:
"канал экстремального глубинного дополнения".

### SRC-AST-002
Date:
2026-02-16 23:52:50Z.

Class:
ASSISTANT_OUTPUT.

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_0_MASTER.

Recovery:
partial.

### SRC-ART-001
Date:
2026-02-17 00:02:34Z recovered/current-conversation equivalent.

Class:
USER_SUPPLIED_ARTIFACT.

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_1_MASTER.

Exact current artifact:
available in channel conversation.

Authorship:
UNKNOWN_OR_JOINT.

### SRC-ART-002
Class:
USER_SUPPLIED_ARTIFACT.

Artifact:
ELYX_E3_EXECUTION_RESULT_V1_1 normal bootstrap.

Use:
historical D3 input evidence.

### SRC-OUT-001
Class:
ASSISTANT_OUTPUT.

Artifact:
initial generated D3_AUGMENTATION_PACKET_V1_1 emitted before upstream execution evidence.

Use:
ERROR_HISTORY, not verified evidence.

### SRC-OUT-002
Class:
ASSISTANT_OUTPUT.

Artifact:
ELYX_D3_EXECUTION_RESULT_V1_1 over supplied normal E3 result.

Use:
historical execution experiment only.

### SRC-ART-003 / SRC-OUT-003
Classes:
USER_SUPPLIED_ARTIFACT / ASSISTANT_OUTPUT.

Content:
SIMULATION_ONLY E3 input and D3 SIM result.

### SRC-ART-004 / SRC-OUT-004
Classes:
USER_SUPPLIED_ARTIFACT / ASSISTANT_OUTPUT.

Content:
REF_ONLY E3 input and D3 REF_ONLY result.

### SRC-ART-005
Class:
USER_SUPPLIED_ARTIFACT.

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_2_MASTER.

Exact:
yes in current conversation.

Authorship:
UNKNOWN_OR_JOINT.

### SRC-ART-006
Class:
USER_SUPPLIED_ARTIFACT.

Artifact:
ELYX_D3_CHANNEL_SPEC_V1_3_MASTER.

Exact:
yes in current conversation.

Authorship:
UNKNOWN_OR_JOINT.

Current strongest contract:
yes.

### SRC-GH-001
Class:
GITHUB_ARTIFACT.

Repository:
Parviz664/Elyxion.

Recovery date:
2026-10-07.

Observed main head at recovery start:
01b97c8edd19fdd59f81de827fb5f4a99861048f.

Search observations:
default-branch code searches for D3 identifiers returned no matches;
branch-name searches returned no D3 branch;
commit searches for D3/DLINE/latent superiority returned no matches.

Evidence ceiling:
bounded repository search, not proof that no detached/unindexed historical object could ever exist.

### SRC-GH-002
Class:
GITHUB_ARTIFACT.

Existing recovery branches:
p0/p1/p3 channel recovery branches demonstrated established repository pattern:
channels/<channel>/ identity/history/timeline/role/contract/boundary/version/decision/routes/interfaces/provenance/gaps/unknown/self-understanding + raw-evidence/recovery/tests.

Use:
format precedent only, not D3 semantic evidence.
