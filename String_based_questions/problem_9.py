st="python developer"

'''b.	Display as ‘Python Developer'''

print(st.title())

'''c.	Count number of e's in that string.'''

print(f'the no of e"s in the above string is {st.count("e")}')


'''d.	Find index position of first ’o’ in the above string.'''


print(f'the index position of the 1st o in the string is {st.index('o')}')


'''e.	Find index position of second ‘o’ in the above string.'''

print(f'the index position of the 2st o in the string is {st.index('o',5)}')

'''f.	Spilt the same string into two elements like ‘python’,’developer’'''

print(f'splitted elemets={st.split(" ")}')

'''g.	Display string in reverse.'''

print(f'string reverse is = {" ".join(st.split(" ")[::-1])}')

'''h.	From the above string, display only ‘on dev’.'''
print(st[4:10])

'''i.	From above string remove ‘thon’'''

print(st.replace('python','py')) # since we can't remove the strign we need to use the replace function

'''j.	Copy the same string into other new strings like str1,str2 and str3 at a time'''

import copy
st1=copy.copy(st)
st2=copy.copy(st)
st3=copy.copy(st)

print(st1,id(st1))  # the three ids are same
print(st2,id(st2))
print(st3,id(st3))