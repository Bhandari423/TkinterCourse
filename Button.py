from tkinter import *

root = Tk()
root.geometry("655x333")        #default window size

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")

def print_fun():
    print("Print this text!")

b1 = Button(f1, text="Print", fg="red", command=print_fun)
b1.pack(side=LEFT)

b2 = Button(f1, text="Download", fg="red")
b2.pack(side=LEFT, padx=23)

b3 = Button(f1, text="Close", fg="red")
b3.pack(side=LEFT)

root.mainloop()