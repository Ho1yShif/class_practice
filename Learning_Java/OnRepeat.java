import java.util.Scanner;

public class OnRepeat {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		boolean isOnRepeat = true;

	while (isOnRepeat) {
		System.out.println("Your favorite song is playing again!");
		System.out.println("Playing current song. Would you like to take this song off repeat? (y/n)");
		String userInput = input.next();

		if (userInput.toLowerCase().equals("y")) {
			isOnRepeat = false;
		}
	
	System.out.println("Playing next song!");
	}
	}
}