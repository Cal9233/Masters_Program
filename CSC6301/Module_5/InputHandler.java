package CSC6301.Module_5;

/**
 * Interface for input handling operations.
 * Follows Interface Segregation Principle by focusing only on input reading.
 * 
 * @author Calvin Malagon
 * @version 2.0.0.0 (Stack Implementation)
 * @since Week 5 of CSC6301 - Stack Maintenance Update
 */
public interface InputHandler {

    /**
     * Reads numbers from input source and adds them to the collection.
     */
    void readNumbers();
}