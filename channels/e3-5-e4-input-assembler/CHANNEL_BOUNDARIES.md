# CHANNEL_BOUNDARIES

## Hard boundary: source meaning

Source meaning stays upstream.

E3.5 may point to it.
E3.5 may validate metadata required by its contract.
E3.5 may not rewrite it.

## Hard boundary: missing information

Missing remains missing.

The earliest v1.0 spec already says E3.5 does not invent missing packets.
Later versions make this stronger through REF_ONLY_STRICT and integrity proofs.

## Hard boundary: trace roots

Historical single-root SIM lane:
SIM root cannot merge into CANON/BOOTSTRAP chains.

Later dual-root BOOTSTRAP lane:
bootstrap root and canon-patch root may coexist as references but must not become one lineage.

E3.5 does not own root-merging authority.

## Hard boundary: downstream logic

Coverage complete != E4 complete.

Even at 10/10 refs:
E4 may still BLOCK for:
- conflict topology;
- forced-order logic;
- safety/invariant failure;
- intent checks.

These are explicitly outside E3.5 guarantee scope by v1.2+.

## Hard boundary: runtime/release

No runtime performance/FPS/thermal claims.
No release handoff claim from E3.5 alone.
No runtime promotion claim.
No CANON readiness claim.

## Hard boundary: waivers

REF_ONLY_STRICT:
no waivers.

PARTIAL_WITH_WAIVERS:
waivers may permit a constrained partial bundle only under the active waiver policy.

A waiver is not proof the missing source exists.

## Neighbor confusion

E-Prime Packet Registry:
can resolve/register refs; E3.5 consumes/proves bundle coverage.

A2:
produces system map/export material; E3.5 only checks its required ref.

E3/D3/E2/D2:
produce semantic/decision/augmentation material; E3.5 must not regenerate it.

E4:
integrates and reasons across the full graph; E3.5 only prepares and proves the input boundary.

## Recovery boundary

This repository recovery does not activate v1.4.1.
It does not make v1.4 owner-canon.
It only records the strongest recovered history and contract state.
