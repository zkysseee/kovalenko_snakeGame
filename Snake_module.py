from tkinter import *
import random
from PIL import Image, ImageTk

class Segment:
    def __init__(self, size, x, y, c):
        self.size = size
        self.c = c
        self.instance = c.create_rectangle(x, y,
                                           x + self.size, y + self.size,
                                           fill='white',
                                           outline='black'
                                           )


class Snake:
    def __init__(self, first_segment:Segment):
        self.c = first_segment.c
        self.segment = first_segment
        self.SEG_SIZE = self.segment.size
        self.segments = [self.segment,
                         Segment(self.SEG_SIZE, self.SEG_SIZE*2, self.SEG_SIZE,self.c),
                         Segment(self.SEG_SIZE, self.SEG_SIZE*3, self.SEG_SIZE, self.c)
                         ]
        self.vector = 'right'
    def move(self):
        """
        Двигаем змейку в заданном направлении
        :return:
        """
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = self.c.coords(self.segments[index+1].instance)
            self.c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = self.c.coords(self.segments[-1].instance)
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
                # print('left')
                self.vector = 'left'
            case 's':
                # print('down')
                self.vector = 'down'
            case 'w':
                # print('up')
                self.vector = 'up'
            case 'd':
                # print('right')
                self.vector = 'right'

    def add_segment(self):
        last_seg =self.c.coords(self.segments[-1].instance)
        x =last_seg[0]
        y =last_seg[1]
        self.segments.insert(0,Segment(self.SEG_SIZE,x,y,self.c))

class Food:
    def __init__(self, snake: Snake, canvas: Canvas, img_path):
        self.s = snake
        self.c = canvas
        self.SEG_SIZE = self.s.segments[0].size
        self.WIDTH, self.HEIGHT = self.c.winfo_width(), self.c.winfo_height()
        self.pos_x, self.pos_y = self.generate_rand_pos()
        self.image = Image.open(img_path).resize((self.SEG_SIZE, self.SEG_SIZE), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        self.instance = self.c.create_image(self.pos_x, self.pos_y,
                                            image=self.image, anchor=NW)

    def check_snake(self):
        snake_head_coords = self.c.coords(self.s.segments[-1].instance)
        # print(snake_head_coords, type(snake_head_coords), snake_head_coords == [self.pos_x, self.pos_y, self.pos_x + SEG_SIZE, self.pos_y + SEG_SIZE])
        if snake_head_coords == [self.pos_x, self.pos_y, self.pos_x + self.SEG_SIZE, self.pos_y + self.SEG_SIZE]:
            self.pos_x, self.pos_y = self.generate_rand_pos()
            self.c.coords(self.instance, self.pos_x, self.pos_y)
            self.s.add_segment()

    def generate_rand_pos(self):
        rand_x = self.SEG_SIZE * (random.randint(1, (self.WIDTH - self.SEG_SIZE) // self.SEG_SIZE))
        rand_y = self.SEG_SIZE * (random.randint(1, (self.HEIGHT - self.SEG_SIZE) // self.SEG_SIZE))
        return rand_x, rand_y
