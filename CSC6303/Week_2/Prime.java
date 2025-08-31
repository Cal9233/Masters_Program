/*
 * Prime Number Checker - Java Version
 * Converted from C++ to Java
 * Author: [Your Name Here]
 * 
 * This program checks if a number is prime.
 * Exits when 0 or negative number is entered.
 * 
 * IMPORTANT: This version handles float inputs the same way as C++:
 * - Float inputs like "3.5" are truncated to integers (becomes 3)
 * - This matches C++ behavior where cin >> int_variable truncates floats
 */

import java.util.Scanner;

public class Prime {
    
    // Prime checking method - exact same algorithm as C++ version
    public static boolean isPrime(int n) {
        if (n <= 1)                     return false;
        if (n <= 3)                     return true;
        if (n % 2 == 0 || n % 3 == 0)   return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number;
        
        do {
            System.out.print("Enter a positive number (0 or negative to exit): ");
            
            // Handle float inputs the same way C++ does (truncation)
            if (scanner.hasNextInt()) {
                number = scanner.nextInt();
            } else if (scanner.hasNextDouble()) {
                // If it's a double/float, truncate it to int (same as C++ behavior)
                double temp = scanner.nextDouble();
                number = (int) temp;  // Truncates the decimal part
            } else {
                // Skip invalid input and continue
                scanner.next();
                continue;
            }
            
            if (number <= 0) break;
            
            if (isPrime(number)) {
                System.out.println(number + " is a prime number.");
            } else {
                System.out.println(number + " is not a prime number.");
            }
            
        } while (true);
        
        scanner.close();
    }
}