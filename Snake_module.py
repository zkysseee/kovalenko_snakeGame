from tkinter import *
class Segment:
    def __init__(self,size, x, y,  c):
        self.size = size
        self.instance = c.create_rectangle(x, y,
                                           x + self.size, y + self.size,
                                           fill='white',
                                           outline='black'
                                           )


class Snake:
    def __init__(self, segments,c):
        self.segments = segments
        self.c = c
        self.vector = 'right'
        self.SEG_SIZE = self.segments[0].size
    def move(self):
        """
        Двигаем змейку в заданном направлении
        :return:
        """
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 =  self.c .coords(self.segments[index+1].instance)
            self.c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 =  self.c .coords(self.segments[-1].instance)
        match self.vector:
            case 'right':
                self.c.coords(self. segments[-1].instance,
                         x1 + self.SEG_SIZE, y1,
                         x2 + self.SEG_SIZE, y2
                         )
            case 'left':
                self.c.coords(self.segments[-1].instance,
                         x1 - self.SEG_SIZE, y1,
                         x2 - self.SEG_SIZE, y2
                         )
            case 'up':
                self.c.coords(self.segments[-1].instance,
                         x1, y1 - self.SEG_SIZE,
                         x2, y2 - self.SEG_SIZE
                         )
            case 'down':
                self.c.coords(self.segments[-1].instance,
                         x1, y1 + self.SEG_SIZE,
                         x2, y2 + self.SEG_SIZE
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
    def __init__(self,snake:Snake , canvas:Canvas):
        self.s = snake
        self.c = canvas
        self.WIDTH,self.HEIGHT = self.c.winfo_width(),self.c.winfo_height()
        self.SEG_SIZE = self.s.segments[0].size
        self.pos_x, self.pos_y =self.generate_rand_pos()
        self.instance = self.c.create_oval(self.pos_x, self.pos_y,
                                      self.pos_x+ self.SEG_SIZE,
                                      self.pos_y+self.SEG_SIZE,
                                      fill = 'red')

    def check_snake(self):
        pass

    
