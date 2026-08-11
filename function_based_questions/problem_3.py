'''Find the Missing Number

Given a list containing n distinct numbers from 0 to n, return the missing number.'''


def missing_number(lst):
    for i in range(0,max(lst)):
        if i not in lst:
            return i
    return None

print(missing_number([0,1,2,6,3,4]))    