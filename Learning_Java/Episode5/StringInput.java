package Episode5;
import java.util.Scanner;

public class StringInput {
	// Name
	public static void main(String[] args) {
	System.out.println("Enter your first name ");
	Scanner scan = new Scanner(System.in);
	String scanName = scan.next();
	System.out.println(scanName);

	// Dummy nextline
	scan.nextLine();
	
	// Sentence
	System.out.println("Enter a full sentence");
	String scanLine = scan.nextLine();
	System.out.println(scanLine);
	scan.close();
	} 
}