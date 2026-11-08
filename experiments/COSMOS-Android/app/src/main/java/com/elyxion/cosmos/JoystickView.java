package com.elyxion.cosmos;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.view.MotionEvent;
import android.view.View;
import java.util.Locale;

/** A true touchable native overlay widget; it does NOT inject input into other apps. */
public final class JoystickView extends View {
    public interface Listener { void onVector(float x, float y); }
    private final Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private float x = 0, y = 0;
    private int trackedPointer = -1;
    private final Listener listener;

    public JoystickView(Context context, Listener callback) {
        super(context);
        listener = callback;
        setContentDescription("ELYXION COSMOS — тестовый джойстик");
    }

    @Override protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        float cx = getWidth() / 2f, cy = getHeight() / 2f;
        float radius = Math.min(getWidth(), getHeight()) * .44f;
        paint.setStyle(Paint.Style.FILL);
        paint.setColor(Color.rgb(11, 37, 44));
        canvas.drawCircle(cx, cy, radius, paint);
        paint.setStyle(Paint.Style.STROKE); paint.setStrokeWidth(dp(2));
        paint.setColor(Color.rgb(124, 206, 189)); canvas.drawCircle(cx, cy, radius, paint);
        paint.setStrokeWidth(dp(1)); paint.setColor(Color.rgb(68, 116, 119));
        canvas.drawCircle(cx, cy, radius * .65f, paint);
        paint.setStyle(Paint.Style.FILL);
        paint.setColor(Color.rgb(80, 160, 149));
        canvas.drawCircle(cx + x * radius * .52f, cy + y * radius * .52f, radius * .32f, paint);
        paint.setColor(Color.rgb(220, 255, 241)); paint.setTextAlign(Paint.Align.CENTER);
        paint.setTextSize(dp(9));
        canvas.drawText("COSMOS", cx, cy + radius * .9f, paint);
    }

    @Override public boolean onTouchEvent(MotionEvent event) {
        int action = event.getActionMasked();
        if (action == MotionEvent.ACTION_DOWN) {
            trackedPointer = event.getPointerId(event.getActionIndex());
            update(event.getX(event.getActionIndex()), event.getY(event.getActionIndex()));
            return true;
        }
        if (action == MotionEvent.ACTION_MOVE && trackedPointer >= 0) {
            int index = event.findPointerIndex(trackedPointer);
            if (index >= 0) update(event.getX(index), event.getY(index));
            return true;
        }
        if (action == MotionEvent.ACTION_UP || action == MotionEvent.ACTION_CANCEL ||
            (action == MotionEvent.ACTION_POINTER_UP && event.getPointerId(event.getActionIndex()) == trackedPointer)) {
            trackedPointer = -1;
            x = 0; y = 0;
            listener.onVector(0, 0);
            postInvalidateOnAnimation();
            return true;
        }
        return true;
    }

    private void update(float px, float py) {
        float radius = Math.min(getWidth(), getHeight()) * .44f;
        if (radius <= 0) return;
        float[] vector = AxisMath.normalized(px, py, getWidth()/2f, getHeight()/2f, radius);
        float dx = vector[0], dy = vector[1];
        if (Math.abs(dx-x) > .015f || Math.abs(dy-y) > .015f) {
            x = dx; y = dy;
            listener.onVector(x, y);
            postInvalidateOnAnimation();
        }
    }
    private float dp(float v) { return v * getResources().getDisplayMetrics().density; }
}
