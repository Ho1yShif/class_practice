import java.util.Scanner;

public class Scoping {
	public static void main(String[] args) {
		// Understanding variable scope in Java
		System.out.println("Pick a number between 1 and 5:");
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();
		input.close();

		// If we create a variable outside the if block, it can be accessed from the else block!
		String favoriteFood = "chocolate";
		// If we print this in the if block, we'll see the new value of pasta
		// If we print it in the else block, we'll see the old value of chocolate

		if (num <= 3) {
			favoriteFood = "pasta";
			System.out.println(favoriteFood);
		} else {
			System.out.println(favoriteFood);
			// Error: favoriteFood can't be resolved to a variable
		}
		
	}
}