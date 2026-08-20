'''Employee — Class Attribute + Instance Attributes

Create an Employee class.

Class attribute:
company = "ABC Technologies"
Instance attributes:
name
salary
department

Create a method:

display()

Create three employee objects with different names, salaries and departments.

Print their details.

Also print the common company name.'''


class Employee:
    company="ABC Technologies"
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print(self.company)
        print(self.name)
        print(self.salary)
        print(self.department)

emp1=Employee("krishna",10000,"AIML")
emp1.display()
emp2=Employee("vamshi",20000,"CSM")
emp2.display()
emp3=Employee("nikhil",10000,"AIML")
emp3.display()