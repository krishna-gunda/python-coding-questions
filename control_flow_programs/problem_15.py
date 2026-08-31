'''
Problem Statement

You are given a list of integers. Find the first element that appears only once in the list.

If every element appears more than once, print -1.

The first unique element means the element whose first occurrence comes before the first occurrence of all other unique elements.

Input

A single line containing space-separated integers.

Output

Print the first element that appears exactly once.

If there is no such element, print:

-1
Example 1

Input:

4 5 1 2 1 4 2 5 7

Output:

7
Example 2

Input:

9 4 9 6 7 4 6

Output:

7
Example 3

Input:

1 2 3 2 1 3

Output:

-1
'''

n=[int(x) for x in input('Enter the numbers with the space ').split()]
result=[]
for i in n:
    if n.count(i)==1:
        result.append(i)
if result:  # here empty list is considered as false
    print(result)
else:
    print(-1)   


# another approach 

frequency={}
n=[int(x) for x in input('Enter the numbers with the space :').split()]
result=[]
for i in n:
    frequency[i]=frequency.get(i,0)+1   # Get the current count of the number; if it is not in the dictionary, start from 0, then add 1.
for i in frequency:
    if frequency.get(i)==1:
        result.append(i)
print(result if result else -1)
