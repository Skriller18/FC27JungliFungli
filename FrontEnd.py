import tkinter
from tkinter import *
from tkinter import Label
from PIL import ImageTk, Image

def btnfn():
    tx = txt.get()
    '''testlabel = Label(text="Your destination is "+tx)
    testlabel.place(x=900, y=60)
    image3 = Image.open("Finalmap.jpg")
    test3 = ImageTk.PhotoImage(image2)
    labei3 = tkinter.Label(image=test2)
    labei3.image = test2
    labei3.place(x=0, y=100)

    image4 = Image.open("FinalBUILDING.jpg")
    test4 = ImageTk.PhotoImage(image2)
    labei4 = tkinter.Label(image=test2)
    labei4.image = test2
    labei4.place(x=850, y=100)'''

    image1 = Image.open("FINALIMAGE.png")
    test1 = ImageTk.PhotoImage(image1)
    labei1 = tkinter.Label(image=test1)
    labei1.image = test1
    labei1.place(x=0, y=100)

    '''image2 = Image.open("MCA_clean.png")
    test2 = ImageTk.PhotoImage(image2)
    labei2 = tkinter.Label(image=test2)
    labei2.image = test2
    labei2.place(x=850, y=100)'''



root = Tk()
root.title("RVDAR")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
dimensions = str(width) + "x" + str(height)
root.geometry(dimensions)

label = Label(text='This is the map of the college and your department')
label.place(x=800, y=0)

label1 = Label(text='Enter your destination')
label1.place(x=550, y=40)

txt = StringVar()
txt1 = StringVar()
txt2 = StringVar()
tx1 = Entry(textvariable=txt)
tx2 = Entry()
tx3=Entry()
tx1.place(x=1000, y=40)
tx2.place(x=1100,y=40)
tx3.place(x=1200,y=40)
tx = txt.get()
Label(text="Room       Destination Department         Leaving Department").place(x=1000, y=80)

btn = Button(text="Enter", command=btnfn)
btn.place(x=1300, y=40)

'''image1 = Image.open("MAINMAP_clean.jpeg")
test1 = ImageTk.PhotoImage(image1)
labei1 = tkinter.Label(image=test1)
labei1.image = test1
labei1.place(x=0, y=100)

image2 = Image.open("MCA_clean.png")
test2 = ImageTk.PhotoImage(image2)
labei2 = tkinter.Label(image=test2)
labei2.image = test2
labei2.place(x=850, y=100)'''


root.mainloop()