package com.elyxion.cosmos;

import android.app.*;
import android.content.*;
import android.graphics.Color;
import android.graphics.drawable.GradientDrawable;
import android.os.Build;
import android.os.IBinder;
import android.content.pm.ServiceInfo;
import android.provider.Settings;
import android.view.*;
import android.widget.*;
import java.util.Locale;

/** User-started foreground service with visible overlay. No Accessibility or input injection. */
public final class OverlayService extends Service {
    public static final String ACTION_STOP = "com.elyxion.cosmos.STOP";
    private static final String CHANNEL = "cosmos_controls";
    private static final int NOTIFICATION_ID = 9003;
    private WindowManager windowManager;
    private JoystickView joystick;
    private LinearLayout actions;
    private TextView state;
    private WindowManager.LayoutParams joystickParams, actionsParams;
    private int tapsA = 0, tapsB = 0;

    @Override public void onCreate() {
        super.onCreate();
        windowManager = (WindowManager) getSystemService(WINDOW_SERVICE);
        NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        nm.createNotificationChannel(new NotificationChannel(CHANNEL, "ELYXION COSMOS controls", NotificationManager.IMPORTANCE_LOW));
        Intent stop = new Intent(this, OverlayService.class).setAction(ACTION_STOP);
        PendingIntent stopPi = PendingIntent.getService(this, 1, stop, PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        Notification notification = new Notification.Builder(this, CHANNEL)
            .setContentTitle("ELYXION COSMOS · Lite")
            .setContentText("Плавающий контроллер · только тест ввода")
            .setSmallIcon(android.R.drawable.ic_media_play)
            .setOngoing(true)
            .addAction(new Notification.Action.Builder(android.R.drawable.ic_delete, "Остановить", stopPi).build())
            .build();
        if (Build.VERSION.SDK_INT >= 34) {
            startForeground(NOTIFICATION_ID, notification, ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE);
        } else { startForeground(NOTIFICATION_ID, notification); }
    }

    @Override public int onStartCommand(Intent intent, int flags, int startId) {
        if (intent != null && ACTION_STOP.equals(intent.getAction())) { stopSelf(); return START_NOT_STICKY; }
        if (!Settings.canDrawOverlays(this)) { stopSelf(); return START_NOT_STICKY; }
        removeWindows();
        createWindows();
        return START_NOT_STICKY;
    }

    private void createWindows() {
        android.content.SharedPreferences prefs = getSharedPreferences("cosmos", MODE_PRIVATE);
        int pct = prefs.getInt("size", 85);
        float alpha = prefs.getInt("opacity", 65) / 100f;
        boolean left = prefs.getBoolean("left", true);
        int size = dp(Math.round(172 * pct / 100f));
        int padWidth = dp(Math.round(118 * pct / 100f));
        int padHeight = dp(Math.round(135 * pct / 100f));
        joystick = new JoystickView(this, (x,y) -> {
            InputBus.move(x, y);
            if (state != null) state.setText(String.format(Locale.US, "X %+.2f · Y %+.2f", x, y));
        });
        joystick.setAlpha(alpha);
        joystickParams = params(size, size, left ? Gravity.BOTTOM | Gravity.LEFT : Gravity.BOTTOM | Gravity.RIGHT);
        joystickParams.x = dp(16); joystickParams.y = dp(28);
        actions = new LinearLayout(this); actions.setOrientation(LinearLayout.VERTICAL);
        actions.setGravity(Gravity.CENTER);
        actions.setAlpha(alpha);
        state = new TextView(this);
        state.setText("A / B · только тест"); state.setTextSize(9); state.setTextColor(Color.WHITE);
        state.setGravity(Gravity.CENTER);
        actions.addView(state, new LinearLayout.LayoutParams(-1, dp(22)));
        actions.addView(actionButton("A", true), new LinearLayout.LayoutParams(-1, 0, 1));
        actions.addView(actionButton("B", false), new LinearLayout.LayoutParams(-1, 0, 1));
        actionsParams = params(padWidth, padHeight, left ? Gravity.BOTTOM | Gravity.RIGHT : Gravity.BOTTOM | Gravity.LEFT);
        actionsParams.x = dp(16); actionsParams.y = dp(36);
        windowManager.addView(joystick, joystickParams);
        windowManager.addView(actions, actionsParams);
    }

    private Button actionButton(String label, boolean isA) {
        Button b = new Button(this);
        b.setText(label); b.setTextSize(18); b.setTextColor(Color.WHITE);
        GradientDrawable bg = new GradientDrawable(); bg.setColor(isA ? 0xff195e58 : 0xff233f4b);
        bg.setCornerRadius(dp(22)); bg.setStroke(dp(1), 0xff74c6b1);
        b.setBackground(bg);
        b.setContentDescription("COSMOS test action " + label);
        b.setOnClickListener(v -> {
            if (isA) { tapsA++; InputBus.pressA(); } else { tapsB++; InputBus.pressB(); }
            state.setText("A:" + tapsA + " B:" + tapsB);
        });
        return b;
    }

    private WindowManager.LayoutParams params(int width, int height, int gravity) {
        WindowManager.LayoutParams p = new WindowManager.LayoutParams(
            width, height, WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,
            WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE | WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL,
            android.graphics.PixelFormat.TRANSLUCENT);
        p.gravity = gravity;
        return p;
    }

    private int dp(int n) { return Math.round(n * getResources().getDisplayMetrics().density); }
    private void removeWindows() {
        if (windowManager == null) return;
        if (joystick != null) { try { windowManager.removeView(joystick); } catch(Exception ignored) {} joystick = null; }
        if (actions != null) { try { windowManager.removeView(actions); } catch(Exception ignored) {} actions = null; }
        InputBus.move(0,0);
        state = null;
    }
    @Override public void onDestroy() { removeWindows(); super.onDestroy(); }
    @Override public IBinder onBind(Intent intent) { return null; }
}
