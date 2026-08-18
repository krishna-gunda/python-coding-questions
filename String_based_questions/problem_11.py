'''Anagram Frequency Checker

Write a function is_anagram(s1, s2) that checks if two strings are anagrams of each 
other, ignoring case, spaces, and punctuation.'''
import string


def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    for i in s1:
        if i in string.punctuation or i == " ":
            s1 = s1.replace(i, "")

    for i in s2:
        if i in string.punctuation or i == " ":
            s2 = s2.replace(i, "")

    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))

    if s1 == s2:
        return "Anagram"
    else:
        return "Not Anagram"

print(is_anagram("Dormitory", "Dirty Room!"))

# another approach

def anagram(s1,s2):
    s3=''
    s4=''
    for i in s1:
        if i.isalnum():
            s3=s3+i
    s3=s3.lower()    
    for j in s2:
        if j.isalnum():
            s4=s4+j
    s4=s4.lower()
    s3="".join(sorted(s3))
    s4="".join(sorted(s4)) 
    
    if s3==s4:
        return "ANAGRAM"
    else:
        return "NOT ANAGRAM"                 
    
print(anagram("Dormitory", "Dirty Room!"))    