from tkinter import *

master = Tk()

variable = StringVar()
variable.set("One")

w = OptionMenu(master, variable, "One", "Two", "Three")
w.pack()

def ok():
    print("Value is", variable.get())
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()