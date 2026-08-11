'''Problem

Employee data is stored as

(Name, Department, Salary)

Print

Highest paid employee
Lowest paid employee
Department-wise average salary
Employees earning above department average
Sort employees by salary (without using sort() or sorted())
Input
5

Krishna AI 85000
Ram HR 55000
Rahul AI 92000
Sita HR 60000
Anu AI 78000
Output
Highest Paid : Rahul

Lowest Paid : Ram

AI Average = 85000

HR Average = 57500

Above Department Average

Rahul
Sita

Sorted Salaries

Ram
Sita
Anu
Krishna
Rahul'''



def store_emply_details(num):
    data={}
    for i in range(num):
        name,dep,sal=input("Enter the details like name,department,salary with space=").split(" ")
        data[name]=(dep,int(sal))
    return data

def max_salary(data):
    
    first_key = next(iter(data))
    max_sal = data[first_key][1]
    max_name = first_key
    min_sal = data[first_key][1]
    min_name = first_key
    for name in data:
        if data[name][1]>max_sal:
          max_sal=data[name][1]
          max_name=name
        elif data[name][1]<min_sal and data[name][1]!=max_sal:
            min_sal=data[name][1]
            min_name=name
    return max_name,max_sal,min_name,min_sal  


def dep_avg_sal(data):
    dic={}   
    count={}
    avg_sal={}
    for name in data:
        if data[name][0] not in dic:
            dic[data[name][0]]=data[name][1]
            count[data[name][0]]=1
        else:
            dic[data[name][0]]+=data[name][1]
            count[data[name][0]]+=1
    for dep in dic.keys():
        sal=dic.get(dep)
        number=count.get(dep)
        avg_sal[dep]=sal/number

                
    return dic ,count,avg_sal     



            
        

data = {
    'nikhil': ('AI', 89),
    'krishna': ('HR', 2345),
    'vamshi': ('AI', 2389),
    'sai': ('AI', 389)
}

#num=int(input("enter the no of employee details to enter in the data base "))
#data=store_emply_details(num)
#print(data)
max_name,max_sal,min_name,min_sal=max_salary(data)
print(f'The highest paid is {max_sal} and name is {max_name}\nThe lowest paid is {min_sal} and name is {min_name}')

print(dep_avg_sal(data))

