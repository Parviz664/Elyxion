# ELYXION COSMOS · iPhone v0.1 (SOURCE / EXPERIMENTAL)

Goal: an iPhone-oriented counterpart to COSMOS Starve Input Probe.

- Native SwiftUI iOS 16+; recommended iPhone 12 Pro Max (also designed for other iPhones).
- Original URL `https://starve.io/` is opened as-is in WKWebView. There is no copied Starve code, modified client, bot, or automated gameplay.
- Small translucent native joystick and A/B buttons **inside** this iOS app, not across all other applications. Default experimental input OFF.
- When manually enabled, joystick sends simulated WASD DOM events, A sends simulated mouse click at center and B sends E. **These events are not trusted hardware events and Starve.io may reject them. No compatibility claims.** Read game terms before using third-party control: https://starve.io/terms.html .
- Open original Starve.io in Safari fallback; Safari cannot receive input from the separate COSMOS web app.
- COSMOS Network Lab runs 12 HTTP requests to the Frankfurt probe, reports P50/P95 and failures. This is not game ping, proxy, or Oracle speed-up.

## iPhone installation

This ZIP is **not an IPA or installed app**. Compile it with Xcode (XcodeGen, SwiftUI, signing by developer Apple ID) or distribute with TestFlight through an Apple Developer account. GitHub macOS CI can compile an **unsigned simulator build only**, not a sideloadable, signed iPhone app. There is no APK on iOS.

If you only have an iPhone, the immediately usable version is the existing Safari web app: https://elyxion-cosmos-lab-white-line.vercel.app/ — use Share → Add to Home Screen. Its joystick controls our independent sandbox, not Starve.io.

## Run tests
`swiftc Sources/InputMath.swift Tests/InputMathCheck.swift -o /tmp/cosmos-input-tests && /tmp/cosmos-input-tests` (on Linux/macOS)

On Mac with Homebrew & Xcode:
```
brew install xcodegen
xcodegen generate
xcodebuild -project ElyxionCOSMOS.xcodeproj -scheme ElyxionCOSMOS -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build
```

No Oracle/WhiteLine/RED changes, no account secrets. This project does not bypass third-party app sandboxing or security restrictions.
