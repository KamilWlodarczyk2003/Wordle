from random import choice
import tkinter as tk

class Word():
    def __init__(self):
        with open('text/simple.txt', 'r') as words:
            self.words_list = words.readlines()
        self.words_list = [word.strip() for word in self.words_list]
    
    def pick_random(self):
        return choice(self.words_list)
    
class My_App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wordle")
        self.window.config(bg="#666666")
        self.window.geometry("600x800")
        self.head_title=tk.Label(text="Wordle", font=("Arial", 24))
        self.head_title.grid(column=0,row=0)
        

    
my_word = Word()

app = My_App()


app.window.mainloop()