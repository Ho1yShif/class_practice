package Episode5;
// Got this code from chatGPT!

import java.io.IOException;

public class StandardIn {
  public static void main(String[] args) {
    try {
      // Read a single byte of input from the user
      int input = System.in.read();

      // Print the byte to the console
      System.out.println("You entered: " + input);
    } catch (IOException e) {
      // Handle any IO exceptions that might occur
      System.err.println("An error occurred while reading input: " + e.getMessage());
    }
  }
}
