/**
 * Exception for account not found operations.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
class AccountNotFoundException extends RuntimeException {

    /**
     * Creates exception with message.
     * 
     * @param message the error message
     */
    public AccountNotFoundException(String message) {
        super(message);
    }
}