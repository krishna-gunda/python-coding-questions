'''Problem:

Given a list of numbers, print the first number divisible by 13.

Once found, stop searching.'''


a=[1,2,12,34,5,6,23,26]
found=False
for i in a:
    if i%13==0: 
        print(f'the number {i} is divisible by 13')
            