'''Manual String Formatter (Immutability Trap)

Given a string s = "hello", write a function capitalize_every_other(s) that returns 
a new string where every alternate character is capitalized, starting with the first 
character (index 0 uppercase, index 1 lowercase, index 2 uppercase, ...).'''

def capitalize_every_other(s):
    result=""
    for i in range(0,len(s)):
        if i%2==0 or i==0:
            result=result+s[i].upper()
        else:
            result=result+s[i]

    return result
print(capitalize_every_other("krishna"))    

# another appraoch
