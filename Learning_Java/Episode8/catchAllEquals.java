package Episode8;

import java.util.Scanner;

public class catchAllEquals {
	public static void main(String[] args) {
	System.out.println("How many hours have you spent watching Vlogbrothers videos?");
	Scanner scan = new Scanner(System.in);
	int vlogbrosWatchTime = scan.nextInt();

	// Conditional statement
	if (vlogbrosWatchTime == 100) {
		System.out.println("You're a Nerdfighter!");
	} else {
		System.out.println("You're not a Nerdfighter yet!");
	}

	scan.close();
	} 
}