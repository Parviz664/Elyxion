# Elyxion COSMOS Starve Input Probe v0.4

Experimental **real Starve.io page** in a **native Android WebView**, with a minimal native joystick and two buttons. No game copies, no fake Starve scene, no game code injection.

- `STARVE.IO · открыть с нашим Lite-геймпадом`: launches the official HTTPS site, no Play Store required.
- Left native joystick maps manual touch continuously to balanced WASD keydown/keyup **inside the app's own WebView**. 8-way direction/hysteresis; no automation, no global keyboard events.
- Native A action sends tap-down/up to the crosshair's position within that WebView. The draggable crosshair selects the target point. B sends E key; Starve binding must be verified in its settings.
- Fullscreen landscape, small translucent joystick/buttons; size/opacity settings reused from 0.3.
- `CHROME` opens the unmodified official Starve.io site in the system browser as fallback.
- No accessibility permissions, no VPN, no rooting, no cross-app input injection; existing v0.3 overlay remains for the local test only.
- CI: compile with Android SDK 35, AGP 8.7.3, Java 17; run pure Java core test and direction mapping test, then upload debug APK.

**PROOF BOUNDARY:** This release tests a promising Android mechanism but HAS NOT proved the live game responds to WebView-generated key events or clicks. The Starve.io website might block WebView, ignore these events, or require more mouse semantics. Do not assert compatibility or any latency improvement until tested on physical Samsung. Avoid using an account if its third-party-software policy may apply: https://starve.io/terms.html.

**Important:** Starve.io terms prohibit automated systems and unauthorized scripts/software. This is human-initiated input only, but the operator must review policy before live use. Do not claim the developers authorize it. Oracle is not connected and network probes do not measure Starve.io game ping.
