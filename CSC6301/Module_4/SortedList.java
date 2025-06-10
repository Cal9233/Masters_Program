package CSC6301.Module_4;

/**
 * Main application coordinator class.
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
 * Explicit REUSE Examples and Justifications:
 * 
 * 1. REUSE of Java Collections Framework (LinkedList):
 * We REUSE LinkedList<Integer> instead of implementing our own doubly-linked
 * list with node management, memory allocation, and pointer manipulation.
 * REUSED COMPONENTS: LinkedList constructor, add(), size(), isEmpty(),
 * iterator()
 * NOT REIMPLEMENTED: Node structure, memory management, pointer operations
 * This REUSE saves approximately 150-200 lines of low-level code and eliminates
 * potential bugs in pointer arithmetic.
 * 
 * 2. REUSE of Collections.binarySearch() Algorithm:
 * We REUSE Java's optimized binary search implementation rather than writing
 * our own search algorithm.
 * REUSED COMPONENTS: Collections.binarySearch(), built-in comparison logic
 * NOT REIMPLEMENTED: Binary search algorithm, midpoint calculations, bounds
 * checking
 * This REUSE provides O(log n) performance with proper edge case handling.
 * 
 * 3. REUSE of Scanner for Input Processing:
 * We REUSE Scanner's robust input handling capabilities rather than dealing
 * with low-level System.in operations.
 * REUSED COMPONENTS: Scanner.hasNextLine(), Scanner.nextLine(), input buffering
 * NOT REIMPLEMENTED: Stream management, character encoding, line parsing
 * This REUSE handles complex input scenarios that would require significant
 * effort to implement reliably.
 * 
 * 4. REUSE of Integer.parseInt() for Type Conversion:
 * We REUSE Java's built-in string-to-integer parsing instead of custom parsing.
 * REUSED COMPONENTS: Integer.parseInt(), NumberFormatException handling
 * NOT REIMPLEMENTED: Character-by-character parsing, sign handling, overflow
 * detection
 * This REUSE ensures proper validation and error handling for number
 * conversion.
 * 
 * 5. REUSE of StringBuilder for String Operations:
 * We REUSE StringBuilder for efficient string concatenation in formatList().
 * REUSED COMPONENTS: StringBuilder.append(), automatic buffer management
 * NOT REIMPLEMENTED: String buffer allocation, capacity management, resizing
 * This REUSE avoids performance issues from string concatenation operators.
 * 
 * REUSE of Design Patterns:
 * The architecture REUSES established patterns (Interface Segregation,
 * Dependency Injection, Factory) that have proven effective in professional
 * software development. We REUSE these well-documented patterns rather than
 * inventing our own architectural approaches.
 * 
 * Benefits of This REUSE Strategy:
 * - Reduced development time through REUSE of proven components
 * - Higher reliability by REUSING battle-tested implementations
 * - Better performance from REUSING optimized algorithms
 * - Easier maintenance through REUSE of standard patterns
 * - Focus on unique business logic rather than REIMPLEMENTING infrastructure
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 4 of CSC6301
 */
public class SortedList {

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
    public SortedList(SortedCollection collection,
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
    public SortedList() {
        this.collection = new SortedIntegerCollection();
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
        SortedList program = new SortedList();

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