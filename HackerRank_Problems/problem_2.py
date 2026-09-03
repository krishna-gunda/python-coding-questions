'''
PROBLEM: Cartesian Product

You are given two lists A and B.

Your task is to find the Cartesian Product of A and B.

The Cartesian Product A × B contains all possible pairs where:
- The first element comes from list A.
- The second element comes from list B.

Example:

A = [1, 2]
B = [3, 4]

A × B = [(1, 3), (1, 4), (2, 3), (2, 4)]

Note:
- A and B are sorted lists.
- Both lists contain no duplicate integers.
- The resulting tuples should be printed in sorted order.

INPUT FORMAT:

The first line contains space-separated integers representing list A.

The second line contains space-separated integers representing list B.

OUTPUT FORMAT:

Print all tuples of the Cartesian Product separated by spaces.

SAMPLE INPUT:

1 2
3 4

SAMPLE OUTPUT:

(1, 3) (1, 4) (2, 3) (2, 4)
'''

from itertools import product

x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

for i in product(x, y):
    print(i, end=" ")


# another approach
# 
x=[2,3]
y=[5,4]
result=[]
for i in x:
    for j in y:
        result.append((i,j))
print(result)    