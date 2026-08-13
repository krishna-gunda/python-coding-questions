'''Write a lambda function that takes a number and returns its double.'''

double=lambda x:x+x

print(double(3))

'''Write a lambda function that takes a number and returns its square.'''

square=lambda x:x*x

print(square(5))

'''Write a lambda function that accepts two numbers and returns their sum.'''

sum=lambda x,y:x+y

print(sum(3,4))

'''Find the Larger Number

Write a lambda function that accepts two numbers and returns the larger number.'''

larger=lambda x,y:x if x>y else y

print(larger(15,20))


'''Finding largest of three numbers'''

large=lambda x,y,z:x if x>y and x>z else ( y if y>x and y>z else z)

print(large(3,7,2))

'''Find the Last Digit

Write a lambda function that accepts an integer and returns its last digit.'''

last_digit=lambda x:x%10

print(last_digit(12345))


'''Convert Celsius to Fahrenheit

Write a lambda function to convert Celsius into Fahrenheit.'''

fahrenheit=lambda c:(c*(9/5))+32

print(fahrenheit(19))