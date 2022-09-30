# 2- Una ventana que permita ingresar los siguientes datos:
#    Apellido y Nombre
#    Domicilio
#    Teléfono
#    DNI

import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics
from tkinter import *

ej_2 = tkinter_basics(title='ejercicio 2', rows=10, cols=4)
ej_2.can_resize(True)

# Get and store data
name = StringVar()
last_name = StringVar()
address = StringVar()
phone = StringVar()
id_card = StringVar()

# Labels
user_name = Label(ej_2.root, text="Name : ")
user_name.grid(column=1, columnspan=2, sticky=W, row=0, rowspan=1, padx=3, pady=3)

user_last_name = Label(ej_2.root, text="Last Name : ")
user_last_name.grid(column=1, columnspan=2, sticky=W, row=2, rowspan=1, padx=3, pady=3)

user_address = Label(ej_2.root, text="Address : ")
user_address.grid(column=1, columnspan=2, sticky=W, row=4, rowspan=1, padx=3, pady=3)

user_phone = Label(ej_2.root, text="Phone : ")
user_phone.grid(column=1, columnspan=2, sticky=W, row=6, rowspan=1, padx=3, pady=3)

user_id = Label(ej_2.root, text="Id card : ")
user_id.grid(column=1, columnspan=2, sticky=W, row=8, rowspan=1, padx=3, pady=3)

# Entries
name_entry = Entry(textvariable=name)
name_entry.grid(column=1, columnspan=2, sticky=NW, row=1, rowspan=1, padx=3, pady=3)

last_name_entry = Entry(textvariable=last_name)
last_name_entry.grid(column=1, columnspan=2, sticky=NW, row=3, rowspan=1, padx=3, pady=3)

address_entry = Entry(textvariable=address)
address_entry.grid(column=1, columnspan=2, sticky=NW, row=5, rowspan=1, padx=3, pady=3)

phone_entry = Entry(textvariable=phone)
phone_entry.grid(column=1, columnspan=2, sticky=NW, row=7, rowspan=1, padx=3, pady=3)

id_card_entry = Entry(textvariable=id_card)
id_card_entry.grid(column=1, columnspan=2, sticky=NW, row=9, rowspan=1, padx=3, pady=3)


# Adapt size
ej_2.root.minsize(400,400)



ej_2.execute_window()