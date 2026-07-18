'''Count the number of spaces.'''

sentence='Hi this is krishna'
count=0
for i in sentence:
    if i==" ":
        count+=1
print(f'the no of space in sentence is {count}')        


'''Count vowels using a loop.'''

vowels=0

for i in sentence.lower():
    if i in ['a','e','i','o','u']:
      vowels+=1
print(f'the no of vowels in sentence is {vowels}')


'''Print each word on a new line.'''

for i in sentence.split(" "):
    print(i,end='\n')
