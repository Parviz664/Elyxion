import com.elyxion.cosmos.SurvivalAdvisor;

/** Behavioral checks for player-entered signals, priority, cooldown and no autonomy. */
public final class SurvivalAdvisorTest {
    private static int count;
    private static void yes(boolean condition) {
        count++;
        if (!condition) throw new AssertionError("Failed assertion " + count);
    }
    private static void eq(Object expected, Object actual) {
        count++;
        if (expected == null ? actual != null : !expected.equals(actual))
            throw new AssertionError("Expected " + expected + " got " + actual + " at " + count);
    }
    public static void main(String[] args) {
        SurvivalAdvisor a = new SurvivalAdvisor();
        yes(a.enabled());
        yes(!a.hasRisk());
        eq(null, a.priority());
        eq(null, a.offer(0,false));
        a.toggle(SurvivalAdvisor.Risk.HUNGER);
        yes(a.hasRisk());
        yes(a.isActive(SurvivalAdvisor.Risk.HUNGER));
        eq(SurvivalAdvisor.Risk.HUNGER,a.priority());
        eq(1,a.riskCount());
        eq("Голод · проверь еду и безопасное место", a.offer(1000,false));
        eq(null,a.offer(1001,false));
        eq(null,a.offer(60999,false));
        yes(a.offer(61000,false)!=null);
        a.toggle(SurvivalAdvisor.Risk.COLD);
        eq(SurvivalAdvisor.Risk.COLD,a.priority());
        eq(2,a.riskCount());
        yes(a.hint().contains("другие сигналы"));
        eq(null,a.offer(61001,false));
        yes(a.offer(61002,true)!=null);
        a.toggle(SurvivalAdvisor.Risk.PREDATOR);
        eq(SurvivalAdvisor.Risk.PREDATOR,a.priority());
        eq(3,a.riskCount());
        yes(a.hint().contains("дистанция"));
        a.setEnabled(false);
        yes(!a.enabled());
        eq(null,a.offer(200000,true));
        a.setEnabled(true);
        yes(a.enabled());
        yes(a.offer(200001,false)!=null);
        a.toggle(SurvivalAdvisor.Risk.PREDATOR);
        eq(SurvivalAdvisor.Risk.COLD,a.priority());
        a.toggle(SurvivalAdvisor.Risk.COLD);
        eq(SurvivalAdvisor.Risk.HUNGER,a.priority());
        a.toggle(SurvivalAdvisor.Risk.HUNGER);
        eq(0,a.riskCount());
        eq(null,a.priority());
        eq(null,a.offer(999999,true));
        a.toggle(SurvivalAdvisor.Risk.COLD);
        a.clear();
        yes(!a.hasRisk());
        yes(!a.isActive(SurvivalAdvisor.Risk.COLD));
        boolean threw=false;
        try { a.toggle(null); } catch (IllegalArgumentException expected) { threw=true; }
        yes(threw);
        System.out.println("SurvivalAdvisor behavioral checks: " + count + " PASS");
    }
}
