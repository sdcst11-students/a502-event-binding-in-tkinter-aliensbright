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
#(-b+-sqrt(b^2-4ac))/2a
import tkinter as tk 
from tkinter import *
import math
win=tk.Tk()

def clickFunction(event):
    try:
        a=1
        b=float(entryb.get())
        c=float(entryc.get())
        sol1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        sol1=round(sol1,2)
        sol2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        sol2=round(sol2,2)
        if sol1<0:
            factor1=f"(x+{-1*sol1})"
        else:
            factor1=f'(x-{sol1})'
        if sol2<0:
            factor2=f"(x+{-1*sol2})"
        else:
            factor2=f'(x-{sol2})'
        entryanswer.delete(0,END)
        entryanswer.insert(0,f"{factor1}{factor2}")
    except:
        entryanswer.delete(0,END)
        entryanswer.insert(0,'Incorrect Values')


instructions=Label(text='Factoring trinomials of type:\nx^2 + bx + c',bg='Cyan')

entryb=Entry(win,width=5)
entryc=Entry(win,width=5)
entryanswer=Entry(win,width=12)

labelx2=Label(text="x^2")
labelx=Label(text="x")
labelEqual=Label(text="=")

button1=Button(win,width=2,text="+")
button2=Button(win,width=2,text="+")
buttonAns=Button(win,width=10,text="Factor")

buttonAns.bind("<Button>",clickFunction)


instructions.grid(column=1,row=1,columnspan=6)
labelx2.grid(column=1,row=2)
button1.grid(column=2,row=2)
entryb.grid(column=3,row=2)
labelx.grid(column=4,row=2)
button2.grid(column=5,row=2)
entryc.grid(column=6,row=2)
labelEqual.grid(column=7,row=2)
entryanswer.grid(column=8,row=2)
buttonAns.grid(column=8,row=1)

win.mainloop()