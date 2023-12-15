#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk 
from tkinter import *
from tkinter import ttk

def clickFunction(event):
    s1=entry1.get()
    s1=float(s1)
    s2=entry2.get()
    s2=float(s2)
    answer=(s1**2+s2**2)**0.5
    hyp.delete(0,END)
    hyp.insert(0,answer)

win = tk.Tk()
entry1=Entry(width=20)
entry2=Entry(width=20)
hyp=Entry(width=20)
button1=Button(text='Calculate:')
label1=Label(text="1st short side length")
label2=Label(text="2nd short side length")

button1.bind("<Button>",clickFunction)

label1.grid(column=1,row=1)
label2.grid(column=1,row=2)
entry1.grid(column=2,row=1)
entry2.grid(column=2,row=2)
button1.grid(column=1,row=3)
hyp.grid(column=2,row=3)

win.mainloop()