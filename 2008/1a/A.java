import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

import static java.util.stream.Collectors.toList;

public class A {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

        int t = in.nextInt();
        for (int ti = 0; ti < t; ti++) {
            in.nextInt();
            in.nextLine();

            List<Long> a = Arrays.stream(in.nextLine().split(" "))
                    .map(Long::parseLong)
                    .collect(toList());

            List<Long> b = Arrays.stream(in.nextLine().split(" "))
                    .map(Long::parseLong)
                    .collect(toList());

            System.out.println("Case #" + (ti + 1) + ": " + new A().solveCase(a, b));
        }
    }

    private long solveCase(List<Long> a, List<Long> b){
        Queue<Long> aQ = new PriorityQueue<>();
        aQ.addAll(a);

        Queue<Long> bQ = new PriorityQueue<>(Comparator.reverseOrder());
        bQ.addAll(b);

        long sum = 0;

        while (aQ.size() > 0) {
            sum += aQ.poll() * bQ.poll();
        }

        return sum;
    }
}