from tkinter import *
root=Tk()


lebel_1=Label(root,text="Name")
lebel_2=Label(root,text="Password")
entry_1=Entry(root)
entry_2=Entry(root)

lebel_1.grid(row=0)
lebel_2.grid(row=1)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)

root.mainloop()