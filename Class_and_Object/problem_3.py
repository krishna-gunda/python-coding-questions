'''3. Bank Account — Methods + Instance Variables

Create a BankAccount class with:

account_holder
balance

Use __init__() to initialize them.

Create these methods:

deposit(amount)
withdraw(amount)
display_balance()

Requirements:

deposit() should add money to the balance.
withdraw() should subtract money.
Don't allow withdrawal if the amount is greater than the balance.
Display the final balance.

Example:

Account Holder: Krishna
Initial Balance: 10000


Deposit: 5000
Withdraw: 3000


Final Balance: 12000'''

class Bank_Account:
    def __init__(self,holder,balance):
        self.account_holder=holder
        self.account_balance=balance
    def deposit(self,amount):
        self.account_balance=self.account_balance+amount
        return self.account_balance
    def withdraw(self,amount):
        if self.account_balance>=amount:
            self.account_balance=self.account_balance-amount
            return self.account_balance
        else:
            return "your balance is insufficient to withdraw"
    def display_balance(self):
        return self.account_balance    
h1=Bank_Account("krishna",5000)
print(h1.deposit(5000))
print(h1.withdraw(11000)) 
print(h1.display_balance())        


# 10000
# your balance is insufficient to withdraw
# 10000