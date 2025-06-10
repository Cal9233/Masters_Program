package CSC6301.Module_4;

import java.util.List;

/**
 * Handles console display operations.
 * Follows Single Responsibility Principle - only handles display logic.
 * Demonstrates code reuse through consistent formatting patterns.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 4 of CSC6301
 */
public class ConsoleDisplayManager implements DisplayManager {

    /**
     * Displays welcome message and instructions.
     * Demonstrates code reuse through consistent message formatting.
     */
    @Override
    public void showWelcome() {
        System.out.println("=== Sorted LinkedList Program ===");
        System.out.println("Enter integer numbers (one per line).");
        System.out.println("Press Enter on an empty line to finish input.");
        System.out.println("Numbers will be automatically sorted from smallest to largest.");
        System.out.println();
    }

    /**
     * Displays the final sorted results.
     * Demonstrates code reuse through formatting methods.
     * 
     * @param numbers the sorted numbers to display
     */
    @Override
    public void showResults(List<Integer> numbers) {
        System.out.println("\n=== Final Results ===");
        System.out.println("Final sorted list (smallest to largest): " + formatList(numbers));
    }

    /**
     * Formats list for display using StringBuilder.
     * 
     * EXPLICIT REUSE: This method REUSES StringBuilder rather than string
     * concatenation operators to avoid creating multiple intermediate String
     * objects.
     * 
     * REUSED COMPONENTS: StringBuilder.append(), automatic buffer management,
     * capacity expansion algorithms
     * NOT REIMPLEMENTED: String buffer allocation, capacity management, resizing
     * logic, memory optimization for string building
     * 
     * This is a common optimization pattern that REUSES Java's efficient string
     * building capabilities rather than implementing our own buffer management.
     * Without this REUSE, we would need to handle buffer allocation and resizing
     * manually, which could introduce performance issues and memory leaks.
     * 
     * @param numbers the numbers to format
     * @return formatted string representation
     */
    private String formatList(List<Integer> numbers) {
        if (numbers.isEmpty()) {
            return "[]";
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