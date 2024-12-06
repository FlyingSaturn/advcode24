import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;

class Day2P1
{
        public static void main(String args[])
        {
            int safe = 0;
            try
            {
                Scanner sc = new Scanner(new File("../inputs/input_day2.txt"));                
                outer:while(sc.hasNextLine())
                {
                    // Taking inputs
                    String line = sc.nextLine();
                    ArrayList<Integer> report = new ArrayList<Integer>();
                    Scanner in = new Scanner(line);
                    while (in.hasNextInt())
                    {
			int i = in.nextInt();
                        report.add(i);
                    }
                    in.close();

                    // Main logic
                    int secondlast = report.get(0);
                    int last = report.get(1);
                    for (int i = 2; i < report.size(); i++)
                    {
                        int sign = (int)Math.signum(last - secondlast);
			int diff = report.get(i) - last;
                        // All increasing or decreasing, so no inflection points or no unevenness 
                        if (sign == 0 || sign != Math.signum(diff))
                            continue outer;
                        // Atleast 1 or atmost 3, which means NOT greater equals 4 (because we are ensuring that there's always increase or decrease
                        if (Math.abs(last - secondlast) >= 4 || Math.abs(diff) >= 4)
                            continue outer;
			secondlast = last;
			last = report.get(i);
			sign = (int)Math.signum(diff);
                    }
                    safe++;
                }
                sc.close();
            }
            catch (FileNotFoundException e)
            {
                System.out.println("Sorry, file not found.");
                e.printStackTrace();
                System.exit(1);
            }
            System.out.println(safe);
        }
}
