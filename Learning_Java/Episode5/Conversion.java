package Episode5;
public class Conversion {
	public static void main(String[] args) {

		// Conversion: at runtime
		int x = 3;
		System.out.println(x / 7.0);

		// Casting: explicit with functions
		String y = String.valueOf(x);
		System.out.println(y);

		// Coercion is the compiler, not the programmer
		System.out.println("Hello " +x);
	}
}