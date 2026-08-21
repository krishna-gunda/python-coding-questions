# ============================================================
# ENCAPSULATION
# ============================================================

# Encapsulation means:
# Protecting the data inside a class and controlling how
# the data can be accessed or modified from outside the class.


# ============================================================
# WITHOUT ENCAPSULATION
# ============================================================

class Bank_Account:

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("The balance is:", self.balance)


b1 = Bank_Account(10000)

# We can access the balance directly from outside the class
# using the object.

print(b1.balance)       # Output: 10000


# We can also change the balance directly from outside.

b1.balance = 0

# Now the balance has been changed to 0.

b1.show_balance()       # Output: The balance is: 0


# PROBLEM:
# Anyone can directly change the bank balance.
#
# In a real-world banking system, a user should not be able
# to directly modify their bank balance.
#
# Therefore, we need a way to protect the variable.
#
# This is where ENCAPSULATION is useful.


# ============================================================
# WITH ENCAPSULATION
# ============================================================

class Bank_Account:

    def __init__(self, balance):

        # __ before the variable makes it a private attribute.
        # It tells Python that this variable is intended to be
        # accessed only inside the class.

        self.__balance = balance

    def show_balance(self):

        # We can access the private variable inside the class.
        print("The balance is:", self.__balance)


b2 = Bank_Account(10000)


# Let us try to change the private variable from outside.

b2.__balance = 0

# This does NOT change the original private variable.
#
# Python treats b2.__balance as a different attribute because
# the original variable is actually name-mangled internally.


b2.show_balance()

# Output:
# The balance is: 10000


# ============================================================
# WHY DO WE USE __ BEFORE A VARIABLE?
# ============================================================

# __balance means that the variable is intended to be private.
#
# It prevents accidental direct access or modification from
# outside the class.
#
# We can access and use __balance inside the class.
#
# Outside the class, we should use methods to interact with
# the private variable.


# ============================================================
# SIMPLE WAY TO REMEMBER ENCAPSULATION
# ============================================================

# WITHOUT ENCAPSULATION:
#
# User
#   |
#   ↓
# Directly changes balance
#   |
#   ↓
# balance = 0
#
#
# WITH ENCAPSULATION:
#
# User
#   |
#   ↓
# Method
#   |
#   ↓
# Validation / Rules
#   |
#   ↓
# Private variable (__balance)


# ============================================================
# IMPORTANT
# ============================================================

# Encapsulation does NOT mean that the variable can NEVER
# be accessed.
#
# It means that we protect the internal data and provide
# controlled ways to access or modify it.


# Interview definition:
#
# "Encapsulation is the process of wrapping data and methods
# together inside a class and restricting direct access to
# the internal data."