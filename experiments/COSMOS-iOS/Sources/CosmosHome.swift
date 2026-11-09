import SwiftUI

private let ink = Color(red: 0.025, green: 0.075, blue: 0.11)
private let teal = Color(red: 0.54, green: 0.90, blue: 0.78)

struct CosmosHome: View {
    @StateObject private var game = StarveSession()
    @StateObject private var network = NetworkLab()
    @State private var panel: Panel = .game
    @State private var smallControls = true
    @State private var transparency = 0.76
    private enum Panel { case game, network }

    var body: some View {
        GeometryReader { geometry in
            ZStack {
                ink.ignoresSafeArea()
                if panel == .game {
                    StarveBrowser(session: game).ignoresSafeArea()
                    VStack(spacing: 0) {
                        topBar
                        Spacer(minLength: 4)
                        controls
                    }
                } else { networkPanel }
            }
            .foregroundStyle(.white)
            .fontDesign(.rounded)
        }
        .statusBarHidden()
        .onDisappear { game.releaseAll() }
    }

    private var topBar: some View {
        HStack(spacing: 10) {
            Text("◈ ELYXION").font(.system(size: 13, weight: .bold, design: .monospaced)).foregroundStyle(teal)
            Spacer()
            Button { game.reload() } label: { Image(systemName: "arrow.clockwise") }
            Button { game.openOfficialSafari() } label: { Image(systemName: "safari") }
            Button { panel = .network; game.releaseAll() } label: { Image(systemName: "waveform.path.ecg") }
        }
        .padding(.horizontal, 15).padding(.vertical, 12)
        .background(ink.opacity(0.87))
    }

    private var controls: some View {
        VStack(spacing: 9) {
            HStack(spacing: 10) {
                Circle().fill(game.experimentalInput ? teal : .orange).frame(width: 6, height: 6)
                Text(game.status).lineLimit(1).font(.system(size: 10))
                Spacer()
                Toggle("", isOn: Binding(get: { game.experimentalInput }, set: { game.setExperimental($0) }))
                    .labelsHidden().scaleEffect(0.77).tint(teal)
            }.padding(.horizontal, 12)
            HStack(alignment: .bottom) {
                Thumbstick(diameter: smallControls ? 113 : 145, opacity: transparency) { dx, dy in
                    game.move(x: dx, y: dy)
                }
                Spacer(minLength: 20)
                VStack(spacing: 10) {
                    actionButton("A", "Касание", size: smallControls ? 59 : 77) { game.tapCenter() }
                    actionButton("B", "Клавиша E", size: smallControls ? 47 : 64) { game.actionE(down: true) }
                }
            }
            HStack(spacing: 12) {
                Button(smallControls ? "Размер: LITE" : "Размер: LARGE") { smallControls.toggle() }
                Spacer()
                Button("Прозрачность") { transparency = transparency > 0.65 ? 0.48 : 0.85 }
                Spacer()
                Button("СЕТЬ") { game.releaseAll(); panel = .network }
            }
            .font(.system(size: 10, weight: .medium, design: .monospaced))
            .foregroundStyle(teal)
        }
        .padding(12)
        .background(ink.opacity(0.72))
    }

    private func actionButton(_ letter: String, _ label: String, size: CGFloat, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            VStack(spacing: 0) {
                Text(letter).font(.system(size: 20, weight: .bold, design: .rounded))
                Text(label).font(.system(size: 8))
            }
            .frame(width: size, height: size)
            .background(Circle().fill(teal.opacity(0.22)))
            .overlay(Circle().stroke(teal.opacity(0.62), lineWidth: 1))
        }
        .buttonStyle(.plain)
        .opacity(transparency)
    }

    private var networkPanel: some View {
        VStack(alignment: .leading, spacing: 18) {
            Button("← Вернуться к игре") { panel = .game }.foregroundStyle(teal)
            Text("COSMOS / NETWORK LAB").font(.system(size: 12, weight: .bold, design: .monospaced)).foregroundStyle(teal)
            Text("Измерить, а не угадать.").font(.system(size: 27, weight: .bold))
            Text("Мы измеряем время HTTP-ответа отдельного сервера во Франкфурте. Это не пинг Starve.io и не доказательство ускорения через Oracle.").font(.system(size: 13)).foregroundStyle(.gray)
            HStack {
                measure("P50", network.median)
                Spacer()
                measure("P95", network.tail)
                Spacer()
                measure("ОШИБКИ", "\(network.failures)")
            }
            Text(network.label).font(.system(size: 12)).foregroundStyle(teal)
            Button(network.running ? "Идёт измерение \(network.count)/12…" : "Запустить 12 измерений") { network.run() }
                .buttonStyle(.borderedProminent).tint(teal).foregroundStyle(ink)
                .disabled(network.running)
            Spacer()
        }
        .padding(24)
    }

    private func measure(_ name: String, _ value: String) -> some View {
        VStack(alignment: .leading, spacing: 5) {
            Text(name).font(.system(size: 11, design: .monospaced)).foregroundStyle(.gray)
            Text(value).font(.system(size: 19, weight: .bold)).foregroundStyle(teal)
        }
    }
}

struct Thumbstick: View {
    var diameter: CGFloat
    var opacity: Double
    var onMove: (Double, Double) -> Void
    @State private var point: CGSize = .zero
    private var limit: CGFloat { diameter * 0.30 }
    var body: some View {
        ZStack {
            Circle().fill(teal.opacity(0.13)).overlay(Circle().stroke(teal.opacity(0.48), lineWidth: 1))
            Circle().stroke(teal.opacity(0.22), style: StrokeStyle(lineWidth: 1, dash: [3, 5])).padding(24)
            Circle().fill(teal.opacity(0.65)).frame(width: diameter * 0.37, height: diameter * 0.37).offset(point)
        }
        .frame(width: diameter, height: diameter)
        .opacity(opacity)
        .contentShape(Circle())
        .gesture(DragGesture(minimumDistance: 0)
            .onChanged { gesture in
                let dx = gesture.location.x - diameter / 2
                let dy = gesture.location.y - diameter / 2
                let norm = max(1, hypot(dx, dy) / limit)
                point = CGSize(width: dx / norm, height: dy / norm)
                onMove(Double(point.width / limit), Double(point.height / limit))
            }
            .onEnded { _ in point = .zero; onMove(0, 0) })
    }
}
