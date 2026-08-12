'''Find the Missing Number

Given a list containing n distinct numbers from 0 to n, return the missing number.'''


def missing_number(lst):
    for i in range(0,max(lst)):
        if i not in lst:
            return i
    return None


print(missing_number([0,1,2,6,3,4]))


# by using the another approach

def mis_num(n,lst):
    result=(n*(n+1)//2)-sum(lst)
    return result

print(mis_num(5,[1,2,4,5]))
print(mis_num(6, [1, 2, 3, 5, 6]))

