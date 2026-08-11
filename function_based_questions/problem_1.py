'Write a function that returns the number 100'

def krishna():
    return 100
print(krishna)   #Refers to the function object (its address in memory).

print(krishna())  # here we are calling the function




'Write a function to find the square of a number.'


def square(num):
    return num*num

print(square(5))  # output 25
print(square(10))  # output 100


'Write a function to check whether a number is positive or negative.'

def checking(num):
    if num >=0:
        print('positive')

    else:
        print('negative')  

x=checking(10)          # here if use the print in the function it directly shows the output but the python returns 
                        # none automatically 
print(x)                # here it prints None 

'''print() = Show the value
return = Give the value back'''


'Write a function to return the largest of two numbers.'

def largest(a,b):
    if a>b:
        return a
    else:
        return b

print(largest(10,20))    # output 20
