'''
Problem Statement

You are given a string containing words separated by spaces.

Find the first word that appears only once in the string.

The comparison should be case-insensitive, meaning "Python" and "python" should be treated as the same word.

However, the output should preserve the original form of the first unique word.

If every word appears more than once, print -1.

Input

A single line containing a sentence.

Output

Print the first word that occurs exactly once, preserving its original capitalization.

If there is no unique word, print:

-1
Example 1

Input:

Python is easy and python is powerful

Output:

easy
Example 2

Input:

Data science is fun data Science is useful

Output:

fun
Example 3

Input:

Python python PYTHON

Output:

-1
'''

# here we need to find only one word that appears first
result=[]
n=input('Enter the string ').split()
m=[i.lower() for i in n]
for i in n:
    if m.count(i.lower())==1:
        result.append(i)
        break
print(result[0] if result else -1) 
        
    


