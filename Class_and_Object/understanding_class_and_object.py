# ============================================================
#                  CLASS AND OBJECT IN PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. REAL-WORLD EXAMPLE
# ------------------------------------------------------------

# Let's understand Class and Object using a real-world example
# of a CAR.
#
# Before manufacturing a real car, we first need a DESIGN or
# BLUEPRINT.
#
# The design can specify:
#
# - How many seats the car should have
# - What color the car should be
# - What the car name should be
# - What the price should be
# - What actions the car can perform
#
# This DESIGN/BLUEPRINT is similar to a CLASS in Python.
#
# The actual car manufactured using that design is similar
# to an OBJECT in Python.
#
# In simple terms:
#
#       CLASS  -> Design / Blueprint
#       OBJECT -> Actual thing created using the design
#
#
# A class can contain:
#
# 1. Attributes -> Data / Properties
# 2. Methods    -> Functions / Actions


# ------------------------------------------------------------
# 2. CREATING A CLASS
# ------------------------------------------------------------

# Let's create a Car class.

class Car:

    # These are ATTRIBUTES.
    # Since they are created directly inside the class,
    # they are called CLASS ATTRIBUTES.

    car_name = "Volvo"
    car_price = 1200000
    color = "Black"


# ------------------------------------------------------------
# 3. CREATING AN OBJECT
# ------------------------------------------------------------

# A class is only a design/blueprint.
# To create an actual car using that design,
# we need to create an OBJECT.

car1 = Car()

# Here:
#
# Car  -> Class
# car1 -> Object
#
# We can create multiple objects from the same class.

car2 = Car()
car3 = Car()

# One class can be used to create many objects.
#
# Just like one car design can be used to manufacture
# thousands of cars.


# ------------------------------------------------------------
# 4. ACCESSING ATTRIBUTES USING THE OBJECT
# ------------------------------------------------------------

# We can access the attributes using the object name.

print(car1.car_name)
print(car1.car_price)
print(car1.color)

# Output:
#
# Volvo
# 1200000
# Black
#
# General syntax:
#
# object_name.attribute_name
#
# Example:
#
# car1.car_name


# ------------------------------------------------------------
# 5. ACCESSING ATTRIBUTES USING THE CLASS NAME
# ------------------------------------------------------------

# Since car_name, car_price and color are CLASS ATTRIBUTES,
# we can also access them directly using the class name.

print(Car.car_name)
print(Car.car_price)
print(Car.color)

# Output:
#
# Volvo
# 1200000
# Black
#
# General syntax:
#
# ClassName.attribute_name
#
# Example:
#
# Car.car_name


# ------------------------------------------------------------
# 6. TYPES OF ATTRIBUTES
# ------------------------------------------------------------

# There are two important types of attributes:
#
# 1. Class Attributes
# 2. Instance Attributes


# ------------------------------------------------------------
# 7. CLASS ATTRIBUTES
# ------------------------------------------------------------

# Class attributes are created directly inside the class.
#
# They are common to all objects unless an object has
# its own value for that attribute.

class Student:

    # These are CLASS ATTRIBUTES.

    college = "JBREC"
    university = "JNTUH"


# Creating objects

student1 = Student()
student2 = Student()

# Both objects can access the same class attributes.

print(student1.college)
print(student2.college)

# We can also access them using the class name.

print(Student.college)
print(Student.university)

# Output:
#
# JBREC
# JBREC
# JBREC
# JNTUH


# ------------------------------------------------------------
# 8. INSTANCE ATTRIBUTES
# ------------------------------------------------------------

# Instance attributes are different from class attributes.
#
# Instance attributes belong to a PARTICULAR OBJECT.
#
# They are usually created using "self".
#
# For example:
#
# student1 can have:
#     name = "Krishna"
#     age = 22
#
# student2 can have:
#     name = "Rahul"
#     age = 21
#
# Therefore, different objects can have different values.


class StudentDetails:

    def __init__(self, name, age):

        # These are INSTANCE ATTRIBUTES.

        self.name = name
        self.age = age


# Creating objects with different values

student1 = StudentDetails("Krishna", 22)
student2 = StudentDetails("Rahul", 21)


# Accessing instance attributes

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# Output:
#
# Krishna
# 22
# Rahul
# 21


# ------------------------------------------------------------
# 9. WHY DO WE USE "self"?
# ------------------------------------------------------------

# "self" refers to the CURRENT OBJECT.
#
# When we write:
#
# self.name = name
#
# it means:
#
# "Store the name inside the current object."
#
# When we create:
#
# student1 = StudentDetails("Krishna", 22)
#
# Python stores:
#
# student1.name = "Krishna"
# student1.age = 22
#
#
# When we create:
#
# student2 = StudentDetails("Rahul", 21)
#
# Python stores:
#
# student2.name = "Rahul"
# student2.age = 21


# ------------------------------------------------------------
# 10. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
# ------------------------------------------------------------

class Employee:

    # CLASS ATTRIBUTE
    # Common information

    company = "ABC Technologies"

    def __init__(self, name, salary):

        # INSTANCE ATTRIBUTES
        # Different for each object

        self.name = name
        self.salary = salary


# Creating two objects

employee1 = Employee("Krishna", 50000)
employee2 = Employee("Rahul", 60000)


# Instance attributes have different values

print(employee1.name)
print(employee1.salary)

print(employee2.name)
print(employee2.salary)


# Class attribute is common

print(employee1.company)
print(employee2.company)

# We can also access the class attribute using
# the class name.

print(Employee.company)


# ------------------------------------------------------------
# 11. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE - SUMMARY
# ------------------------------------------------------------

# CLASS ATTRIBUTE:
#
# class Employee:
#     company = "ABC Technologies"
#
# It is created directly inside the class.
#
# We can access it using:
#
# Employee.company
# employee1.company
# employee2.company
#
#
# INSTANCE ATTRIBUTE:
#
# def __init__(self, name):
#     self.name = name
#
# It belongs to a particular object.
#
# We access it using:
#
# employee1.name
# employee2.name
#
# Different objects can have different values.


# ------------------------------------------------------------
# 12. CLASS WITH ATTRIBUTES AND METHODS
# ------------------------------------------------------------

# A class can contain both:
#
# - Attributes -> Data
# - Methods    -> Actions
#
# A method is simply a function defined inside a class.


class CarWithMethods:

    # Class attribute
    wheels = 4

    def __init__(self, name, color):

        # Instance attributes
        self.name = name
        self.color = color

    # Method
    def start(self):

        print(self.name, "is starting")

    # Method
    def drive(self):

        print(self.name, "is driving")

    # Method
    def stop(self):

        print(self.name, "has stopped")


# Creating an object

car1 = CarWithMethods("Volvo", "Black")


# Accessing attributes

print(car1.name)
print(car1.color)
print(car1.wheels)


# Calling methods

car1.start()
car1.drive()
car1.stop()


# ------------------------------------------------------------
# 13. FINAL REAL-WORLD UNDERSTANDING
# ------------------------------------------------------------

# Think about a CAR manufacturing company.
#
# First, they create a DESIGN/BLUEPRINT.
#
# In Python:
#
#             class Car:
#                 ...
#
# This is the CLASS.
#
#
# Then they manufacture actual cars using that design.
#
# In Python:
#
#             car1 = Car()
#             car2 = Car()
#             car3 = Car()
#
# These are OBJECTS.
#
#
# The car's properties such as:
#
# - name
# - color
# - price
# - model
#
# are ATTRIBUTES.
#
#
# The car's actions such as:
#
# - start()
# - drive()
# - stop()
#
# are METHODS.
#
#
# ------------------------------------------------------------
# IMPORTANT THINGS TO REMEMBER
# ------------------------------------------------------------
#
# CLASS
#     -> Blueprint / Design
#
# OBJECT
#     -> Actual instance created from the class
#
# ATTRIBUTE
#     -> Data / Property of a class or object
#
# METHOD
#     -> Function / Action inside a class
#
# __init__()
#     -> Constructor used to initialize an object
#
# self
#     -> Refers to the current object
#
#
# ------------------------------------------------------------
# SIMPLE FORMULA TO REMEMBER
# ------------------------------------------------------------
#
#       CLASS
#         |
#         | creates
#         v
#       OBJECT
#
#
# Example:
#
#       class Car:
#           ...
#
#       car1 = Car()
#
#       Car  -> Class
#       car1 -> Object
#
#
# ------------------------------------------------------------
# COMPLETE SIMPLE EXAMPLE
# ------------------------------------------------------------

class Car:

    # Class attribute
    wheels = 4

    # Constructor
    def __init__(self, name, price, color):

        # Instance attributes
        self.name = name
        self.price = price
        self.color = color

    # Method
    def display(self):

        print("Car Name:", self.name)
        print("Price:", self.price)
        print("Color:", self.color)
        print("Wheels:", self.wheels)


# Creating objects

car1 = Car("Volvo", 1200000, "Black")
car2 = Car("BMW", 2500000, "White")


# Calling the method

car1.display()

print()

car2.display()


# Expected Output:
#
# Car Name: Volvo
# Price: 1200000
# Color: Black
# Wheels: 4
#
# Car Name: BMW
# Price: 2500000
# Color: White
# Wheels: 4