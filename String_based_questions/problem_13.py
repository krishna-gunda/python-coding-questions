'''Find All Overlapping Occurrences

Python's built-in str.count() does not count overlapping substrings correctly. Write 
a function count_overlapping(main_str, sub_str) that counts overlapping occurrences
using find() (not count(), not regex).

python
count_overlapping("aaaa", "aa")   # → 3  (positions 0,1,2)
"aaaa".count("aa") '''

def count_overlapping(string,sub):
    result=0
    a=string.find(sub)
    for i in range(a,len(string)):
        if string[i:i+len(sub)]==sub:
            result+=1
    return result
print(count_overlapping("abc", "x"))

