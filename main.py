from words import Word
from gui import My_App

BG_COLOR='#666666'
    
my_word = Word()
choosen_word = my_word.pick_random().upper()
print(choosen_word)

app = My_App()
app.create_squares()
app.place_squares()
app.create_keyboard()
app.place_keyboard()

app.window.bind('<Key>', func= lambda event, word = choosen_word: app.writing(event,word))

app.window.mainloop()