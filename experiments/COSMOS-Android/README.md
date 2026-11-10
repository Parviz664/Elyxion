# ELYXION COSMOS · Android v0.7 — Smooth Survival

This version opens **the original** https://starve.io/ in our own WebView. Player-driven input only.

## How to use it

1. Press **ИГРАТЬ В STARVE.IO** in the app.
2. Use the **left joystick** to move; the knob now eases smoothly for appearance **without delaying WASD input**.
3. **БОЙ** shows a second aim joystick; **ПОХОД** simplifies; **ЭКРАН** hides the game controls for in-game menus.
4. If you need a hint, tap **◇** (right near top), then **ХОЛОД**, **ЕДА**, or **ХИЩНИКИ**. Select more than one to prioritize predators, then cold, then hunger.
5. The suggestion appears for 5 seconds, then fades away. With a risk still marked, it may repeat at most once per minute. **СПОКОЙНО** clears all marks; **ПОДСКАЗКИ: ВЫКЛ** mutes them.
6. The game hotbar slots 1–4 are still manual; the assistant NEVER equips, clicks, attacks, moves or acts for the user.

### Important limitations
- The assistant **does not read** player health, hunger, temperature, enemies or any other game data. **The player marks conditions manually**. There is no automatic condition detection in v0.7.
- Input is sent as Android-native events to an in-app WebView. Whether the live Starve.io game accepts them is NOT confirmed on a Samsung. WebView page load is not game success.
- There is no Starve.io authorization for this third-party experimental app. Official Terms of Use restrict unauthorized software and automation: https://starve.io/terms.html. No botting, injecting JavaScript into the game, screen-scraping, modification or reverse engineering is implemented.
- Oracle network acceleration is not present. The network lab probes OUR endpoint, not Starve.io.
- The APK is debug-signed, independently unaudited, and Android/Samsung may block sideloading. Do not bypass device protection without understanding the risk.

## Verify
Run `bash qa/run-core-tests.sh`, `bash qa/run-direction-tests.sh`, `bash qa/run-aim-tests.sh`, `bash qa/run-survival-tests.sh`, and `python3 qa/verify_package.py`.
Android build: Java 17, SDK 35, Gradle 8.9.
