package CSC6301.Module_4;


/**
 * Interface for input handling operations.
 * Follows Interface Segregation Principle by focusing only on input reading.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 4 of CSC6301
 */
public interface InputHandler {

    /**
     * Reads numbers from input source and adds them to the collection.
     */
    void readNumbers();
}