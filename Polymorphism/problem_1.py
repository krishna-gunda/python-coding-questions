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


