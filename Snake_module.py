from tkinter import *
import random
from PIL import Image, ImageTk


class Segment:
    def __init__(self, x, y,):
        self.size = Game.SEG_SIZE
        self.__c = Game.c
        self.instance = self.__c.create_rectangle(x, y,
                                                  x + self.size, y + self.size,
                                                  fill='white',
                                                  outline='green'
                                                  )


class Snake:
    def __init__(self, first_segment: Segment):
        self.__c: Canvas = Game.c
        self.__segment = first_segment
        self.SEG_SIZE = self.__segment.size
        self.segments = [self.__segment,
            Segment(self.SEG_SIZE*2, self.SEG_SIZE,),
            Segment(self.SEG_SIZE*3, self.SEG_SIZE,),
            ]
        self.vector = 'stop'
        self.score = 0
        self.score_text = self.__c.create_text(Game.text_x, Game.text_y,
                                               text="Счет: 0",
                                               fill='white'
                                               )
        self.head = self.segments[-1].instance

    def move(self):
        """
        Двигаем змейку в заданном направлении
        :return:
        """
        if self.vector == 'stop':
             return
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = self.__c.coords(self.segments[index + 1].instance)
            self.__c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = self.get_head_pos()
        match self.vector:
            case 'right':
                self.__c.coords(self. head,
                                x1 + self.SEG_SIZE, y1,
                                x2 + self.SEG_SIZE, y2
                                )
            case 'left':
                self.__c.coords(self.head,
                                x1 - self.SEG_SIZE, y1,
                                x2 - self.SEG_SIZE, y2
                                )
            case 'up':
                self.__c.coords(self.head,
                                x1, y1 - self.SEG_SIZE,
                                x2, y2 - self.SEG_SIZE
                                )
            case 'down':
                self.__c.coords(self.head,
                                x1, y1 + self.SEG_SIZE,
                                x2, y2 + self.SEG_SIZE
                                )


    def get_head_pos(self):
        return self.__c.coords(self.head)

    def check_in_field(self):
        """
        Проверка, а не вышли ли мы за пределы поля
        :return:
        """
        x1, y1, x2, y2 = self.get_head_pos()
        return not(x1 < 0 or x2 > self.__c.winfo_width()
                   or y1 < 0 or y2 > self.__c.winfo_height())

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

    def add_segment(self, val):
        last_seg = self.__c.coords(self.head)
        x = last_seg[0]
        y = last_seg[1]
        if val > 0:
            for i in range(val):
                self.segments.insert(0, Segment( x, y,))
        else:
            for i in range(abs(val)):
                self.__c.delete(self.segments[0].instance)
                self.segments.pop(0)

    def change_score(self, val):
        self.__c.delete(self.score_text)
        self.score += val
        self.score_text = self.__c.create_text(Game.text_x, Game.text_y, text=f'Счёт: {self.score}', fill='white')

    def bite_yourself(self):
        for index in range(len(self.segments)-1):
            if self.__c.coords(self.segments[index].instance)== self.get_head_pos():
                return True
            return False

class Food:
    def __init__(self, snake: Snake, canvas: Canvas, img_path, val=1):
        self.s = snake
        self.c = canvas
        self.SEG_SIZE = self.s.segments[0].size
        self.WIDTH, self.HEIGHT = self.c.winfo_width(), self.c.winfo_height()
        self.pos_x, self.pos_y = self.generate_rand_pos()
        self.image = Image.open(img_path).resize((self.SEG_SIZE, self.SEG_SIZE), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        self.instance = self.c.create_image(self.pos_x, self.pos_y,
                                            image=self.image, anchor=NW)
        self.val = val

    def check_snake(self):
        snake_head_coords = self.c.coords(self.s.segments[-1].instance)
        # print(snake_head_coords, type(snake_head_coords), snake_head_coords == [self.pos_x, self.pos_y, self.pos_x + SEG_SIZE, self.pos_y + SEG_SIZE])
        if snake_head_coords == [self.pos_x, self.pos_y, self.pos_x + self.SEG_SIZE, self.pos_y + self.SEG_SIZE]:
            self.pos_x, self.pos_y = self.generate_rand_pos()
            self.c.coords(self.instance, self.pos_x, self.pos_y)
            self.s.add_segment(self.val)
            self.s.change_score(self.val)

    def generate_rand_pos(self):
        rand_x = self.SEG_SIZE * (random.randint(1, (self.WIDTH - self.SEG_SIZE) // self.SEG_SIZE))
        rand_y = self.SEG_SIZE * (random.randint(1, (self.HEIGHT - self.SEG_SIZE) // self.SEG_SIZE))
        return rand_x, rand_y

class Game:
    root = None
    c = None
    score_text = None
    WIDTH = 800
    HEIGHT = 600
    SEG_SIZE = 20
    text_x, text_y = WIDTH * 0.9 , HEIGHT * 0.1

    def __new__(cls,*args,**kwargs):
        cls.root = kwargs['root']
        cls.c = Canvas(cls.root, width=cls.WIDTH, height=cls.HEIGHT, bg='#003300')
        cls.c.pack()
        cls.c.update()
        return super().__new__(cls)

    def __init__(self,root):
        self.start_new = True


    def init_game(self):
        self.s = Snake(Segment(self.SEG_SIZE, self.SEG_SIZE,))

        self.c.focus_set()
        self.c.bind("<Key>", self.s.change_direction)
        self.apple = Food(self.s, self.c, "images/apple.png", -1)
        self.taco = Food(self.s, self.c, "images/taco.png", 3)


    def main(self):
        if self.start_new:
            self.init_game()
            self.start_new = False
        self.s.move()
        if not self.s.check_in_field() or self.s.bite_yourself():
            self.c.delete('all')
            self.start_new = True
        self.apple.check_snake()
        self.taco.check_snake()
        self.c.after(300, self.main)


