import Foundation

@MainActor
final class NetworkLab: ObservableObject {
    @Published var running = false
    @Published var label = "Не измерено"
    @Published var median = "—"
    @Published var tail = "—"
    @Published var failures = 0
    @Published var count = 0

    private let probe = URL(string: "https://elyxion-cosmos-lab-white-line.vercel.app/api/echo")!

    func run() {
        guard !running else { return }
        running = true
        label = "12 HTTPS-запросов к Frankfurt, не ping Starve.io"
        median = "—"; tail = "—"; failures = 0; count = 0
        Task {
            var times: [Double] = []
            for i in 0..<12 {
                var components = URLComponents(url: probe, resolvingAgainstBaseURL: false)!
                components.queryItems = [URLQueryItem(name: "n", value: "\(Int(Date().timeIntervalSince1970 * 1000))_\(i)")]
                var req = URLRequest(url: components.url!)
                req.cachePolicy = .reloadIgnoringLocalAndRemoteCacheData
                req.timeoutInterval = 8
                let start = ProcessInfo.processInfo.systemUptime
                do {
                    let (_, response) = try await URLSession.shared.data(for: req)
                    guard let response = response as? HTTPURLResponse,
                          (200..<300).contains(response.statusCode) else { throw URLError(.badServerResponse) }
                    times.append((ProcessInfo.processInfo.systemUptime - start) * 1000)
                } catch { failures += 1 }
                count = i + 1
            }
            if let p50 = InputMath.percentile(times, 0.5), let p95 = InputMath.percentile(times, 0.95) {
                median = String(format: "%.0f ms", p50)
                tail = String(format: "%.0f ms", p95)
                label = "Готово · HTTP RTT до COSMOS Frankfurt. Не пинг сервера Starve.io."
            } else { label = "Ошибка измерения: нет успешных HTTPS-ответов" }
            running = false
        }
    }
}
