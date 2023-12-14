"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk 
from tkinter import *
win=tk.Tk()
instructions=Label(text='Factoring trinomials of \ntype: x^2 + bx + c',bg='Cyan')
label1=Label(text='What is the value of b?')
label2=Label(text='What is the value of c?')
entry1=Entry()
entry2=Entry()

instructions.grid(column=1,row=1,columnspan=2)
label1.grid(column=1,row=2)
label2.grid(column=1,row=3)
entry1.grid(column=2,row=2)
entry2.grid(column=2,row=3)

win.mainloop()