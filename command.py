from tkinter import *
root=Tk()

def printname():
    print("My name is uttam")

button = Button(root,text="name",command=printname)
button.pack()

root.mainloop()