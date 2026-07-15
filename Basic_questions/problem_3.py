'''Swap two variables without using a third variable.'''


a=4
b=2
a,b=b,a
print(f'a is {a} and b is {b}')


#another approach

a=4
b=2
b=a+b
a=b-a
b=b-a
print(f'a is {a} and b is {b}')