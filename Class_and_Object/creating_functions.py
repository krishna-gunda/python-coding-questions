# ============================================================
#              METHODS (FUNCTIONS) INSIDE A CLASS
# ============================================================


# A function that is created inside a class is called a METHOD.


# ------------------------------------------------------------
# 1. CREATING A CLASS WITH A METHOD
# ------------------------------------------------------------

# Let's create a class called "Car".

class Car:

    # This is a method inside the Car class.
    def driving():
        print("Started driving")


# Here:
#
# Car       -> Class
# driving() -> Method
#
# The driving() method belongs to the Car class.


# ------------------------------------------------------------
# 2. CREATING AN OBJECT
# ------------------------------------------------------------

# To create an object from the Car class:

# car1 = Car()


# Now "car1" is an object of the Car class.


# ------------------------------------------------------------
# 3. CALLING THE METHOD USING THE OBJECT
# ------------------------------------------------------------

# We can call the method using the object:

# car1.driving()


# But if we run the above code, we get an error:
#
# TypeError: Car.driving() takes 0 positional arguments
# but 1 was given


# ------------------------------------------------------------
# 4. WHY DO WE GET THIS ERROR?
# ------------------------------------------------------------

# The reason is that Python automatically passes the object
# as the first argument when we call a method using an object.
#
# When we write:
#
#     car1.driving()
#
# Python internally treats it approximately like:
#
#     Car.driving(car1)
#
#
# But our method was created as:
#
#     def driving():
#
# It does not have any parameter to receive the object.
#
# Therefore Python says:
#
#     "I received 1 argument, but your method accepts 0."


# ------------------------------------------------------------
# 5. SOLUTION: USE "self"
# ------------------------------------------------------------

# We use "self" as the first parameter of an instance method.
#
# "self" refers to the CURRENT OBJECT.
#
# So when we write:
#
#     def driving(self):
#
# the "self" parameter receives the object that called
# the method.


class Car:

    def driving(self):
        print("Started driving")


# ------------------------------------------------------------
# 6. CREATING THE OBJECT
# ------------------------------------------------------------

car1 = Car()


# ------------------------------------------------------------
# 7. CALLING THE METHOD
# ------------------------------------------------------------

car1.driving()


# Output:
#
# Started driving


# ------------------------------------------------------------
# 8. WHAT ACTUALLY HAPPENS?
# ------------------------------------------------------------

# When we write:
#
#     car1.driving()
#
# Python automatically passes "car1" to the method.
#
# It is approximately equivalent to:
#
#     Car.driving(car1)
#
#
# Therefore:
#
#     def driving(self):
#
# "self" receives:
#
#     car1
#
#
# We can think of it like this:
#
#
#             Car CLASS
#                 |
#          ----------------
#          |              |
#       driving()        ...
#          ^
#          |
#        car1
#       OBJECT
#
#
# car1.driving()
#
# means:
#
# "Call the driving method of the Car class
#  using the car1 object."


# ------------------------------------------------------------
# 9. WHY IS IT CALLED "self"?
# ------------------------------------------------------------

# "self" represents the current object.
#
# For example:

class Car:

    def driving(self):
        print("Started driving")
        print("Current object is:", self)


car1 = Car()
car2 = Car()

car1.driving()
car2.driving()


# Here:
#
# When car1 calls driving():
#
#     self -> car1
#
#
# When car2 calls driving():
#
#     self -> car2
#
#
# Therefore, "self" changes depending on which object
# is calling the method.


# ------------------------------------------------------------
# 10. METHOD WITH INSTANCE ATTRIBUTES
# ------------------------------------------------------------

# We can use "self" to access the attributes of the
# current object.

class Car:

    def __init__(self, name):
        self.name = name

    def driving(self):
        print(self.name, "is driving")


car1 = Car("Volvo")
car2 = Car("BMW")

car1.driving()
car2.driving()


# Output:
#
# Volvo is driving
# BMW is driving


# Here:
#
# car1.driving()
#
# self -> car1
#
# Therefore:
#
# self.name
#
# means:
#
# car1.name
#
#
# Similarly:
#
# car2.driving()
#
# self -> car2
#
# Therefore:
#
# self.name
#
# means:
#
# car2.name


# ============================================================
# IMPORTANT POINTS TO REMEMBER
# ============================================================

# 1. A function inside a class is called a METHOD.
#
# 2. When we call an instance method using an object,
#    Python automatically passes that object as the first
#    argument.
#
# 3. We use "self" to receive that object.
#
# 4. "self" refers to the current object.
#
# 5. This is why we normally write:
#
#       def driving(self):
#
#    instead of:
#
#       def driving():
#
#
# 6. When we write:
#
#       car1.driving()
#
#    Python approximately treats it as:
#
#       Car.driving(car1)
#
#
# 7. Therefore:
#
#       self -> car1
#
#
# ============================================================
# SIMPLE FORMULA TO REMEMBER
# ============================================================
#
#     class ClassName:
#
#         def method(self):
#             ...
#
#
#     object1 = ClassName()
#
#     object1.method()
#
#
# In the above:
#
#     ClassName -> Class
#     object1   -> Object
#     method()  -> Method
#     self      -> Current Object
#
# ============================================================