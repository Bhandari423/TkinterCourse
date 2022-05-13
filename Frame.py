#Frame: they are different blocks in a gui window where one can put different widgets

from tkinter import *

root = Tk()
root.geometry("655x333")        #default window size

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

#PUTTING LABEL IN FRAME F1
f1_label = Label(f1, text="Project Tkinter - Text Editor")
f1_label.pack(pady=140)

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

f2_label = Label(f2, text="Welcome to my Text Editor!", font="helvetica 16 bold", fg="red")
f2_label.pack(pady=22)

root.mainloop()