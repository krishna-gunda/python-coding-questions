
# encapsulation

class Bank_Account:
    def __init__(self,balance):
        self.balance=balance
    def show_balance(self):
        print("The balance is ",self.balance)

b1=Bank_Account(10000)
# before showing the balance we can access the balance from outside by using the object and we can change the balance directly
# the real use case is so the user can change the balance directly without bank permission 
# this is not at all possible in the real world
b1.balance=0 # here we are changing the balance again to the 0 
# so in order to protect this variable we have the encapsulation
b1.show_balance() # here the bank balance showing as 0

# with encapsualtion method

class Bank_Account:
    def __init__(self,balance):
        self.__balance=balance # here we nee put __ underscore to make the variable private and it can't be changed outside the class
    def show_balance(self):
        print("The balance is ",self.__balance)

b2=Bank_Account(10000)
# let us try to chnage the variable 
b2.__balance=0 # here we are changing the varible to 0
b2.show_balance() # but the result is 10000 so by using the encapsualtion we can change the varible in the class itself and in the methods we can acess from outside but we can't change 


