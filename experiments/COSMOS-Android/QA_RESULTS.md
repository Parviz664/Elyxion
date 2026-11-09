# ELYXION COSMOS Android v0.6 · QA Evidence

## Local pure-Java checks
- 11 original neutral/clamp/bus/latency tests: PASS
- 14 original direction-state transitions + 2500 randomized transitions + 3 neutral-release assertions: PASS
- 16 independent AimMath geometry and bounds assertions: PASS
- Release hashes: SHA-256 manifest to be verified after file packaging.

## Android build
- GitHub Actions compilation: PENDING for v0.6.
- Android emulator/runtime multi-touch and WebView keyboard/mouse acceptance: NOT TESTED.
- Real Samsung installation and original Starve.io character movement: NOT CONFIRMED.
- Original game compatibility with HUD, mouse events, and mobile browser login: UNKNOWN.
- Network tests are separate HTTP probes, not proof of game RTT or acceleration via Oracle.

## Required real-device acceptance
1. Original public website loads, player can join and move without external peripherals.
2. Continuous diagonal movement + independent aim joystick + held A (kiting test).
3. No stuck WASD or pressed A after app pause, navigation, screen mode switch or crash.
4. Hotbar slots 1–4 and crafting/inventory taps do not interfere.
5. Test both left/right-handed layout, Lite and Combat layouts, plus error/recovery.
6. Obtain signed/reviewed distribution method before mass use.

## Safety boundary
No automated gameplay, game code manipulation, or claimed authorization from Starve.io. This is an experimental third-party WebView client. Test results will separate successful app compilation from actual in-game compatibility.
