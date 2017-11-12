import java.util.*;
import java.io.*;

public class A {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

        int t = in.nextInt();
        for (int ti = 0; ti < t; ti++) {
            System.out.println("Case #" + (ti + 1) + ": " + new A().solveCase(in));
        }
    }

    private int solveCase(Scanner in){
        Set<String> engines = new HashSet<>();
        Set<String> queries = new HashSet<>();

        int s = in.nextInt();
        in.nextLine();

        for (int i = 0; i < s; i++) {
            String engine = in.nextLine();
            engines.add(engine);
        }

        int q = in.nextInt();
        in.nextLine();

        int count = 0;
        for (int j = 0; j < q; j++) {
            String query = in.nextLine();
            queries.add(query);

            if (queries.size() == engines.size()){
                count++;
                queries.clear();
                queries.add(query);
            }
        }

        return count;
    }
}