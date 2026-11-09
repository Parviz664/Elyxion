# ELYXION COSMOS Android v0.6 · Playability Research Preview

Experimental manual controller for opening the **original** https://starve.io/ in Android WebView. This is NOT an official Starve.io app, and game acceptance of synthetic native KeyEvents/MouseEvents has not been verified. Do not assume authorization for third-party tools.

## Community-grounded changes

Older Starve.io Android Play Store reviews repeatedly mention clunky D-pad movement, inability to attack while moving, missing handedness controls, and high perceived lag. [Archived public reviews](https://play.google.com/store/apps/details?id=com.addictinggames.starveio), [r/starveio mobile requests](https://www.reddit.com/r/starveio/comments/krw32o). These are historically reported pain points, not controlled performance measurements.

- **БОЙ**: two independent native touch joysticks. Left/right handed preference from Home applies. Left moves via WASD; right directs the mouse aim; A holds attack/harvest; B generates E as an experimental mapping.
- **ПОХОД**: one movement joystick, smaller A/B buttons, free touches on the visible game web page.
- **ЭКРАН**: hides all gameplay controls except the minimal top bar, for navigating menus, crafting and chat by ordinary touches.
- **Hotbar**: explicit item keys 1, 2, 3, 4 on the top strip; no auto hotkeys.
- **Input styles**: A switches between manually dispatched mouse-primary click and touch, without injecting JavaScript into the site.
- **Two-finger handling**: game view splits motion pointers, movement and aim can be held simultaneously, key release is enforced when app pauses or mode changes.
- **QA**: event counter and user-shareable JSON; counts dispatched WebView events, NOT accepted commands/game latency.
- **COSMOS Network Lab**: 12 HTTP requests to a separate Frankfurt test endpoint, not Starve.io ping, not Oracle route optimization.

## Install and first test

Use the GitHub prerelease's direct debug APK, if personally comfortable sideloading developer builds and obeying your device's security warnings. This app is not independently audited or store signed. Samsung Auto Blocker may prevent sideloading; there is no requirement to disable safeguards solely to run an unverified preview.

1. Open Elyxion. Tap **ИГРАТЬ В STARVE.IO**.
2. Try **ЭКРАН** to navigate original menus and join a server manually, then **БОЙ** for movement and combat.
3. Test moving diagonally while turning the right aim joystick and holding A. Compare **A: МЫШЬ** vs **A: КАСАНИЕ** only if needed.
4. Test rapid item selection 1–4, open inventory, switch to **ПОХОД**, and check the experience.
5. Open **QA** to share counts and note which actual in-game actions succeeded. There is no automatic server integration or proof that the game accepted input.

## Engineering and safety

No bots, no root, no AccessibilityService, no injection into other installed apps, no websocket interception, no reverse engineering. Source code here only synthesizes Android input events to our own embedded WebView. Starve.io's content and servers remain third-party. Compatibility and permissions unknown.

Build: Java 17 + Android SDK 35 + Gradle 8.9; GitHub Actions builds a debug APK from isolated branch. Physical Samsung hardware and real online play remain separate acceptance gates.
