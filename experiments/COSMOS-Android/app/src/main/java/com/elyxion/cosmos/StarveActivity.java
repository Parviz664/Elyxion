package com.elyxion.cosmos;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Canvas;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.os.SystemClock;
import android.content.pm.ActivityInfo;
import android.view.*;
import android.webkit.*;
import android.widget.*;

/** An experimental, manual controller for the real https://starve.io/ page.
 *  Android WebView receives ordinary KeyEvents and touch events from THIS activity.
 *  No JS injection, no bot, no reverse engineering and no OS-wide input injection.
 *  Neither WebView compatibility nor game acceptance is guaranteed. */
public final class StarveActivity extends Activity {
    private static final String URL = "https://starve.io/";
    private FrameLayout root;
    private WebView web;
    private TextView status;
    private View aim;
    private final DirectionKeyState directions = new DirectionKeyState();
    private int keyState;
    private long[] keyDownTimes = new long[4];
    private long tapDownTime;
    private boolean tapping, actionEHeld;
    private boolean mouseAction = true;
    private TextView inputMode;
    private JoystickView moveStick, aimStick;
    private LinearLayout buttons, quickSlots;
    private TextView combatControl, exploreControl, screenControl;
    private int layoutMode = 0; // 0 combat, 1 exploration, 2 unobstructed UI
    private long lastAimDispatchMs;
    private int inputEvents;
    private boolean pageLoaded;
    private AssistantHud survivalHud;


    private long eDownTime;
    private float aimX = .54f, aimY = .50f;
    private final int[] codes = {KeyEvent.KEYCODE_W, KeyEvent.KEYCODE_A, KeyEvent.KEYCODE_S, KeyEvent.KEYCODE_D};
    private final int[] bits = {1,2,4,8};
    private int accent = 0xff99e9d8;

    @SuppressLint("SetJavaScriptEnabled")
    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_SENSOR_LANDSCAPE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getWindow().getDecorView().setSystemUiVisibility(5894 | View.SYSTEM_UI_FLAG_LAYOUT_STABLE);
        root = new FrameLayout(this);
        root.setMotionEventSplittingEnabled(true); // Separate fingers for movement, aim and attack.
        root.setBackgroundColor(0xff0a1d26); setContentView(root);
        web = new WebView(this);
        web.setBackgroundColor(0xff0a1d26);
        web.setFocusableInTouchMode(true);
        WebSettings settings = web.getSettings();
        settings.setJavaScriptEnabled(true); // Official game requires JS.
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(false);
        settings.setAllowContentAccess(false);
        settings.setAllowFileAccessFromFileURLs(false);
        settings.setAllowUniversalAccessFromFileURLs(false);
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_NEVER_ALLOW);
        settings.setMediaPlaybackRequiresUserGesture(true);
        settings.setSupportMultipleWindows(false);
        web.setWebChromeClient(new WebChromeClient());
        web.setWebViewClient(new WebViewClient() {
            @Override public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest req) {
                Uri uri = req.getUrl();
                String host = uri.getHost();
                if ("https".equalsIgnoreCase(uri.getScheme()) && ("starve.io".equalsIgnoreCase(host) || "www.starve.io".equalsIgnoreCase(host))) return false;
                if ("https".equalsIgnoreCase(uri.getScheme())) {
                    try { startActivity(new Intent(Intent.ACTION_VIEW, uri)); } catch(Exception ignored) {}
                }
                return true;
            }
            @Override public void onPageStarted(WebView v,String url,android.graphics.Bitmap favicon) {
                releaseKeys();pageLoaded=false;status.setText("STARVE.IO · ЗАГРУЗКА");
            }
            @Override public void onPageFinished(WebView v,String url) {
                pageLoaded=true;
                status.setText("САЙТ ЗАГРУЖЕН · ПРОВЕРЬ УПРАВЛЕНИЕ В ИГРЕ");
                v.requestFocus();
            }
            @Override public void onReceivedError(WebView v,WebResourceRequest request,WebResourceError error) {
                if (request.isForMainFrame()) {pageLoaded=false;status.setText("НЕ УДАЛОСЬ ЗАГРУЗИТЬ · ОТКРОЙ В CHROME");}
            }
            @Override public boolean onRenderProcessGone(WebView view,RenderProcessGoneDetail detail) {
                releaseKeys();pageLoaded=false;
                status.setText("WEBVIEW ОСТАНОВЛЕН · ОТКРОЙ CHROME ИЛИ ЗАПУСТИ ЗАНОВО");
                if (web != null) {
                    root.removeView(web);
                    web.destroy();
                    web = null;
                }
                return true;
            }
        });
        root.addView(web,new FrameLayout.LayoutParams(-1,-1));
        int sizePct = getSharedPreferences("cosmos",MODE_PRIVATE).getInt("size",80);
        float opacity = getSharedPreferences("cosmos",MODE_PRIVATE).getInt("opacity",65)/100f;
        boolean left = getSharedPreferences("cosmos",MODE_PRIVATE).getBoolean("left",true);
        int size = dp(Math.round(150*sizePct/100f));
        moveStick = new JoystickView(this, this::onStick);
        moveStick.setContentDescription("Движение персонажа, восьминаправленный джойстик");
        moveStick.setAlpha(opacity); moveStick.setFocusable(false);
        FrameLayout.LayoutParams joyP = new FrameLayout.LayoutParams(size,size,Gravity.BOTTOM | (left?Gravity.LEFT:Gravity.RIGHT));
        joyP.setMargins(dp(12),0,dp(12),dp(14));root.addView(moveStick,joyP);
        int aimSize = Math.max(dp(96),Math.round(size*.86f));
        aimStick = new JoystickView(this, this::onAimStick);
        aimStick.setContentDescription("Прицеливание отдельным пальцем, удержание направления");
        aimStick.setAlpha(opacity); aimStick.setFocusable(false);
        FrameLayout.LayoutParams aimJoyP = new FrameLayout.LayoutParams(aimSize,aimSize,Gravity.BOTTOM | (left?Gravity.RIGHT:Gravity.LEFT));
        aimJoyP.setMargins(dp(12),0,dp(12),dp(8));root.addView(aimStick,aimJoyP);
        buttons = new LinearLayout(this); buttons.setOrientation(LinearLayout.VERTICAL);buttons.setAlpha(opacity);
        buttons.addView(makeActionButton("A · УДАР / СБОР", true),new LinearLayout.LayoutParams(dp(114),dp(54)));
        buttons.addView(makeActionButton("B · E", false),new LinearLayout.LayoutParams(dp(114),dp(47)));
        FrameLayout.LayoutParams btnP = new FrameLayout.LayoutParams(dp(114),dp(103),Gravity.BOTTOM | (left?Gravity.RIGHT:Gravity.LEFT));
        btnP.setMargins(dp(17),0,dp(17),aimSize+dp(14));root.addView(buttons,btnP);
        aim = new View(this) {
            private final Paint p = new Paint(Paint.ANTI_ALIAS_FLAG);
            @Override public void onDraw(Canvas c) {
                float x=getWidth()/2f,y=getHeight()/2f;
                p.setStyle(Paint.Style.STROKE);p.setStrokeWidth(dp(1.5f));p.setColor(0xffd3f9e5);
                c.drawCircle(x,y,dp(8),p);c.drawLine(x-dp(14),y,x+dp(14),y,p);c.drawLine(x,y-dp(14),x,y+dp(14),p);
            }
            @Override public boolean onTouchEvent(android.view.MotionEvent e) {
                if(e.getActionMasked()==MotionEvent.ACTION_DOWN)return true;
                if(e.getActionMasked()==MotionEvent.ACTION_MOVE||e.getActionMasked()==MotionEvent.ACTION_UP) {
                    if(web==null)return true;
                    int[] loc=new int[2];getLocationOnScreen(loc);
                    aimX=Math.max(.05f,Math.min(.95f,(loc[0]+e.getX())/Math.max(1,web.getWidth())));
                    aimY=Math.max(.05f,Math.min(.95f,(loc[1]+e.getY())/Math.max(1,web.getHeight())));
                    placeAim();sendAimMotion();return true;
                }
                return true;
            }
        };
        FrameLayout.LayoutParams aimP = new FrameLayout.LayoutParams(dp(38),dp(38),Gravity.TOP | Gravity.LEFT);root.addView(aim,aimP);
        root.post(this::placeAim);
        LinearLayout tools = new LinearLayout(this); tools.setGravity(Gravity.CENTER_VERTICAL);
        tools.setPadding(dp(6),0,dp(6),0);tools.setBackgroundColor(0xcc07181e);
        status = new TextView(this);status.setText("STARVE.IO · НАЧАЛО");status.setTextColor(accent);status.setTextSize(10);
        tools.addView(status,new LinearLayout.LayoutParams(0,dp(32),1));
        inputMode = smallTool("A: МЫШЬ");
        inputMode.setOnClickListener(v -> {
            // Never switch modes in the middle of a held action.
            sendAimTap(false);
            mouseAction = !mouseAction;
            inputMode.setText(mouseAction ? "A: МЫШЬ" : "A: КАСАНИЕ");
            status.setText("РЕЖИМ A ИЗМЕНЁН · ПРИЁМ ИГРОЙ НЕ ПОДТВЕРЖДЁН");
        });
        tools.addView(inputMode);
        combatControl = smallTool("БОЙ");combatControl.setOnClickListener(v->setLayoutMode(0));tools.addView(combatControl);
        exploreControl = smallTool("ПОХОД");exploreControl.setOnClickListener(v->setLayoutMode(1));tools.addView(exploreControl);
        screenControl = smallTool("ЭКРАН");screenControl.setOnClickListener(v->setLayoutMode(2));tools.addView(screenControl);
        TextView qaButton=smallTool("QA");qaButton.setOnClickListener(v->showQa());tools.addView(qaButton);
        TextView browser = smallTool("CHROME"); browser.setOnClickListener(v->openChrome());tools.addView(browser);
        TextView reload=smallTool("↻");reload.setOnClickListener(v->{releaseKeys();if(web!=null)web.reload();});tools.addView(reload);
        TextView close=smallTool("✕");close.setOnClickListener(v->finish());tools.addView(close);
        root.addView(tools,new FrameLayout.LayoutParams(-1,dp(32),Gravity.TOP));
        quickSlots = new LinearLayout(this);quickSlots.setGravity(Gravity.CENTER);
        quickSlots.setAlpha(Math.min(1f,opacity+.18f));
        for(int number=1;number<=4;number++) {
            final int n=number;
            TextView slot=smallTool("["+number+"]");
            slot.setTextSize(13);
            slot.setBackgroundColor(0xbc102b32);
            slot.setContentDescription("Быстрый слот предмета "+number);
            slot.setOnClickListener(v->sendHotbar(n));
            LinearLayout.LayoutParams lp=new LinearLayout.LayoutParams(dp(44),dp(34));lp.setMargins(dp(3),0,dp(3),0);
            quickSlots.addView(slot,lp);
        }
        FrameLayout.LayoutParams quickP=new FrameLayout.LayoutParams(-2,dp(34),Gravity.TOP|Gravity.CENTER_HORIZONTAL);
        quickP.topMargin=dp(37);root.addView(quickSlots,quickP);
        survivalHud = new AssistantHud(this,root);
        setLayoutMode(0);
        // User navigates to and joins the genuine site, never an automatic login.
        web.loadUrl(URL);
    }
    private TextView smallTool(String str) {
        TextView t=new TextView(this);t.setText(str);t.setTextColor(Color.WHITE);t.setTextSize(10);t.setGravity(Gravity.CENTER);
        t.setPadding(dp(9),0,dp(9),0);return t;
    }
    private View makeActionButton(String label,boolean actionA) {
        TextView btn=new TextView(this);btn.setText(label);btn.setTextColor(Color.WHITE);btn.setTextSize(12);
        btn.setGravity(Gravity.CENTER);
        GradientDrawable bg=new GradientDrawable();bg.setColor(actionA?0xff205c53:0xff264350);bg.setCornerRadius(dp(19));bg.setStroke(dp(1),0xff79bbac);btn.setBackground(bg);
        btn.setOnTouchListener((v,event)-> {
            switch(event.getActionMasked()) {
                case MotionEvent.ACTION_DOWN:
                    if(actionA)sendAimTap(true);else setEKey(true);
                    return true;
                case MotionEvent.ACTION_UP:
                case MotionEvent.ACTION_CANCEL:
                    if(actionA)sendAimTap(false);else setEKey(false);
                    return true;
                default:return true;
            }
        });
        return btn;
    }
    private void showQa() {
        String info="Сайт загружен: "+(pageLoaded?"да":"нет")+
            "\nОтправлено событий в WebView: "+inputEvents+
            "\nРежим: "+(layoutMode==0?"бой":layoutMode==1?"поход":"экран")+
            "\nТип действия A: "+(mouseAction?"мышь":"касание")+
            "\n\nПроверь на реальном сервере вручную:\n"+
            "1. Движение по диагонали\n2. Поворот прицеливания, не отпуская движение\n"+
            "3. Удержание A\n4. Слоты 1–4\n5. Открытие инвентаря без ложных нажатий"+
            "\n\nСчётчик — это отправка событий, не доказательство их принятия игрой.";
        new android.app.AlertDialog.Builder(this).setTitle("ELYXION · Проверка ввода")
            .setMessage(info)
            .setPositiveButton("Поделиться JSON",(dialog,which)->shareQa())
            .setNegativeButton("Вернуться",null).show();
    }
    private void shareQa() {
        try {
            org.json.JSONObject data=new org.json.JSONObject();
            data.put("app","ELYXION COSMOS v0.7");
            data.put("testedUrl",URL);
            data.put("pageLoaded",pageLoaded);
            data.put("webViewEventsDispatched",inputEvents);
            data.put("layoutMode",layoutMode==0?"combat":layoutMode==1?"explore":"screen");
            data.put("buttonAMode",mouseAction?"mouse":"touch");
            data.put("gameAcceptedEvents",org.json.JSONObject.NULL);
            data.put("assistantReadsGameState",false);
            data.put("assistantManuallyMarkedRiskCount",survivalHud==null?0:survivalHud.markedRiskCount());
            data.put("assistantEnabled",survivalHud!=null&&survivalHud.hintsEnabled());
            data.put("note","Browser event counts are not end-to-end game confirmation");
            Intent send=new Intent(Intent.ACTION_SEND);send.setType("application/json");
            send.putExtra(Intent.EXTRA_TEXT,data.toString(2));
            startActivity(Intent.createChooser(send,"Отправить отчёт COSMOS"));
        }catch(Exception ex){Toast.makeText(this,"Отчёт недоступен",Toast.LENGTH_SHORT).show();}
    }
    private void setLayoutMode(int mode) {
        // No simulated input remains held while menus and game UI gain focus.
        releaseKeys();
        layoutMode=mode;
        boolean playing=mode!=2;
        moveStick.setVisibility(playing?View.VISIBLE:View.GONE);
        aimStick.setVisibility(mode==0?View.VISIBLE:View.GONE);
        buttons.setVisibility(playing?View.VISIBLE:View.GONE);
        quickSlots.setVisibility(playing?View.VISIBLE:View.GONE);
        if(aim!=null)aim.setVisibility(playing?View.VISIBLE:View.GONE);
        if(survivalHud!=null)survivalHud.setPlaying(playing);
        combatControl.setTextColor(mode==0?accent:Color.WHITE);
        exploreControl.setTextColor(mode==1?accent:Color.WHITE);
        screenControl.setTextColor(mode==2?accent:Color.WHITE);
        status.setText(mode==0?"БОЙ · ДВИЖЕНИЕ + ПРИЦЕЛ":
                mode==1?"ПОХОД · ЛЁГКОЕ УПРАВЛЕНИЕ":"ЭКРАН · КАСАНИЯ МЕНЮ");
    }
    private void onAimStick(float x,float y) {
        if(layoutMode!=0||web==null) return;
        // Joystick release does not reset aim, so the player can keep targeting.
        if(!Float.isFinite(x)||!Float.isFinite(y)||Math.hypot(x,y)<.14)return;
        float[] target=AimMath.target(x,y,web.getWidth(),web.getHeight(),.36f);
        aimX=target[0];aimY=target[1];
        placeAim();
        long now=SystemClock.uptimeMillis();
        if(now-lastAimDispatchMs>=16){lastAimDispatchMs=now;sendAimMotion();}
    }
    private void sendAimMotion() {
        if(!mouseAction||web==null||web.getWidth()<1||web.getHeight()<1)return;
        long now=SystemClock.uptimeMillis();
        MotionEvent.PointerProperties pp=new MotionEvent.PointerProperties();pp.id=0;pp.toolType=MotionEvent.TOOL_TYPE_MOUSE;
        MotionEvent.PointerCoords pc=new MotionEvent.PointerCoords();
        pc.x=web.getWidth()*aimX;pc.y=web.getHeight()*aimY;pc.size=1f;pc.pressure=tapping?1f:0f;
        MotionEvent e=MotionEvent.obtain(tapping?tapDownTime:now,now,
                tapping?MotionEvent.ACTION_MOVE:MotionEvent.ACTION_HOVER_MOVE,1,
                new MotionEvent.PointerProperties[]{pp},new MotionEvent.PointerCoords[]{pc},
                0,tapping?MotionEvent.BUTTON_PRIMARY:0,1f,1f,0,0,InputDevice.SOURCE_MOUSE,0);
        if(tapping)web.dispatchTouchEvent(e);else web.dispatchGenericMotionEvent(e);
        inputEvents++;e.recycle();
    }
    private void sendHotbar(int slot) {
        if(web==null||slot<1||slot>4)return;
        int key=KeyEvent.KEYCODE_1+slot-1;
        long now=SystemClock.uptimeMillis();
        web.requestFocus();
        web.dispatchKeyEvent(new KeyEvent(now,now,KeyEvent.ACTION_DOWN,key,0,0,
                KeyCharacterMap.VIRTUAL_KEYBOARD,0,0,InputDevice.SOURCE_KEYBOARD));
        web.dispatchKeyEvent(new KeyEvent(now,now+1,KeyEvent.ACTION_UP,key,0,0,
                KeyCharacterMap.VIRTUAL_KEYBOARD,0,0,InputDevice.SOURCE_KEYBOARD));
        inputEvents+=2;
        status.setText("СЛОТ "+slot+" → WEBVIEW · ПРИЁМ НЕ ПОДТВЕРЖДЁН");
    }
    private void onStick(float x,float y) {
        int next = directions.update(x,y);
        int before=keyState;
        if(before==next)return;
        // Stop old directions before engaging new ones to avoid accidental opposites.
        for(int i=0;i<4;i++)if((before&bits[i])!=0&&(next&bits[i])==0)sendKey(codes[i],false,i);
        for(int i=0;i<4;i++)if((before&bits[i])==0&&(next&bits[i])!=0)sendKey(codes[i],true,i);
        keyState=next;
    }
    private void sendKey(int code,boolean down,int keyIndex) {
        if(web==null)return;
        long now=SystemClock.uptimeMillis();
        long start;
        if(keyIndex>=0&&keyIndex<4){if(down)keyDownTimes[keyIndex]=now;start=keyDownTimes[keyIndex];}
        else start=now;
        KeyEvent event=new KeyEvent(start,now,down?KeyEvent.ACTION_DOWN:KeyEvent.ACTION_UP,code,0,0,KeyCharacterMap.VIRTUAL_KEYBOARD,0,0,InputDevice.SOURCE_KEYBOARD);
        web.requestFocus();web.dispatchKeyEvent(event);inputEvents++;
        if (status != null) status.setText("WASD → WEBVIEW · РЕАКЦИЯ ИГРЫ НЕИЗВЕСТНА");
    }
    private void setEKey(boolean down) {
        if(web==null || down==actionEHeld) return;
        long now=SystemClock.uptimeMillis();
        if(down)eDownTime=now;
        KeyEvent e=new KeyEvent(eDownTime,now,down?KeyEvent.ACTION_DOWN:KeyEvent.ACTION_UP,
                KeyEvent.KEYCODE_E,0,0,KeyCharacterMap.VIRTUAL_KEYBOARD,0,0,InputDevice.SOURCE_KEYBOARD);
        web.requestFocus();web.dispatchKeyEvent(e);inputEvents++;
        actionEHeld=down;
    }
    private void sendAimTap(boolean down) {
        if(web==null || web.getWidth()<1 || web.getHeight()<1)return;
        if(down)tapDownTime=SystemClock.uptimeMillis();
        if(!down&&!tapping)return;
        long now=SystemClock.uptimeMillis();
        MotionEvent event;
        if (mouseAction) {
            // Native mouse-pointer event; no JavaScript injection or automated clicking.
            MotionEvent.PointerProperties pp = new MotionEvent.PointerProperties();
            pp.id = 0; pp.toolType = MotionEvent.TOOL_TYPE_MOUSE;
            MotionEvent.PointerCoords pc = new MotionEvent.PointerCoords();
            pc.x = web.getWidth() * aimX; pc.y = web.getHeight() * aimY;
            pc.pressure = down ? 1f : 0f; pc.size = 1f;
            event = MotionEvent.obtain(tapDownTime, now,
                down ? MotionEvent.ACTION_DOWN : MotionEvent.ACTION_UP,
                1, new MotionEvent.PointerProperties[]{pp},
                new MotionEvent.PointerCoords[]{pc}, 0,
                down ? MotionEvent.BUTTON_PRIMARY : 0, 1f, 1f,
                0, 0, InputDevice.SOURCE_MOUSE, 0);
        } else {
            event = MotionEvent.obtain(tapDownTime, now,
                down ? MotionEvent.ACTION_DOWN : MotionEvent.ACTION_UP,
                web.getWidth()*aimX, web.getHeight()*aimY, 0);
            event.setSource(InputDevice.SOURCE_TOUCHSCREEN);
        }
        web.dispatchTouchEvent(event);inputEvents++;
        event.recycle(); tapping=down;
        if (status != null) status.setText("A → WEBVIEW · РЕАКЦИЯ ИГРЫ НЕИЗВЕСТНА");
    }
    private void placeAim() {
        if(aim==null||web==null)return;
        FrameLayout.LayoutParams p=(FrameLayout.LayoutParams)aim.getLayoutParams();
        p.leftMargin=Math.max(0,Math.round(web.getWidth()*aimX)-dp(19));
        p.topMargin=Math.max(dp(35),Math.round(web.getHeight()*aimY)-dp(19));
        aim.setLayoutParams(p);
    }
    private void releaseKeys() {
        for(int i=0;i<4;i++)if((keyState&bits[i])!=0)sendKey(codes[i],false,i);
        keyState=0;directions.release();sendAimTap(false);
        setEKey(false);
    }
    private void openChrome() {
        releaseKeys();
        try {startActivity(new Intent(Intent.ACTION_VIEW,Uri.parse(URL)));}catch(Exception ignored){}
    }
    @Override public void onBackPressed() {
        releaseKeys();
        if(web!=null && web.canGoBack())web.goBack();else super.onBackPressed();
    }
    @Override protected void onPause(){if(survivalHud!=null)survivalHud.pause();releaseKeys();if(web!=null)web.onPause();super.onPause();}
    @Override protected void onResume(){super.onResume();if(web!=null)web.onResume();if(survivalHud!=null)survivalHud.resume();}
    @Override protected void onDestroy(){if(survivalHud!=null)survivalHud.destroy();releaseKeys();if(web!=null){root.removeView(web);web.destroy();web=null;}super.onDestroy();}
    private int dp(float x){return Math.round(x*getResources().getDisplayMetrics().density);}
}
