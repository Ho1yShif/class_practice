import java.util.Scanner;

public class DoubleInput {
	// Name
	public static void main(String[] args) {
	// Int
	System.out.println("What was your GPA in college on a scale of 0.0 to 4.0?");
	Scanner scan = new Scanner(System.in);
	double scanDouble = scan.nextDouble();
	System.out.println(scanDouble);
	scan.close();
	} 
}