from cProfile import label
from tkinter import ttk
from tkinter.font import names

import main
from Snake_module import *

root = Tk()

root.title("Snake Game")
root.resizable(False, False)

game = Game(root = root)
game.main()

main.menu = Menu(root)
root.config(menu=main.menu)
records_menu= Menu(main.menu, tearoff=False)
main.menu.add_cascade(label='Рекорды',menu=records_menu)

def show_records():
    top=Toplevel(root)
    table= ttk.Treeview(top, columns=('name','score'))
    table.heading('name',text='Имя')
    table.heading('score',text='Счет')

    with open('scores.txt', 'r') as f:
        for line in f:
            name, score= line.split(':')
            table.insert('','end',values=(name,score))

    table.pack()


records_menu.add_command(label='Показать рекорды',command=show_records)


about_menu= Menu(main.menu, tearoff=False)
main.menu.add_cascade(label='Об игре',menu=about_menu)

def show_about():
    top = Toplevel(root)
    frame = Frame(top,bg='white', padx=20,pady=20)
    lbl = Label(frame,
                text ="я сделал эту игру \n за 1,5 месяца\n xD",
                bg='white',
                padx=10,
                pady=10
                )
    lbl.pack()
    frame.pack()
about_menu.add_command(label='О разработчике',command=show_about)

main.menu.add_command(label='Выход', command=root.quit)


root.mainloop()

