# CHANNEL_INTERFACE_MAP — A0_ORCHESTRATOR

## v2.2 interfaces

### Ingress
Expected input classes:
- A_MINUS_1 Vision Artifact JSON;
- P3/P4/P5 JSON;
- CANON_BINDING_PACKET_V2 wrapper;
- A1/A2/A3 handoffs;
- LAW_CONFIG;
- unknown JSON;
- raw/partially broken JSON.

### Structural ingress laws
- one payload;
- no manual routing;
- no manual patch selection;
- no manual source_trace edits;
- fallback non-JSON as raw text candidate.

### Egress
Report + `next_message_to_next_agent: string`.

### Primary downstream
A_MINUS_1 by safe hard-guard default for unknown parse-valid artifacts.

---

## v3.0 interfaces

### Ingress
v2.2-compatible classes retained.

### Egress
`copy_paste_payload_object: object` is the sole forwardable payload.

Optional:
`copy_paste_payload_chunks` for transport.

### Operator protocol
- copy exact object field;
- paste to `routing.next_agent`;
- do not stringify;
- no manual editing.

### Payload-type routes
- CANON_BINDING_PACKET_V2 → A1
- A1_ARCH_ANCHOR_V3 → A2
- A2_SYSTEMS_MAP_V4 → A3

### A3 bundle edge
Automatic bundle construction only if one single input already embeds both required source objects or is already an A3 bundle.

---

## v4.1 interfaces — partially recovered

### Adult ingress
A_ULTRA crystal/carry artifact.

### A0 checks
Recovered:
- crystal completeness;
- sacred carry;
- source_trace;
- release_gate_result;
- transport envelope;
- zero mutation / no reclassification.

### Egress
E0-ready object with readiness:
- READY_FOR_E0
- READY_FOR_E0_WITH_CONSTRAINTS
- BLOCKED_FOR_E0

Exact object schema: UNKNOWN.

### Adult downstream
E0.

### Legacy interface
A1/A2/A3 compatibility/recovery only.

---

## Neighbor-role confusion guards

### A_MINUS_1 / A_ULTRA
Owns interpretation/crystallization before A0. A0 must not redo meaning.

### A1
Historical v3.0 downstream architecture anchor. Not A0's semantic author.

### A2
Historical admissibility tribunal. A0 does not inherit its judgement authority.

### A3
Historical packaging/sealing stage. A0 v3.0 can route to it but is not A3.

### E0
Latest-known adult downstream bind root. A0 prepares/carries; E0 owns its own bind authority.
