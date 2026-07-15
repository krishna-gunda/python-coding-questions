'''Sort a list using both sorted() and sort().'''

a=[1,4,3,6,8,2,3,43,52]

c=sorted(a)  # here sorted will create a new list it does not change the original list
print(c)


print(a.sort()) # here the original list is changed and returns None
print(a)