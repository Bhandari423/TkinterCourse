#PIL: Python Image Library
#ImageTk: it supports jpg image format

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("444x200")

#it supports png format only
# photo = PhotoImage(file="1.png")

#for jpg format
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

img_label = Label(image=photo)
img_label.pack()




root.mainloop()