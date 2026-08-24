class Payment:
    def __init__(self,pay):
        self.payment=pay
        print(f'Processing the payment {self.payment} using the {self.__class__.__name__}')
    def showmsg(self):
        print("Welcome to the payment system")    
class Creditcard(Payment):
    def __init__(self,pay):
        self.pay=pay
        super().showmsg()
        super().__init__(self.pay)
        commition=self.pay*(2/100)
        print(f'Transaction fee is {commition}')
        print(f'The final amount is {self.pay+commition}')
        

class Debitcard(Payment):
    def __init__(self,pay):
        self.pay=pay
        super().showmsg()
        super().__init__(self.pay)
        commition=25
        print(f'Transaction fee is {commition}')
        print(f'The final amount is {self.pay+commition}')
class Netbanking(Payment):
    def __init__(self,pay):
        self.pay=pay
        super().showmsg()
        super().__init__(self.pay)
        commition=50
        print(f'Transaction fee is {commition}')
        print(f'The final amount is {self.pay+commition}')

                

cr=Creditcard(4000)
db=Debitcard(3000)
nb=Netbanking(50000)



#####################################################################
# adding the another approach



# Parent class
class Payment:

    def __init__(self, amount):
        self.amount = amount

    def show_message(self):
        print("Welcome to the Payment System")

    def process_payment(self):
        print("Processing payment...")




class CreditCard(Payment):

    def process_payment(self):

        # Calling the parent class method
        super().show_message()

        # Credit Card commission = 2%
        commission = self.amount * 2 / 100

        final_amount = self.amount + commission

        print(f"Payment of ₹{self.amount} processed using Credit Card")
        print(f"Transaction fee: ₹{commission}")
        print(f"Final amount: ₹{final_amount}")



class DebitCard(Payment):

    def process_payment(self):

        # Calling the parent class method
        super().show_message()

        # Debit Card fixed commission
        commission = 25

        final_amount = self.amount + commission

        print(f"Payment of ₹{self.amount} processed using Debit Card")
        print(f"Transaction fee: ₹{commission}")
        print(f"Final amount: ₹{final_amount}")




class NetBanking(Payment):

    def process_payment(self):

        # Calling the parent class method
        super().show_message()

        # Net Banking fixed commission
        commission = 50

        final_amount = self.amount + commission

        print(f"Payment of ₹{self.amount} processed using Net Banking")
        print(f"Transaction fee: ₹{commission}")
        print(f"Final amount: ₹{final_amount}")




payment1 = CreditCard(4000)
payment2 = DebitCard(3000)
payment3 = NetBanking(50000)




payments = [payment1, payment2, payment3]

for payment in payments:

    payment.process_payment()

    print("-----------------------------")


