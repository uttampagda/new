from tkinter import *
def deleteall():
    canvas.delete(ALL)
root=Tk()
canvas = Canvas(root,width=200,height=400)
canvas.pack()
blackline=canvas.create_line(0,0,100,200)
greenline=canvas.create_line(0,400,100,200,fill="green")
rec=canvas.create_rectangle(100,200,150,300,fill="grey")
button=Button(root,text="Delete",command=deleteall)
button.pack()
root.mainloop()
