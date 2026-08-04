'''Check Palindrome Number ⭐⭐⭐

Concepts: while, if

Problem:
Check whether a number is a palindrome.'''

a=int(input('enter a number='))
b=a
result=0

if a==0:
    print("enter a valid number")

else:
    while a!=0:
        rem=a%10
        result=result*10+rem
        a=a//10
    if result==b:
        print(f'the number {b} is palindrome')
    else:
        print(f'the number {b} is not palindrome')        
