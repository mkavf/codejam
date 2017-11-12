import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class B {

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

        int t = in.nextInt();
        for (int ti = 0; ti < t; ti++) {
            int[] res = new B().solveCase(in);
            System.out.println("Case #" + (ti + 1) + ": " + res[0] + " " + res[1]);
        }
    }

    private int[] solveCase(Scanner in){
        int turnaround = in.nextInt();
        in.nextLine();

        int na = in.nextInt();
        int nb = in.nextInt();
        in.nextLine();


        Queue<Integer> startFromA = new PriorityQueue<>();
        Queue<Integer> startFromB = new PriorityQueue<>();

        Queue<Integer> availableAtA = new PriorityQueue<>();
        Queue<Integer> availableAtB = new PriorityQueue<>();

        for (int i = 0; i < na; i++){
            String[] tripTimes = in.nextLine().split(" ");
            processTime(startFromA, availableAtB, tripTimes, turnaround);
        }

        for (int i = 0; i < nb; i++){
            String[] tripTimes = in.nextLine().split(" ");
            processTime(startFromB, availableAtA, tripTimes, turnaround);
        }

        return new int[] {solveForStation(startFromA, availableAtA), solveForStation(startFromB, availableAtB)};
    }

    private int solveForStation(Queue<Integer> startQ, Queue<Integer> availableQ) {
        int count = 0;

        while (startQ.size() > 0){
            Integer start = startQ.poll();

            Integer available = availableQ.peek();

            if (available != null && available <= start){
                availableQ.poll();
            }else{
                count++;
            }
        }

        return count;
    }

    private void processTime(Queue<Integer> startQ, Queue<Integer> availableQ,
                                    String[] tripTime, int turnaround) {

        Integer start = timeToMinutes(tripTime[0]);
        Integer end = timeToMinutes(tripTime[1]);

        startQ.add(start);
        availableQ.add(end + turnaround);
    }

    private int timeToMinutes(String tripTime) {
        String[] time = tripTime.split(":");

        return Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
    }
}