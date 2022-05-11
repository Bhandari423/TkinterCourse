from tkinter import *

root = Tk()
root.geometry("700x400")

root.title("My GUI")

########## IMPORTANT LABEL OPTIONS #########
#bg - background color
#fg - foreground color
#padx, pady - padding
#font style - 1. font=("comicsansms", 10, "bold")  2.font="comicsansms 10 bold"
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''
Robotics is an interdisciplinary branch of computer science and engineering.[1] Robotics involves design, construction, 
\noperation, and use of robots. The goal of robotics is to design machines that can help and assist humans. 
\nRobotics integrates fields of mechanical engineering, electrical engineering, information engineering, mechatronics, 
\nelectronics, bioengineering, computer engineering, control engineering, software engineering, 
\nmathematics, etc.''', bg="red", fg="white", padx=24, pady=34, font=("comicsansms", 10, "bold"), borderwidth=10, relief=SUNKEN)


##### IMPORTANT PACK OPTIONS #########
#anchor - north-west(nw), north-east(ne)
#side - TOP, BOTTOM, LEFT, RIGHT
#fill - if user maximize window, then content also gets filled in it
#padding - padx, pady


# title_label.pack(anchor="nw")
# title_label.pack(side=BOTTOM, anchor="se", fill=X)    #for south you need to mention side
title_label.pack(side=LEFT, fill=Y, padx=30, pady=32)
root.mainloop()