'''Print the memory address of a variable using id().'''


a=10
print(id(a))


# this prints the memeory location of the object 

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  #1463474837696

print(id(b)) # 1463474835712


# Although a and b have the same contents, they are different objects, so they have different IDs.


x = 100
y = x

print(id(x)) #140717373904408

print(id(y))  #140717373904408


# Since x and y reference the same object, both id() calls return the same value.


