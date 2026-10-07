# CHANNEL_INTERFACE_MAP

## Upstream fan-in

### E3

required key:
E3_SUPERIORITY_PACKET.

historical minimum:
v1.0-v1.3 expected E3_SUPERIORITY_PACKET_V1_1.

v1.4 supplied minimum:
E3_SUPERIORITY_PACKET_V1_2.

note:
assistant later questioned whether this minimum was too high for observed producers.
That remains an unaccepted review finding.

### D3

required key:
D3_AUGMENTATION_PACKET.

same version caveat as E3 family.

### E2

required key:
E2_VARIANT_PACKET.

### D2

required key:
D2_ENHANCEMENT_PACKET.

### E1

required key:
E1_SIM_CONSTRAINTS.

v1.4 minimum:
ELYX_E1_SIMULATION_LANE_CONSTRAINT_RESPONSE_V1_2.

historical tension:
this key name still carries SIM language even when v1.3+ supports BOOTSTRAP dual-root mode.
No accepted replacement key is recovered.

### D1

required key:
D1_RELEASE_GATE_REPORT.

v1.4 minimum:
D1_RELEASE_GATE_REPORT_V2_2.

### D0

required key:
D0_ACK_PROCESSING_RESULT.

v1.4 minimum:
ELYX_D0_ACK_PROCESSING_RESULT_V1_1.

### E0

required key:
E0_DECISION_PACKET.

v1.4 minimum:
ELYX_E0_DECISION_PACKET_V1_3.

### E-Prime

required key:
EPRIME_SIMULATION_RESPONSE.

v1.4 minimum:
ELYX_EPRIME_SIMULATION_RESPONSE_V1.

separate integration:
E-Prime Packet Registry later becomes a ref-resolution helper for E3.5/E4.

### A2

required key:
A2_SYSTEMS_MAP.

v1.4 minimum:
A2_SYSTEMS_MAP_V4.

separate direct evidence:
A2 v1.6.1 exports A2_SYSTEMS_MAP_V4 using E3_5_INGEST_PROFILE_MIN_V1.

## Downstream

primary consumer:
E4_INTEGRATION_AND_EXECUTION_READINESS_ROUTING.

E3.5 handoff payload family:
E4_REQUIRED_SOURCES_BUNDLE.

supporting proof families:
coverage proof;
strict ref integrity proof;
type validation report;
dual-root proof when applicable;
waivers when applicable.

## Interface invariant

Upstream producer owns source meaning.
E3.5 owns only bundle/ref/proof metadata.
E4 owns downstream integration analysis.

## P/A note

E3.5 is not a P-channel or A-channel.
However, A2 is a real upstream dependency through RS-10.
No P-layer bridge is recovered as part of E3.5's own interface.
