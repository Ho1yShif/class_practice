import java.util.Scanner;

public class NumInput {
	// Name
	public static void main(String[] args) {
	// Int
	System.out.println("How many books has John Green published?");
	Scanner scan = new Scanner(System.in);
	int scanInt = scan.nextInt();
	System.out.println(scanInt);
	scan.close();
	} 
}