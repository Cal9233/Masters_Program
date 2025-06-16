package CSC6301.Module_5;

/**
 * Main application coordinator class for Stack-based sorted collection.
 * Follows Single Responsibility Principle - only coordinates application flow.
 * Follows Dependency Inversion Principle - depends on abstractions.
 * 
 * EXPLICIT CODE REUSE DOCUMENTATION:
 * 
 * This project demonstrates extensive REUSE of existing, well-tested components
 * rather than building everything from scratch. The philosophy here is to REUSE
 * proven implementations while focusing development efforts on unique business
 * logic.
 * 
 * Explicit REUSE Examples and Justifications for Stack Implementation:
 * 
 * 1. REUSE of Java Collections Framework (Stack):
 * We REUSE {@code Stack<Integer>} instead of implementing our own
 * stack data structure with array management, capacity handling, and LIFO
 * operations.
 * REUSED COMPONENTS: Stack constructor, push(), pop(), peek(), isEmpty(),
 * size()
 * NOT REIMPLEMENTED: Dynamic array resizing, capacity management, LIFO logic
 * This REUSE saves approximately 100-150 lines of low-level data structure
 * code.
 * 
 * 2. REUSE of Collections.sort() Algorithm:
 * We REUSE Java's optimized sorting implementation for maintaining order
 * when converting stack to sorted list.
 * REUSED COMPONENTS: Collections.sort(), Comparable interface, merge sort
 * algorithm
 * NOT REIMPLEMENTED: Sorting algorithms, comparison logic, performance
 * optimization
 * This REUSE provides optimal O(n log n) performance with stable sorting.
 * 
 * 3. REUSE of ArrayList for Temporary Storage:
 * We REUSE ArrayList for intermediate operations during sorting processes.
 * REUSED COMPONENTS: ArrayList dynamic resizing, get(), set(), add() operations
 * NOT REIMPLEMENTED: Dynamic array management, memory allocation, bounds
 * checking
 * This REUSE enables efficient random access needed for sorting operations.
 * 
 * 4. REUSE of Scanner for Input Processing:
 * We REUSE Scanner's robust input handling capabilities rather than dealing
 * with low-level System.in operations.
 * REUSED COMPONENTS: Scanner.hasNextLine(), Scanner.nextLine(), input buffering
 * NOT REIMPLEMENTED: Stream management, character encoding, line parsing
 * This REUSE handles complex input scenarios reliably.
 * 
 * 5. REUSE of Integer.parseInt() for Type Conversion:
 * We REUSE Java's built-in string-to-integer parsing instead of custom parsing.
 * REUSED COMPONENTS: Integer.parseInt(), NumberFormatException handling
 * NOT REIMPLEMENTED: Character parsing, sign handling, overflow detection
 * This REUSE ensures proper validation and error handling.
 * 
 * 6. REUSE of StringBuilder for String Operations:
 * We REUSE StringBuilder for efficient string concatenation in display
 * operations.
 * REUSED COMPONENTS: StringBuilder.append(), automatic buffer management
 * NOT REIMPLEMENTED: String buffer allocation, capacity management, resizing
 * This REUSE avoids performance issues from string concatenation operators.
 * 
 * REUSE of Design Patterns:
 * The architecture REUSES established patterns (Interface Segregation,
 * Dependency Injection, Factory) that have proven effective in professional
 * software development.
 * 
 * Stack-Specific REUSE Benefits:
 * - REUSE Stack's LIFO operations for natural input ordering
 * - REUSE Collections framework for sorting when display is needed
 * - REUSE existing interfaces to maintain architectural consistency
 * - REUSE proven error handling patterns for stack operations
 * 
 * Benefits of This REUSE Strategy:
 * - Reduced development time through REUSE of proven components
 * - Higher reliability by REUSING battle-tested implementations
 * - Better performance from REUSING optimized algorithms
 * - Easier maintenance through REUSE of standard patterns
 * - Focus on unique business logic rather than REIMPLEMENTING infrastructure
 * 
 * @author Calvin Malagon
 * @version 2.0.0.0 (Stack Implementation)
 * @since Week 5 of CSC6301 - Stack Maintenance Update
 */
public class SortedStack {

    private final SortedCollection collection;
    private final InputHandler inputHandler;
    private final DisplayManager displayManager;

    /**
     * Constructor with dependency injection.
     * Follows Dependency Inversion Principle - depends on interfaces.
     * Demonstrates code reuse through composition.
     * 
     * @param collection     the sorted collection implementation
     * @param inputHandler   the input handler implementation
     * @param displayManager the display manager implementation
     */
    public SortedStack(SortedCollection collection,
            InputHandler inputHandler,
            DisplayManager displayManager) {
        this.collection = collection;
        this.inputHandler = inputHandler;
        this.displayManager = displayManager;
    }

    /**
     * Default constructor creating standard implementations.
     * Demonstrates code reuse through factory pattern.
     */
    public SortedStack() {
        this.collection = new SortedIntegerStack();
        this.inputHandler = new ConsoleInputHandler(collection);
        this.displayManager = new ConsoleDisplayManager();
    }

    /**
     * Main method - entry point of the program.
     * Demonstrates code reuse through delegation and proper resource management.
     * 
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        SortedStack program = new SortedStack();
        try {
            program.run();
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            program.cleanup();
        }
    }

    /**
     * Main execution method.
     * Follows Single Responsibility - only coordinates the application flow.
     * Demonstrates code reuse through delegation to specialized components.
     */
    public void run() {
        displayManager.showWelcome();
        inputHandler.readNumbers();
        displayManager.showResults(collection.getNumbers());
    }

    /**
     * Cleanup resources.
     * Demonstrates code reuse for resource management patterns.
     */
    private void cleanup() {
        if (inputHandler instanceof ConsoleInputHandler) {
            ((ConsoleInputHandler) inputHandler).close();
        }
    }
}