/**
 * A transaction validator for savings accounts that enforces minimum balance
 * requirements.
 * This validator ensures that withdrawals do not cause the account balance
 * to fall below the specified minimum balance threshold.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
public class SavingsAccountValidator implements TransactionValidator {
    private final double minimumBalance;

    /**
     * Constructs a new SavingsAccountValidator with the specified minimum balance
     * requirement.
     * 
     * @param minimumBalance the minimum balance that must be maintained in the
     *                       account
     */
    public SavingsAccountValidator(double minimumBalance) {
        this.minimumBalance = minimumBalance;
    }

    /**
     * Validates a withdrawal transaction for a savings account.
     * Ensures the amount is positive and that the withdrawal will not cause
     * the account balance to fall below the minimum balance requirement.
     * 
     * @param account the savings account from which funds will be withdrawn
     * @param amount  the amount to withdraw
     * @throws IllegalArgumentException   if the amount is zero or negative
     * @throws InsufficientFundsException if the withdrawal would violate the
     *                                    minimum balance requirement
     */
    @Override
    public void validate(Account account, double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }

        double balanceAfterWithdrawal = account.getCurrentBalance() - amount;
        if (balanceAfterWithdrawal < minimumBalance) {
            throw new InsufficientFundsException(
                    String.format("Savings account requires minimum balance of $%.2f. " +
                            "Available for withdrawal: $%.2f",
                            minimumBalance,
                            account.getCurrentBalance() - minimumBalance));
        }
    }
}