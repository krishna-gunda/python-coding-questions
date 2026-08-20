#__init__ is a special method or function which is also known as python constructor

class car:

    name="volvo"
    color="Black"
    cost=200    # this are the class attributes 
    def speed(self):  # here self refers to the currrent object c1 
        print(f'the speed is {self.cost}')  # here self refers to c1 and then cl.speed is known as 200 so it prints 200

c1=car()
# after creating the object to the class 
# we need maunally call the functions or methods to execute
c1.speed() # here we are calling the function manually 

# to over come this we have constructor which automatically call the methods when object is created

class Bike:
    name="YAMAHA"
    cost=120000
    color="BLACK"

    def __init__(self): # this is the special function that executes this method when object is created
        print(f'the name of the bike is {self.name} and cost is {self.cost} and the color is {self.color}')


b1=Bike() # it automatically executes the function without calling 

