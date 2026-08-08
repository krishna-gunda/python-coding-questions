'''1. Student Marks Analyzer ⭐⭐⭐⭐☆
Topics
List
Dictionary
Loops
Functions
if-else
Problem

You are given the names of students and their marks in three subjects.

Store the data in a dictionary.

Then answer Q queries. For each student name:

Print Average
Print Highest Mark
Print Lowest Mark
If the student does not exist print "Student Not Found".
Input
4

Krishna 90 80 70
Ram 65 72 80
Rahul 100 95 98
Sita 55 60 58

3

Krishna
Rahul
Ravi
Output
Average = 80.0
Highest = 90
Lowest = 70

Average = 97.67
Highest = 100
Lowest = 95

Student Not Found'''

data={}
def store(num):
    for i in range(num):
        
        name,sub1,sub2,sub3=input("enter the name ,3 subject marks with the space").split(" ")
        data[name]=int(sub1),int(sub2),int(sub3)
    return data

print(store(3))


def output(num):
    lis=[]
    for i in range(num):
        name=input("enter the name ")
        lis.append(name)
    for name in lis:
        if name in data:
            marks=data.get(name)
            print(f'Average={sum(marks)/len(marks)}')
            print(f'Highest marks={max(marks)}')
            print(f'Lowest marks={min(marks)}')
        else:
            print(f'{name} not in the data')        
output(3)     

