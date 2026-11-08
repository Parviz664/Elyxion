package com.elyxion.cosmos;

import android.app.Activity;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;
import android.os.SystemClock;
import android.view.View;

/** First-party target: proves overlay input actually controls a native game scene. */
public final class DemoActivity extends Activity {
    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        getWindow().setStatusBarColor(0xff071116);
        getWindow().setNavigationBarColor(0xff071116);
        setContentView(new DemoCanvas());
    }
    private final class DemoCanvas extends View {
        private final Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        private float px = .5f, py = .45f, collectibleX = .7f, collectibleY = .35f;
        private int collected = 0, lastA = InputBus.a(), lastB = InputBus.b();
        private long last = SystemClock.elapsedRealtimeNanos();
        DemoCanvas() { super(DemoActivity.this); setContentDescription("ELYXION — родная тестовая игра"); }
        @Override protected void onDraw(Canvas canvas) {
            super.onDraw(canvas);
            long now = SystemClock.elapsedRealtimeNanos();
            float dt = Math.max(0, Math.min(.05f,(now-last)/1_000_000_000f));
            last = now;
            float space = Math.min(getWidth(),getHeight());
            if (space <= 0) return;
            px = clamp(px + InputBus.x() * 180 * dt / getWidth());
            py = clamp(py + InputBus.y() * 180 * dt / getHeight());
            int a = InputBus.a(), b = InputBus.b();
            if (a != lastA) {
                lastA = a;
                if (Math.hypot((px-collectibleX)*getWidth(),(py-collectibleY)*getHeight()) < 110 * getResources().getDisplayMetrics().density) {
                    collected++;
                    collectibleX = .25f + ((collected * .19f) % .55f);
                    collectibleY = .27f + ((collected * .13f) % .28f);
                }
            }
            if (b != lastB) {
                lastB = b;
                px = clamp(px + InputBus.x()*.10f);
                py = clamp(py + InputBus.y()*.10f);
            }
            canvas.drawColor(0xff091b24);
            paint.setColor(0xff12343d);
            for (int i=0;i<=10;i++) {
                canvas.drawLine(i*getWidth()/10f,0,i*getWidth()/10f,getHeight(),paint);
                canvas.drawLine(0,i*getHeight()/10f,getWidth(),i*getHeight()/10f,paint);
            }
            paint.setColor(0xffeab869);
            canvas.drawCircle(collectibleX*getWidth(),collectibleY*getHeight(),17*getResources().getDisplayMetrics().density,paint);
            paint.setColor(0xff8df0c9);
            canvas.drawCircle(px*getWidth(),py*getHeight(),17*getResources().getDisplayMetrics().density,paint);
            paint.setTextAlign(Paint.Align.CENTER);
            paint.setTextSize(17*getResources().getDisplayMetrics().scaledDensity);
            paint.setColor(Color.WHITE);
            canvas.drawText("ELYXION · NATIVE INPUT DEMO",getWidth()/2f,66*getResources().getDisplayMetrics().density,paint);
            paint.setTextSize(12*getResources().getDisplayMetrics().scaledDensity);
            canvas.drawText("A = собрать рядом · B = рывок",getWidth()/2f,94*getResources().getDisplayMetrics().density,paint);
            canvas.drawText("Кристаллы: "+collected,getWidth()/2f,116*getResources().getDisplayMetrics().density,paint);
            canvas.drawText("Это НЕ Starve.io · исходный код полностью наш",getWidth()/2f,139*getResources().getDisplayMetrics().density,paint);
            postInvalidateOnAnimation();
        }
        private float clamp(float v) {return Math.max(.05f,Math.min(.95f,v));}
    }
}
