'''17.	How to convert a list to string? Give one example?'''

'''if the list only containg strings'''

lst=['Iam','Btech','student','course','is','AIML']

print(' '.join(lst))


'''If it contains mixed of data types'''

lst=[True,10.2,40,'student','AIML']
string=' '
for i in lst:
    string=string+" "+str(i)
print(string)    
