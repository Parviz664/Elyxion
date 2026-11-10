package com.elyxion.cosmos;

import android.app.Activity;
import android.graphics.Color;
import android.graphics.drawable.GradientDrawable;
import android.os.Handler;
import android.os.Looper;
import android.os.SystemClock;
import android.view.Gravity;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;

/**
 * Deliberately passive, optional HUD over our OWN game container.
 * Every danger signal comes from the player. The page is never inspected or modified.
 */
public final class AssistantHud {
    private final Activity activity;
    private final FrameLayout root;
    private final SurvivalAdvisor advisor = new SurvivalAdvisor();
    private final Handler handler = new Handler(Looper.getMainLooper());
    private final TextView trigger;
    private TextView hint;
    private LinearLayout panel;
    private TextView cold, hunger, predator, mute;
    private boolean playing = true;
    private final Runnable hide = () -> hint.setVisibility(View.GONE);
    private final Runnable repeat = new Runnable() {
        @Override public void run() {
            if (playing && panel.getVisibility() != View.VISIBLE) offer(false);
            handler.postDelayed(this, SurvivalAdvisor.MIN_INTERVAL_MS);
        }
    };

    public AssistantHud(Activity activity, FrameLayout root) {
        this.activity = activity;
        this.root = root;
        trigger = label("◇");
        trigger.setTextSize(20);
        trigger.setContentDescription("Помощник Elyxion. Открыть ручные сигналы выживания");
        trigger.setBackground(background(0xb714343c, 0xff679b90));
        FrameLayout.LayoutParams triggerLp = new FrameLayout.LayoutParams(dp(48),dp(44),Gravity.TOP|Gravity.RIGHT);
        triggerLp.rightMargin=dp(7);
        triggerLp.topMargin=dp(77);
        root.addView(trigger,triggerLp);
        trigger.setOnClickListener(v -> {
            boolean open = panel.getVisibility()!=View.VISIBLE;
            panel.setVisibility(open ? View.VISIBLE : View.GONE);
            hint.setVisibility(View.GONE);
            handler.removeCallbacks(hide);
        });

        panel = new LinearLayout(activity);
        panel.setOrientation(LinearLayout.VERTICAL);
        panel.setPadding(dp(9),dp(6),dp(9),dp(6));
        panel.setBackground(background(0xf014343c,0xff6b9f94));
        TextView title = label("ОТМЕТЬ СИТУАЦИЮ · ИГРУ НЕ СЧИТЫВАЕМ");
        title.setTextSize(9);
        panel.addView(title,new LinearLayout.LayoutParams(-1,dp(26)));
        LinearLayout chips = new LinearLayout(activity);
        cold = riskChip("❄ ХОЛОД",SurvivalAdvisor.Risk.COLD);
        hunger = riskChip("ЕДА",SurvivalAdvisor.Risk.HUNGER);
        predator = riskChip("ХИЩНИКИ",SurvivalAdvisor.Risk.PREDATOR);
        chips.addView(cold);chips.addView(hunger);chips.addView(predator);
        TextView calm = label("✓ СПОКОЙНО");
        calm.setOnClickListener(v -> {
            advisor.clear();
            hint.setVisibility(View.GONE);
            panel.setVisibility(View.GONE);
            refresh();
        });
        chips.addView(calm);
        panel.addView(chips,new LinearLayout.LayoutParams(-2,dp(38)));
        mute = label("ПОДСКАЗКИ: ВКЛ · НАЖМИ ДЛЯ ВЫКЛ");
        mute.setTextSize(9);
        mute.setOnClickListener(v -> {
            advisor.setEnabled(!advisor.enabled());
            hint.setVisibility(View.GONE);
            refresh();
        });
        panel.addView(mute,new LinearLayout.LayoutParams(-1,dp(30)));
        FrameLayout.LayoutParams panelLp=new FrameLayout.LayoutParams(-2,-2,Gravity.TOP|Gravity.RIGHT);
        panelLp.topMargin=dp(126);
        panelLp.rightMargin=dp(7);
        root.addView(panel,panelLp);
        panel.setVisibility(View.GONE);

        hint = label("");
        hint.setTextSize(11);
        hint.setMaxWidth(dp(330));
        hint.setPadding(dp(10),dp(7),dp(10),dp(7));
        hint.setGravity(Gravity.CENTER_VERTICAL);
        hint.setBackground(background(0xe5133a3f,0xff7ac5ab));
        FrameLayout.LayoutParams hintLp = new FrameLayout.LayoutParams(-2,-2,Gravity.TOP|Gravity.LEFT);
        hintLp.topMargin=dp(78);
        hintLp.leftMargin=dp(8);
        root.addView(hint,hintLp);
        hint.setVisibility(View.GONE);
        hint.setOnClickListener(v->hint.setVisibility(View.GONE));
        refresh();
    }

    private TextView label(String title) {
        TextView tv = new TextView(activity);
        tv.setText(title);
        tv.setGravity(Gravity.CENTER);
        tv.setTextColor(0xffd7f4e9);
        tv.setTextSize(11);
        tv.setPadding(dp(7),0,dp(7),0);
        return tv;
    }

    private GradientDrawable background(int fill, int edge) {
        GradientDrawable bg = new GradientDrawable();
        bg.setColor(fill);
        bg.setStroke(dp(1),edge);
        bg.setCornerRadius(dp(11));
        return bg;
    }

    private TextView riskChip(String name, SurvivalAdvisor.Risk risk) {
        TextView chip = label(name);
        chip.setOnClickListener(v -> {
            advisor.toggle(risk);
            panel.setVisibility(View.GONE);
            refresh();
            offer(true);
        });
        return chip;
    }

    private void refresh() {
        trigger.setText(!advisor.enabled()?"◇":advisor.hasRisk()?"◆":"◇");
        trigger.setTextColor(advisor.enabled()&&advisor.hasRisk()?0xffa6f4c9:Color.WHITE);
        cold.setTextColor(advisor.isActive(SurvivalAdvisor.Risk.COLD)?0xff86d6ff:Color.WHITE);
        hunger.setTextColor(advisor.isActive(SurvivalAdvisor.Risk.HUNGER)?0xffffd08a:Color.WHITE);
        predator.setTextColor(advisor.isActive(SurvivalAdvisor.Risk.PREDATOR)?0xffffafa6:Color.WHITE);
        mute.setText(advisor.enabled()?"ПОДСКАЗКИ: ВКЛ · НАЖМИ ДЛЯ ВЫКЛ":"ПОДСКАЗКИ: ВЫКЛ · НАЖМИ ДЛЯ ВКЛ");
    }

    private void offer(boolean userTriggered) {
        if(!playing)return;
        String suggestion=advisor.offer(SystemClock.uptimeMillis(),userTriggered);
        if(suggestion==null) {
            if(userTriggered)hint.setVisibility(View.GONE);
            return;
        }
        hint.setText("◇ COSMOS · " + suggestion);
        hint.setVisibility(View.VISIBLE);
        handler.removeCallbacks(hide);
        handler.postDelayed(hide,5000L);
    }

    public void setPlaying(boolean playing) {
        this.playing=playing;
        if(!playing) {
            panel.setVisibility(View.GONE);
            hint.setVisibility(View.GONE);
        }
        trigger.setVisibility(playing?View.VISIBLE:View.GONE);
    }

    public void resume() {
        handler.removeCallbacks(repeat);
        handler.postDelayed(repeat,SurvivalAdvisor.MIN_INTERVAL_MS);
    }

    public void pause() {
        handler.removeCallbacks(repeat);
        handler.removeCallbacks(hide);
        panel.setVisibility(View.GONE);
        hint.setVisibility(View.GONE);
    }

    public void destroy() { pause(); }

    public boolean gameStateRead() { return false; }
    public boolean hintsEnabled() { return advisor.enabled(); }
    public int markedRiskCount() { return advisor.riskCount(); }

    private int dp(int dp) {return Math.round(dp * activity.getResources().getDisplayMetrics().density);}
}
