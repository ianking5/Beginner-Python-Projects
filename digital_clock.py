from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('My Clock')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(myWindow, font = ('cambria', 40, 'bold'), 
                                background='orange',
                                foreground='white')

clock.pack(anchor= 'center')
time()

mainloop()