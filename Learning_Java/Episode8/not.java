package Episode8;

import java.util.Scanner;

public class not {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	System.out.println("How many books by the Green brothers have you read?");
	int greenBooksRead = scan.nextInt();

	// NOT operator
	if (!(greenBooksRead == 0)) {
		System.out.println("You're a Nerdfighter!");
	} else {
		System.out.println("You're not a Nerdfighter yet!");
	}

	scan.close();
	}
}