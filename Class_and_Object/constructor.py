# ============================================================
#                  __init__() / CONSTRUCTOR
# ============================================================


# __init__() is a special method in Python.
#
# It is commonly called a CONSTRUCTOR.
#
# The __init__() method is automatically executed when an
# object is created from a class.
#
#
# IMPORTANT:
#
# __init__() does NOT automatically execute every method
# present inside the class.
#
# Only the __init__() method is automatically called when
# the object is created.


# ------------------------------------------------------------
# 1. EXAMPLE WITHOUT __init__()
# ------------------------------------------------------------

class Car:

    # These are CLASS ATTRIBUTES.

    name = "Volvo"
    color = "Black"
    cost = 200

    # This is a METHOD.

    def speed(self):

        # self refers to the current object.
        #
        # If c1 calls this method:
        #
        # self -> c1
        #
        # Therefore:
        #
        # self.cost -> c1.cost
        #
        # Since cost = 200:
        #
        # self.cost -> 200

        print(f"The speed is {self.cost}")


# ------------------------------------------------------------
# 2. CREATING THE OBJECT
# ------------------------------------------------------------

c1 = Car()


# The object has been created.
#
# But the speed() method has NOT automatically executed.
#
# We need to call the method manually.

c1.speed()


# Output:
#
# The speed is 200


# ------------------------------------------------------------
# 3. WHY DO WE NEED TO CALL speed() MANUALLY?
# ------------------------------------------------------------

# When we create:
#
#     c1 = Car()
#
# Python creates the object.
#
# But Python does NOT automatically execute every method
# inside the class.
#
# Therefore, we have to explicitly call:
#
#     c1.speed()
#
# to execute the speed() method.


# ============================================================
#                  USING __init__()
# ============================================================


# Now let's see how __init__() works.


class Bike:

    # These are CLASS ATTRIBUTES.

    name = "YAMAHA"
    cost = 120000
    color = "BLACK"


    # --------------------------------------------------------
    # __init__() METHOD
    # --------------------------------------------------------

    def __init__(self):

        # __init__() is a special method.
        #
        # It is automatically executed when an object
        # of the Bike class is created.
        #
        # self refers to the current object.
        #
        # If b1 creates the object:
        #
        # self -> b1
        #
        # Therefore:
        #
        # self.name  -> b1.name
        # self.cost  -> b1.cost
        # self.color -> b1.color

        print(
            f"The name of the bike is {self.name}, "
            f"cost is {self.cost}, "
            f"and color is {self.color}"
        )


# ------------------------------------------------------------
# 4. CREATING THE OBJECT
# ------------------------------------------------------------

b1 = Bike()


# We did NOT write:
#
#     b1.__init__()
#
# Python automatically calls __init__() when we write:
#
#     b1 = Bike()
#
#
# Output:
#
# The name of the bike is YAMAHA,
# cost is 120000,
# and color is BLACK


# ============================================================
#              WHAT EXACTLY HAPPENS?
# ============================================================


# When we write:
#
#     b1 = Bike()
#
# Python creates the Bike object.
#
# Then Python automatically executes:
#
#     __init__()
#
# So we can think of it approximately as:
#
#     b1 = Bike()
#          |
#          v
#     __init__(b1)
#
#
# Therefore:
#
#     self -> b1
#
#
# And inside __init__():
#
#     self.name
#
# becomes:
#
#     b1.name
#
#
# self.cost
#
# becomes:
#
#     b1.cost
#
#
# self.color
#
# becomes:
#
#     b1.color


# ============================================================
#          __init__() WITH INSTANCE ATTRIBUTES
# ============================================================


# The most common use of __init__() is to initialize
# INSTANCE ATTRIBUTES.


class Student:

    def __init__(self, name, age):

        # These are INSTANCE ATTRIBUTES.

        self.name = name
        self.age = age


# When we create the object:

s1 = Student("Krishna", 22)


# Python automatically calls:

# __init__(s1, "Krishna", 22)


# Therefore:

# self -> s1
#
# self.name = name
# becomes:
#
# s1.name = "Krishna"
#
#
# self.age = age
# becomes:
#
# s1.age = 22


print(s1.name)
print(s1.age)


# Output:
#
# Krishna
# 22


# ============================================================
#          IMPORTANT DIFFERENCE
# ============================================================


class CarExample:

    # Class attribute
    cost = 200

    def speed(self):

        print("Speed method executed")

    def __init__(self):

        print("Constructor executed")


# Create object

c1 = CarExample()


# Output:
#
# Constructor executed
#
# Notice that:
#
# speed() did NOT execute automatically.
#
# Why?
#
# Because __init__() is automatically called,
# but speed() is a normal method.


# To execute speed(), we need to call it manually:

c1.speed()


# Output:
#
# Speed method executed


# ============================================================
# IMPORTANT POINTS TO REMEMBER
# ============================================================


# 1. __init__() is a special method in Python.
#
#
# 2. It is commonly called a constructor.
#
#
# 3. __init__() automatically executes when an object
#    is created.
#
#
# 4. Normal methods do NOT automatically execute.
#
#    Example:
#
#        c1.speed()
#
#    We need to call them manually.
#
#
# 5. self refers to the current object.
#
#
# 6. __init__() is commonly used to initialize
#    instance attributes.
#
#
# 7. Example:
#
#        class Student:
#
#            def __init__(self, name, age):
#                self.name = name
#                self.age = age
#
#
#        s1 = Student("Krishna", 22)
#
#
#    Here:
#
#        self -> s1
#        self.name -> s1.name
#        self.age -> s1.age


# ============================================================
#                 EASY REAL-WORLD EXAMPLE
# ============================================================


# Imagine buying a new bike.
#
# When the bike object is created, we may want some
# information to be initialized automatically.
#
# For example:
#
#     name
#     cost
#     color
#
# __init__() can automatically initialize these values
# when the object is created.


class BikeDetails:

    def __init__(self, name, cost, color):

        self.name = name
        self.cost = cost
        self.color = color

        print("Bike object created successfully!")


b1 = BikeDetails("YAMAHA", 120000, "BLACK")
b2 = BikeDetails("HONDA", 100000, "RED")


print(b1.name)
print(b1.cost)
print(b1.color)

print(b2.name)
print(b2.cost)
print(b2.color)


# ============================================================
#                    FINAL SUMMARY
# ============================================================


# CLASS
#   -> Blueprint / Design
#
#
# OBJECT
#   -> Actual instance created from the class
#
#
# ATTRIBUTE
#   -> Data / Property
#
#
# METHOD
#   -> Function inside a class
#
#
# __init__()
#   -> Special method
#   -> Automatically executes when an object is created
#   -> Commonly called a constructor
#   -> Mainly used to initialize instance attributes
#
#
# self
#   -> Refers to the current object
#
#
# Example:
#
#     class Car:
#
#         def __init__(self, name):
#             self.name = name
#
#
#     c1 = Car("Volvo")
#
#
# Here:
#
#     Car        -> Class
#     c1         -> Object
#     __init__() -> Constructor
#     self       -> c1
#     name       -> Instance attribute
#
#
# ============================================================
# MOST IMPORTANT CONCEPT
# ============================================================
#
# When we write:
#
#     c1 = Car("Volvo")
#
# Python automatically calls __init__().
#
# But when we have:
#
#     def speed(self):
#         ...
#
# Python does NOT automatically call speed().
#
# We must write:
#
#     c1.speed()
#
# ============================================================