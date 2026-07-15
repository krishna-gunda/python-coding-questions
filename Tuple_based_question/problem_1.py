'''How can you assign the first element 
of a list to one variable and the remaining 
elements to another variable?  without using the for loop and index'''


a=[1,2,3,4,5]
b,*c,d=a   
print(b)
print(c)
print(d)


