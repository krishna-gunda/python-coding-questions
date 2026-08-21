'''1. Bank Account — Basic Encapsulation

Create a BankAccount class with a private variable __balance.

Create methods:

deposit(amount)
withdraw(amount)
show_balance()

Rules:

Deposit amount must be greater than 0.
Withdrawal amount must not be greater than the balance.
Balance should not be directly modified from outside.'''

class Bank_Account:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("The amount is not accepted")
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print("withdrawed the amount ",amount)
        else:
            print(f'the amount {amount} is not avaiable in the account')
    def show_balance(self):
        print('The balance in the account is ',self.__balance)

user1=Bank_Account(10000)
user1.deposite(10)
user1.withdraw(1000)
user1.show_balance()
