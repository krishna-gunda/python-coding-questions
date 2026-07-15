a=['krishna','vamshi','nikhil']
b=[20,30,40]

c=zip(a,b)
print(c) # c is the object it returns the object
print(tuple(c))  # we need to convert this into any list or tuple  the interable's inside are tuple only


for name,age in zip(a,b):
    print(f'name={name} and age={age}',end='\n')