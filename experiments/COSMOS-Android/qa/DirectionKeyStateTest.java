import com.elyxion.cosmos.DirectionKeyState;
public final class DirectionKeyStateTest {
    static int count=0;
    static void eq(int exp,int actual){if(exp!=actual)throw new AssertionError("Expected " +exp+ " got "+actual);count++;}
    public static void main(String[] args){
        DirectionKeyState m=new DirectionKeyState();
        eq(0,m.state());eq(1,m.update(0,-1));eq(1,m.update(0,-.29f));eq(0,m.update(0,-.1f));
        eq(3,m.update(-1,-1));eq(8,m.update(1,0));eq(4,m.update(0,1));eq(0,m.release());
        eq(0,m.update(Float.NaN,0));eq(0,m.update(Float.POSITIVE_INFINITY,0));
        eq(0,m.update(.20f,0));eq(8,m.update(.41f,0));eq(8,m.update(.26f,0));eq(0,m.update(.21f,0));
        // Fuzz diagonal transitions, switching directions, and neutral release.
        java.util.Random random=new java.util.Random(6092026L);
        for(int i=0;i<2500;i++) {
            float x=random.nextFloat()*2f-1f;
            float y=random.nextFloat()*2f-1f;
            int mask=m.update(x,y);
            if((mask&5)==5||(mask&10)==10)throw new AssertionError("Opposite keys pressed: "+mask);
            count++;
        }
        eq(0,m.release());eq(0,m.state());eq(0,m.update(0,0));
        System.out.println("Directional key mapping and 2500 transitions: "+count+" PASS");
    }
}
