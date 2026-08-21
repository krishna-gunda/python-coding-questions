'''Real-World Problem: Bank Account Management System'''

class Bank:
    def __init__(self,name,number,amount,pin):
        self.__account_holder=name
        self.__account_number=number
        self.__balance=amount
        self.__pin=pin
    def show_account_details(self):
        return self.__account_holder,self.__account_number,self.__balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Amount should be greater than 0")
    def withdraw(self,amount):
        if amount>self.__balance and amount>0:
            print("The amount is not available in your account")
        else:
            self.__balance-=amount
            print(f'The {amount} is withdrawn and the balance is {self.__balance}')
    def check_balance(self,pin):
        if self.__pin==pin:
            print(f'The balance is {self.__balance}')
        else:
            print(f'The pin {pin} entered is wrong') 
    def change_pin(self,old,pin):
        if self.__pin==old:
            self.__pin=pin
            print("Pin changed successfully")
            
        else:
            print("The previous pin is wrong enter the correct pin to change the pin")
            
    def account_number(self):
        print(f'The account Number is {self.__account_number}')

account = Bank(
    "Krishna",
    "123456",
    10000,
    1234
)
print(account.show_account_details())
account.deposite(20000)
account.withdraw(8000)
account.change_pin(1234,4567)


