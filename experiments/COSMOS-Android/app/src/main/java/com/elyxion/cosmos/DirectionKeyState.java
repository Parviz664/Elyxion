package com.elyxion.cosmos;

/** Pure-Java 8-way joystick → balanced WASD key state. No auto-play or repeats. */
public final class DirectionKeyState {
    public static final int W = 1, A = 2, S = 4, D = 8;
    private static final float ON = 0.34f, OFF = 0.23f;
    private int state;
    public int state() { return state; }
    public int update(float x, float y) {
        if (!Float.isFinite(x) || !Float.isFinite(y)) return release();
        int n = state;
        n = updateAxis(n, W, S, -y);
        n = updateAxis(n, A, D, -x);
        state = n;
        return n;
    }
    private int updateAxis(int n, int neg, int pos, float v) {
        // The argument is positive when the first-listed key should be down.
        boolean oldNeg = (n & neg) != 0;
        boolean oldPos = (n & pos) != 0;
        boolean nextNeg = v > (oldNeg ? OFF : ON);
        boolean nextPos = v < -(oldPos ? OFF : ON);
        n &= ~(neg|pos);
        if(nextNeg) n |= neg;
        else if(nextPos) n |= pos;
        return n;
    }
    public int release() { state = 0; return state; }
}
