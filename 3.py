#3
def click(event):
    x, y=event.x, event.y
    can.coords((circle, x-20, y-20, x+20, y+20))
root = Tk()
can = Canvas(root, width=500, height=400)
can.pack()
circle = can.create_oval(333,222,333,222)
can.bind('<Button-1>', click)
root.mainloop()
