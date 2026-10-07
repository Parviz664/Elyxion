# E0 — Intent Lock / Handshake Gate → Dual-Lock Binder

Recovery status: SELF_RECOVERY_PASS_WITH_GAPS  
Repository status: historical recovery surface, not automatic canon promotion  
Recovered on: 2026-10-07  
Branch: channel/e0-intent-lock-handshake-recovery-v0.1

## Strongest-known identity

Technical ID remained stable:
E0_INTENT_LOCK_AND_HANDSHAKE_GATE

Historical human name:
E0 Канал Фиксации Намерения и Входного Handshake

Latest recovered human name (v1.5):
E0 Канал Двойного Замка (Kernel Truth + Dream Seal) и Входного Bind/Dispatch

The strongest recovered role is not the original role. E0 evolved from a direct E-Prime + A2 ingress validator into a dual-lock binder that expects kernel truth from E6/E-Prime-side refs and a dream seal from A3.

## Current strongest-known operational posture

Latest fully supplied E0 channel spec: ELYX_E0_CHANNEL_SPEC_V1_5_MASTER / 1.5.0.

Latest observed ingest outcome in this conversation: BLOCK.

Reason: the supplied A3 PRE-E0 bundle was only the dream-side input; E0 v1.5 requires the second lock, E6_KERNEL_BUNDLE_REF_ONLY with verified packet_registry_ref + registry_seal_ref. A further compatibility gap exists because supplied A3 v2.2 is not explicitly accepted by the v1.5 accepted_artifact_types list.

This recovery does not repair either gap.

## Core recovery law

History is architecture. Do not rewrite E0 as if v1.5 existed from birth.

Preserve:
- v1.1 direct E-Prime + A2 gate;
- deadlock caused by strict A2 shape expectations;
- v1.1/v1.2 no-ideal-waiting and safe-autofill transition;
- v1.3 A3 handshake carrier + E4/D4 sync seeding;
- v1.4 registry/seal no-inference hardening;
- v1.5 role realignment into E6 kernel + A3 dream dual-lock binder.

Most channel-defining material here is USER_SUPPLIED_ARTIFACT, not proven AUTHOR_RAW.
