package com.elyxion.cosmos;

/** Pure input normalization: playable from touch devices, testable on a desktop JDK. */
public final class AxisMath {
    private AxisMath() {}
    public static float[] normalized(float px, float py, float centerX, float centerY, float radius) {
        if (radius <= 0) return new float[]{0f, 0f};
        float dx = (px - centerX) / radius, dy = (py - centerY) / radius;
        double length = Math.hypot(dx,dy);
        if (length > 1) { dx /= length; dy /= length; }
        if (Math.hypot(dx,dy) < .085) return new float[]{0f,0f};
        return new float[]{dx,dy};
    }
}
