import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

class Day4P2
{
	ArrayList<ArrayList<Character>> pg = new ArrayList<>();
	Day4P2(String filepath)
	{
	   try
	   {
		Scanner sc = new Scanner(new File(filepath));
		while (sc.hasNextLine())
                {
                    // Taking inputs
                    String line = sc.nextLine(); int l = line.length();
		    ArrayList<Character> row = new ArrayList<>();
		    for (int i = 0; i < l; i++)
		    {
			row.add(line.charAt(i));
		    } 
		    pg.add(row);
		}
	   }

	    catch (FileNotFoundException e)
            {
                System.out.println("Sorry, file not found.");
                e.printStackTrace();
                System.exit(1);
            }

	}
	
	public static void main(String args[])
	{
		Day4P2 obj = new Day4P2("../inputs/input_day4.txt");
		for (int i = 0; i < obj.pg.size(); i++)
		{
			int l = obj.pg.get(i).size();
			for (int j = 0; j < l; j++)
				System.out.print(obj.pg.get(i).get(j));
			System.out.println();		
		}
	}
}	

