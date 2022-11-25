import java.util.Scanner;

public class Switch {
	public static void main(String[] args) {
		// Challenge: Create a multiple choice question to practice if-else control flow
		// My response: learn switch statements instead

		String question = """
				Which programming language is the most intuitive?
				A) Java
				B) Python
				C) Brain****
				D) JavaScript

				Please enter A/B/C/D as your answer.
				""";
		System.out.println(question);
		Scanner input = new Scanner(System.in);
		String answer = input.next();

		// Matching lowercase responses for each answer option
		switch (answer.toLowerCase()) {
			case "a":
				System.out.println("Nope! Java is pretty hard if you're a beginner. Try again!");
				break;
			case "b":
				System.out.println("That's correct! Great job!");
				break;
			case "c":
				System.out.println("What the **** is wrong with you. Try again!");
				break;
			case "d":
				System.out.println("Sure– the === operator is sooo intuitive. Try again!");
				break;
		}

		input.close();
	}
}