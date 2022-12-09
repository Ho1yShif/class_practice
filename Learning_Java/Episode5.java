import java.util.Scanner;

public class Episode5 {
	public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	String scanData = scan.nextLine();
	System.out.println(scanData);
	System.out.println(scanData + " is of type " + ((Object)scanData).getClass().getSimpleName());  
	String b = scan.next();
	System.out.println(b);
	scan.close();
	} 
}
