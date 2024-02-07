from tkinter import *

def display():
    if(x.get()==1):
        print("You found this program fun! I'm glad")
    else:
        print("You don't find it fun...I'm sorry...")


def displayy():
    if (y.get() == 1):
        print("Its Working Lets gooo")
    else:
        print("Well... I mean it's still working")


window = Tk()

fun = PhotoImage(file='img.png')

x = IntVar()
y = IntVar()
check_button = Checkbutton(window, text="Is this program fun?",
                           background="#0000FF", variable=x,
                           onvalue=1, offvalue=0,
                           command=display, bg="blue",
                           activebackground="blue", fg="#00FF00", activeforeground="#00FF00",
                           font=("Arial", 15),
                           image=fun, compound="right")


checks_button = Checkbutton(window, text="Is this a working Checkbox?",
                           background="purple", variable=y,
                           onvalue=1, offvalue=0,
                           command=displayy, bg="purple",
                           activebackground="purple", fg="#00FF00", activeforeground="#00FF00",
                           font=("Arial", 15)
                          )
check_button.pack()
checks_button.pack()
window.mainloop()