package com.elyxion.cosmos;

/**
 * Manual, privacy-preserving hints for survival play.
 * The player marks situations; this class NEVER observes, scrapes, or infers game state.
 * Hints never select inventory, click, move, or perform any gameplay action.
 */
public final class SurvivalAdvisor {
    public enum Risk { COLD, HUNGER, PREDATOR }
    public static final long MIN_INTERVAL_MS = 60_000L;
    private static final int COLD = 1, HUNGER = 2, PREDATOR = 4;
    private int flags;
    private long lastHintAt = Long.MIN_VALUE / 2;
    private boolean enabled = true;

    public void toggle(Risk risk) { flags ^= mask(risk); }
    public void clear() { flags = 0; }
    public boolean isActive(Risk risk) { return (flags & mask(risk)) != 0; }
    public boolean hasRisk() { return flags != 0; }
    public boolean enabled() { return enabled; }
    public void setEnabled(boolean value) { enabled = value; }
    public int riskCount() { return Integer.bitCount(flags); }

    public Risk priority() {
        if ((flags & PREDATOR) != 0) return Risk.PREDATOR;
        if ((flags & COLD) != 0) return Risk.COLD;
        if ((flags & HUNGER) != 0) return Risk.HUNGER;
        return null;
    }

    public String hint() {
        Risk priority = priority();
        if (priority == null) return "Свободный путь · помощь не нужна";
        String recommendation;
        switch (priority) {
            case PREDATOR:
                recommendation = "Опасность рядом · сначала дистанция, потом оружие";
                break;
            case COLD:
                recommendation = "Холод · найди источник тепла или укрытие";
                break;
            case HUNGER:
                recommendation = "Голод · проверь еду и безопасное место";
                break;
            default: throw new IllegalStateException();
        }
        if (riskCount() > 1) return recommendation + " · другие сигналы сохранены";
        return recommendation;
    }

    /**
     * @param nowMs Monotonic time, such as SystemClock.uptimeMillis().
     * @param requested true only for an explicit user tap, which may bypass cooldown.
     */
    public String offer(long nowMs, boolean requested) {
        if (!enabled || !hasRisk()) return null;
        if (!requested && (nowMs - lastHintAt < MIN_INTERVAL_MS)) return null;
        lastHintAt = nowMs;
        return hint();
    }

    private static int mask(Risk risk) {
        if (risk == null) throw new IllegalArgumentException("risk");
        switch (risk) {
            case COLD: return COLD;
            case HUNGER: return HUNGER;
            case PREDATOR: return PREDATOR;
            default: throw new IllegalArgumentException("risk");
        }
    }
}
