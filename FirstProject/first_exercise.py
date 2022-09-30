# Integrando todos los temas vistos de interfaz gráfica diseñar:
# 1- Una ventana que permita ingresar usuario y contraseña.
import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics
from tkinter import *


ej_1 = tkinter_basics(title='ejercicio 1', iconUrl='./icons/j2.ico', rows=4, cols=4)
ej_1.can_resize(False)
ej_1.change_theme('dark')

# Get and store data
username = StringVar()
password = StringVar()

# Labels
user_name = Label(ej_1.root, text="User : ", fg="white", background='#000000')
user_name.grid(column=1, columnspan=2, sticky=W, row=0, rowspan=1, padx=3, pady=3)

user_password = Label(ej_1.root, text="Password : ", fg="white", background='#000000')
user_password.grid(column=1, columnspan=2, sticky=W, row=2, rowspan=1, padx=3, pady=3)

# Entries
username_entry = Entry(textvariable=username)
username_entry.grid(column=1, columnspan=2, sticky=NW, row=1, rowspan=1, padx=3, pady=3)

password_entry = Entry(textvariable=password,  show='*')
password_entry.grid(column=1, columnspan=2, sticky=NW, row=3, rowspan=1, padx=3, pady=3)


# Adapt size
ej_1.root.minsize(300,200)



ej_1.execute_window()
