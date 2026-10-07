# CHANNEL_ERRORS_AND_CORRECTIONS

## ERR-D4-001 — premature evidentiary PASS

An assistant-generated v1.1 packet asserted E4 immutability, selected stabilizations, evidence bindings and quantitative gains before the complete required upstream evidence set was independently visible in the immediate payload.

Detection: recovery cross-check against v1.1 must-have packets.

Repair: classify that packet as `ASSISTANT_OUTPUT / NOT SOURCE PROOF`.

Resulting invariant: D4 cannot bootstrap evidence from its own output.

## ERR-D4-002 — byte-equivalence asserted without reproducible byte comparison

Historical assistant output claimed byte-equivalence PASS while no reproducible baseline byte comparison artifact was available in visible context.

Repair: preserve as historical claim, not verified proof. Current v1.2 requires trusted baseline refs/seal before a valid immutability proof.

## ERR-D4-003 — generated scores mistaken for measured reality

Historical packets contain portability gain, confidence and budget numbers.

Repair: treat them as assistant-generated evaluation values inside a design packet, not runtime measurements. D4 forbids runtime-performance claims.

## ERR-D4-004 — epoch collapse

False reconstruction: "D4 has always been D-line-only over D3."

Repair: preserve v1.1 E4-baseline mixed-stack era, v1.2 D3-baseline D-line-only era and explicit supersession.

## ERR-D4-005 — provenance overclaim

The user pasted complete v1.1/v1.2 JSON artifacts.

Repair: classify them as `USER_SUPPLIED_ARTIFACT`, not automatic line-by-line `AUTHOR_RAW`.

## ERR-D4-006 — readiness conflation

v1.2 final verdict says the spec is ready, while the last strict execution blocked.

Repair: separate specification readiness = READY from execution instance = BLOCK.

## ERR-D4-007 — E-channel leakage after v1.2

Historical v1.1 used E-channel refs.

Repair: v1.2 explicitly forbids importing E-channel logic/refs into current execution.

## ERR-D4-008 — unsupported exact v1.0 reconstruction

Prior assistant memory says v1.0 existed, but exact spec is absent.

Repair: keep v1.0 `PARTIALLY_RECOVERED`; no synthetic schema.

## Owner control pattern

Strong exact owner-control phrase:
`Работать строго по контракту Д4!`

This is a process constraint, not proof that every historical assistant packet complied perfectly.
