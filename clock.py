from tkinter import *
from tkinter .ttk import *
from time import strftime

window = Tk()

window.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text= string)
    label.after(1000, time)

label = Label(window, font=("arial", 40, "bold"),
            background="white",
            foreground="DarkOrchid3")

label.pack(anchor="center")

time()
mainloop()
