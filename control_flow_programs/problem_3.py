'''Check whether a triangle is valid using three angles.'''

a,b,c=map(int,input("enter the triangle numbers with the space seperation : ").split())

if a+b+c==180:
    print("Its valid Triangle")
else:
    print("Not Valid Triangle")    