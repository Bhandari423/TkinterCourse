from tkinter import *

root = Tk()
root.geometry("655x333")        #default window size

#Heading
Label(root, text="Welcome to my first Form!", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
paymentmode = Label(root, text="Payment Mode")

#Pack Text for our form
name.grid(row=1 , column=2)
phone.grid(row=2 , column=2)
gender.grid(row=3 , column=2)
paymentmode.grid(row=4 , column=2)

#Tkinter Variables for storing entries
name_val = StringVar()
phone_val = StringVar()
gender_val = StringVar()
paymentmode_val = StringVar()
foodService_val = IntVar()

#Entries for our form
nameentry = Entry(root, textvariable=name_val)
phoneentry = Entry(root, textvariable=phone_val)
genderentry = Entry(root, textvariable=gender_val)
paymentmodeentry = Entry(root, textvariable=paymentmode_val)

#Packing the entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
paymentmodeentry.grid(row=4, column=3)

#CHECKBOX
foodService = Checkbutton(text="Want to prebook your food?", variable=foodService_val)
foodService.grid(row=5, column=3)

def getVals():
    print("It works!")

#Button
Button(text="Submit", command=getVals).grid(row=6, column=3)

root.mainloop()