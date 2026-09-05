'''
# ============================================================

# Problem: Exception Handling - Integer Division

# ============================================================

#

# You are given two values, a and b.

# Your task is to perform integer division (a // b)

# and print the result.

#

# Input Format:

# The first line contains an integer T, the number of test cases.

# The next T lines each contain two space-separated values, a and b.

#

# Output Format:

# For each test case:

# - Print the result of integer division a // b.

# - If a ZeroDivisionError occurs, print:

# Error Code: integer division or modulo by zero

# - If a ValueError occurs, print the corresponding error message.

#

# Sample Input:

#

# 3

# 1 0

# 2 $

# 3 1

#

# Sample Output:

#

# Error Code: integer division or modulo by zero

# Error Code: invalid literal for int() with base 10: '$'

# 3

#

# ============================================================
'''

# soultion
t=int(input())

for i in range(t):
    a,b=map(str,input().split())
    try:
        print(int(a)//int(b))
    except (ValueError,ZeroDivisionError) as e:
        print(f'Error Code: {e}') 
         