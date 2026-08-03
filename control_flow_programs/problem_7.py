''' Write a Python program to determine whether the given 
number is a Harshad Number (divisible by the sum of its digits).'''


a=input('enter a number ')
result=0
for i in a:
    result+=int(i)
if int(a)%result==0:
    print(f'{a} is a Harshad Number')
else:
    print(f'{a} is not a Harshad Number')    

