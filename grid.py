from tkinter import *
root=Tk()


lebel_1=Label(root,text="Username")
lebel_2=Label(root,text="Password")
entry_1=Entry(root)
entry_2=Entry(root)

lebel_1.grid(row=1)
lebel_2.grid(row=0)
entry_1.grid(row=1,column=2)
entry_2.grid(row=0,column=1)

c = Checkbutton(root,text="keep me logged in this accout")
c.grid(columnspan=2)

root.mainloop()
