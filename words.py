from random import choice

class Word():
    def __init__(self):
        with open('text/simple.txt', 'r') as words:
            self.words_list = words.readlines()
        self.words_list = [word.strip() for word in self.words_list]
    
    def pick_random(self):
        return choice(self.words_list)