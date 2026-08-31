'''Problem Statement

Write a Python program that takes an integer as input and determines whether the number is even or odd.

If the number is even, print Even.

If the number is odd, print Odd.

Input

A single integer n.

Output

Print:

Even if the number is even.
Odd if the number is odd.'''


a=int(input('Enter a number :'))
if a==0:
    print('The value is Zero')
elif a%2==0:
    print('Even')    
else:
    print('Odd')    