import java.util.Scanner;

public class StringInput {
	// Name
	public static void main(String[] args) {
	System.out.println("Enter your first name ");
	Scanner scan = new Scanner(System.in);
	String scanWord = scan.next();
	System.out.println(scanWord);

	// Dummy nextline
	scan.nextLine();
	
	// Sentence
	System.out.println("Enter a full sentence");
	String scanLine = scan.nextLine();
	System.out.println(scanLine);
	scan.close();
	} 
}