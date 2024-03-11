from random import choice
import tkinter as tk

class Word():
    def __init__(self):
        with open('text/simple.txt', 'r') as words:
            self.words_list = words.readlines()
        words_list = [word.strip() for word in self.words_list]
    
    def pick_random(self):
        return choice(self.words_list)

    
my_word = Word()

print(my_word.pick_random())

root = tk.Tk()
root.title('Wordle')
root.geometry("600x800")
head_title = tk.Label(root, text="Wordle")
head_title.grid(column=0,row=0)

root.mainloop()