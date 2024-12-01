from Snake_module import *

root = Tk()

root.title("Snake Game")
root.resizable(False, False)

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20

c = Canvas(root, width=WIDTH, height=HEIGHT, bg='#003300')
c.pack()
root.update()


s = Snake(Segment(SEG_SIZE, SEG_SIZE, SEG_SIZE, c))

c.focus_set()
c.bind("<Key>", s.change_direction)
apple = Food(s,c, "images/apple.png" ,)
taco = Food(s,c, "images/taco.png" ,)


def main():
    s.move()
    apple.check_snake()
    taco.check_snake()
    root.after(300, main)

main()
root.mainloop()