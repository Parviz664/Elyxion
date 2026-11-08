package com.elyxion.cosmos;

import android.os.SystemClock;
import org.json.JSONArray;
import org.json.JSONObject;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/** On-demand HTTPS probe to OUR Frankfurt endpoint; never a game ping or transparent proxy. */
public final class NetworkProbe {
    private NetworkProbe() {}
    public static final String PROBE_URL = "https://elyxion-cosmos-lab-white-line.vercel.app/api/echo";
    public static final int COUNT = 12;

    public static final class Result {
        public final List<Double> samples = new ArrayList<>();
        public int errors = 0;
        public String label, errorMessage = "";
        public long timestamp;
        public double p50() { return ProbeMath.percentile(samples, .50); }
        public double p95() { return ProbeMath.percentile(samples, .95); }
        public double jitter() { return ProbeMath.variability(samples); }
        public String description() {
            return "COSMOS Frankfurt · " + label + "\n" + samples.size() + "/" + COUNT + " успешных запросов" +
                    "\nHTTP P50 " + ProbeMath.metric(p50()) + " ms" +
                    " · P95 " + ProbeMath.metric(p95()) + " ms" +
                    "\nVariation " + ProbeMath.metric(jitter()) + " ms · Errors " + errors;
        }
        public String json() {
            try {
                JSONObject o = new JSONObject();
                o.put("version", "cosmos-android-0.3-alpha");
                o.put("kind", "HTTPS application round trip; NOT Starve.io game ping");
                o.put("destination", PROBE_URL);
                o.put("network_label_manual", label);
                o.put("utc_epoch_ms", timestamp);
                o.put("attempted", COUNT);
                o.put("succeeded", samples.size());
                o.put("failed", errors);
                o.put("p50_ms", Double.isNaN(p50()) ? JSONObject.NULL : p50());
                o.put("p95_ms", Double.isNaN(p95()) ? JSONObject.NULL : p95());
                o.put("variation_ms", Double.isNaN(jitter()) ? JSONObject.NULL : jitter());
                JSONArray a = new JSONArray(); for (Double sample : samples) a.put(sample);
                o.put("samples_ms", a);
                if (!errorMessage.isEmpty()) o.put("last_error", errorMessage);
                return o.toString(2);
            } catch (Exception e) { return "{}"; }
        }
    }

    /** Call from a background thread only. */
    public static Result run(String label) {
        Result result = new Result(); result.label = label; result.timestamp = System.currentTimeMillis();
        for (int i = 0; i < COUNT; i++) {
            HttpURLConnection conn = null;
            long start = SystemClock.elapsedRealtimeNanos();
            try {
                URL url = new URL(PROBE_URL + "?android=0.3&request=" + i + "&t=" + result.timestamp);
                conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setConnectTimeout(5000); conn.setReadTimeout(5000);
                conn.setUseCaches(false);
                conn.setRequestProperty("Cache-Control", "no-store");
                int code = conn.getResponseCode();
                if (code < 200 || code >= 300) throw new Exception("HTTP " + code);
                try (InputStream input = conn.getInputStream()) {
                    byte[] buffer = new byte[4096];
                    if (input.read(buffer) < 0) throw new Exception("Empty response");
                }
                double elapsedMs = (SystemClock.elapsedRealtimeNanos() - start) / 1_000_000.0;
                result.samples.add(elapsedMs);
            } catch (Exception error) {
                result.errors++;
                result.errorMessage = error.getClass().getSimpleName() + ": " + error.getMessage();
            } finally { if (conn != null) conn.disconnect(); }
        }
        return result;
    }
}
