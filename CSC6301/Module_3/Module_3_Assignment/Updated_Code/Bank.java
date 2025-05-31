import java.util.ArrayList;
import java.util.List;

/**
 * Manages a collection of bank accounts and banking operations.
 * SRP: Only responsible for bank-level operations and account management.
 * Encapsulation: Private account collection, behavior-focused public interface.
 */
public class Bank {
    // Instance variable used by multiple methods
    private final List<Account> accounts;

    public Bank() {
        this.accounts = new ArrayList<>();
    }

    // Express banking behavior in abstract terms, not data manipulation

    public void openAccount(String accountHolderName, String accountNumber, double initialBalance) {
        if (accountExists(accountNumber)) {
            throw new AccountAlreadyExistsException("Account " + accountNumber + " already exists");
        }

        Account newAccount = new Account(accountHolderName, accountNumber, initialBalance);
        accounts.add(newAccount);
    }

    public void closeAccount(String accountNumber) {
        Account account = findAccountByNumber(accountNumber);
        if (account == null) {
            throw new AccountNotFoundException("Account " + accountNumber + " not found");
        }

        if (account.getCurrentBalance() > 0) {
            throw new IllegalStateException(
                    "Cannot close account with positive balance. Please withdraw all funds first.");
        }

        accounts.remove(account);
    }

    public void deposit(String accountNumber, double amount) {
        Account account = findAccountByNumber(accountNumber);
        if (account == null) {
            throw new AccountNotFoundException("Account " + accountNumber + " not found");
        }

        account.deposit(amount); // Delegate to Account's behavior
    }

    public void withdraw(String accountNumber, double amount) {
        Account account = findAccountByNumber(accountNumber);
        if (account == null) {
            throw new AccountNotFoundException("Account " + accountNumber + " not found");
        }

        account.withdraw(amount); // Delegate to Account's behavior
    }

    public void transfer(String fromAccountNumber, String toAccountNumber, double amount) {
        if (fromAccountNumber.equals(toAccountNumber)) {
            throw new IllegalArgumentException("Cannot transfer to the same account");
        }

        Account fromAccount = findAccountByNumber(fromAccountNumber);
        Account toAccount = findAccountByNumber(toAccountNumber);

        if (fromAccount == null) {
            throw new AccountNotFoundException("Source account " + fromAccountNumber + " not found");
        }
        if (toAccount == null) {
            throw new AccountNotFoundException("Destination account " + toAccountNumber + " not found");
        }

        // Use Account's behavior to ensure business rules are followed
        fromAccount.withdraw(amount);
        toAccount.deposit(amount);
    }

    public double getAccountBalance(String accountNumber) {
        Account account = findAccountByNumber(accountNumber);
        if (account == null) {
            throw new AccountNotFoundException("Account " + accountNumber + " not found");
        }

        return account.getCurrentBalance();
    }

    public boolean accountExists(String accountNumber) {
        return findAccountByNumber(accountNumber) != null;
    }

    public List<String> getAccountNumbers() {
        List<String> accountNumbers = new ArrayList<>();
        for (Account account : accounts) {
            accountNumbers.add(account.getAccountNumber());
        }
        return accountNumbers; // Return defensive copy
    }

    public int getTotalAccountCount() {
        return accounts.size();
    }

    public double getTotalBankAssets() {
        double total = 0;
        for (Account account : accounts) {
            total += account.getCurrentBalance();
        }
        return total;
    }

    public List<Account> findAccountsByHolder(String accountHolderName) {
        if (accountHolderName == null || accountHolderName.trim().isEmpty()) {
            throw new IllegalArgumentException("Account holder name cannot be null or empty");
        }

        List<Account> matchingAccounts = new ArrayList<>();
        for (Account account : accounts) {
            if (account.isOwnedBy(accountHolderName)) {
                matchingAccounts.add(account);
            }
        }
        return matchingAccounts;
    }

    // Private helper methods following Law of Demeter
    // Only manipulate objects this Bank owns
    private Account findAccountByNumber(String accountNumber) {
        if (accountNumber == null)
            return null;

        for (Account account : accounts) {
            if (account.belongsTo(accountNumber)) {
                return account;
            }
        }
        return null;
    }

    // Read-only access for reporting purposes only
    public List<Account> getAllAccounts() {
        return new ArrayList<>(accounts); // Return defensive copy
    }
}

/**
 * Custom exception for account not found.
 * SRP: Only responsible for account not found errors.
 */
class AccountNotFoundException extends RuntimeException {
    public AccountNotFoundException(String message) {
        super(message);
    }
}

/**
 * Custom exception for duplicate accounts.
 * SRP: Only responsible for duplicate account errors.
 */
class AccountAlreadyExistsException extends RuntimeException {
    public AccountAlreadyExistsException(String message) {
        super(message);
    }
}