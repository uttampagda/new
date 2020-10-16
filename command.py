from tkinter import *
root=Tk()

def printname():
    print("This is command project")

button = Button(root,text="name 1",command=printname)
button.pack()

root.mainloop()
