import random

# Account Class
class Account:
    def __init__(self, firstName, lastName, ssn):
        self.accountNumber = self.generateAccountNumber()
        self.pin = self.generatePin()
        self.ownerFirstName = firstName
        self.ownerLastName = lastName
        self.ssn = ssn
        self.balance = 0

    # generates random account number starting from 10000000 to 99999999
    def generateAccountNumber(self):
        return random.randint(10000000, 99999999)

    # generates random PIN number starting from 0 to 9999
    def generatePin(self):
        return f"{random.randint(0, 9999):04d}"

    # fetches account number
    def getAccountNumber(self):
        return self.accountNumber

    # fetches account owner first name
    def getOwnerFirstName(self):
        return self.ownerFirstName

    # sets account owner first name
    def setOwnerFirstName(self, firstName):
        self.ownerFirstName = firstName

    # fetches account owner last name
    def getOwnerLastName(self):
        return self.ownerLastName

    # sets account owner last name
    def setOwnerLastName(self, lastName):
        self.ownerLastName = lastName

    # fetches account owner ssn
    def getSsn(self):
        return self.ssn

    # sets account owner ssn
    def setSsn(self, ssn):
        self.ssn = ssn

    # sets account owner PIN
    def getPin(self):
        return self.pin

    # sets account owner PIN
    def setPin(self, pin):
        self.pin = pin

    # gets account balance from users account
    def getBalance(self):
        return self.balance

    # deposits money from account
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        >>> account = Account("Calvin", "Malagon", "999-12-3456")
        >>> account.deposit(5000)
        5000
        >>> account.deposit(500)
        5500
        """
        self.balance += amount
        return self.balance
    
    # withdraws money from account
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        >>> account = Account("Calvin", "Malagon", "999-12-3456")
        >>> account.deposit(1000)
        1000
        >>> account.withdraw(300)
        700
        >>> account.withdraw(800)
        -100
        """
        self.balance -= amount
        return self.balance

    # checks if PIN matches with self user account pin
    def isValidPin(self, pin):
        """
        Check if the given PIN is valid.
        
        >>> account = Account("Test", "User", "999-12-3456")
        >>> account.isValidPin(account.getPin())
        True
        >>> account.isValidPin("0000")
        False
        """
        return self.pin == pin
    
    # returns account information as string
    def toString(self):
        """
        Returns a string representation of the account.
        
        >>> account = Account("Nicole", "Ortiz", "999-45-6789")
        >>> account.deposit(10000)  # $100.00
        10000
        >>> print(account.toString())
        +======================================================+
                Account Number: ...
                Owner First Name: Nicole
                Owner Last Name: Ortiz
                Owner SSN: XXX-XX-6789
                PIN: ...
                Balance: $100.00
        +======================================================+
        """
        return (
            "+======================================================+\n"
            f"        Account Number: {self.accountNumber}\n"
            f"        Owner First Name: {self.ownerFirstName}\n"
            f"        Owner Last Name: {self.ownerLastName}\n"
            f"        Owner SSN: XXX-XX-{self.ssn[-4:]}\n"
            f"        PIN: {self.pin}\n"
            f"        Balance: ${self.balance / 100:.2f}\n"
            "+======================================================+"
        )


#Bank Class
class Bank:
    def __init__(self, max_accounts=100):
        self.accounts = [None] * max_accounts
        self.max_accounts = max_accounts

    # adds new account into Bank class 
    def addAccountToBank(self, account):
        """
        Add an account to the bank.
        
        >>> bank = Bank(3)
        >>> account1 = Account("Test", "User2", "999-12-3456")
        >>> bank.addAccountToBank(account1)
        True
        >>> account2 = Account("Test", "User3", "999-78-9012")
        >>> bank.addAccountToBank(account2)
        True
        >>> account3 = Account("Test", "User4", "999-34-5678")
        >>> bank.addAccountToBank(account3)
        True
        >>> account4 = Account("Test", "User5", "999-90-1234")
        >>> bank.addAccountToBank(account4)
        No more accounts available
        False
        """
        for i in range(self.max_accounts):
            if self.accounts[i] is None:
                self.accounts[i] = account
                return True
        print("No more accounts available")
        return False

    # removes account from Bank class 
    def removeAccountFromBank(self, account):
        """
        Remove an account from the bank.
        
        >>> bank = Bank(3)
        >>> account1 = Account("Test", "User6", "999-12-3456")
        >>> bank.addAccountToBank(account1)
        True
        >>> bank.removeAccountFromBank(account1)
        True
        >>> bank.removeAccountFromBank(account1)
        False
        """
        for i in range(self.max_accounts):
            if self.accounts[i] is not None and self.accounts[i].getAccountNumber() == account.getAccountNumber():
                self.accounts[i] = None
                return True
        return False

    # finds and returns account in Bank class 
    def findAccount(self, accountNumber):
        """
        Find an account by account number.
        
        >>> bank = Bank(3)
        >>> account1 = Account("Test", "User7", "999-12-3456")
        >>> bank.addAccountToBank(account1)
        True
        >>> found_account = bank.findAccount(account1.getAccountNumber())
        >>> found_account.getOwnerFirstName()
        'Test'
        >>> bank.findAccount(12345678) is None
        True
        """
        for account in self.accounts:
            if account is not None and account.getAccountNumber() == accountNumber:
                return account
        return None

    # Multiplies account balance by monthly annual rate
    def addMonthlyInterest(self, annual_rate):
        """
        Add monthly interest to all accounts.
        
        >>> bank = Bank(3)
        >>> account1 = Account("Test", "User8", "999-12-3456")
        >>> bank.addAccountToBank(account1)
        True
        >>> account1.deposit(10000)  # $100.00
        10000
        >>> bank.addMonthlyInterest(7.7)  # 7.7% annual rate
        +=====================================================+
               Deposited interest: $64
               into account number: ...
               new balance: $10064
        +=====================================================+
        """
        monthly_rate = annual_rate / 12 / 100
        
        for account in self.accounts:
            if account is not None:
                interest = int(account.getBalance() * monthly_rate)
                account.deposit(interest)
                print("+=====================================================+")
                print(f"       Deposited interest: ${interest}")
                print(f"       into account number: {account.accountNumber}")
                print(f"       new balance: ${account.getBalance()}")
                print("+=====================================================+")

#CoinCollector Class
class CoinCollector:
    # converts valid string to cents
    @staticmethod
    def parseChange(coins):
        """
        Parse a string of coins and return the total value in cents.
        
        >>> CoinCollector.parseChange("PNDQHW")
        191
        >>> CoinCollector.parseChange("QQQQQ")
        125
        >>> CoinCollector.parseChange("PPPPPNNNNN")
        30
        """
        coins = coins.upper()
        coin_values = {
            'P': 1,
            'N': 5,
            'D': 10,
            'Q': 25,
            'H': 50,
            'W': 100
        }
        
        total_cents = 0
        invalid_coins = []
        
        for coin in coins:
            if coin in coin_values:
                total_cents += coin_values[coin]
            else:
                invalid_coins.append(coin)
        
        if invalid_coins:
            print(f"Invalid coin: {', '.join(invalid_coins)}")
        
        return total_cents

#BankUtility Class
class BankUtility:
    # returns if passing parameter is number or not
    @staticmethod
    def isNumeric(number_to_check):
        """
        Checks if string is number or not
        
        >>> BankUtility.isNumeric("PNDQHW")
        False
        >>> BankUtility.isNumeric("1206")
        True
        >>> BankUtility.isNumeric("")
        False
        """
        try:
            if number_to_check.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False
        
    # returns if passing parameter is string or not
    @staticmethod
    def promptUserForString(prompt):
        return input(prompt).strip()

    # returns if passing parameter is number and if greater than zero
    @staticmethod
    def promptUserForPositiveNumber(prompt):
        while True:
            try:
                number = float(input(prompt).strip())
                if number <= 0:
                    print("Error: Amount cannot be zero or negative. Try again")
                else:
                    return number
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

    # converts passing parameter from dollar to cents
    @staticmethod
    def convertFromDollarsToCents(amount):
        """
        Convert a dollar amount to cents.
        
        >>> BankUtility.convertFromDollarsToCents(3.57)
        357
        >>> BankUtility.convertFromDollarsToCents(0.01)
        1
        """
        return int(amount * 100)
    
    # generates random number
    @staticmethod
    def generateRandomInteger(min_value, max_value):
        """
        Generate a random integer between min_value and max_value (inclusive).
        
        >>> 0 <= BankUtility.generateRandomInteger(0, 5) <= 5
        True
        >>> 10 <= BankUtility.generateRandomInteger(10, 20) <= 20
        True
        """
        return random.randint(min_value, max_value)
    
# BankManager Class
class BankManager:
    def __init__(self):
        self.bank = Bank()
    
    # runs all options for user
    def run(self):
        print('\n')
        print("                         Hello! Welcome to \n")
        print("+==================================================================+")
        print("|                          Bank of CSC6003!                        |")
        print("+==================================================================+")
        print('\n')
        while True:
            try:
                self.display_menu()
                print('\n')
                choice = input("What do you want to do?: ").strip()
                if choice.isdigit():
                    choice = int(choice)
                
                if choice == 1:
                    print('\n')
                    self.openAccount()
                    print('\n')
                elif choice == 2:
                    print('\n')
                    self.getAccountInfo()
                    print('\n')
                elif choice == 3:
                    print('\n')
                    self.changePin()
                    print('\n')
                elif choice == 4:
                    print('\n')
                    self.depositMoney()
                    print('\n')
                elif choice == 5:
                    print('\n')
                    self.transferMoney()
                    print('\n')
                elif choice == 6:
                    print('\n')
                    self.withdrawMoney()
                    print('\n')
                elif choice == 7:
                    print('\n')
                    self.atmWithdrawal()
                    print('\n')
                elif choice == 8:
                    print('\n')
                    self.depositChange()
                    print('\n')
                elif choice == 9:
                    print('\n')
                    self.closeAccount()
                    print('\n')
                elif choice == 10:
                    print('\n')
                    self.addMonthlyInterest()
                    print('\n')
                elif choice == 11:
                    print('\n')
                    print("+======================================================================================+")
                    print("|        Thank you for using our banking system at Bank of CSC6003!. Goodbye!          |")
                    print("+======================================================================================+")
                    print('\n')
                    break
                else:
                    print("Error: Invalid choice. Please try again.")
            # handling any errors with exceptions
            except KeyboardInterrupt:
                print(f'\nError: Program terminated by user.')
                break
            except AttributeError:
                print("\nError: Program terminated by user.")
                break
            except Exception as e:
                print(f"\nError: An error occurred in the main loop: {e}")

    # displays all options in Bank Manager Class
    def display_menu(self):
        print("=" * 60)
        print("What do you want to do?")
        print("1. Open an account")
        print("2. Get account information and balance")
        print("3. Change PIN")
        print("4. Deposit money in account")
        print("5. Transfer money between accounts")
        print("6. Withdraw money from account")
        print("7. ATM withdrawal")
        print("8. Deposit change")
        print("9. Close an account")
        print("10. Add monthly interest to all accounts")
        print("11. End Program")
        print("=" * 60)

    # prompts for account number and pin
    def promptForAccountNumberAndPin(self):
        while True:
            try:
                accountNumber = int(BankUtility.promptUserForString("Enter account number: "))
                account = self.bank.findAccount(accountNumber)
                
                if account is None:
                    print(f"Error: Account not found for account number: {accountNumber}")
                    return None
                
                pin = BankUtility.promptUserForString("Enter PIN: ")
                
                if not account.isValidPin(pin):
                    print("Error: Invalid PIN")
                    return None
                
                return account
            except ValueError:
                print("Error: Account number must be a valid number.")

    # opens a new account
    def openAccount(self):
        print("+=========================================+")        
        print("|              OPEN ACCOUNT               |")
        print("+=========================================+")
        print('\n')
        firstName = BankUtility.promptUserForString("Enter Account Owner's First Name: ")
        if BankUtility.isNumeric(firstName) or len(firstName) is 0:
            print("Error: Invalid first name. Please enter a valid first name.")
            return
        lastName = BankUtility.promptUserForString("Enter Account Owner's Last Name: ")
        if BankUtility.isNumeric(lastName) or len(lastName) is 0:
            print("Error: Invalid last name. Please enter a valid last name.")
            return
        ssn = BankUtility.promptUserForString("Enter Account Owner's SSN (9 digits): ")
        if not BankUtility.isNumeric(ssn) or len(ssn) != 9:
            print("Error: Invalid SSN. Please enter 9 digits.")
            return

        account = Account(firstName, lastName, ssn)
        if self.bank.addAccountToBank(account):
            print(account.toString())
        else:
            print("Error: Failed to open account. Bank is full.")

    # fetches an accounts information
    def getAccountInfo(self):
        account = self.promptForAccountNumberAndPin()
        if account:
            print(account.toString())

    # updates an accounts pin
    def changePin(self):
        account = self.promptForAccountNumberAndPin()
        if account:
            new_pin = BankUtility.promptUserForString("Enter new PIN: ")
            if new_pin == account.pin:
                print("Error: New pin must not be the same as the old pin.")
            else:
                confirm_pin = BankUtility.promptUserForString("Enter new PIN again to confirm: ")
                
                if new_pin == confirm_pin:
                    if BankUtility.isNumeric(new_pin) and len(new_pin) == 4:
                        account.setPin(new_pin)
                        print('\n')
                        print("+==========================================================+")
                        print("|                Pin Updated Successfully!                 |")
                        print("+==========================================================+")
                    else:
                        print("Error: PIN must be 4 digits, try again.")
                else:
                    print("Error: PINs do not match, try again.")

    # deposits money from an account
    def depositMoney(self):
        account = self.promptForAccountNumberAndPin()
        if account:
            amount = BankUtility.promptUserForPositiveNumber("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
            cents = BankUtility.convertFromDollarsToCents(amount)
            new_balance = account.deposit(cents)       
            print('\n')             
            print("+=====================================================================+")
            print("|                        Deposit Complete!                            |")
            print("|                      --------------------                           |")
            print(f"|                   New balance: ${new_balance / 100:.2f}")
            print("|                                                                     |")
            print("+=====================================================================+")

    # withdrawals money from an account
    def withdrawMoney(self):
        account = self.promptForAccountNumberAndPin()
        if account:
            amount = BankUtility.promptUserForPositiveNumber("Enter amount to withdraw in dollars and cents (e.g. 2.57): ")
            cents = BankUtility.convertFromDollarsToCents(amount)
            if cents > account.getBalance():
                print(f"Insufficient funds in account {account.getAccountNumber()}")
            else:
                new_balance = account.withdraw(cents)
                print('\n')
                print("+==========================================================================================+")
                print("|                                 Withdrawn Complete!                                      |")
                print("|                                --------------------                                      |")
                print(f"|                        New balance: ${new_balance / 100:.2f}")
                print("|                                                                                          |")
                print("+==========================================================================================+")

    # transfers money from one account into another
    def transferMoney(self):
        print("+================================+")
        print("|    Account tranferring money   |")
        print("+================================+")
        print('\n')
        from_account = self.promptForAccountNumberAndPin()
        if from_account:
            print("+===============================+")
            print("|    Account recieving money    |")
            print("+===============================+")
            print('\n')
            to_account = self.promptForAccountNumberAndPin()
            if to_account:
                amount = BankUtility.promptUserForPositiveNumber("Enter amount to transfer in dollars and cents (e.g. 2.57): ")
                cents = BankUtility.convertFromDollarsToCents(amount)
                if cents > from_account.getBalance():
                    print(f"Insufficient funds in account {from_account.getAccountNumber()}")
                else:
                    from_account.withdraw(cents)
                    to_account.deposit(cents)
                    print('\n')
                    print("+=====================================================================================================+")
                    print("|                                Transfer Complete!                                                   |")
                    print("|                               --------------------                                                  |")
                    print(f"    New balance in account: {from_account.getAccountNumber()} is: ${from_account.getBalance() / 100:.2f}")
                    print(f"    New balance in account: {to_account.getAccountNumber()} is: ${to_account.getBalance() / 100:.2f}")
                    print("|                                                                                                     |")
                    print("+=====================================================================================================+")

    # converts withdrawals money from account based off of multiples of $5 (limit $1000)
    def atmWithdrawal(self):
        account = self.promptForAccountNumberAndPin()
        if account:
            amount = BankUtility.promptUserForPositiveNumber("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): ")
            if amount < 5 or amount > 1000 or amount % 5 != 0:
                print("Error: Invalid amount. Try again.")
            else:
                cents = int(amount * 100)
                if cents > account.getBalance():
                    print(f"Insufficient funds in account {account.getAccountNumber()}")
                else:
                    twenties = int(amount // 20)
                    tens = int((amount % 20) // 10)
                    fives = int((amount % 10) // 5)
                    
                    print(f"Number of 20-dollar bills: {twenties}")
                    print(f"Number of 10-dollar bills: {tens}")
                    print(f"Number of 5-dollar bills: {fives}")
                    
                    new_balance = account.withdraw(cents)      
                    print('\n')          
                    print("+====================================================================================+")
                    print("|                            ATM Withdrawal Complete!                                |")
                    print("|                          ----------------------------                              |")
                    print(f"                       New balance: ${new_balance / 100:.2f}")
                    print("|                                                                                    |")
                    print("+====================================================================================+")

    # method that converts string to coins and deposits money into an account
    def depositChange(self):
        account = self.promptForAccountNumberAndPin()
        if account:
            print('\n')
            print(f"'P' = 1 cent")
            print(f"'N' = 5 cents")
            print(f"'D' = 10 cents")
            print(f"'Q' = 25 cents")
            print(f"'H' = 50 cents")
            print(f"'W' = 100 cents")
            print('\n')
            coins = BankUtility.promptUserForString("Deposit coins: ")
            cents = CoinCollector.parseChange(coins)
            new_balance = account.deposit(cents)
            print('\n')
            print("+====================================================================================+")
            print("|                            Change Deposit Complete!                                |")
            print("|                          ----------------------------                              |")
            print(f"                    ${cents / 100:.2f} in coins deposited into account")
            print(f"                    New balance: ${new_balance / 100:.2f}")
            print("|                                                                                    |")
            print("+====================================================================================+")


    # method that closes an account in Bank class
    def closeAccount(self):
        account = self.promptForAccountNumberAndPin()
        if account:
            if self.bank.removeAccountFromBank(account):
                print('\n')
                print("+==============================================+")
                print("|                   Complete                   |")
                print("|              -----------------               |")
                print(f"|           Account {account.getAccountNumber()} closed            |")
                print("|                                              |")
                print("+==============================================+")
            else:
                print(f"Error: Failed to close account {account.getAccountNumber()}")

    # method that adds monthly interest rate to all accounts in Bank class
    def addMonthlyInterest(self):
        rate = BankUtility.promptUserForPositiveNumber("Enter annual interest rate percentage (e.g. 2.75 for 2.75%): ")
        self.bank.addMonthlyInterest(rate)

# runs doctests, initiates BankManager and runs program
if __name__ == "__main__":
    import doctest
    # due to account number and PIN being randomly generated its difficult to create doctests
    # optionflags=doctest.ELLIPSIS ignores values that are '...'
    # '...' is a placeholder value I have for the randomly generated account number and PIN
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    bank_manager = BankManager()
    bank_manager.run()