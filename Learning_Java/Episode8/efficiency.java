package Episode8;

import java.util.Scanner;

public class efficiency {
	public static void main(String[] args) {
	
	// Improve efficiency by avoiding calculations when input is 1
	System.out.println("Enter an integer:");
	Scanner scan = new Scanner(System.in);
	int num = scan.nextInt();

	if (num == 1) {
		System.out.println(1);
	} else {
		// Perform calculation after check
		System.out.println(num * num);
	}

	scan.close();
	} 
}