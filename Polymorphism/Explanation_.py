# ============================================================
# POLYMORPHISM IN PYTHON
# ============================================================

# What is Polymorphism?
#
# Polymorphism means "many forms".
#
# In Python, polymorphism allows us to use the SAME method name
# with DIFFERENT classes, where each class can perform a
# DIFFERENT action.
#
# Simple example:
#
#     car()
#
# can exist in different classes, but the behavior of car()
# can be different in each class.


# ============================================================
# 1. SIMPLE POLYMORPHISM
# ============================================================

class Vehicle:

    def car(self):
        print("Vehicle class is executing")


class Car:

    def car(self):
        print("Car class is executing")


# Both classes have the SAME method name: car()
#
# But they are completely different classes.


vehicle1 = Vehicle()
vehicle1.car()

# Output:
# Vehicle class is executing


car1 = Car()
car1.car()

# Output:
# Car class is executing


# WHY IS THIS POLYMORPHISM?
#
# Because we are using the same method name:
#
#     car()
#
# in different classes.
#
# But the behavior is different:
#
# Vehicle -> "Vehicle class is executing"
# Car     -> "Car class is executing"


# ============================================================
# 2. POLYMORPHISM WITH INHERITANCE
# ============================================================

# Polymorphism is commonly used with inheritance.
#
# A child class can OVERRIDE the method of the parent class.
#
# Method overriding means:
#
# Parent class has a method
# Child class creates the SAME method
# Child class changes the behavior of that method.


class Vehicle:

    def car(self):
        print("Vehicle is moving")


class Car(Vehicle):

    def car(self):
        print("Car is moving")


vehicle1 = Vehicle()
vehicle1.car()

# Output:
# Vehicle is moving


car1 = Car()
car1.car()

# Output:
# Car is moving


# IMPORTANT:
#
# Car inherited from Vehicle.
#
# Vehicle has:
#     car()
#
# Car also has:
#     car()
#
# Since Car has its own car() method, the Car method
# OVERRIDES the Vehicle method.


# ============================================================
# 3. METHOD OVERRIDING
# ============================================================

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


animal1 = Animal()
animal1.sound()

# Output:
# Animal makes a sound


dog1 = Dog()
dog1.sound()

# Output:
# Dog barks


# Here:
#
# Animal -> sound()
# Dog    -> sound()
#
# Same method name.
# Different behavior.
#
# This is called METHOD OVERRIDING.
#
# Method overriding is one of the important ways
# polymorphism is achieved in Python.


# ============================================================
# 4. USING super()
# ============================================================

# Sometimes we don't want to completely replace the
# parent method.
#
# We want:
#
#     1. Parent behavior
#     +
#     2. Child behavior
#
# In that situation, we can use super().


class Vehicle:

    def car(self):
        print("Vehicle class is executing")


class Transport(Vehicle):

    def car(self):

        # Call the parent class car() method
        super().car()

        # Add extra behavior
        print("Transport class is executing")


transport1 = Transport()
transport1.car()

# Output:
#
# Vehicle class is executing
# Transport class is executing


# ============================================================
# HOW super() WORKS
# ============================================================

# Transport inherits from Vehicle.
#
# Vehicle has:
#
#     car()
#
# Transport also has:
#
#     car()
#
# When we write:
#
#     super().car()
#
# Python goes to the PARENT class (Vehicle)
# and executes its car() method.


# So:
#
# transport1.car()
#
# first enters:
#
#     Transport.car()
#
# Then:
#
#     super().car()
#
# calls:
#
#     Vehicle.car()
#
# Then Python returns to Transport.car()
# and executes the next print statement.


# ============================================================
# 5. VERY IMPORTANT DIFFERENCE
# ============================================================

# CASE 1: Child overrides parent method WITHOUT super()


class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        print("Child method")


child1 = Child()
child1.show()

# Output:
# Child method


# Why?
#
# Child has its own show() method.
#
# Therefore, Python executes the Child method.
#
# Parent method is NOT executed.


# ============================================================
# CASE 2: Child overrides parent method WITH super()
# ============================================================


class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):

        super().show()

        print("Child method")


child1 = Child()
child1.show()

# Output:
#
# Parent method
# Child method


# Why?
#
# super().show()
#
# calls the parent class method first.
#
# Then the child method continues executing.


# ============================================================
# 6. REAL-WORLD EXAMPLE
# ============================================================

class Payment:

    def pay(self):
        print("Processing payment")


class CreditCard(Payment):

    def pay(self):
        print("Processing payment using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Processing payment using UPI")


class Cash(Payment):

    def pay(self):
        print("Processing payment using Cash")


# Same method:
#
#     pay()
#
# Different classes:
#
#     CreditCard
#     UPI
#     Cash
#
# Different behavior.


payment1 = CreditCard()
payment1.pay()

# Output:
# Processing payment using Credit Card


payment2 = UPI()
payment2.pay()

# Output:
# Processing payment using UPI


payment3 = Cash()
payment3.pay()

# Output:
# Processing payment using Cash


# ============================================================
# 7. THE MAIN IDEA OF POLYMORPHISM
# ============================================================

# The main idea is:
#
# SAME METHOD NAME
#        +
# DIFFERENT OBJECTS
#        =
# DIFFERENT BEHAVIOR
#
#
# Example:
#
# CreditCard -> pay() -> Credit Card payment
# UPI        -> pay() -> UPI payment
# Cash       -> pay() -> Cash payment


# ============================================================
# 8. EASY WAY TO REMEMBER
# ============================================================

# Polymorphism = ONE NAME, MANY FORMS
#
# Example:
#
#     pay()
#
# CreditCard -> pay() -> Credit Card payment
# UPI        -> pay() -> UPI payment
# Cash       -> pay() -> Cash payment
#
#
# Method Overriding:
#
# Parent has method
# Child creates the same method
# Child changes the behavior
#
#
# super():
#
# Used when the child wants to call the
# parent class method.


# ============================================================
# FINAL SUMMARY
# ============================================================

# 1. Polymorphism means "many forms".
#
# 2. We can use the same method name in different classes.
#
# 3. The same method can perform different actions
#    depending on the object/class.
#
# 4. In inheritance, a child class can override
#    the parent's method.
#
# 5. If the child method is called normally:
#
#       child_object.method()
#
#    the child method executes.
#
# 6. If we want to execute the parent method from
#    the child method, we use:
#
#       super().method()
#
# 7. Polymorphism helps us write flexible and reusable code.


# ============================================================
# ONE-LINE INTERVIEW ANSWER
# ============================================================

# Polymorphism is an OOP concept that allows the same
# method name to have different behaviors depending on
# the object or class using it.