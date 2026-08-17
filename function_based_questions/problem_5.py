'''Collatz Sequence Explorer with Early Exit
Given a starting number n, generate its Collatz sequence (if even, divide by 2; 
if odd, multiply by 3 and add 1; repeat until you reach 1). Use a while loop. 
While generating it, if the sequence ever produces a number greater than 10,000, 
break out and print "Diverging too fast." If the number 27 appears anywhere in the 
sequence, print a special message using elif logic — but don't stop the loop'''


n = int(input("Enter a number="))

while n != 1:

    if n > 10000:
        print("Diverging too fast.")
        break

    elif n == 27:
        print("27 appears in the loop")
        continue

    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1

    print(n)
             