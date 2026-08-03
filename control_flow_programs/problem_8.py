'''Sum Until User Enters 0 ⭐⭐⭐

Concepts: while

Problem:

Keep accepting numbers from the user until they enter 0.

Finally print the sum of all entered numbers.'''

a=int(input("enter the number "))
result=0
while a!=0:
    result+=a
    a=int(input("enter the number "))
print(f'the sum of all digits is {result}')    

# another method

answer=0
while True:
    b=int(input("enter th enumber "))
    if b==0:
        break
    else:
        answer+=b
print(f'the sum of all the numbers is {answer}')        
