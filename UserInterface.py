import tkinter as tk
from tkinter import *


class UserInterface:
    def BuildUI():
        # for the user interface
        from tkinter import ttk

        ui = Tk(className='Finding Houses')
        ui.geometry("500x500")  # no problem with this one
        # setting size
        # ui.geometry("500x500")

        # title
        title = Label(ui, text="Finding Your House:").grid(row=0, column=1)
        # window.pack()

        bathroom = Label(ui, text="# Bathroom:").grid(row=2, column=0)
        entry1 = Entry(ui).grid(row=2, column=1)

        bedroom = Label(ui, text="# Bedroom:").grid(row=3, column=0)
        entry2 = Entry(ui).grid(row=3, column=1)

        footage = Label(ui, text="Sq Footage:").grid(row=4, column=0)
        # entry3 = Entry(ui).grid(row=4, column=1)
        width = Entry(ui, width=8).grid(row=4, column=1, sticky=W)
        x = Label(ui, text="x").grid(row=4, column=1, sticky=S)
        height = Entry(ui, width=8).grid(row=4, column=1, sticky=E)

        garage = Label(ui, text="Garage?:").grid(row=5, column=0)
        y1 = Checkbutton(ui, text="yes").grid(row=5, column=1, sticky=W)
        n1 = Checkbutton(ui, text="no").grid(row=5, column=1, sticky=E)

        backyard = Label(ui, text="Backyard?:").grid(row=6, column=0)
        y2 = Checkbutton(ui, text="yes").grid(row=6, column=1, sticky=NW)
        n2 = Checkbutton(ui, text="no").grid(row=6, column=1, sticky=E)

        basement = Label(ui, text="Basement?:").grid(row=7, column=0)
        y3 = Checkbutton(ui, text="yes").grid(row=7, column=1, sticky=W)
        n3 = Checkbutton(ui, text="no").grid(row=7, column=1, sticky=E)

        city = Label(ui, text="City:").grid(row=8, column=0)
        cities = Listbox(ui, height=3)
        cities.insert(1, "Boise")
        cities.insert(2, "Second City")
        cities.insert(3, "Third City")
        cities.grid(column=1, row=8)
        cities.pack_slaves()
        # button to run the program
        find = Button(ui, text='Results', width=5).grid(column=1, sticky=S)
        # add button to gui window
        # find.pack_slaves()


        ui.mainloop()


def BuildUI():
    UserInterface.BuildUI()
    return None