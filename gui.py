import tkinter as tk
from pynput.keyboard import Key, Listener



class My_App():
    BG_COLOR='#666666'
    KLAWIATURA="QWERTYUIOPASDFGHJKLZXCVBNM"
    DARK_GREY="#474747"
    LIGHT_GREY="#a3a3a3"
    
    current_box=0
    input_word=''
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wordle")
        self.window.config(bg=self.BG_COLOR)
        self.window.geometry("1200x950")
        self.inv_title=tk.Label(text="", font=("Coco Gothic", 50, 'bold'), bg=self.BG_COLOR, pady=10, fg=self.BG_COLOR)
        self.inv_title.grid(column=2,row=0,columnspan=4)
        self.head_title=tk.Label(text="Wordly", font=("Coco Gothic", 50, 'bold'), bg=self.BG_COLOR, fg="#f4f4f4")
        self.head_title.place(x=482,y=7)
        
    def create_squares(self):
        self.squares=[]
        for x in range(0,6):
            line_list=[]
            for x in range(0,5):
                block_canvas = tk.Canvas(self.window, height=75, width=75, bg=self.BG_COLOR, highlightbackground="#2b2b2b")
                line_list.append(block_canvas)
            self.squares.append(line_list)
    
    def place_squares(self):
        ypos=1
        for y in range(0,6):
            xpos=1
            for x in range(0,5):
                padx_value=2
                if(xpos==1):
                    padx_value=(390,2)
                self.squares[ypos-1][xpos-1].grid(row=ypos, column=xpos, padx=padx_value, pady=2)
                
                xpos+=1
            ypos+=1
    
    def draw_rounded_square(self,image , x, y, width, height, corner_radius, fill_color, outline_color):
        image.create_rectangle(x + corner_radius, y,
                                    x + width - corner_radius, y + height,
                                    fill=fill_color, outline=outline_color, tags="rounded_square")
        image.create_rectangle(x, y + corner_radius,
                                    x + width, y + height - corner_radius,
                                    fill=fill_color, outline=outline_color, tags="rounded_square")
        image.create_oval(x, y,
                                x + corner_radius * 2, y + corner_radius * 2,
                                fill=fill_color, outline=outline_color, tags="rounded_square")
        image.create_oval(x + width - corner_radius * 2, y,
                                x + width, y + corner_radius * 2,
                                fill=fill_color, outline=outline_color, tags="rounded_square")
        image.create_oval(x, y + height - corner_radius * 2,
                                x + corner_radius * 2, y + height,
                                fill=fill_color, outline=outline_color, tags="rounded_square")
        image.create_oval(x + width - corner_radius * 2, y + height - corner_radius * 2,
                                x + width, y + height,
                                fill=fill_color, outline=outline_color, tags="rounded_square")
            
    
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
                keys = tk.Canvas(self.window, height=80, width=70, bg=self.BG_COLOR, highlightthickness=0)
                
                self.draw_rounded_square(keys,0,0,70,80,10,self.DARK_GREY, self.DARK_GREY)
                
                keys.create_text(34, 40 , text=self.KLAWIATURA[iterator], font=("Coco Gothic", 35, 'bold'), fill='#d6d6d6', tags='text')
                keys.bind("<Button-1>", lambda event, canvas=keys: self.key_click(event, canvas))
                keys.bind("<ButtonRelease-1>", lambda event: self.unclick(event))
                iterator+=1
                keys_row.append(keys)
            self.keys_column.append(keys_row)
                
    def place_keyboard(self):
        ypos=630
        for row in self.keys_column:
            
            if self.keys_column.index(row) == 1:
                xpos =240
            elif self.keys_column.index(row) == 2:
                xpos=320
            else:
                xpos=200
                
                
            for key in row:
                key.place(x=xpos,y=ypos)
                xpos+=80
            ypos+=100
            
    def writing(self, event, word):
        print(f"word: {word}")
        print(f"current: {self.input_word}")
        key=event.keysym.upper()
        
        if key in self.KLAWIATURA:
            
            if len(self.input_word) < 5:
                self.input_word +=key
                
        elif key == "BACKSPACE" and len(self.input_word) > 0:
            
            index = len(self.input_word) - 1
            self.input_word = self.input_word[:-1]
            self.squares[self.current_box][index].delete('text')
        
        elif key == "RETURN" and len(self.input_word) == 5:
            
            for x in range(0,5):
                
                if self.input_word[x] in word:
                    if self.input_word[x] == word[x]:
                        self.squares[self.current_box][x].configure(bg="green")
                    else:
                        self.squares[self.current_box][x].configure(bg="yellow")
                        
            self.current_box += 1
            self.input_word=''
            
        self.block_writing()
        
    def block_writing(self):
        for x in range(0, len(self.input_word)):
            self.squares[self.current_box][x].create_text(37,40,text=self.input_word[x],font=("Coco Gothic", 38, 'bold'), fill='#d6d6d6', tag="text")
            
    def key_click(self, event, canvas):

        canvas = event.widget
        text = canvas.find_withtag("text")
        
        canvas.itemconfig("rounded_square", fill=self.LIGHT_GREY, outline=self.LIGHT_GREY)
        
        if text:
            key = canvas.itemcget(text[0], "text")
            if len(self.input_word) < 5:
                self.input_word += key
                self.block_writing()
                
    def unclick(self,event):
        canvas = event.widget
        text = canvas.find_withtag("text")
        
        canvas.itemconfig("rounded_square", fill=self.DARK_GREY, outline=self.DARK_GREY)
        