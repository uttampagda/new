from tkinter import *
root = Tk()
root.geometry("750x450")
one= Label(root,text="One",fg="white",bg="blue")
one.pack()
two= Label(root,text="two",fg="black",bg="black")
two.pack(fill=X)
three= Label(root,text="three",fg="yellow",bg="red")
three.pack(side=LEFT,fill=y)
root.mainloop()


