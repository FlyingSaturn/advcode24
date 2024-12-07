import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

class Day4P2 {
  ArrayList < ArrayList < Character >> pg = new ArrayList < > ();
  int S;
  Day4P2(String filepath) {
    S = 0;
    try {
      Scanner sc = new Scanner(new File(filepath));
      while (sc.hasNextLine()) {
        // Taking inputs
        String line = sc.nextLine();
        int l = line.length();
        ArrayList < Character > row = new ArrayList < > ();
        for (int i = 0; i < l; i++) {
          row.add(line.charAt(i));
        }
        pg.add(row);
      }
    } catch (FileNotFoundException e) {
      System.out.println("Sorry, file not found.");
      e.printStackTrace();
      System.exit(1);
    }

  }

  public static void main(String args[]) {
    Day4P2 obj = new Day4P2("../inputs/input_day4.txt");
    obj.poscheck();
    System.out.println(obj.S);
  }

  void poscheck() {
    // Avoiding the boundaries because of X-MAS
    int m = pg.size() - 1;
    for (int i = 1; i < m; i++) {
      int n = pg.get(i).size() - 1;
      for (int j = 1; j < n; j++)
        checker(i, j);
    }
  }
  void checker(int i, int j) {
    if (pg.get(i).get(j) != 'A')
      return;
    int f = 0;
    // Principal diagonal, M above
    if (pg.get(i - 1).get(j - 1) == 'M' && pg.get(i + 1).get(j + 1) == 'S')
      f++;
    // Principal diagonal, S above
    else if (pg.get(i - 1).get(j - 1) == 'S' && pg.get(i + 1).get(j + 1) == 'M')
      f++;
    // Non-principal diagonal, M above
    if (pg.get(i - 1).get(j + 1) == 'M' && pg.get(i + 1).get(j - 1) == 'S')
      f++;
    // Non-principal diagonal, M above
    else if (pg.get(i - 1).get(j + 1) == 'S' && pg.get(i + 1).get(j - 1) == 'M')
      f++;
    if (f == 2)
        S++;
  }
}
