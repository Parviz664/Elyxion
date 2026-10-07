# CHANNEL VERSION LINEAGE

## Lineage summary

`v2.0`
→ `v2.1`
→ `v2.2`
→ `v2.3`
→ `v2.4`

This sequence is strongly supported, but recovery depth differs by version.

| Version | Artifact | Recovery class | Provenance | What is actually known |
|---|---|---|---|---|
| 2.0 | `ELYX_D1_CHANNEL_SPEC_V2_0_MASTER` | PARTIALLY_RECOVERED | ASSISTANT_PROPOSAL recovered from prior chat | D1 Core+Composer, anti-boredom/contemplation, 40 levers, fidelity critical 100% / overall >=99%, E1 + D2–D6 handoffs |
| 2.1 | `ELYX_D1_CHANNEL_SPEC_V2_1_MASTER` | EXACT_VERSION_RECOVERED | USER_SUPPLIED_ARTIFACT | full master present in D1 conversation; 48 levers; E-Prime/E0/D0 inbound; E1/D2/D3/D4 outbound; overall fidelity 99.3 |
| 2.2 | `ELYX_D1_CHANNEL_SPEC_V2_2_MASTER` | EXACT_VERSION_RECOVERED | USER_SUPPLIED_ARTIFACT | full master present; sync seed + locked-context; E1 alignment; 60 levers; D4/E4 alignment |
| 2.3 | `ELYX_D1_CHANNEL_SPEC_V2_3_MASTER` | REFERRED_TO_ONLY | RECOVERED_FROM_LATER_REFERENCE | existence proven by v2.4 supersession and D2 requirement `D1_GUARD_PACKET_V2_3_OR_HIGHER`; body unknown |
| 2.4 | `ELYX_D1_CHANNEL_SPEC_V2_4_MASTER` | EXACT_VERSION_RECOVERED | USER_SUPPLIED_ARTIFACT | full master present; D-line only; D0 locked context; D Registry+Seal; no-inference; anti-injection; outputs D2–D6 |

## v2.0 → v2.1

Supported delta from available evidence:

- lever count 40 → 48;
- evidence/fidelity/uncertainty structure becomes fully visible in recovered master;
- current v2.1 metadata explicitly says `derived_from: ELYX_D1_CHANNEL_SPEC_V2_0_MASTER`.

Full v2.0 delta cannot be reconstructed because the v2.0 body is absent.

## v2.1 → v2.2

Exact deltas directly present in v2.2:

- locked-context consistency gate;
- sync seed propagation;
- E1 execution-draft alignment;
- 48 → 60 levers;
- recovery and clarity/control lever categories;
- D4 rarity/recovery signals;
- E4 route integration;
- fail condition for locked-context failure;
- PASS_WITH_WARNINGS fidelity floor raised from 98.5 to 98.8.

## v2.2 → v2.3

**UNKNOWN.**

No body recovered. Do not interpolate.

## v2.3 → v2.4

Exact v2.4 patch metadata identifies a breaking dependency cleanup with schema preservation.

Major exact changes:

- all E0/E1/E-Prime/E4 dependencies removed;
- D0 becomes the only channel upstream source family;
- runtime evidence remains an inbound source;
- D Packet Registry + D Registry Seal become mandatory;
- no-inference becomes a hard contract;
- prompt-injection hardening added;
- locked context bound only to D0;
- E-channel reinjection explicitly blocked;
- downstream made D2–D6 only;
- new risks R17/R18 and fail conditions 016/017;
- composer may act only after D-registry/seal + locked-context pass.

## Version-status rule

A later `supersedes` field proves existence of the named predecessor but not its contents.

Therefore v2.3 is intentionally left incomplete.
