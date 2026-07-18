'''Find the longest word in a sentence.'''

sentence="I love hyderabad Very much"
max_=0
word=''
for i in sentence.split(" "):
    if len(i)>max_:
        max_=len(i)
        word=i
print(f'the largest word is {word}')    



'''Find the shortest word.'''

min_=0
small_word=''
for i in sentence.split(" "):
    if len(i)>=min_:
        min_=len(i)
        small_word=i
print(f'the smallest word is {small_word}')  