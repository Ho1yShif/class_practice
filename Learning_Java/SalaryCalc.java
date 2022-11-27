import java.util.Scanner;

public class SalaryCalc {
	// Practice simple function: announcement with print statement
	public static void announcement() {
		System.out.println("Waiting for announcement...");
		System.out.println("Enter anything below to see the announcement!");
		
		Scanner input = new Scanner(System.in);
		input.next();
		System.out.println("PSA: I wish I got a CompSci degree!");
	}
	
	// Practice simple meal price calculation [with a non-void return value]
	public static double calcMealPrice(double mealPrice, double tipRate, double taxRate) {
		double tip = tipRate * mealPrice;
		double tax = taxRate * mealPrice;
		double total = tip + tax + mealPrice;
		System.out.println("The total cost of your meal is $" + total);
		return total;
	}

	// Practice nested functions by dividing total meal price
	public static double splitBill(double totalPrice, int numPeople) {
		double individual = totalPrice / numPeople;
		System.out.println("The cost per person for your meal is $" + individual);
		return individual;
	}

	public static double calcSalary(int weeklyHours, double hourlyRate, int vacationDays) {
		if (weeklyHours <= 0 || hourlyRate <= 0){
			return -1;
		}
		
		// Assume the employee has unpaid vacation and each vacation day is 8 hours of work
		double unpaidTime = vacationDays * hourlyRate * 8;
		double salary = (weeklyHours * hourlyRate * 52) - unpaidTime;
		System.out.println("The annual salary is: $" + salary);
		return salary;
	}

	public static void main(String[] args) {
		// splitBill(calcMealPrice(20.00, 0.15, 0.05), 3);
		double res = calcSalary(40, 52.88, 8);
		System.out.println(res);
	}
}