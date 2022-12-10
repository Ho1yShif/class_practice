import java.util.Scanner;

public class Episode5 {
	public static void main(String[] args) {

	System.out.println("Enter your first name ");
	Scanner scan = new Scanner(System.in);
	String scanFirstWord = scan.next();
	System.out.println(scanFirstWord);

	System.out.println("Enter a full sentence");
	String scanLine = scan.nextLine();
	System.out.println(scanLine);
	scan.close();
	} 
}
