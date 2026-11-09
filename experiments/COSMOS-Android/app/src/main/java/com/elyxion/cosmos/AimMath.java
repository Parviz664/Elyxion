package com.elyxion.cosmos;

/** Pure Java manual aim geometry; no game code or screen injection. */
public final class AimMath {
    private AimMath() { }
    public static float[] target(float x,float y,int width,int height,float fraction) {
        if(width<=0||height<=0||!Float.isFinite(x)||!Float.isFinite(y))return new float[]{.5f,.5f};
        double len=Math.hypot(x,y);
        if(len>1){x=(float)(x/len);y=(float)(y/len);}
        float span=Math.max(.12f,Math.min(.44f,Float.isFinite(fraction)?fraction:.36f));
        float radius=Math.min(width,height)*span;
        float tx=.5f+x*radius/width,ty=.5f+y*radius/height;
        return new float[]{Math.max(.05f,Math.min(.95f,tx)),Math.max(.05f,Math.min(.95f,ty))};
    }
}
