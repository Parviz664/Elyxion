# COSMOS Android v0.7 QA

- v0.6 Java mapping, aim, and core tests are retained.
- New independently executable `SurvivalAdvisorTest`: flags, priorities, quiet 60-second cooldown, mute, reset and combined threats.
- v0.7 changes: visual-only joystick smoothing; WASD inputs NOT smoothed/delayed; single compact optional player-marked survival helper; prompt hidden after 5 sec; prompt offers at most once per minute for lingering user-marked risks.
- Source SHA256SUMS verified during CI; actual Android Gradle compile required before reporting release success.
- **Not tested on physical Samsung**. The page can load while game input still fails.
- **Does not read the real game state**. User chooses cold/hunger/predator marks. No autonomous gameplay or unauthorized data extraction.
- v0.7 APK is NOT approved by Starve.io and not independently security audited.
- No measured game ping or acceleration via Oracle.
