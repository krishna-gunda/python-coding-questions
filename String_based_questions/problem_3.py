'''Count occurrences of a character.'''

a='elephant'

seen=[]

for i in a:
    if i not in seen:
        print(f'{i} =count is {a.count(i)}')
        seen.append(i)


'''Find the index of a substring.'''

print(a.find('pha'))  # if the string not found it returns -1

print(a.index("pha"))  # if the string not found it raises error 
