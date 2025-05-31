/**
 * Interface for validating banking transactions before they are executed.
 * Implementations of this interface define specific business rules and
 * constraints for different types of accounts and transactions.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
public interface TransactionValidator {

    /**
     * Validates a transaction against the implemented business rules.
     * This method should throw appropriate exceptions if the transaction
     * violates any validation rules.
     * 
     * @param account the account involved in the transaction
     * @param amount  the transaction amount to validate
     * @throws IllegalArgumentException   if the amount is invalid
     * @throws InsufficientFundsException if the transaction would cause
     *                                    insufficient funds
     */
    void validate(Account account, double amount);
}