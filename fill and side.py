from tkinter import *
root = Tk()
root.geometry("700x400")
one= Label(root,text="one",fg="white",bg="black")
one.pack()
two= Label(root,text="two",fg="red",bg="black")
two.pack(fill=X)
three= Label(root,text="three",fg="yellow",bg="red")
three.pack(side=LEFT,fill=Y)
root.mainloop()


