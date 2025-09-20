
/**
 * Prime Number Checker - Java Implementation
 *
 * This program provides an interactive prime number checking utility that allows users
 * to input positive integers and determine whether they are prime numbers. The program
 * uses an optimized trial division algorithm and continues execution until the user
 * enters a non-positive number.
 *
 * @author Calvin Malagon
 * @version 1.0
 * @since 2025
 */
import java.util.Scanner;

/**
 * Main class containing the prime number checking functionality.
 *
 * This class provides both the core prime checking algorithm and the user
 * interface for interactive prime number testing.
 */
public class Prime {

    /**
     * Determines whether a given integer is a prime number using an optimized
     * trial division algorithm.
     *
     * @param n the integer to test for primality
     * @return true if the number is prime, false otherwise
     */
    public static boolean isPrime(int n) {
        // Handle edge cases: numbers ≤ 1 are not prime by mathematical definition
        if (n <= 1) {
            return false;
        }

        // Handle small primes: 2 and 3 are the only primes ≤ 3
        if (n <= 3) {
            return true;
        }

        // Eliminate even numbers and multiples of 3
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        // Check for factors from 5 to √n, skipping even numbers
        for (int i = 5; i * i <= n; i += 6) {
            // Check both 6k-1 and 6k+1 forms in the same iteration
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }

        // No factors found, number is prime
        return true;
    }

    /**
     * Main entry point for the prime number checking application.
     *
     * @param args command-line arguments (not used in this implementation)
     */
    public static void main(String[] args) {
        // Initialize scanner for user input
        Scanner scanner = new Scanner(System.in);
        int number; // Variable to store the processed input number

        // Main program loop - continues until user enters non-positive number
        do {
            System.out.print("Enter a positive number (0 or negative to exit): ");

            // Attempt to read input as integer first (most common case)
            if (scanner.hasNextInt()) {
                number = scanner.nextInt();
            } // Handle floating-point input with C++ compatible truncation behavior
            else if (scanner.hasNextDouble()) {
                // If it's a double/float, truncate it to int (same as C++ behavior)
                double temp = scanner.nextDouble();
                number = (int) temp;  // Truncates the decimal part
            } // Handle invalid input types
            else {
                // Skip invalid input and continue to next iteration
                scanner.next();
                continue;
            }

            // Check for exit condition - terminate if number is non-positive
            if (number <= 0) {
                break;
            }

            // Perform prime check and display appropriate result message
            if (isPrime(number)) {
                System.out.println(number + " is a prime number.");
            } else {
                System.out.println(number + " is not a prime number.");
            }

        } while (true); // Loop continues until break statement is reached

        // Clean up resources before program termination
        scanner.close();
    }
}
