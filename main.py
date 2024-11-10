from tkinter import *

root = Tk()

root.title("Snake Game")
root.resizable(False , False)

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20

c = Canvas(root , width=WIDTH , height= HEIGHT, bg='#003300')
c.pack()






root.mainloop()