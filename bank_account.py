# Define the Account class and assign attributes
class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    # Deposit money into the account
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited ₦{amount}. New balance: ₦{self.account_balance}")

    # Withdraw money from the account
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew ₦{amount}. New balance: ₦{self.account_balance}")
        else:
            print(f"Insufficient balance! Current balance: ₦{self.account_balance}")

    # Method to check the account balance
    def check_balance(self):
        return self.account_balance


#Testing the program by creating an instance of the account
my_account = Account("2301960110", 58000.0, "Mary Grace")

# Perform transactions using the methods
print("Initial balance:", "₦", my_account.check_balance())

my_account.deposit(50000)  # Deposit money

my_account.withdraw(13000)  # Withdraw money

my_account.withdraw(100000)  # Attempt to withdraw more than the balance

print("Final balance:", "₦",my_account.check_balance()) # Check the balance again


# Creating multiple instances and performing different transactions
account_1 = Account("3208413622", 32000.0, "Sam Bolt")
account_2 = Account("0067259098", 48000.0, "Jane Porter")

# Depositing into account_1
account_1.deposit(15000)
print("Account 1 Balance:", "₦",account_1.check_balance())

# Withdrawing from account_2
account_2.withdraw(7000)
print("Account 2 Balance:", "₦",account_2.check_balance())