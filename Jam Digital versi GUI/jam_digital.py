from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import *

root = Tk()
root.title('Jam Digital')
root.geometry('650x500')

def time():
    display = strftime('%I:%M:%S %p')
    label.config(text = display)
    label.after(1000, time)

def date():
    display1 = datetime.now()
    label1.config(text = display1.__format__('%A, %d %B %Y'))


label1 = Label(root, font=('Monokai,Bold', 30), foreground = 'black')
label1.pack()

label = Label(root, font=('Monokai,Bold', 35), foreground = 'black')
label.pack()

date()
time()
mainloop()