from tkinter import *
root=Tk()
root.geometry("700x600")
def printname(event):
    print("My name is uttam")

button1 = Button(root,text="name")
button1.bind("<Button-1>",printname)
button1.pack()

root.mainloop()
