

n=[int(x) for x in input('Enter numbers with the space :').split()]
result=[]
for i in range(len(n)):
    count=0
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            count+=1
        else:
            if n[i]<n[j]:
                count=count+1
                break
            else:
                count=count+1
    result.append(count)
print(result)                
            

