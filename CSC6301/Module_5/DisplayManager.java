package CSC6301.Module_5;

import java.util.List;

/**
 * Interface for display operations.
 * Follows Interface Segregation Principle by focusing only on display needs.
 * 
 * @author Calvin Malagon
 * @version 2.0.0.0 (Stack Implementation)
 * @since Week 5 of CSC6301 - Stack Maintenance Update
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