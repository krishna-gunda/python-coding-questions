class FoodOrder:
    def __init__(self,name,amount):
        self.customer_name=name
        self.amount=amount
    def show_details(self):
        print(f'The customer name is {self.customer_name} and the order amount is {self.amount}')    
    def calculate_delivery_charge(self):
        print("calculating delivery charge....")

class Swiggy(FoodOrder):
    def calcualating_charge(self):
        super().show_details()
        super().calculate_delivery_charge()
        if self.amount>=500:
            print("Delivery charges 0")
        else:
            print(f'Delivery charges are {self.amount+40}')   
class Zomato(FoodOrder):
    def calculating_charge(self):
        super().show_details()
        super().calculate_delivery_charge()
        if self.amount>=500:
            print(f'Delivery charges are {self.amount+20}')
        else:
             print(f'Delivery charges are {self.amount+50}')    

class Restarent(FoodOrder):
    def calculating_charge(self):
        super().show_details()
        super().calculate_delivery_charge()
        
        print(f'Delivery charges are {self.amount}')
                 

swi=Swiggy("krishna",200)
swi.calcualating_charge()
print("===========================================")
zm=Zomato("Vamshi",500)
zm.calculating_charge()
print("===========================================")
res=Restarent("nikhil",700)
res.calculating_charge()