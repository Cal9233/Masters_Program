/**
 * Exception thrown when a withdrawal or transfer operation fails due to
 * insufficient funds.
 * This is a runtime exception that indicates an account does not have enough
 * balance to complete the requested transaction.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
public class InsufficientFundsException extends RuntimeException {

    /**
     * Constructs a new InsufficientFundsException with the specified error message.
     * 
     * @param message the detail message explaining the insufficient funds condition
     */
    public InsufficientFundsException(String message) {
        super(message);
    }

    /**
     * Constructs a new InsufficientFundsException with the specified error message
     * and cause.
     * 
     * @param message the detail message explaining the insufficient funds condition
     * @param cause   the underlying cause of this exception
     */
    public InsufficientFundsException(String message, Throwable cause) {
        super(message, cause);
    }
}