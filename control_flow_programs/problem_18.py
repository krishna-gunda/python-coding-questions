lis=[1, -1, 5, -2, 3]
k=3
res=[]
result=[]
for i in lis:
    if sum(result)==k:
        res.append(len(result))
        result.clear()
    else:
        result.append(i)
print(max(res))
      

        

        
    