import os, keyboard, time
from tkinter import *
from tkinter.ttk import *
def open_program():
    input_value = txtfld.get()
    if input_value == "69420":
        os.system("console_systemcrasher.py")
        time.sleep(3)
    else:
        window.destroy()

window = Tk()
window.iconbitmap("icon.png")
btn = Button(window, text="Initialize", command=open_program)
btn.place(x=100, y=100)

lbl = Label(window, text="Enter 69420 in the text box and press the button.", font=("Cascadia Code", 8))
lbl.place(x=1, y=50)

txtfld = Entry(window)
txtfld.place(x=80, y=150)

window.title('System Crasher by Retro on GitHub')
window.geometry("300x200+10+10")
window.mainloop()