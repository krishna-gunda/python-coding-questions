'''
PROBLEM: Permutations of a String

You are given a string S and an integer K.

Your task is to generate and print all possible permutations of size K from the string S.

The permutations must be printed in lexicographic (alphabetical) sorted order.

INPUT FORMAT:

The input contains two values separated by a space:
- The first value is the string S.
- The second value is the integer K.

CONSTRAINTS:

- The string S contains only uppercase English characters.
- The value of K is a positive integer.
- K will not be greater than the length of S.

OUTPUT FORMAT:

Print all possible permutations of size K.
Each permutation should be printed on a separate line.

The permutations must be printed in lexicographic sorted order.

SAMPLE INPUT:

HACK 2

SAMPLE OUTPUT:

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

EXPLANATION:

The given string is:

S = HACK

K = 2

We need to select 2 characters at a time and arrange them in every possible order.

The possible permutations are:

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

They are printed in lexicographic sorted order.
'''

from itertools import permutations
char,length=map(str,input().split())
for i in list(permutations(sorted(list(char)),int(length))):
    print("".join(i))