'''Count Digits ⭐⭐⭐

Concepts: while

Problem:
Count the number of digits in an integer.'''


a=int(input("enter a number="))
b=a
count=0
if a==0:
    print("the digit count is one")
else:
    while a!=0:
        rem=a%10
        count+=1    
        a=a//10
    print(f'the total no of digits in {b} is {count}')    
