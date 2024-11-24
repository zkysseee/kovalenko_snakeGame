import random
from tkinter import *

root = Tk()

root.title("Snake Game")
root.resizable(False, False)

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20

c = Canvas(root, width=WIDTH, height=HEIGHT, bg='#003300')
c.pack()


class Segment:
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill='white',
                                           outline='black'
                                           )


class Snake:
    def __init__(self, segments):
        self.segments = segments
        self.vector = 'right'

    def move(self):
        """
        Двигаем змейку в заданном направлении
        :return:
        """
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-1].instance)
        match self.vector:
            case 'right':
                c.coords(self. segments[-1].instance,
                         x1 + SEG_SIZE, y1,
                         x2 + SEG_SIZE, y2
                         )
            case 'left':
                c.coords(self.segments[-1].instance,
                         x1 - SEG_SIZE, y1,
                         x2 - SEG_SIZE, y2
                         )
            case 'up':
                c.coords(self.segments[-1].instance,
                         x1, y1 - SEG_SIZE,
                         x2, y2 - SEG_SIZE
                         )
            case 'down':
                c.coords(self.segments[-1].instance,
                         x1, y1 + SEG_SIZE,
                         x2, y2 + SEG_SIZE
                         )

    def change_direction(self, event):
        """
        Меняем вектор направления при нажатии на клавиши WASD
        :param event:
        :return:
        """
        match event.char.lower():
            case 'a':
                print('left')
                self.vector = 'left'
            case 's':
                print('down')
                self.vector = 'down'
            case 'w':
                print('up')
                self.vector = 'up'
            case 'd':
                print('right')
                self.vector = 'right'
        # print(event)
class Food:
    def __init__(self):
        self.pos_x = SEG_SIZE*(random.randint(1, (WIDTH - SEG_SIZE) // SEG_SIZE))
        self.pos_y =SEG_SIZE*(random.randint(1, (HEIGHT - SEG_SIZE) // SEG_SIZE))
        self.instance = c.create_oval(self.pos_x, self.pos_y,
                                      self.pos_x+SEG_SIZE,
                                      self.pos_y+SEG_SIZE,
                                      fill = 'red')

segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE*2, SEG_SIZE),
            Segment(SEG_SIZE*3, SEG_SIZE),
            ]

s = Snake(segments)

c.focus_set()
c.bind("<Key>", s.change_direction)
# c.bind("<Key-S>", s.change_direction)
# c.bind("<w>", s.change_direction)
# c.bind("<Return>", s.change_direction)  # Клавиша Enter
# c.bind("<Control-c>", s.change_direction)
# c.bind("<KeyPress-f>", s.change_direction)
# c.bind("<Button-1>", s.change_direction)
apple = Food()

def main():
    s.move()
    root.after(300, main)

main()
root.mainloop()