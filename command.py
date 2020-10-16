from tkinter import *
root=Tk()

def printname():
    print("This my project")

button = Button(root,text="Your name",command=printname)
button.pack()

root.mainloop()
