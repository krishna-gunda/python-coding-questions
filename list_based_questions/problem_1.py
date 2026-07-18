'''Generate a list [10,12,14,16,18,20] by using range function?'''

lis=[]
for i in range(10,21,2):
    lis.append(i)
print(lis)    


lst=[10,20,'Python',10.5,1,10,True,False,0]

'''a.	How to display the count of elements in the above list?'''

print(f'the count of elements of the list is {len(lst)}')


'''b.	How to count no of occurrences of ‘10’ in the above list?'''

print(f'the no of occurences of 10 is {lst.count(10)}')

'''c.	What are the no of occurrences ‘1’ in the above list?'''

print(f'the no of occurences of 1 is {lst.count(1)}') # here the true returns 1 so there are 2 ones


'''d.	How to add complex number 10+5j to the above list?'''


a=10+5j
lst.append(a)
print(lst)

'''e.	How to add both complex number 1+2j and float value 1.3 to the above list.'''

a=[1+2j,1.3]

lst.extend(a)
print(lst)

'''f.	How to add bool value ‘True’ between 10 and 20 in the above list?'''
lst.insert(1,True)
print(lst)

'''g.	How to remove the str value ‘Python’ from the above list?'''
lst.remove('Python')
print(lst)

'''h.	How to reverse the above list?'''

print(f'the reverse of the list is {lst[::-1]}')

'''j.	Display index position of float value 10.5 in the above list?'''

print(lst.index(10.5)) # 3

'''k.	Replace float value 10.5 with 20.5'''

lst[3]=20.5
print(lst)
