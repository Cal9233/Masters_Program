/**
 * Represents a bank account with basic operations and validation.
 * This class encapsulates account information and provides methods for
 * deposits, withdrawals, and balance inquiries with appropriate validation.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
public class Account {
    private final String accountHolderName;
    private final String accountNumber;
    private double balance;
    private final TransactionValidator withdrawalValidator;

    /**
     * Constructs a new Account with the specified details and validator.
     * 
     * @param accountHolderName   the name of the account holder (at least 2
     *                            characters)
     * @param accountNumber       the account number (format: Letter followed by 4
     *                            digits)
     * @param initialBalance      the initial balance (must be non-negative)
     * @param withdrawalValidator the validator for withdrawal transactions
     * @throws IllegalArgumentException if any parameter is invalid
     */
    public Account(String accountHolderName, String accountNumber, double initialBalance,
            TransactionValidator withdrawalValidator) {
        validateAccountHolderName(accountHolderName);
        validateAccountNumber(accountNumber);
        validateInitialBalance(initialBalance);
        validateWithdrawalValidator(withdrawalValidator);
        this.accountHolderName = accountHolderName.trim();
        this.accountNumber = accountNumber.trim();
        this.balance = initialBalance;
        this.withdrawalValidator = withdrawalValidator;
    }

    /**
     * Deposits money into the account.
     * 
     * @param amount the amount to deposit (must be positive and not exceed
     *               $1,000,000)
     * @throws IllegalArgumentException if the amount is invalid
     */
    public void deposit(double amount) {
        validateDepositAmount(amount);
        balance += amount;
    }

    /**
     * Withdraws money from the account.
     * The withdrawal is validated using the account's withdrawal validator.
     * 
     * @param amount the amount to withdraw
     * @throws IllegalArgumentException   if the amount is invalid
     * @throws InsufficientFundsException if withdrawal validation fails
     */
    public void withdraw(double amount) {
        withdrawalValidator.validate(this, amount);
        balance -= amount;
    }

    /**
     * Checks if the specified amount can be withdrawn from the account.
     * 
     * @param amount the amount to check
     * @return true if the amount can be withdrawn, false otherwise
     */
    public boolean canWithdraw(double amount) {
        return amount > 0 && hasSufficientBalance(amount);
    }

    /**
     * Checks if the account has sufficient balance for the specified amount.
     * 
     * @param amount the amount to check
     * @return true if the balance is sufficient, false otherwise
     */
    public boolean hasSufficientBalance(double amount) {
        return balance >= amount;
    }

    /**
     * Checks if this account belongs to the specified account number.
     * 
     * @param accountNumber the account number to check
     * @return true if this account matches the given account number, false
     *         otherwise
     */
    public boolean belongsTo(String accountNumber) {
        return this.accountNumber.equals(accountNumber);
    }

    /**
     * Checks if this account is owned by the specified account holder.
     * The comparison is case-insensitive.
     * 
     * @param accountHolderName the account holder name to check
     * @return true if this account is owned by the given name, false otherwise
     */
    public boolean isOwnedBy(String accountHolderName) {
        return this.accountHolderName.equalsIgnoreCase(accountHolderName);
    }

    /**
     * Gets the current balance of the account.
     * 
     * @return the current account balance
     */
    public double getCurrentBalance() {
        return balance;
    }

    /**
     * Gets the account number.
     * 
     * @return the account number
     */
    public String getAccountNumber() {
        return accountNumber;
    }

    /**
     * Gets the account holder's name.
     * 
     * @return the account holder name
     */
    public String getAccountHolderName() {
        return accountHolderName;
    }

    /**
     * Validates the account holder name.
     * 
     * @param name the name to validate
     * @throws IllegalArgumentException if the name is null, empty, or less than 2
     *                                  characters
     */
    private void validateAccountHolderName(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Account holder name cannot be null or empty");
        }
        if (name.trim().length() < 2) {
            throw new IllegalArgumentException("Account holder name must be at least 2 characters");
        }
    }

    /**
     * Validates the account number format.
     * 
     * @param accountNumber the account number to validate
     * @throws IllegalArgumentException if the account number doesn't match required
     *                                  format
     */
    private void validateAccountNumber(String accountNumber) {
        if (accountNumber == null || accountNumber.trim().isEmpty()) {
            throw new IllegalArgumentException("Account number cannot be null or empty");
        }
        if (!accountNumber.matches("^[A-Z][0-9]{4}$")) {
            throw new IllegalArgumentException(
                    "Account number must follow format: Letter followed by 4 digits (e.g., C0011)");
        }
    }

    /**
     * Validates the initial balance.
     * 
     * @param balance the balance to validate
     * @throws IllegalArgumentException if the balance is negative
     */
    private void validateInitialBalance(double balance) {
        if (balance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
    }

    /**
     * Validates the withdrawal validator.
     * 
     * @param validator the validator to validate
     * @throws IllegalArgumentException if the validator is null
     */
    private void validateWithdrawalValidator(TransactionValidator validator) {
        if (validator == null) {
            throw new IllegalArgumentException("Withdrawal validator cannot be null");
        }
    }

    /**
     * Validates the deposit amount.
     * 
     * @param amount the amount to validate
     * @throws IllegalArgumentException if the amount is invalid
     */
    private void validateDepositAmount(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }
        if (amount > 1_000_000) {
            throw new IllegalArgumentException("Deposit amount cannot exceed $1,000,000");
        }
    }

    /**
     * Checks equality based on account number.
     * 
     * @param obj the object to compare
     * @return true if the objects are equal, false otherwise
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;
        Account account = (Account) obj;
        return accountNumber.equals(account.accountNumber);
    }

    /**
     * Returns a hash code based on the account number.
     * 
     * @return the hash code
     */
    @Override
    public int hashCode() {
        return accountNumber.hashCode();
    }

    /**
     * Returns a string representation of the account.
     * 
     * @return formatted string with account number, holder name, and balance
     */
    @Override
    public String toString() {
        return String.format("Account[%s, %s, Balance: %.2f]",
                accountNumber, accountHolderName, balance);
    }
}