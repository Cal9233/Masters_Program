package CSC6301.Module_4;


import java.util.List;

/**
 * Interface for display operations.
 * Follows Interface Segregation Principle by focusing only on display needs.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 4 of CSC6301
 */
public interface DisplayManager {

    /**
     * Shows welcome message and instructions.
     */
    void showWelcome();

    /**
     * Shows the final sorted results.
     * 
     * @param numbers the sorted numbers to display
     */
    void showResults(List<Integer> numbers);
}