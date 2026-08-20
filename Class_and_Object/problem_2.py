'''2. Car Class — Class vs Instance Attributes

Create a Car class with:

Class attributes:
wheels = 4
vehicle_type = "Car"
Instance attributes:
brand
color
price

Create two car objects with different values.

Create a method called display() that prints all the details.'''

class Car:
    wheels=4
    vehicle_type="car"
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
    def display(self):
        print(f'the vechile type is {self.vehicle_type} and has {Car.wheels} wheels and brand is {self.brand} and color is {self.color} and the price is {self.price}')

# creating the object for the Car

c1=Car('BMW','Black',2400000)
c1.display() 

# You need to call display() manually because display() is a normal method. Python automatically calls __init__() when you create the object, but it does not automatically call display().