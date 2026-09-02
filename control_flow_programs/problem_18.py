lis=[1, 2, 3,4]
k=5

result=[]
for i in range(len(lis)):
    res=[]
    for j in range(i,len(lis)):
        res.append(lis[j])
        if sum(res)==k:
            result.append(res)
            break
        elif sum(res)>k:
            
            break


print(result)
print(f'The maximum consicutive numbers whose sum is k are {result[0]}')




        

        
    