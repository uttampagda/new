from tkinter import *
root=Tk()


lebel_1=Label(root,text="UserName")
lebel_2=Label(root,text="UserPassword")
entry_1=Entry(root)
entry_2=Entry(root)

lebel_1.grid(row=1)
lebel_2.grid(row=0)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=2)

c = Checkbutton(root,text="keep me logged in this accout")
c.grid(columnspan=3)

root.mainloop()
