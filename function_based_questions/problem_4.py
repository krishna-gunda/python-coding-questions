'''1. Prime Pattern Matrix
Print an n x n grid of numbers from 1 to n*n (filled row-wise), but replace every 
prime number with * and every multiple of 5 with #. If a number is both prime and 
a multiple of 5 (i.e., 5 itself), print @ instead. Use nested for loops and range(),
and use continue to skip printing a space after the last column of each row.'''



n = int(input("Enter the number "))

for i in range(1, (n*n) + 1):

    if i >= 2:
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            if i % 5 == 0:
                print("@", end=" ")
            else:
                print("#", end=" ")
        else:
            print(i, end=" ")

    else:
        print(i, end=" ")

    if i % n == 0:
        print()