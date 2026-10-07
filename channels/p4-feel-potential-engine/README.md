# P4 Feel Potential Engine — channel recovery

Recovery status: **SELF_RECOVERY_PASS_WITH_GAPS (pre post-write audit)**

Channel:
- technical id: `ELYX_P4_FEEL_POTENTIAL_ENGINE_v3.2`
- current strongest exact contract: `ELYX_P4_SPEC_V3_2_2`, semver `3.2.2`
- current output family: `ELYX_P4_FILTER_SHORTLIST_PACKET_V3_2_2`
- recovered role: feel-potential sorter / shortlist / final cut over P3-rendered candidates
- canonization authority: **NONE**
- semantic rewriting authority: **NONE**
- author-selection bypass: **FORBIDDEN**

This directory is a historical recovery, not a redesign.

Core rule:
> История канала является частью архитектуры канала.

Absolute recovery rule:
> НЕ ИЗОБРЕТАТЬ НЕДОСТАЮЩУЮ ИСТОРИЮ.

Strongest recovered local seam:
`P3 rendered ladder -> P4 filter/shortlist/final structural spine`.

Global P-route remains historically split between:
- `P0 -> -P1 -> P1 -> P2 -> P3 -> P4`
- `P0 -> P1 -> P2 -> P3 -> P4`

Current global authority over that route is HOLD/UNRESOLVED in the P Control Point. This recovery does not resolve it.

Important historical correction:
early in-channel P4 executions claimed `dependency_integrity=true` while omitting required intermediate dependencies from linear P3 chains. Later full-spine/role-aware executions repaired the behavior. See `CHANNEL_ERROR_CORRECTION_LOG.md`.

Files in this recovery preserve:
- identity;
- history;
- timeline;
- function evolution;
- exact/current contract boundary;
- version lineage;
- decisions;
- route history;
- interface map;
- provenance;
- known errors/corrections;
- gaps/unknowns;
- self-understanding;
- selected raw evidence;
- recovery assertions and audits.

No E-Prime Chat Archive material is used as this channel's storage location.
