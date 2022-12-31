package Episode8;

import java.util.Scanner;

public class not {
	public static void main(String[] args) {
	System.out.println("How many hours have you spent watching Vlogbrothers videos?");
	Scanner scan = new Scanner(System.in);
	int vlogbrosWatchTime = scan.nextInt();

	// NOT operator
	if (!(vlogbrosWatchTime == 100)) {
		System.out.println("You're not a Nerdfighter yet!");
	} else {
		System.out.println("You're not a Nerdfighter yet!");
	}

	scan.close();
	} 
}