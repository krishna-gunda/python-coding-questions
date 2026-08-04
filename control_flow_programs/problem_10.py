'''Reverse a Number ⭐⭐⭐

Concepts: while, %, //

Problem:
Write a program to reverse a given number.'''


a=int(input("enter a number "))
result=0


if a==0:
    print("Enter valid number")
else:
    while a!=0:
        rem=a%10
        result=result*10+rem
        a=a//10
    print(f'the reverse of the number is {result}')    



