from tkinter import *
root = Tk()
root.geometry("700x400")
one= Label(root,text="One",fg="white",bg="blue")
one.pack()
two= Label(root,text="two",fg="black",bg="black")
two.pack(fill=X)
three= Label(root,text="thre",fg="black",bg="blue")
three.pack(side=LEFT,fill=y)
root.mainloop()


