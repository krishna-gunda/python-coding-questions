'''Print every character of a string with out for loop.'''

a='krishna'
print(*a,sep='-')



'''Find the length of a string.'''

len(a)
print("the length of the string is_"+str(len(a)))



'''Access the first and last character.'''

b,*c,d=a

print(f'first character is {b}')
print(f'last character is {d}')


'''Reverse a string using slicing.'''

print(f'reverse of the string is {a[::-1]}')

'''Print characters at even indexes.'''

print(f'Even character indexes are {a[::2]}')  # here the step size is 2 so it prints even indexes


'''Print characters at odd indexes.'''

print(f'odd character indexes are {a[1::2]}')