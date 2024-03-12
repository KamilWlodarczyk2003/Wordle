from words import Word
import tkinter as tk

BG_COLOR='#666666'



    
class My_App():
    def __init__(self):
        self.window = tk.Tk()
        self.BLANK_SQUARE=tk.PhotoImage(file='img/Simple_blank.png').subsample(12, 12)
        self.window.title("Wordle")
        self.window.config(bg=BG_COLOR)
        self.window.geometry("1200x900")
        self.head_title=tk.Label(text="Wordle", font=("Arial", 24, 'bold'), bg=BG_COLOR, pady=10)
        self.head_title.grid(column=0,row=0)
        
    def create_squares(self):
        self.squares=[]
        for x in range(0,6):
            line_list=[]
            for x in range(0,5):
                block_canvas = tk.Canvas(self.window, height=50, width=50, bg=BG_COLOR)
                #block_canvas.create_image(50,50,image=self.BLANK_SQUARE)
                line_list.append(block_canvas)
            self.squares.append(line_list)
    
    def place_squares(self):
        ypos=1
        for y in range(0,6):
            xpos=1
            for x in range(0,5):
                self.squares[ypos-1][xpos-1].grid(row=ypos, column=xpos, padx=2, pady=2)
                xpos+=1
            ypos+=1
    
    def draw_rounded_square(self,image , x, y, width, height, corner_radius, fill_color="lightgray", outline_color="lightgray"):
        image.create_rectangle(x + corner_radius, y,
                                    x + width - corner_radius, y + height,
                                    fill=fill_color, outline=outline_color)
        image.create_rectangle(x, y + corner_radius,
                                    x + width, y + height - corner_radius,
                                    fill=fill_color, outline=outline_color)
        image.create_oval(x, y,
                                x + corner_radius * 2, y + corner_radius * 2,
                                fill=fill_color, outline=outline_color)
        image.create_oval(x + width - corner_radius * 2, y,
                                x + width, y + corner_radius * 2,
                                fill=fill_color, outline=outline_color)
        image.create_oval(x, y + height - corner_radius * 2,
                                x + corner_radius * 2, y + height,
                                fill=fill_color, outline=outline_color)
        image.create_oval(x + width - corner_radius * 2, y + height - corner_radius * 2,
                                x + width, y + height,
                                fill=fill_color, outline=outline_color)
            
    
    KLAWIATURA="QWERTYUIOPASDFGHJKLZXCVBNM"
    def create_keyboard(self):
        self.keys_column=[]
        iterator=0
        h=0
        for y in range(0,3):
            keys_row=[]
            if y == 1:
                h=1
            if y == 2:
                h=3
            for x in range(0,10-h):
                keys = tk.Canvas(self.window, height=50, width=40, bg=BG_COLOR, highlightthickness=0)
                #keys.create_image(20, 25, image=self.BLANK_SQUARE)
                
                self.draw_rounded_square(keys,0,0,40,50,10)
                
                keys.create_text(20, 25 , text=self.KLAWIATURA[iterator], font=("Coco Gothic", 20, 'bold'), fill='white')
                iterator+=1
                keys_row.append(keys)
            self.keys_column.append(keys_row)
                
    def place_keyboard(self):
        ypos=6
        for row in self.keys_column:
            xpos=1
            for key in row:
                key.grid(column=xpos, row=ypos)
                xpos+=1
            ypos+=1
                
                
                
        

    
my_word = Word()

app = My_App()
app.create_squares()
app.place_squares()
app.create_keyboard()
app.place_keyboard()


app.window.mainloop()