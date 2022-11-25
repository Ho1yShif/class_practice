import java.util.Scanner;

public class Strings {
	public static void main(String[] args) {
		// Practicing concatenation data types
		String fName = "Zack";
		String lName = "Ovits";
		// System.out.println(fName + " " + lName);

		// Practicing input/output with Scanner
		System.out.println("Please enter a new first name for the last name 'Ovits'");
		Scanner input = new Scanner(System.in);
		fName = input.nextLine();
		input.close();
		System.out.println(fName + " " + lName);
	}
}