from words import Word
import tkinter as tk
from gui import My_App

BG_COLOR='#666666'



    

                
                
                
        

    
my_word = Word()

app = My_App()
app.create_squares()
app.place_squares()
app.create_keyboard()
app.place_keyboard()


app.window.mainloop()