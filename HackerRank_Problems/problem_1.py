'''HackerRank — Designer Door Mat

You are given two integers N and M.

Your task is to design a door mat pattern using the characters .|. and -, with the word WELCOME in the center.

Input Format

The first line contains two space-separated integers:

N M

Where:

N is the number of rows.
M is the width of the mat.
N is always an odd positive integer.
M is 3 times N.
Output Format

Print the designed door mat pattern.

The pattern should follow these rules:

The total number of rows must be N.
The total width of every row must be M.
The top half should contain increasing .|. patterns.
The middle row should contain WELCOME.
The bottom half should contain decreasing .|. patterns.
The pattern should be centered using -.
Sample Input
9 27
Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
Another Example

Input:

7 21

Expected output:

---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''


n,m=map(int,input("Enter the Length and height using space :").split())

for i in range(n):
    if i==n//2:
        print("Welcome".center(m,"-"))
    elif i<n//2:
        pattern=".|."*(2*i+1)
        print(pattern.center(m,"-")) 
    else:
        pattern=".|."*(2 * (n - i) - 1)
        print(pattern.center(m,"-"))       
     
        