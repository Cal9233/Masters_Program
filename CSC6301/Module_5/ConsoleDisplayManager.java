package CSC6301.Module_5;

import java.util.List;

/**
 * Handles console display operations for Stack-based sorted collection.
 * Follows Single Responsibility Principle - only handles display logic.
 * Demonstrates code reuse through consistent formatting patterns.
 * 
 * @author Calvin Malagon
 * @version 2.0.0.0 (Stack Implementation)
 * @since Week 5 of CSC6301 - Stack Maintenance Update
 */

public class ConsoleDisplayManager implements DisplayManager {

    /**
     * Displays welcome message and instructions for Stack program.
     * Demonstrates code reuse through consistent message formatting.
     */
    @Override
    public void showWelcome() {
        System.out.println("=== Sorted Stack Program ===");
        System.out.println("Enter integer numbers (one per line).");
        System.out.println("Press Enter on an empty line to finish input.");
        System.out.println("Numbers will be stored in a Stack and displayed sorted from smallest to largest.");
        System.out.println();
    }

    /**
     * Displays the final sorted results from the Stack.
     * Demonstrates code reuse through formatting methods.
     * 
     * @param numbers the sorted numbers to display
     */
    @Override
    public void showResults(List<Integer> numbers) {
        System.out.println("\n=== Final Results ===");
        System.out.println("Stack contents sorted (smallest to largest): " + formatList(numbers));
        System.out.println("Total numbers in Stack: " + numbers.size());
    }

    /**
     * Formats list for display using StringBuilder.
     * 
     * EXPLICIT REUSE: This method REUSES StringBuilder rather than string
     * concatenation operators to avoid creating multiple intermediate String
     * objects during Stack display formatting.
     * 
     * REUSED COMPONENTS: StringBuilder.append(), automatic buffer management,
     * capacity expansion algorithms, toString() conversion
     * NOT REIMPLEMENTED: String buffer allocation, capacity management, resizing
     * logic, memory optimization for string building operations
     * 
     * This is a common optimization pattern that REUSES Java's efficient string
     * building capabilities rather than implementing our own buffer management.
     * For Stack display, this is particularly important as we may have many
     * elements to format, and string concatenation would create numerous
     * temporary objects.
     * 
     * @param numbers the numbers to format
     * @return formatted string representation of Stack contents
     */
    private String formatList(List<Integer> numbers) {
        if (numbers.isEmpty()) {
            return "[Stack Empty]";
        }

        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < numbers.size(); i++) {
            sb.append(numbers.get(i));
            if (i < numbers.size() - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
}