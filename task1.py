"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk 
from tkinter import *



def clickFunction(event):
        p1=nameE.get()
        p2=StuNumE.get()
        p3=GrdE.get()
        StuInfo=(f"Name: {p1} Student Number: {p2} Grade: {p3}")
        InfoStu.delete(0,END)
        InfoStu.insert(0,StuInfo)
win = tk.Tk()
win.title('Student Info')

nameL=Label(text='Name:')
StuNumL=Label(text='Student Number:')
GrdL=Label(text='Grade:')

nameE=Entry(width=50)
StuNumE=Entry(width=50)
GrdE=Entry(width=50)

InfoB=Button(text='Student Information')
InfoStu=Entry(win,width=50)


InfoB.bind("<Button>",clickFunction)

nameL.grid(column=1,row=1)
StuNumL.grid(column=1,row=2)
GrdL.grid(column=1,row=3)

nameE.grid(column=2,row=1)
StuNumE.grid(column=2,row=2)
GrdE.grid(column=2,row=3)

InfoB.grid(column=1,row=4)
InfoStu.grid(column=2,row=4)

win.mainloop()