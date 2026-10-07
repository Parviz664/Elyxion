# PRIMARY_ARTIFACT_REGISTER

## Evidence classes

AUTHOR_RAW
AUTHOR_CONFIRMED
AUTHOR_DECISION
USER_SUPPLIED_ARTIFACT
ASSISTANT_PROPOSAL
ASSISTANT_INTERPRETATION
JOINT_ITERATION
RECOVERED_FROM_LATER_REFERENCE
GITHUB_ARTIFACT
UNKNOWN_ORIGIN

## Artifact register

### ART-E1-001
artifact:
ELYX_E1_CHANNEL_SPEC_V1_0_MASTER

first recovered user-supplied timestamp:
2026-02-16 21:06:03Z

evidence_class:
USER_SUPPLIED_ARTIFACT

origin caveat:
a prior assistant generation around 21:04Z is also recovered; therefore line-by-line AUTHOR_RAW authorship is not claimed.

recovery status:
EXACT_VERSION_RECOVERED

### ART-E1-002
artifact:
ELYX_E1_CHANNEL_SPEC_V1_1_MASTER

evidence:
named only in v1.2 supersedes_artifact_type.

evidence_class:
RECOVERED_FROM_LATER_REFERENCE

recovery status:
REFERRED_TO_ONLY / CONTENT_NOT_RECOVERED

### ART-E1-003
artifact:
ELYX_E1_CHANNEL_SPEC_V1_2_MASTER

timestamp:
2026-02-17 21:37:07Z

evidence_class:
USER_SUPPLIED_ARTIFACT

recovery status:
EXACT_VERSION_RECOVERED

### ART-E1-004
artifact:
ELYX_E1_EXECUTION_RESULT_V1_2

timestamp:
2026-02-17 after author command to obey E1

evidence_class:
ASSISTANT_GENERATED_OUTPUT

recovery status:
EXACT_RESPONSE_RECOVERED

### ART-E1-005
artifact:
ELYX_E1_SIMULATION_LANE_CONSTRAINT_RESPONSE_V1_2

timestamp:
2026-02-18

evidence_class:
ASSISTANT_GENERATED_OUTPUT

recovery status:
EXACT_RESPONSE_RECOVERED

### ART-E1-006
artifact:
ELYX_E1_KERNEL_UPDATE_COMPAT_ACK_V1_2

timestamp:
2026-02-18

evidence_class:
ASSISTANT_GENERATED_OUTPUT

recovery status:
EXACT_RESPONSE_RECOVERED

### ART-E1-007
artifact:
ELYX_E1_CHANNEL_SPEC_V1_3_MASTER

timestamp:
2026-02-20 11:15:58Z

evidence_class:
USER_SUPPLIED_ARTIFACT

recovery status:
EXACT_VERSION_RECOVERED

### ART-E1-008
artifact:
ELYX_E1_CHANNEL_SPEC_AUDIT_RESULT_V1_3

evidence_class:
ASSISTANT_INTERPRETATION

recovery status:
RECOVERED

authority:
non-canonical unless owner adopts fixes.

### ART-E1-009
artifact:
ELYX_E1_CHANNEL_SPEC_V1_4_MASTER

internal patch date:
2026-03-03

re-supplied/recovered later:
yes

evidence_class:
USER_SUPPLIED_ARTIFACT

recovery status:
EXACT_VERSION_RECOVERED

### ART-E1-010
artifact:
ELYX_E1_CHANNEL_SPEC_AUDIT_RESULT_V1_4

evidence_class:
ASSISTANT_INTERPRETATION

recovery status:
RECOVERED

authority:
does not prove v1.4.1 existed.

### ART-E1-011
artifact:
ELYX_E1_CHANNEL_SPEC_V1_5_MASTER

timestamp:
2026-03-13 07:05:32Z

evidence_class:
USER_SUPPLIED_ARTIFACT / RECOVERED_FROM_PRIOR_CONVERSATION

recovery status:
EXACT_EXISTENCE + PARTIAL_CONTENT

### ART-E1-012
artifact:
ELYX_E1_CHANNEL_SPEC_V1_6_MASTER

timestamp:
2026-03-13 14:27:08Z

evidence_class:
USER_SUPPLIED_ARTIFACT / RECOVERED_FROM_PRIOR_CONVERSATION

recovery status:
EXACT_EXISTENCE + PARTIAL_CONTENT

## Negative GitHub evidence

Before this recovery:
- default branch code search returned no E1_CONSTRAINED_IMPLEMENTATION_THINKING_ENGINE;
- no E1_SKELETON_PACKET hit;
- no E1_EXECUTION_DRAFT_PACKET hit;
- branch search returned no dedicated E1 recovery branch.

This negative evidence does not prove E1 never existed elsewhere; it only proves it was not found in the searched GitHub surface.
