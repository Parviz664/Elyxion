import Foundation

/// Pure logic; independent from iOS UI, testable with swiftc on Linux.
enum InputMath {
    static func keys(x: Double, y: Double, deadZone: Double = 0.18) -> Set<String> {
        guard x.isFinite && y.isFinite else { return [] }
        let dx = max(-1, min(1, x)), dy = max(-1, min(1, y))
        guard hypot(dx, dy) >= deadZone else { return [] }
        var result = Set<String>()
        if dx < -deadZone { result.insert("a") }
        if dx > deadZone { result.insert("d") }
        if dy < -deadZone { result.insert("w") }
        if dy > deadZone { result.insert("s") }
        return result
    }

    static func percentile(_ values: [Double], _ p: Double) -> Double? {
        let sorted = values.filter { $0.isFinite && $0 >= 0 }.sorted()
        guard !sorted.isEmpty else { return nil }
        let idx = max(0, min(1, p)) * Double(sorted.count - 1)
        let lo = Int(floor(idx)), hi = Int(ceil(idx))
        return sorted[lo] + (sorted[hi] - sorted[lo]) * (idx - Double(lo))
    }
}
