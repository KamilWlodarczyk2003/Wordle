from words import Word
import tkinter as tk

BG_COLOR='#666666'
#BLANK_SQUARE=tk.PhotoImage(file='img/Simple_blank.png')


    
class My_App():
    def __init__(self):
        self.window = tk.Tk()
        self.BLANK_SQUARE=tk.PhotoImage(file='img/Simple_blank.png')
        self.window.title("Wordle")
        self.window.config(bg=BG_COLOR)
        self.window.geometry("600x800")
        self.head_title=tk.Label(text="Wordle", font=("Arial", 24, 'bold'), bg=BG_COLOR, pady=10)
        self.head_title.grid(column=0,row=0)
        
    def create_squares(self):
        self.squares=[]
        for x in range(0,6):
            line_list=[]
            for x in range(0,5):
                block_canvas = tk.Canvas(self.window, height=50, width=50, bg=BG_COLOR)
                block_canvas.create_image(50,50,image=self.BLANK_SQUARE)
                line_list.append(block_canvas)
            self.squares.append(line_list)
    
    def place_squares(self):
        ypos=1
        for y in range(0,6):
            xpos=1
            for x in range(0,5):
                self.squares[ypos-1][xpos-1].grid(row=ypos, column=xpos)
                xpos+=1
            ypos+=1
                
        

    
my_word = Word()

app = My_App()
app.create_squares()
app.place_squares()


app.window.mainloop()