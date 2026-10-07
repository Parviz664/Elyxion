# CHANNEL_GAP_REGISTER

## GAP-D4-001 — exact v1.0 artifact missing
Severity: HIGH for full lineage fidelity.
Known: assistant referred to v1.0; early function partially recovered.
Missing: exact spec/schema.
Rule: do not synthesize.

## GAP-D4-002 — exact birth-message RAW incomplete
Recovered conversation metadata preserves semantic content and timestamp, not every original character.
Rule: mark old wording as recovered paraphrase.

## GAP-D4-003 — original authorship of supplied specs unknown
User supplied v1.1/v1.2 artifacts.
Missing: proof of who authored each line originally.
Rule: `USER_SUPPLIED_ARTIFACT`, not automatic `AUTHOR_RAW`.

## GAP-D4-004 — exact D6 interface missing
v1.2 authority mentions D5/D6; explicit next_step defines D5.
D6 remains partial.

## GAP-D4-005 — required v1.2 input packets absent in last strict run
Registry/seal and trusted packet closure were missing.
Impact: execution BLOCK.

## GAP-D4-006 — no pre-existing durable D4 GitHub history found on main
Searches by channel/spec IDs returned no D4 artifacts.

## GAP-D4-007 — E-Prime archive has infrastructure, not D4 transcript payload
Inspected branch tree did not provide extra D4 primary RAW.

## GAP-D4-008 — exact rationale for every v1.2 field
Patch metadata gives explicit change intent, but not separate owner rationale for every field.
Rule: do not invent motives.
