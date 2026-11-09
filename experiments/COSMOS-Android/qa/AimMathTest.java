import com.elyxion.cosmos.AimMath;
public final class AimMathTest {
    static int tests=0;
    static void near(float expected,float actual){if(Math.abs(expected-actual)>.0005)throw new AssertionError(expected+" vs "+actual);tests++;}
    static void check(boolean c){if(!c)throw new AssertionError();tests++;}
    public static void main(String[] args){
        float[] a=AimMath.target(0,0,1000,400,.36f);near(.5f,a[0]);near(.5f,a[1]);
        a=AimMath.target(1,0,1000,400,.36f);near(.644f,a[0]);near(.5f,a[1]);
        a=AimMath.target(0,-1,1000,400,.36f);near(.5f,a[0]);near(.14f,a[1]);
        a=AimMath.target(1,1,1000,400,.36f);check(a[0]>.5f);check(a[1]>.5f);
        check(Math.hypot((a[0]-.5f)*1000,(a[1]-.5f)*400)<=144.01);
        a=AimMath.target(Float.NaN,0,1000,400,.36f);near(.5f,a[0]);near(.5f,a[1]);
        a=AimMath.target(1,0,0,0,.36f);near(.5f,a[0]);near(.5f,a[1]);
        a=AimMath.target(1000,0,1000,400,.9f);check(a[0]<=.95f);check(a[0]>=.5f);
        a=AimMath.target(-1,0,100,100,.36f);near(.14f,a[0]);
        System.out.println("Aim geometry: "+tests+" PASS");
    }
}
