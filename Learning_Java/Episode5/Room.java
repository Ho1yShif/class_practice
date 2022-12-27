package Episode5;
import java.util.Scanner;

public class Room {
	public static void main(String[] args) {
	// Goal: Find the area of a room in square feet

	System.out.println("How many books has John Green published?");
	Scanner scan = new Scanner(System.in);
	
	int roomLength = scan.nextInt();
	System.out.println(roomLength);

	double roomWidth = scan.nextInt();
	System.out.println(roomWidth);

	double roomArea = roomLength * roomArea;
	scan.close();
	} 
}