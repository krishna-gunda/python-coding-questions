lis = [1, -1, 5, -2, 0]
k=3

result=[]
for i in range(len(lis)):
    res=[]
    for j in range(i,len(lis)):
        res.append(lis[j])
        if sum(res)==k:
            result.append(len(res))
            
        



if result:
    print(f'The maximum consicutive numbers whose sum is k are {max(result)}')
else:
    print(0)
