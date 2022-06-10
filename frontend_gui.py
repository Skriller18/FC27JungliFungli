from tkinter import *
from tkinter import Label

from PIL import ImageTk, Image
import os
root = Tk()
root.title("RVDAR")

def btact(txt):
    tx = txt.get()
    msg = "Your chosen room is "+tx
    Label(text=msg).grid(row=27, column=0)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
dimensions = str(width)+"x"+str(height)
root.geometry(dimensions)

label = Label(text='This is the map of the department you are in')
label.grid(row=0, column=0)

img = ImageTk.PhotoImage(Image.open("startpoint.jpg"))
panel = Label(root, image=img)
panel.grid(row=2, column=0, pady=15)

label1 = Label(text="Enter the room number you want to go")
label1.grid(row=25, column=0)

tx1 = Entry().grid(row=25, column=1)
txt = StringVar()
tx1 = Entry(textvariable=txt)

Button(text="Submit", command=btact(tx1)).grid(row=26, column=0, padx=25)


root.mainloop()

