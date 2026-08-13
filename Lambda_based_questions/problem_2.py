# '''Square Every Number in a list'''

# numbers=[1,3,5,6]
# square=map(lambda x:x*x ,numbers)
# print(list(square))


# '''Dynamic Input'''

# numbers=list(map(int,input("Enter the numbers with the space=").split(" ")))
# square=map(lambda x:x*x ,numbers)
# print(list(square))

# '''Find Even Numbers'''

# numbers=list(map(int,input("Enter the numbers with the space=").split(" ")))

# even=filter(lambda x:x%2==0,numbers)

# print(list(even))

# '''Sort Numbers Based on Absolute Value'''

# number=[-10, 5, -3, 8, -2]

# sort=sorted(number,key=lambda x:abs(x))
# print(sort)


'''Sort Tuples by Second Element'''

data = [
    ("A", 50),
    ("B", 20),
    ("C", 80),
    ("D", 40)
]

tuple_sort=sorted(data,key=lambda x:x[1],reverse=True) #descending order
print(tuple_sort)


students = [
    {"name": "Krishna", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Anil", "marks": 95},
    {"name": "Sita", "marks": 68}
]
dict_sort=sorted(students,key=lambda x:x['marks'])

print(dict_sort)