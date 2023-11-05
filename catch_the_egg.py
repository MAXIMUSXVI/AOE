from tkinter import *
import random
import time

class Egg:
    #Класс яйца
    def __init__(self, canvas, basket):
        self.canvas = canvas
        self.basket = basket
        self.oval = canvas.create_oval(0, 0, 20, 25, fill='ivory')
        self.canvas.move(self.oval, random. randint(0, 500), 0)
        self.touch_bottom = False
        self.score = 0
        self.score_text = canvas.create_text(150, 100, anchor=W, fill='royalblue', font=("Arial", 24), text="Игра окончена!")

    def touch_bakset(self, egg_pos):
        basket_pos = self.canvas.coords(self.basket.rect)
        if egg_pos[2] >= basket_pos[0] and egg_pos[0] <= basket_pos[2]:
            if egg_pos[2] >= basket_pos[1] and egg_pos[1] <= basket_pos[3]:
                return True
            return False

    def fall(self):
        self.canvas.move(self.oval, 0, 2)
        pos = self.canvas.coords(self.oval)
        if pos[3] >= 400:
            self.touch_bottom = True
            canvas.create_text(150, 100, anchor=W, fill='tomato', font=("Arial", 24), text="Игра окончена!")
        if self.touch_basket(pos == True):
            self.canvas.coords(self.oval, 0, 0, 20, 25)
            self.canvas.move(self.oval, random.randint(0, 500), 0)
            self.score = self.score + 1
            self.canvas.itemconfig(self.score_text, text="Яиц собрано: " str(self.score))

class Basket:
    #Класс корзины
    def __init__(self, canvas):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(0, 0, 100, 30, outline="")
        self.image = canvas.create_image(0, 0, anchor=NW, image-basket_image)
        slef.canvas.move(self.rect, 200, 350)
        self.canvas.move(self.image, 170, 290)
        self.canvas.bind_all("<KeyPress-a>", self.turn_left)
        self.canvas.bind_all("<KeyPress-d>", self.turn_right)
        
    def turn_left(self, event):
        sekf.x = -2

    def turn_right(self, event):
        self.x = 2

    def move_basket(self):
        self.canvas.move(self.rect, self.x, 0)
        self.canvas.move(self.image, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2]  >= 500:
            self.x = 0
        

#-------------------------------MAIN----------------------------
window = Tk()
window.title("Поймай Яйцо")
window.resizable(0, 0)
window.wm_attributes("-tompost", 1)
canvas = Canvas(window, width=500, height=400, highlightthickness=0)
canvas.pack()
bg = PhotoImage(file="c:/Users/User/Desktop/bg.png")
canvas.create_image(0, 0, anchor=NW, image=bg)
basket_image = PhotoImage(file="C:/Users/User/Desktop/basket.png")

basket = Basket(canvas)
egg = Egg(canvas, basket)

        while True:
            if egg.touch_bottom == False:
                egg.fall()
                basket.move_basket()
            else:
                break
            window.update()
            time.sleep(0.01)
