import java.util.Scanner;

public class FortuneTeller {
	public static void main(String[] args) {
		// Designing my own fortune teller control flow
		System.out.println("Pick a number between 1 and 10:");
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();
		input.close();

		if (num < 5) {
			System.out.println("You won't have a good life, sorry");
		} else {
			System.out.println("You just won free tickets to see Paramore at MSG!");
		}
	}
}