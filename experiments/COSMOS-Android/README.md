# ELYXION COSMOS Android v0.5 — Starve Input Probe

Experimental Android build for Samsung Galaxy A37 and similar devices. Opens the genuine https://starve.io/ website in an Android WebView with native manual controls. It does not contain Starve.io assets.

## One-tap start

1. Open ELYXION COSMOS and press **▶ ИГРАТЬ В STARVE.IO**.
2. The genuine website loads in landscape. WASD movement is available through the left joystick. No overlay or notification permission is needed for in-app play.
3. **A: МЫШЬ** switches button A between native primary-button mouse events (default) and touchscreen taps. **B** sends E. Adjust bindings in the site's own settings.
4. **CHROME** opens the unmodified official site outside Elyxion; the controller cannot operate that separate tab.

## v0.5 changes

- One-tap launch as the first action, with no startup permission prompts.
- Native mouse/touch A modes; WebView receives physical-style KeyEvents for WASD.
- Key and button release on navigation and app pause; cleanup when WebView renderer fails.
- Optional OS-wide overlay retained only for our separate local test scene.
- 12 HTTPS requests to the Frankfurt diagnostic service remain separate. This is NOT Starve.io ping, game traffic routing, or Oracle acceleration.

## Verification boundary

Compiling and running unit tests does not establish whether the live third-party game accepts these native WebView events. No automated play, JS injection, rooting, AccessibilityService injection, or game modification. Check https://starve.io/terms.html for third-party software limitations. Compatibility and developer authorization are NOT confirmed.

Build requires Android SDK 35, Java 17, Gradle 8.9. GitHub Actions produces a debug APK with applicationId com.elyxion.cosmos.starveprobe. Samsung Auto Blocker may block installing debug APKs; do not weaken phone security without understanding the risk. Independent security review and app-store signing are not complete.
