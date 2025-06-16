package CSC6301.Module_5;

import java.util.Scanner;

/**
 * Handles console input operations.
 * Follows Single Responsibility Principle - only handles input processing.
 * Follows Dependency Inversion Principle - depends on SortedCollection
 * abstraction.
 * 
 * @author Calvin Malagon
 * @version 2.0.0.0 (Stack Implementation)
 * @since Week 5 of CSC6301 - Stack Maintenance Update
 */
public class ConsoleInputHandler implements InputHandler {

    private final Scanner scanner;
    private final SortedCollection collection;

    /**
     * Constructor with dependency injection.
     * Follows Dependency Inversion Principle - depends on interface.
     * 
     * @param collection the sorted collection to populate
     */
    public ConsoleInputHandler(SortedCollection collection) {
        this.scanner = new Scanner(System.in);
        this.collection = collection;
    }

    /**
     * Reads numbers from user input until empty line.
     * 
     * EXPLICIT REUSE: This method REUSES Scanner and Integer.parseInt() for input
     * processing rather than implementing custom parsing logic.
     * 
     * REUSED COMPONENTS: Scanner.hasNextLine(), Scanner.nextLine(),
     * Integer.parseInt()
     * NOT REIMPLEMENTED: Input stream buffering, character encoding support,
     * number parsing edge cases, exception handling for invalid formats
     * 
     * This REUSE approach leverages Java's robust input handling, which includes
     * proper buffering, encoding support, and error handling. Building equivalent
     * functionality without REUSE would require managing input streams, character
     * encoding, and number parsing edge cases - areas where the standard library
     * excels and has been thoroughly tested.
     */
    @Override
    public void readNumbers() {
        System.out.print("Enter number: ");

        while (scanner.hasNextLine()) {
            String input = scanner.nextLine().trim();

            if (input.isEmpty()) {
                break; // Terminate on empty line
            }

            if (isValidInteger(input)) {
                Integer number = Integer.parseInt(input);
                collection.add(number);
                System.out.println("Added " + number);
                System.out.print("Enter number (or press Enter to finish): ");
            } else {
                System.out.println("Invalid input. Please enter a valid integer or press Enter to finish.");
                System.out.print("Enter number (or press Enter to finish): ");
            }
        }
    }

    /**
     * Validates input string as integer.
     * Demonstrates code reuse through separation of validation logic.
     * 
     * @param input the string to validate
     * @return true if valid integer
     */
    private boolean isValidInteger(String input) {
        try {
            Integer.parseInt(input);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    /**
     * Closes the scanner resource.
     * Demonstrates code reuse for resource management.
     */
    public void close() {
        if (scanner != null) {
            scanner.close();
        }
    }
}