public class StudentProfile {
	String fName;
	String lName;
	String major;
	int gradYear;
	int studentId;
	double numCredits;
	double gpa;

	public StudentProfile(String fName, String lName, String major,
							int gradYear, int studentId,
							double numCredits, double gpa) {
							// Assign attributues
							this.fName = fName;
							this.lName = lName;
							this.major = major;
							this.studentId = studentId;
							this.gradYear = gradYear;
							this.numCredits = numCredits;
							this.gpa = gpa;
							}
	
	public String Describe() {
		String description = this.fName + " " + this.lName + "is a " + this.major
			+ " major with student ID " + this.studentId + "and a " + this.gpa
			+ " GPA graduating in " + this.gradYear + ".";
		return description;
	}

	public double RemainingCredits() {
		// Need 120 credits to graduate
		double res = 0.00;
		if (this.numCredits <= 120) {
			res = 120 - this.numCredits;
		}
		return res;
	}

	// Based on this GPA calculator: https://gpacalculator.net/wp-content/uploads/2012/07/grade-point-equivalent.png
	public String Grade() {
		if (this.gpa > 3.67) {return "A";} else if
		(this.gpa > 3.33) {return "A-";} else if
		(this.gpa > 3.00) {return "B+";} else if
		(this.gpa > 2.67) {return "B-";} else if
		(this.gpa > 2.33) {return "C+";} else if
		(this.gpa > 2.00) {return "C";} else if
		(this.gpa > 1.00) {return "D";} else
		{return "F";}
	}

	public int IncrementGradYear() {
		this.gradYear += 1;
		return this.gradYear;
	}

	public static void main(String[] args) {
		StudentProfile Shif = new StudentProfile("Shifra", "Isaacs", "BAIT",
								2022, 192008440, 122.0, 3.827);
		StudentProfile Moshe = new StudentProfile("Moshe", "Gutfreund", "Finance",
		2024, 613613613, 75.0, 4.00);

		int newMosheGradYear = Moshe.IncrementGradYear();
		System.out.println(newMosheGradYear);

		double ShifCredsLeft = Shif.RemainingCredits();
		System.out.println("Shifra has " + ShifCredsLeft + " credits left before graduation!");
	}
}