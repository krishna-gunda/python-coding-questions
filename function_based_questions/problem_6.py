'''Triangular Number Pyramid with Skips
Using nested loops (for inside for), print a right-angled triangle pattern of numbers from 1 to 9 
repeating (1,2,3...9,1,2,3...), for n rows where row i has i numbers. However, skip printing entirely 
(use continue) for any row number that's a multiple of 3, and stop the whole pyramid (using a flag + 
break, no early-return) if any row would exceed 15 numbers.'''

n = int(input("Enter a number = "))

num = 1
stop = False

for i in range(1, n + 1):

    # Stop if the row would exceed 15 numbers
    if i > 15:
        stop = True
        break

    # Skip rows that are multiples of 3
    if i % 3 == 0:
        continue

    # Print i numbers in the row
    for j in range(i):
        print(num, end=" ")

        num += 1

        # Restart from 1 after 9
        if num == 10:
            num = 1

    print()

    # Check the flag
    if stop:
        break