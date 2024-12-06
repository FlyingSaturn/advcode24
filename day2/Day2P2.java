import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;

class Day2P2 {
    public static void main(String args[]) {
        int safe = 0;
        try {
            Scanner sc = new Scanner(new File("input_day2.txt"));
            outer: while (sc.hasNextLine()) {
                // Taking inputs
                String line = sc.nextLine();
                ArrayList < Integer > report = new ArrayList < Integer > ();
                Scanner in = new Scanner(line);
                while (in.hasNextInt()) {
                    int i = in .nextInt();
                    report.add(i);
                } in.close();

                // Main logic
                if ((new Day2P2()).consistent(report))
                    safe++;
                else if ((new Day2P2()).consideration(report))
                    safe++;
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("Sorry, file not found.");
            e.printStackTrace();
            System.exit(1);
        }
        System.out.println(safe);
    }
    boolean consistent(ArrayList < Integer > report) {
        int secondlast = report.get(0);
        int last = report.get(1);
        for (int i = 2; i < report.size(); i++) {
            int sign = (int) Math.signum(last - secondlast);
            int diff = report.get(i) - last;
            // All increasing or decreasing, so no inflection points or no unevenness 
            if (sign == 0 || sign != Math.signum(diff))
                return false;
            // Atleast 1 or atmost 3, which means NOT greater equals 4 (because we are ensuring that there's always increase or decrease
            if (Math.abs(last - secondlast) >= 4 || Math.abs(diff) >= 4)
                return false;
            secondlast = last;
            last = report.get(i);
            sign = (int) Math.signum(diff);
        }
        return true;
    }

    boolean consideration(ArrayList < Integer > arr) {
        for (int i = 0; i < arr.size(); ++i) {
            ArrayList < Integer > arr1 = new ArrayList < Integer > (arr);
            arr1.remove(i);
            if (consistent(arr1))
                return true;
            // We are just calculating THE POSSIBILITY, not finding every possible permutations. It's JUST true lol
            // Thanks to https://github.com/helenzhangyc/aoc2024/blob/main/Day%202%20Red-Nosed%20Reports/d2p2.cpp
        }
        return false;
    }
}
