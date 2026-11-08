import com.elyxion.cosmos.AxisMath;
import com.elyxion.cosmos.InputBus;
import com.elyxion.cosmos.ProbeMath;
import java.util.Arrays;
import java.util.List;
public class NativeCoreTest {
    private static void ok(boolean test,String label){ if(!test)throw new AssertionError(label);System.out.println("PASS "+label); }
    public static void main(String[]args){
        float[] neutral=AxisMath.normalized(100,100,100,100,70);
        ok(neutral[0]==0&&neutral[1]==0,"neutral center");
        float[] right=AxisMath.normalized(200,100,100,100,70);
        ok(Math.abs(right[0]-1f)<.0001&&right[1]==0,"clamped full right");
        float[] diag=AxisMath.normalized(200,200,100,100,70);
        ok(Math.abs(Math.hypot(diag[0],diag[1])-1)<.0001,"normalized diagonal");
        float[] dead=AxisMath.normalized(104,100,100,100,70);
        ok(dead[0]==0,"8.5 percent dead zone");
        InputBus.reset(); InputBus.move(3,-4);
        ok(InputBus.x()==1&&InputBus.y()==-1,"bus clamps and transfers axis");
        InputBus.pressA(); InputBus.pressB();InputBus.pressB();
        ok(InputBus.a()==1&&InputBus.b()==2,"A and B event counters");
        InputBus.reset();ok(InputBus.x()==0&&InputBus.y()==0&&InputBus.a()==0,"bus reset");
        List<Double> d=Arrays.asList(10.0,20.0,30.0,40.0,50.0);
        ok(ProbeMath.percentile(d,.5)==30,"p50 interpolation");
        ok(Math.abs(ProbeMath.percentile(d,.95)-48)<.00001,"p95 interpolation");
        ok(ProbeMath.variability(d)==10,"consecutive variation");
        ok(Double.isNaN(ProbeMath.percentile(List.of(),.5)),"no fake samples");
        System.out.println("CORE TESTS COMPLETE");
    }
}
