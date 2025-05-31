/**
 * A basic implementation of TransactionValidator for withdrawal operations.
 * This validator performs standard checks including positive amount validation
 * and sufficient funds verification.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
public class BasicWithdrawalValidator implements TransactionValidator {

    /**
     * Validates a withdrawal transaction against basic business rules.
     * Ensures the amount is positive and the account has sufficient funds.
     * 
     * @param account the account from which funds will be withdrawn
     * @param amount  the amount to withdraw
     * @throws IllegalArgumentException   if the amount is zero or negative
     * @throws InsufficientFundsException if the account has insufficient funds
     */
    @Override
    public void validate(Account account, double amount) {
        validatePositiveAmount(amount);
        validateSufficientFunds(account, amount);
    }

    /**
     * Validates that the withdrawal amount is positive.
     * 
     * @param amount the amount to validate
     * @throws IllegalArgumentException if the amount is zero or negative
     */
    private void validatePositiveAmount(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
    }

    /**
     * Validates that the account has sufficient funds for the withdrawal.
     * 
     * @param account the account to check
     * @param amount  the amount to withdraw
     * @throws InsufficientFundsException if the account has insufficient funds
     */
    private void validateSufficientFunds(Account account, double amount) {
        if (!account.hasSufficientBalance(amount)) {
            throw new InsufficientFundsException(
                    String.format("Insufficient funds. Available: $%.2f, Requested: $%.2f",
                            account.getCurrentBalance(), amount));
        }
    }
}