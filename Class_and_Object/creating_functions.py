# lets create the functions (methood in the python)

# creating the class
# class car:
#     def driving():
#         print("Started driving")

# here we have created the class with the function

# when we are calling the function we need to crreate the object by using the object we can call the function
# creating the object 
#car1=car()
# calling the function using the object 
#car1.driving() # here when we call like this we get error car.driving() takes 0 positional arguments but 1 was given

# we get error because what is the proof that we calling only the function that is inside car class 
# so we give the self key word in the argument while creating the function the self keyword refers to the
# object that we created 

class car:
    def driving(self):
        print("Started driving")

car1=car()
car1.driving()


 