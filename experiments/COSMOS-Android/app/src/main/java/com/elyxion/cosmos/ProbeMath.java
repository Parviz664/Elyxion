package com.elyxion.cosmos;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;

/** Platform-free statistics: only SUCCESSFUL end-to-end HTTP samples are included. */
public final class ProbeMath {
    private ProbeMath() {}
    public static double percentile(List<Double> source, double p) {
        if (source == null || source.isEmpty()) return Double.NaN;
        List<Double> data = new ArrayList<>(source);
        Collections.sort(data);
        double index = Math.max(0, Math.min(data.size() - 1, (data.size() - 1) * p));
        int low = (int) Math.floor(index), high = (int) Math.ceil(index);
        return data.get(low) + (data.get(high) - data.get(low)) * (index - low);
    }
    public static double variability(List<Double> ordered) {
        if (ordered == null || ordered.size() < 2) return Double.NaN;
        double total = 0;
        for (int i = 1; i < ordered.size(); i++) total += Math.abs(ordered.get(i) - ordered.get(i-1));
        return total / (ordered.size() - 1);
    }
    public static String metric(double v) {
        return Double.isNaN(v) ? "—" : String.format(Locale.US, "%.1f", v);
    }
}
