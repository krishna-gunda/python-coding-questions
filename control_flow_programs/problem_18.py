lis=[int(i) for i in input('Enter the numbers with the space :').split()]
k=int(input('Enter the value'))

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
