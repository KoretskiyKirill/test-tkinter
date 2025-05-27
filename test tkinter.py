#уровень C сложный
#1
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()
def down(down):
    messagebox.showinfo("вниз", "вниз")
def up(up):
    messagebox.showinfo("вверх", "вверх")

def left(left):
    messagebox.showinfo("влево", "влево")
def right(right):
    messagebox.showinfo("вправо", "вправо")
root.bind('<Down>', down)
root.bind('<Up>', up)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.mainloop()

#2
root = Tk()
def count():
    summ = 0
    lst = list(map(int, ent.get().split("+")))
    for i in lst:
        summ += i
    lbl['text'] = summ
ent = Entry(root, width= 25)
ent.pack(side='left')
btn = Button(root, text="=", command= count)
btn.pack(side='left')
lbl = Label(root)
lbl.pack(side='left')
root.mainloop()
#3
root = Tk()
can = Canvas(root, width=500, height=400)
can.pack()
circle = can
root.mainloop()