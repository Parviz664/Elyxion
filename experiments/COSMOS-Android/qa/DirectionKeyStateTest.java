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
        System.out.println("Directional key mapping: "+count+" PASS");
    }
}
