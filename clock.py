import time
from tkinter import *

canvas = Tk() 
canvas.title('Digital Clock') 
canvas.geometry('400x200')
label = Label(canvas,font =('Helvetica',20,'bold'),bg='blue',fg='white')
label.grid(row=1 , column =1)

def clock() :
    inp = time.strftime('%H:%M:%S')
    label.config(text = inp)
    label.after(1000,clock) #time in milliseconds

clock()
canvas.mainloop()