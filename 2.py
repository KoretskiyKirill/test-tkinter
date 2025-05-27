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
