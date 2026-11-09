import SwiftUI
import WebKit

@MainActor
final class StarveSession: ObservableObject {
    static let official = URL(string: "https://starve.io/")!
    let webView: WKWebView
    @Published var experimentalInput = false
    @Published var status = "Официальный сайт · управление не подтверждено"
    private var pressed = Set<String>()

    init() {
        let configuration = WKWebViewConfiguration()
        configuration.allowsInlineMediaPlayback = true
        configuration.defaultWebpagePreferences.allowsContentJavaScript = true
        webView = WKWebView(frame: .zero, configuration: configuration)
        webView.scrollView.isScrollEnabled = false
        webView.isOpaque = false
        webView.backgroundColor = UIColor(red: 0.03, green: 0.07, blue: 0.10, alpha: 1)
        webView.load(URLRequest(url: Self.official, cachePolicy: .reloadRevalidatingCacheData))
    }

    func reload() { releaseAll(); webView.load(URLRequest(url: Self.official)) }
    func openOfficialSafari() { UIApplication.shared.open(Self.official) }

    /// Manual user-directed key simulation, not trusted hardware events.
    /// The target game may reject such events. OFF unless explicitly enabled.
    private func emit(_ key: String, down: Bool) {
        guard experimentalInput, ["w","a","s","d","e"].contains(key) else { return }
        let code = "Key" + key.uppercased()
        let event = down ? "keydown" : "keyup"
        let ascii = Int(Character(key.uppercased()).asciiValue ?? 0)
        let js = """
        (() => {
          const e = new KeyboardEvent('\(event)', {
            key: '\(key)', code: '\(code)', bubbles: true, cancelable: true
          });
          for (const target of [window, document]) target.dispatchEvent(e);
        })();
        """
        _ = ascii
        webView.evaluateJavaScript(js, completionHandler: nil)
    }

    func move(x: Double, y: Double) {
        let next = experimentalInput ? InputMath.keys(x: x, y: y) : Set<String>()
        for key in pressed.subtracting(next) { emit(key, down: false) }
        for key in next.subtracting(pressed) { emit(key, down: true) }
        pressed = next
    }

    func actionE(down: Bool) { emit("e", down: down) }

    func tapCenter() {
        guard experimentalInput else { return }
        let js = """
        (() => {
          const x = innerWidth * 0.5, y = innerHeight * 0.5;
          const target = document.elementFromPoint(x, y);
          if (!target) return;
          for (const kind of ['mousedown','mouseup','click']) {
            target.dispatchEvent(new MouseEvent(kind, { bubbles:true, cancelable:true, clientX:x, clientY:y }));
          }
        })();
        """
        webView.evaluateJavaScript(js, completionHandler: nil)
    }

    func releaseAll() {
        for key in pressed { emit(key, down: false) }
        pressed.removeAll()
    }
    func setExperimental(_ value: Bool) {
        if !value { releaseAll() }
        experimentalInput = value
        status = value ? "Пробный ввод включён · игра может игнорировать события" : "Оригинальная Starve.io · пробный ввод выключен"
    }
}

struct StarveBrowser: UIViewRepresentable {
    let session: StarveSession
    func makeUIView(context: Context) -> WKWebView { session.webView }
    func updateUIView(_ uiView: WKWebView, context: Context) {}
}
