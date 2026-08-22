'''1. Employee Salary System — Hierarchical Inheritance 🔥

Create a base class Employee with:

name
employee_id
base_salary

Create three child classes:

Developer
DataScientist
Manager
Requirements

Employee should have:

calculate_salary()
display_details()

Salary rules:

Developer

Bonus = 20% of base salary
Total salary = base salary + bonus

DataScientist

Bonus = 30% of base salary
Total salary = base salary + bonus

Manager

Bonus = 40% of base salary
Total salary = base salary + bonus

Each child class should override calculate_salary().

Example
Employee: Krishna
ID: 101
Role: Data Scientist
Base Salary: 50000

Bonus: 15000
Total Salary: 65000
Challenge

Use super() wherever appropriate instead of repeating the parent-class code.'''



class Employee:
    def __init__(self,name,empid,base_salary):
        self.name=name
        self.emp_id=empid
        self.base_salary=base_salary
        
    def show_details(self):
        print(f'The employee name is {self.name} and EmpID is {self.emp_id} and the base salary is {self.base_salary}')

    def calculate_salary(self,num):
        bonus=self.base_salary*(num/100)
        print(f'The salary is {self.base_salary+bonus}')


class Developer(Employee):
    def __init__(self,name,empid,base_salary):
        super().__init__(name,empid,base_salary) #here super will send the current object to the parent class using the super
    def calculate_salary(self):
        super().calculate_salary(20) # here 20 is represented as percentage and it will go to the parent class and do the calculation

# dev=Developer("krishna",102,30000)
# dev.show_details()
# dev.calculate_salary()

class Datascientist(Employee):
    def __init__(self,name,id,base_salary):
        super().__init__(name,id,base_salary)
    def calculate_salary(self):
            super().calculate_salary(30)
# data=Datascientist("nikhil",102,34000)
# data.show_details()
# data.calculate_salary()

class Manager(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id,salary)
    def calculate_Salary(self):
        super().calculate_salary(40)
mag1=Manager("vamshi",202,32000)
mag1.show_details()
mag1.calculate_Salary()        
