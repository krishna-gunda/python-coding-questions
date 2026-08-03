'calculate to matrix'

import pandas as pd

matrix1=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])

matrix2=pd.DataFrame([[9,8,7],[6,5,4],[3,2,1]])
'Multiplying the matrix'
print(matrix1*matrix2)          


'adding the matrix'

print(matrix1+matrix2)


'''manual multiplying'''


a=[[1,2],[3,4]]
b=[[1,2],[3,4]]
row=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        row.append(a[i][j]+b[i][j])
print(row)        