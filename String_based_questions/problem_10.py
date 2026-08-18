'''Write a function reverse_words(sentence) that reverses the order of words in a 
sentence but keeps each word spelled normally — without using reversed(), slicing 
with [::-1], or the reverse() method. You must use split() and join() only, plus 
basic loops.'''

def reverse_words(text):
    result=''
    words=text.split(" ")
    for word in words:
        result=word+" "+result
    return result.strip()

print(reverse_words("krishna is btech graduated"))    