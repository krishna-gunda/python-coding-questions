"""Lets understand the diffrence between the deep copy and shallow copy """

a=[100,200,300]
b=a
b.append(500)
print(b)
print(a)

'''Here we are not creating the another list instead we are refering the two variables with the same object 
so what ever the changes in the b that would be done in the a the both ids will be same so if we change in the data
then automatically changes'''

"This is not about the deep copy and shallow copy"

"""this is the deep copy Completely separate objects, so changes never affect the original """
import copy
c=[10,[20,30],40,50]
e=copy.deepcopy(c)
e[1].append(100)
print(e)
print(c)

'''this is the shallow copy Separate outer list, but nested mutable objects are shared.'''
d=copy.copy(c)
d[1].append(200)
print(d)    
print(c)
"""[10, [20, 30, 200], 40, 50]
   [10, [20, 30, 200], 40, 50]"""