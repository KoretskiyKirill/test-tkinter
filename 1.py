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
