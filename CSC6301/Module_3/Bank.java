import java.util.ArrayList;
import java.util.List;

/**
 * Represents a bank that manages multiple customer accounts.
 * This class provides functionality for opening and closing accounts,
 * performing transactions (deposits, withdrawals, transfers), and
 * retrieving account information.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
public class Bank {
    private final List<Account> accounts;

    /**
     * Constructs a new Bank with an empty list of accounts.
     */
    public Bank() {
        this.accounts = new ArrayList<>();
    }

    /**
     * Opens a new account with a basic withdrawal validator.
     * This is a convenience method that uses the default BasicWithdrawalValidator.
     * 
     * @param accountHolderName the name of the account holder
     * @param accountNumber     the unique account number
     * @param initialBalance    the initial balance for the account
     * @throws AccountAlreadyExistsException if an account with the given number
     *                                       already exists
     * @throws IllegalArgumentException      if any parameter is invalid
     */
    public void openAccount(String accountHolderName, String accountNumber, double initialBalance) {
        openAccount(accountHolderName, accountNumber, initialBalance, new BasicWithdrawalValidator());
    }

    /**
     * Opens a new account with a custom transaction validator.
     * 
     * @param accountHolderName the name of the account holder
     * @param accountNumber     the unique account number
     * @param initialBalance    the initial balance for the account
     * @param validator         the transaction validator to use for this account
     * @throws AccountAlreadyExistsException if an account with the given number
     *                                       already exists
     * @throws IllegalArgumentException      if any parameter is invalid
     */
    public void openAccount(String accountHolderName, String accountNumber, double initialBalance,
            TransactionValidator validator) {
        if (accountExists(accountNumber)) {
            throw new AccountAlreadyExistsException("Account " + accountNumber + " already exists");
        }

        Account newAccount = new Account(accountHolderName, accountNumber, initialBalance, validator);
        accounts.add(newAccount);
    }

    /**
     * Opens a new savings account with a minimum balance requirement.
     * Savings accounts use a SavingsAccountValidator that enforces the minimum
     * balance.
     * 
     * @param accountHolderName the name of the account holder
     * @param accountNumber     the unique account number
     * @param initialBalance    the initial balance for the account
     * @param minimumBalance    the minimum balance that must be maintained
     * @throws AccountAlreadyExistsException if an account with the given number
     *                                       already exists
     * @throws IllegalArgumentException      if any parameter is invalid
     */
    public void openSavingsAccount(String accountHolderName, String accountNumber,
            double initialBalance, double minimumBalance) {
        TransactionValidator savingsValidator = new SavingsAccountValidator(minimumBalance);
        openAccount(accountHolderName, accountNumber, initialBalance, savingsValidator);
    }

    /**
     * Closes an existing account.
     * The account can only be closed if it has a zero balance.
     * 
     * @param accountNumber the account number to close
     * @throws AccountNotFoundException if the account does not exist
     * @throws IllegalStateException    if the account has a positive balance
     */
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

    /**
     * Deposits money into the specified account.
     * 
     * @param accountNumber the account number to deposit into
     * @param amount        the amount to deposit (must be positive)
     * @throws AccountNotFoundException if the account does not exist
     * @throws IllegalArgumentException if the amount is negative or zero
     */
    public void deposit(String accountNumber, double amount) {
        Account account = findAccountByNumber(accountNumber);
        if (account == null) {
            throw new AccountNotFoundException("Account " + accountNumber + " not found");
        }

        account.deposit(amount);
    }

    /**
     * Withdraws money from the specified account.
     * The withdrawal is subject to the account's transaction validator rules.
     * 
     * @param accountNumber the account number to withdraw from
     * @param amount        the amount to withdraw (must be positive)
     * @throws AccountNotFoundException   if the account does not exist
     * @throws IllegalArgumentException   if the amount is negative or zero
     * @throws InsufficientFundsException if there are insufficient funds
     */
    public void withdraw(String accountNumber, double amount) {
        Account account = findAccountByNumber(accountNumber);
        if (account == null) {
            throw new AccountNotFoundException("Account " + accountNumber + " not found");
        }

        account.withdraw(amount);
    }

    /**
     * Transfers money from one account to another.
     * This operation performs a withdrawal from the source account and a deposit to
     * the destination account.
     * 
     * @param fromAccountNumber the source account number
     * @param toAccountNumber   the destination account number
     * @param amount            the amount to transfer (must be positive)
     * @throws IllegalArgumentException   if trying to transfer to the same account
     *                                    or if amount is invalid
     * @throws AccountNotFoundException   if either account does not exist
     * @throws InsufficientFundsException if the source account has insufficient
     *                                    funds
     */
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

        fromAccount.withdraw(amount);
        toAccount.deposit(amount);
    }

    /**
     * Retrieves the current balance of the specified account.
     * 
     * @param accountNumber the account number to query
     * @return the current account balance
     * @throws AccountNotFoundException if the account does not exist
     */
    public double getAccountBalance(String accountNumber) {
        Account account = findAccountByNumber(accountNumber);
        if (account == null) {
            throw new AccountNotFoundException("Account " + accountNumber + " not found");
        }

        return account.getCurrentBalance();
    }

    /**
     * Checks if an account with the given number exists in the bank.
     * 
     * @param accountNumber the account number to check
     * @return true if the account exists, false otherwise
     */
    public boolean accountExists(String accountNumber) {
        return findAccountByNumber(accountNumber) != null;
    }

    /**
     * Retrieves a list of all account numbers in the bank.
     * 
     * @return a new list containing all account numbers
     */
    public List<String> getAccountNumbers() {
        List<String> accountNumbers = new ArrayList<>();
        for (Account account : accounts) {
            accountNumbers.add(account.getAccountNumber());
        }
        return accountNumbers;
    }

    /**
     * Gets the total number of accounts in the bank.
     * 
     * @return the total count of accounts
     */
    public int getTotalAccountCount() {
        return accounts.size();
    }

    /**
     * Calculates the total assets held by the bank.
     * This is the sum of all account balances.
     * 
     * @return the total bank assets
     */
    public double getTotalBankAssets() {
        double total = 0;
        for (Account account : accounts) {
            total += account.getCurrentBalance();
        }
        return total;
    }

    /**
     * Finds all accounts belonging to a specific account holder.
     * The search is performed using the account holder's name.
     * 
     * @param accountHolderName the name of the account holder to search for
     * @return a list of accounts owned by the specified account holder
     * @throws IllegalArgumentException if the account holder name is null or empty
     */
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

    /**
     * Finds an account by its account number.
     * This is a private helper method used internally by other methods.
     * 
     * @param accountNumber the account number to search for
     * @return the Account object if found, null otherwise
     */
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

    /**
     * Retrieves all accounts in the bank.
     * Returns a defensive copy to prevent external modification of the internal
     * list.
     * 
     * @return a new list containing all accounts in the bank
     */
    public List<Account> getAllAccounts() {
        return new ArrayList<>(accounts);
    }
}