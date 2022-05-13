from tkinter import *

root = Tk()
root.geometry("655x333")        #default window size

user = Label(root, text="Username")
pasw = Label(root, text="Password")
user.grid()
pasw.grid(row=1)

#Variable classes in Tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

user_val = StringVar()
pasw_val = StringVar()

user_entry = Entry(root, textvariable=user_val)
pasw_entry = Entry(root, textvariable=pasw_val)

user_entry.grid(row=0, column=1)
pasw_entry.grid(row=1, column=1)


def getvals():
    print(user_val.get())
    print(pasw_val.get())

Button(text="Submit", command=getvals).grid()

root.mainloop()