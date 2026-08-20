'''1. Student Class — Basic

Create a Student class with:

name
age
marks

Use __init__() to initialize the instance attributes.

Create two student objects and display their details using a method called display().

Concepts: class, object, __init__(), instance attributes, self, methods.'''


class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(f'the name is {self.name}')
        print(f'the age is {self.age}')
        print(f'the marks is {self.marks}')

s1=Student("krishna",23,90)
s1.display()
s2=Student("Vamshi",22,100)
s2.display()       



