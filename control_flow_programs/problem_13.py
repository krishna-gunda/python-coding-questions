'''Guess the Secret Number ⭐⭐⭐⭐

Problem

Secret number = random

Keep asking the user until they guess correctly.'''

import random
i=0
secret_number=random.randint(1,100)


while i<5:
    
        a=int(input("enter a number="))
        i+=1
        if a==secret_number:
            print("congratulations you gussed the correct number")
            break
        elif a>secret_number:
            print("the number is two high")
        else :
            print("the number is low ") 
else:
        print(f'you loose the game and the secret number is {secret_number} ')       
               

    