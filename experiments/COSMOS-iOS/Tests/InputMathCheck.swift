import Foundation

func expect(_ condition: @autoclosure () -> Bool, _ label: String) {
    guard condition() else { fputs("FAIL: \(label)\n", stderr); exit(1) }
}
@main
enum TestRunner {
    static func main() {
        expect(InputMath.keys(x: 0, y: 0).isEmpty, "neutral")
        expect(InputMath.keys(x: 0, y: -1) == ["w"], "up")
        expect(InputMath.keys(x: 0, y: 1) == ["s"], "down")
        expect(InputMath.keys(x: 1, y: 0) == ["d"], "right")
        expect(InputMath.keys(x: -1, y: 0) == ["a"], "left")
        expect(InputMath.keys(x: -1, y: -1) == ["a", "w"], "upper left")
        expect(InputMath.keys(x: 1, y: 1) == ["d", "s"], "lower right")
        expect(InputMath.keys(x: 0.1, y: 0.1).isEmpty, "deadzone")
        expect(InputMath.keys(x: .nan, y: 0).isEmpty, "NaN safe")
        expect(InputMath.percentile([],0.5) == nil, "empty samples")
        expect(InputMath.percentile([10,20,30],0.5) == 20, "p50")
        expect(InputMath.percentile([10,20,30],0.95)! > 28, "p95")
        print("PASS: 12 Swift logic checks")
    }
}
