import java.util.Scanner;

/**
 * Created by Rosario on 20.03.14.
 */
public class SCCTest {
    public static void main(String[] args) {
        DirectedGraph graph = new DirectedGraph(new Scanner(System.in));
        SCC scc = new SCC(graph);

        System.out.println(scc.count() + " different SCCs");
        int i = 0;
        for (Iterable<Integer> s : scc.getSCCs()) {
            System.out.print(i + ": [ ");
            for (Integer x : s) {
                System.out.print(x + " ");
            }
            System.out.println("]");
            ++i;
        }
    }
}