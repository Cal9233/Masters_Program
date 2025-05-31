import java.util.List;

/**
 * A demonstration application for the banking system.
 * This class showcases the functionality of the Bank class through
 * sample account operations and transactions.
 * 
 * @author Calvin Malagon
 * @version 1.0.0.0
 * @since Week 3 of CSC6301
 */
public class BankingApp {

    /**
     * The main entry point of the banking application.
     * Demonstrates account creation, deposits, withdrawals, and information
     * display.
     * 
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        try {
            Bank bank = new Bank();
            bank.openAccount("Peter Irmgard", "C0011", 5000);
            bank.openAccount("Katja Ruedi", "C0121", 4500);
            bank.openAccount("Marcella Gebhard", "C0222", 20000);
            List<Account> accounts = bank.getAllAccounts();
            for (Account account : accounts) {
                System.out.println(formatAccountInfo(account));
            }
            System.out.println("\nAfter depositing 1000 into account1:");
            bank.deposit("C0011", 1000);
            Account account1 = findAccountByNumber(accounts, "C0011");
            System.out.println(formatAccountInfo(account1));
            System.out.println("No transaction in account2:");
            Account account2 = findAccountByNumber(accounts, "C0121");
            System.out.println(formatAccountInfo(account2));
            System.out.println("After withdrawing 5000 from account3:");
            bank.withdraw("C0222", 5000);
            Account account3 = findAccountByNumber(accounts, "C0222");
            System.out.println(formatAccountInfo(account3));
        } catch (Exception e) {
            System.err.println("Banking operation failed: " + e.getMessage());
        }
    }

    /**
     * Formats account information into a readable string.
     * 
     * @param account the Account object to format
     * @return formatted string with account holder name, number, and balance
     */
    private static String formatAccountInfo(Account account) {
        return String.format("Name: %s, Account Number: %s, Balance: %.1f",
                account.getAccountHolderName(),
                account.getAccountNumber(),
                account.getCurrentBalance());
    }

    /**
     * Finds an account by its account number in a list of accounts.
     * 
     * @param accounts      the list of accounts to search
     * @param accountNumber the account number to find
     * @return the Account object if found, null otherwise
     */
    private static Account findAccountByNumber(List<Account> accounts, String accountNumber) {
        for (Account account : accounts) {
            if (account.belongsTo(accountNumber)) {
                return account;
            }
        }
        return null;
    }
}