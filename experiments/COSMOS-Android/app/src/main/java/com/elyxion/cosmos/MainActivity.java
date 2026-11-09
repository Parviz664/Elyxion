package com.elyxion.cosmos;

import android.app.Activity;
import android.content.*;
import android.graphics.Color;
import android.graphics.Typeface;
import android.net.Uri;
import android.os.Bundle;
import android.provider.Settings;
import android.view.*;
import android.widget.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public final class MainActivity extends Activity {
    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    private LinearLayout screen;
    private TextView status, networkResult;
    private Spinner networkLabel;
    private NetworkProbe.Result lastProbe;
    private int green = 0xff91f1d2, white = 0xffd7f4e9;

    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setStatusBarColor(0xff071116);
        getWindow().setNavigationBarColor(0xff071116);
        build();
    }
    private void build() {
        ScrollView scroll = new ScrollView(this); scroll.setFillViewport(true);
        scroll.setBackgroundColor(0xff071116);
        screen = new LinearLayout(this); screen.setOrientation(LinearLayout.VERTICAL);
        screen.setPadding(dp(20), dp(18), dp(20), dp(30));
        scroll.addView(screen); setContentView(scroll);
        title("ELYXION · COSMOS LITE");
        subtitle("ANDROID v0.5 · НАСТОЯЩИЙ САЙТ STARVE.IO");
        text("Твой лёгкий геймпад: WASD + действие A + клавиша B. Откроется оригинальная игра внутри Elyxion.", 14, white);
        button("▶  ИГРАТЬ В STARVE.IO", () -> {
            // The in-app WebView does not require overlay or notification permissions.
            stopService(new Intent(this, OverlayService.class));
            startActivity(new Intent(this, StarveActivity.class));
        });
        text("Не требуется разрешение на плавающие окна. Первое нажатие открывает официальный сайт; реакция игры на наш ввод ещё не подтверждена.", 11, 0xffa6b8b1);
        subtitle("УДОБСТВО УПРАВЛЕНИЯ");
        text("Размер джойстика: 65–125%", 12, 0xffa9ccbf);
        SeekBar sizeBar = new SeekBar(this); sizeBar.setMax(60);
        sizeBar.setProgress(getSharedPreferences("cosmos", MODE_PRIVATE).getInt("size",80)-65);
        screen.addView(sizeBar);
        sizeBar.setOnSeekBarChangeListener(listener(p -> putInt("size",65+p)));
        text("Прозрачность: 30–100%", 12, 0xffa9ccbf);
        SeekBar alphaBar = new SeekBar(this); alphaBar.setMax(70);
        alphaBar.setProgress(getSharedPreferences("cosmos", MODE_PRIVATE).getInt("opacity",65)-30);
        screen.addView(alphaBar);
        alphaBar.setOnSeekBarChangeListener(listener(p -> putInt("opacity",30+p)));
        Switch hand = new Switch(this); hand.setText("Джойстик слева"); hand.setTextColor(white);
        hand.setChecked(getSharedPreferences("cosmos", MODE_PRIVATE).getBoolean("left",true));
        hand.setOnCheckedChangeListener((b,checked)->getSharedPreferences("cosmos",MODE_PRIVATE).edit().putBoolean("left",checked).apply());
        screen.addView(hand);
        subtitle("COSMOS NETWORK · FRANKFURT");
        text("12 HTTPS-измерений P50 / P95 до нашего тестового узла. Не пинг Starve.io и не доказательство ускорения через Oracle.",12,white);
        networkLabel = new Spinner(this);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item,
                new String[]{"Wi-Fi (выбрал вручную)", "Мобильный интернет (вручную)", "Неизвестно"});
        networkLabel.setAdapter(adapter); screen.addView(networkLabel);
        button("Измерить соединение", this::startProbe);
        networkResult = text("Нет измерений", 13, green);
        button("Поделиться JSON-отчётом", this::shareLast);
        subtitle("ДОПОЛНИТЕЛЬНО · ТОЛЬКО ДЛЯ ТЕСТОВ");
        text("Плавающее окно поверх чужих приложений не может само передавать им управление. Этот режим нужен только для нашей локальной тестовой сцены.", 11, 0xffa6b8b1);
        status = text("", 11, 0xffbdcacc);
        button("Тест нашего Android-джойстика", () -> {
            if (!Settings.canDrawOverlays(this)) { askOverlayPermission(); return; }
            InputBus.reset(); startOverlay();
            startActivity(new Intent(this, DemoActivity.class));
        });
        button("Скрыть тестовый геймпад", this::stopOverlay);
        button("Открыть Starve.io в Chrome (без Elyxion)", () -> {
            try { startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse("https://starve.io/"))); }
            catch (Exception e) { Toast.makeText(this, "Нет браузера для открытия ссылки", Toast.LENGTH_SHORT).show(); }
        });
        updateStatus();
    }
    private void startProbe() {
        String label = String.valueOf(networkLabel.getSelectedItem());
        networkResult.setText("Выполняются 12 HTTPS-запросов…");
        executor.execute(() -> {
            NetworkProbe.Result result = NetworkProbe.run(label);
            runOnUiThread(() -> { lastProbe = result; networkResult.setText(result.description()); });
        });
    }
    private void shareLast() {
        if (lastProbe == null) { Toast.makeText(this,"Сначала выполни измерение",Toast.LENGTH_SHORT).show(); return; }
        Intent send = new Intent(Intent.ACTION_SEND);
        send.setType("application/json");
        send.putExtra(Intent.EXTRA_TEXT, lastProbe.json());
        startActivity(Intent.createChooser(send,"Поделиться результатом COSMOS"));
    }
    private void askOverlayPermission() {
        if (Settings.canDrawOverlays(this)) { updateStatus(); return; }
        Intent settings = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION, Uri.parse("package:"+getPackageName()));
        startActivity(settings);
    }
    private void startOverlay() {
        if (!Settings.canDrawOverlays(this)) { askOverlayPermission(); return; }
        Intent intent = new Intent(this, OverlayService.class);
        try { startForegroundService(intent); }
        catch(Exception e) { Toast.makeText(this,"Не удалось показать: "+e.getMessage(),Toast.LENGTH_LONG).show(); }
    }
    private void stopOverlay() {
        stopService(new Intent(this, OverlayService.class));
        Toast.makeText(this,"COSMOS скрыт",Toast.LENGTH_SHORT).show();
    }
    @Override protected void onResume() { super.onResume(); if (status != null) updateStatus(); }
    private void updateStatus() { status.setText("Разрешение наложения: " + (Settings.canDrawOverlays(this) ? "ГОТОВО" : "НЕ ВЫДАНО")); }
    private void putInt(String key,int value) { getSharedPreferences("cosmos",MODE_PRIVATE).edit().putInt(key,value).apply(); }
    private interface Progress { void changed(int progress); }
    private SeekBar.OnSeekBarChangeListener listener(Progress callback) {
        return new SeekBar.OnSeekBarChangeListener() {
            @Override public void onProgressChanged(SeekBar seekBar,int progress,boolean user) { if(user) callback.changed(progress); }
            @Override public void onStartTrackingTouch(SeekBar s) {}
            @Override public void onStopTrackingTouch(SeekBar s) {}
        };
    }
    private int dp(int px) { return Math.round(px*getResources().getDisplayMetrics().density); }
    private void button(String label,Runnable action) {
        Button button = new Button(this); button.setText(label); button.setAllCaps(false);
        button.setTextColor(0xffd8fff0); button.setBackgroundTintList(android.content.res.ColorStateList.valueOf(0xff1d554f));
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1,dp(48)); lp.topMargin=dp(9);
        screen.addView(button,lp); button.setOnClickListener(v -> action.run());
    }
    private TextView text(String value,int sp,int color) {
        TextView v = new TextView(this); v.setText(value); v.setTextSize(sp); v.setTextColor(color); v.setLineSpacing(dp(2),1.0f);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1,-2); lp.topMargin=dp(12); screen.addView(v,lp); return v;
    }
    private void title(String t) { TextView v=text(t,21,green);v.setTypeface(null,Typeface.BOLD); }
    private void subtitle(String t) { TextView v=text(t,12,0xff9bb3b2);v.setLetterSpacing(.09f); }
    @Override protected void onDestroy() { executor.shutdownNow(); super.onDestroy(); }
}
