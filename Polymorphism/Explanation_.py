# polymorphism

# polymorphism is the technique that we can use the same method names for the diffrent classes
# in the diffrent classes we can use the same method name and the methods would perform diffrent actions based on the class
# when ever we call the child class method the child method would only execute and call the child class method

#lets se an example

class Vechile:
    def car(self):
        print("The vechile class is executing")

class Car:
    def car(self):
        print("The car class is executing")

# in the above example we have created the same methods with the diffrent classes

vech1=Vechile()
vech1.car()        