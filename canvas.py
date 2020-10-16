from tkinter import *
def deleteall():
    canvas.delete(ALL)
root=Tk()
canvas = Canvas(root,width=260,height=460)
canvas.pack()
blackline=canvas.create_line(0,0,111,222)
greenline=canvas.create_line(0,4050,100,200,fill="green")
rec=canvas.create_rectangle(100,200,145,305,fill="white")
button=Button(root,text="Dlete",command=deleteall)
button.pack()
root.mainloop()
