package com.elyxion.cosmos;

import java.util.concurrent.atomic.AtomicInteger;

/** In-process user-input bridge to the first-party native DemoActivity only. */
public final class InputBus {
    private InputBus() {}
    private static volatile float x, y;
    private static final AtomicInteger pressesA = new AtomicInteger();
    private static final AtomicInteger pressesB = new AtomicInteger();
    public static void move(float horizontal, float vertical) {
        x = Math.max(-1f,Math.min(1f,horizontal));
        y = Math.max(-1f,Math.min(1f,vertical));
    }
    public static float x() { return x; }
    public static float y() { return y; }
    public static void pressA() { pressesA.incrementAndGet(); }
    public static void pressB() { pressesB.incrementAndGet(); }
    public static int a() { return pressesA.get(); }
    public static int b() { return pressesB.get(); }
    public static void reset() { x = 0; y = 0; pressesA.set(0); pressesB.set(0); }
}
