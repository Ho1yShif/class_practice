package Episode5;
import java.util.Scanner;

public class Room {
	public static void main(String[] args) {
	// Goal: Find the area of a room in square feet

	// Fix this part
	System.out.println("What is the length of your room?");
	Scanner scan = new Scanner(System.in);
	int roomLength = scan.nextInt();

	System.out.println("What is the width of your room?");
	double roomWidth = scan.nextInt();

	double roomArea = roomLength * roomWidth;
	System.out.println("The area of your room is " + roomArea + "in square feet");
	scan.close();
	} 
}