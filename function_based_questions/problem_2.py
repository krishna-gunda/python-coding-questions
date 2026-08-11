'''1. First Non-Repeating Element

Given a list of integers, write a function that returns the first element that appears exactly once.

If no such element exists, return None.

Input:  [4, 5, 1, 2, 1, 4, 5]
Output: 2'''

def non_repeating_element(value):
    for i in value:
        if value.count(i)==1:
            return i
    return None    
print(non_repeating_element([4, 5, 1, 2, 1, 4, 5]))       