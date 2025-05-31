/**
 * Exception for duplicate account creation.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
class AccountAlreadyExistsException extends RuntimeException {
    /**
     * Creates exception with message.
     * 
     * @param message the error message
     */
    public AccountAlreadyExistsException(String message) {
        super(message);
    }
}