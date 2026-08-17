'''5. Number Guessing Game with Bounded Attempts and Hints
Simulate a number-guessing game (no actual random input needed — hardcode a target 
and a list of guesses to iterate over). Use a while loop with a maximum attempt 
counter. For each guess, use if/elif/else to say "too high," "too low," or "correct." 
If three consecutive guesses are on the same side (all too high or all too low), 
break early and print "Stuck in a loop, giving up." Use continue to skip processing 
if a guess is repeated from the previous one.'''
i=0
target_number=25
lis=[]
put=[]
while i<=5:
    i+=1
    n=int(input("Enter a number="))
    put.append(n)
    if i>1:
        if put[i-1]==put[i-2]:
            continue
    if n>target_number:
        print("The number is too high")
        lis.append("too_high")
    elif n<target_number:
        print("The number is too low")
        lis.append("too_low")
    else:
        print("The number is correct")
        break
    if i%3==0:
        print(lis)
        length=lis.count("too_low")
        if length==3:
            print("all_too_low")
            lis.clear()
        else:
            print("all_too_high")
            lis.clear()        
            




