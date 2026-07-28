"ARM strong number"

"condition the number is equal to the sum of all digits where each digit caluclate power to the length of the numbers"


a=153
result=0
length=len(str(a))
for i in range(length):
    result=result+((a%10)**(length))
    a=a//10
print(result)    


def arm(num):
    result=0
    length=len(str(num))
    for i in range(length):
      result=result+(num%10)**(length)
      num=num//10
    return result

print(arm(153))
