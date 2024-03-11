from random import choice

with open('text/simple.txt', 'r') as words:
    words_list = words.readlines()
    
words_list = [word.strip() for word in words_list]
random_word = choice(words_list)
print(random_word)