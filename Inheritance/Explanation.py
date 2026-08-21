# ============================================================
#                    INHERITANCE IN PYTHON
# ============================================================

# Inheritance is an OOP concept that allows a child class
# to reuse the methods and attributes of a parent class.
#
# In simple words:
#
# Parent class  -> Contains common things
# Child class   -> Gets the common things + has its own things
#
#
# REAL-WORLD EXAMPLE:
#
# Employee
#    |
#    |------ Developer
#    |
#    |------ Tester
#
# Every employee needs to work.
# But a Developer can code and a Tester can test.
#
# So, we can keep the common method work() inside Employee
# and allow Developer and Tester to inherit it.


# ------------------------------------------------------------
# WITHOUT INHERITANCE
# ------------------------------------------------------------

class Employee:
    def work(self):
        print("The employee is working")


class Developer:
    def code(self):
        print("The developer is coding")


class Tester:
    def testing(self):
        print("The tester is testing the application")


# Here, Employee, Developer and Tester are separate classes.
#
# Developer can use only its own method code().
# Tester can use only its own method testing().
#
# Developer cannot use work() because work() belongs to
# the Employee class.


# ------------------------------------------------------------
# INHERITANCE
# ------------------------------------------------------------

class Employee:
    def work(self):
        print("The employee is working")


# Developer(Employee)
#
# Employee inside the brackets means:
# Developer is inheriting from Employee.
#
# Employee  -> Parent class
# Developer -> Child class
#
# Developer will now get the work() method from Employee.

class Developer(Employee):
    def code(self):
        print("The developer is coding")


# Tester is also inheriting from Employee.
#
# Therefore, Tester can also use work().

class Tester(Employee):
    def testing(self):
        print("The tester is testing the application")


# ------------------------------------------------------------
# USING THE DEVELOPER CLASS
# ------------------------------------------------------------

d = Developer()

d.work()
# work() belongs to Employee.
# But Developer inherited Employee.
# Therefore, Developer can use work().

d.code()
# code() belongs to Developer.
# Therefore, Developer can use its own method.


# Output:
# The employee is working
# The developer is coding


# ------------------------------------------------------------
# USING THE TESTER CLASS
# ------------------------------------------------------------

t = Tester()

t.work()
# work() is inherited from Employee.

t.testing()
# testing() is the Tester class's own method.


# Output:
# The employee is working
# The tester is testing the application


# ============================================================
# IMPORTANT POINT
# ============================================================

# Inheritance means:
#
# Child class = Parent class features + Child's own features
#
# Developer = Employee + Developer
# Tester    = Employee + Tester
#
#
# Employee
#    |
#    |------ work()
#    |
#    +------ Developer
#    |          |
#    |          +------ code()
#    |
#    +------ Tester
#               |
#               +------ testing()
#
#
# So:
#
# Developer can use:
#     work()  -> inherited from Employee
#     code()  -> Developer's own method
#
# Tester can use:
#     work()     -> inherited from Employee
#     testing()  -> Tester's own method
#
#
# The main purpose of inheritance is CODE REUSABILITY.
#
# Instead of writing the same common method again and again
# in Developer and Tester, we write it once in Employee
# and inherit it in the child classes.
#
# In simple words:
#
# "Inheritance allows a child class to reuse the properties
# and methods of a parent class."