'''Square Every Number in a list'''

numbers=[1,3,5,6]
square=map(lambda x:x*x ,numbers)
print(list(square))


'''Dynamic Input'''

numbers=list(map(int,input("Enter the numbers with the space=").split(" ")))
square=map(lambda x:x*x ,numbers)
print(list(square))

'''Find Even Numbers'''

numbers=list(map(int,input("Enter the numbers with the space=").split(" ")))

even=filter(lambda x:x%2==0,numbers)

print(list(even))

'''Sort Numbers Based on Absolute Value'''

number=[-10, 5, -3, 8, -2]

sort=sorted(number,key=lambda x:abs(x))
print(list(sort))

