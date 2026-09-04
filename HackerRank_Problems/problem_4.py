'''
============================================================
                ALPHABET RANGOLI
============================================================

Problem Statement:

You are given an integer N.

Your task is to print an alphabet rangoli pattern of size N.

The pattern uses lowercase English alphabets starting from 'a'.

For example, when N = 5, the alphabets used are:

a b c d e

The pattern should expand from the top to the middle and then
shrink symmetrically.

Input Format:

A single integer N representing the size of the rangoli.

Constraints:

1 <= N <= 26

Output Format:

Print the alphabet rangoli pattern of size N.

Each alphabet must be separated by a hyphen (-).

The entire pattern must be centered using hyphens.

Example 1:

Input:
3

Output:

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----


Example 2:

Input:
5

Output:

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------


Example 3:

Input:
1

Output:

a


Important:

- Use lowercase alphabets only.
- Separate every character with '-'.
- The pattern must be symmetric.
- The middle row must contain the alphabet 'a'.
- The output should contain exactly 2*N - 1 rows.
- The width of every row should be the same.
'''

def print_rangoli(size):
    width=(4*size)-3
    a=101
    for i in range(97+(size-1),96,-1):
        r=[chr(i) for i in range(97+(size-1),a,-1)]
        right=list(chr(i))+r[::-1]
        left=[chr(i) for i in range(97+(size-1),a,-1)]
        string="-".join(left+right)
        print(string.center(width,"-"))
        a-=1
    b=0  
    for i in range(98,97+size):
      r=[chr(i) for i in range(99+b,97+size)]
      right=list(chr(i))+r
      left=r[::-1]
      string="-".join(left+right)
      print(string.center(width,"-"))
      b+=1
print_rangoli(5)

#output

'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

