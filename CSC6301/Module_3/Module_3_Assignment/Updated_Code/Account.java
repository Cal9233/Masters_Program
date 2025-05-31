/**
 * Represents a bank account with secure operations.
 * SRP: Only responsible for account data and account-specific behavior.
 * Encapsulation: All fields private, behavior-focused methods, no direct data
 * access.
 */
public class Account {
    // All instance variables are private and used by multiple methods
    private final String accountHolderName;
    private final String accountNumber;
    private double balance;

    // Constructor with validation - enforces business rules
    public Account(String accountHolderName, String accountNumber, double initialBalance) {
        validateAccountHolderName(accountHolderName);
        validateAccountNumber(accountNumber);
        validateInitialBalance(initialBalance);

        this.accountHolderName = accountHolderName.trim();
        this.accountNumber = accountNumber.trim();
        this.balance = initialBalance;
    }

    // Behavior-focused methods instead of getters/setters
    // Express what the account CAN DO, not what data it HAS

    public void deposit(double amount) {
        validateDepositAmount(amount);
        balance += amount;
    }

    public void withdraw(double amount) {
        validateWithdrawAmount(amount);
        if (!hasSufficientBalance(amount)) {
            throw new InsufficientFundsException(
                    "Insufficient funds. Available: " + balance + ", Requested: " + amount);
        }
        balance -= amount;
    }

    public boolean canWithdraw(double amount) {
        return amount > 0 && hasSufficientBalance(amount);
    }

    public boolean hasSufficientBalance(double amount) {
        return balance >= amount;
    }

    public boolean belongsTo(String accountNumber) {
        return this.accountNumber.equals(accountNumber);
    }

    public boolean isOwnedBy(String accountHolderName) {
        return this.accountHolderName.equalsIgnoreCase(accountHolderName);
    }

    // Minimal read-only access for essential operations only
    public double getCurrentBalance() {
        return balance;
    }

    public String getAccountNumber() {
        return accountNumber; // Immutable, safe to return
    }

    public String getAccountHolderName() {
        return accountHolderName; // Immutable, safe to return
    }

    // Private helper methods following Law of Demeter
    // Only manipulate this account's own data
    private void validateAccountHolderName(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Account holder name cannot be null or empty");
        }
        if (name.trim().length() < 2) {
            throw new IllegalArgumentException("Account holder name must be at least 2 characters");
        }
    }

    private void validateAccountNumber(String accountNumber) {
        if (accountNumber == null || accountNumber.trim().isEmpty()) {
            throw new IllegalArgumentException("Account number cannot be null or empty");
        }
        if (!accountNumber.matches("^[A-Z][0-9]{4}$")) {
            throw new IllegalArgumentException(
                    "Account number must follow format: Letter followed by 4 digits (e.g., C0011)");
        }
    }

    private void validateInitialBalance(double balance) {
        if (balance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
    }

    private void validateDepositAmount(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }
        if (amount > 1_000_000) {
            throw new IllegalArgumentException("Deposit amount cannot exceed $1,000,000");
        }
    }

    private void validateWithdrawAmount(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;

        Account account = (Account) obj;
        return accountNumber.equals(account.accountNumber);
    }

    @Override
    public int hashCode() {
        return accountNumber.hashCode();
    }

    @Override
    public String toString() {
        return String.format("Account[%s, %s, Balance: %.2f]",
                accountNumber, accountHolderName, balance);
    }
}

/**
 * Custom exception for insufficient funds.
 * SRP: Only responsible for insufficient funds errors.
 */
class InsufficientFundsException extends RuntimeException {
    public InsufficientFundsException(String message) {
        super(message);
    }
}