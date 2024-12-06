import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;

class Day2P2
{
        public static void main(String args[])
        {
            int safe = 0;
            try
            {
                Scanner sc = new Scanner(new File("input_day2.txt"));                
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
		    boolean dampened = false;
                    for (int i = 0; i <= report.size()-4; i++)
                    {
			ArrayList<Integer> arr1 = new ArrayList<Integer>();
			for (int j = 0; j < 4; j++)
				arr1.add(report.get(i + j));
			int index = (new Day2P2()).consideration(arr1);
			if (index == -2)
				continue outer;
			else if (index >= 0)
			{	
				if(!dampened)
				{	
					report.remove(index);
					i--;
					dampened = true;
					continue;
				}
				else
					continue outer;	
			}
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

	boolean consistent(int secondlast, int last, int current)
	{
	int sign = (int)Math.signum(last - secondlast);
        int diff = current - last;
        // All increasing or decreasing, so no inflection points or no unevenness 
        if (sign == 0 || sign != Math.signum(diff))
        	return false;
        // Atleast 1 or atmost 3, which means NOT greater equals 4 (because we are ensuring that there's always increase or decrease
        else if (Math.abs(last - secondlast) >= 4 || Math.abs(diff) >= 4)
        	return false;
	return true;
	}

	int consideration(ArrayList<Integer> arr) 
	{
		boolean toBeDumped[] = new boolean[4];
		for(int i = 0; i < 4; i++)
		{	
			ArrayList<Integer> arr1 = new ArrayList<Integer>(arr);
			arr1.remove(i);
			if(!consistent(arr1.get(0), arr1.get(1), arr1.get(2)))
				toBeDumped[i] = true; 
				// 0 4 1 2, (4, 1, 2) inconsistent: 0 not to be dumped, (0, 1, 2) consistent: 4 to be dumped, (0, 4, 2) inconsistent, 1 not to be dumped, (0, 4, 1) inconsistent, 2 not to be dumped
		}
		int last = 0, k = 0;
		for (int i = 3; i >= 0; i--)
		{
			if (toBeDumped[i] == true)
			{
				last = i;
				k++;
			}
			if (k > 2)
				return -2;
		}
		if (k == 0)
		return -1; // Means safe without any dumping
		return last;
	}
}
