import tkinter as tk
from tkinter import *

# for the user interface
from tkinter import ttk
from tkinter.ttk import *


def getparameters():
    numbathrooms = int(numbath.get())  # getting the
    numbedrooms = int(numbed.get())
    sqfoot = int(sq.get())

    garage = garopt.get()
    garage_yn = ""

    backyard = backopt.get()
    backyard_yn = ""

    basement = baseopt.get()
    basement_yn = ""

    # if they want a garage
    if garage == 0:
        garage_yn = "y"
    elif garage == 1:
        garage_yn = "n"

    # if they want a backyard
    if backyard == 0:
        backyard_yn = "y"
    elif backyard == 1:
        backyard_yn = "n"

    # if they want a basement
    if basement == 0:
        basement_yn = "y"
    elif baseopt.get() == 1:
        basement_yn = "n"

    citychoice = cities.get(cities.curselection())
    toppref = top_pref.get(top_pref.curselection())
    secpref = sec_pref.get(sec_pref.curselection())

    # testing that I get the correct values:
    print("# bath: " + str(numbathrooms))
    print("# beds: " + str(numbedrooms))
    print("sqr foot: " + str(sqfoot))
    print("garage? " + garage_yn)
    print("backyard? " + backyard_yn)
    print("basement? " + basement_yn)
    print("city? " + citychoice)
    print("Which is most important? " + toppref)
    print("Second most important? " + secpref)


ui = Tk(className="Finding Houses")
ui.geometry("325x500")  # no problem with this one

# variables for each entry
numbath = StringVar()
numbed = StringVar()

sq = StringVar()

garopt = IntVar()
backopt = IntVar()
baseopt = IntVar()

# title
title = Label(ui, text="Finding Your House:").grid(row=0, column=0, padx=25, pady=20, columnspan=2)
# window.pack()

bathroomlabel = Label(ui, text="# Bathroom:").grid(row=2, column=0, padx=20)
entry1 = Entry(ui, textvariable=numbath, width=5).grid(row=2, column=1, sticky=W, padx=10)

bedroomlabel = Label(ui, text="# Bedroom:").grid(row=3, column=0, padx=20)
entry2 = Entry(ui, textvariable=numbed, width=5).grid(row=3, column=1, sticky=W, padx=10)

footagelabel = Label(ui, text="Sq Footage:").grid(row=4, column=0, padx=20)
sqrfoot = Entry(ui, textvariable=sq, width=8).grid(row=4, column=1, sticky=W, padx=10)

garagelabel = Label(ui, text="Garage?:").grid(row=5, column=0, padx=20)
y1 = Radiobutton(ui, text="yes", variable=garopt, value=0).grid(row=5, column=1, sticky=W, padx=20)
n1 = Radiobutton(ui, text="no", variable=garopt, value=1).grid(row=5, column=1, sticky=E, padx=20)

backyardlabel = Label(ui, text="Backyard?:").grid(row=6, column=0, padx=20)
y2 = Radiobutton(ui, text="yes", variable=backopt, value=0).grid(row=6, column=1, sticky=W, padx=20)
n2 = Radiobutton(ui, text="no", variable=backopt, value=1).grid(row=6, column=1, sticky=E, padx=20)

basementlabel = Label(ui, text="Basement?:").grid(row=7, column=0, padx=20)
y3 = Radiobutton(ui, text="yes", variable=baseopt, value=0).grid(row=7, column=1, sticky=W, padx=20)
n3 = Radiobutton(ui, text="no", variable=baseopt, value=1).grid(row=7, column=1, sticky=E, padx=20)

citylabel = Label(ui, text="City:").grid(row=8, column=0)
cities = Listbox(ui, height=3, exportselection=0)
cities.insert(1, "Boise, Idaho")
cities.insert(2, "Reno, Nevada")
cities.insert(3, "Midland, Texas")
cities.grid(column=1, row=8)
cities.pack_slaves()
# button to run the program
find = Button(ui, text='Results', width=5, command=getparameters).grid(column=0, row=13, sticky=S, padx=20, pady=30,
                                                                       columnspan=2)
# add button to gui window
# find.pack_slaves()

# choosing top preferences
toppreflabel = Label(ui, text="Top Preferences").grid(column=1, row=10, padx=10, pady=10)

firstlabel = Label(ui, text="First").grid(column=1, row=11, padx=10, pady=10, sticky=W)
top_pref = Listbox(ui, height=6, width=8, exportselection=0)
top_pref.insert(1, "Sq Footage")
top_pref.insert(2, "Bathrooms")
top_pref.insert(3, "Bedrooms")
top_pref.insert(4, "Basement")
top_pref.insert(5, "Backyard")
top_pref.insert(6, "Garage")
top_pref.grid(column=1, row=12, sticky=W)
top_pref.pack_slaves()

secondlabel = Label(ui, text="Second").grid(column=1, row=11, padx=10, pady=10, sticky=E)
sec_pref = Listbox(ui, height=6, width=8, exportselection=0)
sec_pref.insert(1, "Sq Footage")
sec_pref.insert(2, "Bathrooms")
sec_pref.insert(3, "Bedrooms")
sec_pref.insert(4, "Basement")
sec_pref.insert(5, "Backyard")
sec_pref.insert(6, "Garage")
sec_pref.grid(column=1, row=12, sticky=E)
sec_pref.pack_slaves()

ui.mainloop()
