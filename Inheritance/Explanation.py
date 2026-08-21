class Employee:
    def work(self):
        print("The work is started")  # this is Employee class

# lets create another class
class Developer:
    def code(self):
        print("The developer is coding") # This is the Developer class

class Tester:
    def testing(self):
        print("The tester is testing the app") # this is the test class


# here we have created 3 classes employee.developer and the tester but here we can see that 
# we can call the methods by creating the objects to the classes we can only use the methods of that class only
# we can't access the empolyee class methods in the developer and the tester 
# what if if want to use the method of the employee class in the developer and the tester to make it possible here comes the inheritance

class Employee:
    def work(self):
        print("The work is started")  # this is Employee class

# lets create another class
class Developer(Employee): # we can create the inheritance easily by using the brackets for the class and here you can see the Employee class is the parent class where we are going to inherit the code of the employee class
    def code(self):
        print("The developer is coding") # This is the Developer class

class Tester:
    def testing(self):
        print("The tester is testing the app") # this is the test class

d=Developer()
d.work()        # the output is The work is started
# here we are calling the diffrent class method by using the inheritance concept 
d.code() # we can also call the own method of that class





