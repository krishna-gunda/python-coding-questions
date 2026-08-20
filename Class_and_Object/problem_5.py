'''Product — Discount Calculation

Create a Product class with:

name
price
quantity

Use __init__() to initialize them.

Create a method:

total_price()

which calculates:

price × quantity

Create another method:

apply_discount(discount)

which applies the given percentage discount.

Example:

Product: Laptop
Price: 50000
Quantity: 2
Discount: 10%


Total before discount: 100000
Total after discount: 90000'''

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_price(self):
        self.money=self.price*self.quantity
        return self.money
    def apply_discount(self,discount):
        discount_amount=self.money*(discount/100)
        self.total_money= self.money-discount_amount
        return self.total_money
    def total_amount(self):
        print(f'The total amount before discount is {self.money}')
        print(f'The total amount after discount is {self.total_money}')

obj1=Product("Chapathi",20,5)
print(obj1.total_price())
print(obj1.apply_discount(20))
obj1.total_amount()