public class Triangle {
	double base;
	double height;
	double sideOne;
	double sideTwo;
	double sideThree;

	// This class constructor has no return type!
	public Triangle(double base, double height,
					double sideOne, double sideTwo, double sideThree) {
					// Assign attributes
					this.base = base;
					this.height = height;
					this.sideOne = sideOne;
					this.sideTwo = sideTwo;
					this.sideThree = sideThree;
					}
	
	// Don't use the static keyword here because static indicates NOT using the attributes
	// Here, we specifically want to use the instance attributes!
	public double findArea() {
		double area = (this.base * this.height) / 2;
		return area;
	}

	public String triangleStatus() {
		// Determine if triangle is equilateral, isosceles, or scalene
		if (this.sideOne == this.sideTwo && this.sideOne == this.sideThree) {
			return "equilateral";
		} else if (this.sideOne == this.sideTwo || this.sideOne == this.sideThree
		|| this.sideTwo == this.sideThree) {
			return "isosceles";
		} else {
			return "scalene";
		}
	}
	
	// Main function must be inside the class!
	public static void main(String[] args) {
		Triangle triangleA = new Triangle(3, 4, 3, 4, 5);
	}
}