#pack: place things in a box
#grid: like excel, place things in a grid
#place: place anything at a certain points (x,y coordinates)
#canvas: To draw different shapes
#label: user can't interact with label

from tkinter import *

root = Tk()
root.geometry("733x450")        #width x height
root.minsize(300, 100)          #width, height      #one can minimize window upto given width and height
root.maxsize(1000, 900)         #width, height      #one can maximize window upto given width and height

label = Label(text="Hi! This is my GUI")
#pack this label otherwise it will not appear
label.pack()


root.mainloop()