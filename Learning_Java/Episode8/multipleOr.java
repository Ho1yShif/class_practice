package Episode8;

import java.util.Scanner;

public class multipleOr {
	public static void main(String[] args) {
	System.out.println("How many hours have you spent watching Vlogbrothers videos?");
	Scanner scan = new Scanner(System.in);
	int vlogbrosWatchTime = scan.nextInt();

	System.out.println("How many books by the Green brothers have you read?");
	int greenBooksRead = scan.nextInt();

	// OR operator
	if (vlogbrosWatchTime >= 100 || greenBooksRead > 0) {
		System.out.println("You're a Nerdfighter!");
	} else {
		System.out.println("You're not a Nerdfighter yet!");
	}

	scan.close();
	}
}