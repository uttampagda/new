from tkinter import *
root=Tk()

def printfor():
    print("This is command project")

button = Button(root,text="name 1",command=printfor)
button.pack()

root.mainloop()
