# Tomamos como base el Ejercicio 1 del TP1 donde pedimos usuario y contraseña y
# realizamos lo siguiente:
# a. Al título de la Ventana poner Ingreso de Usuario. Cambiar el icono por defecto.
# b. Cambiar el color de fondo de la ventana. Establecer un tamaño adecuado y no permitir modificarlo.
# c. Controlar que el usuario ingresado sea admin contraseña admin o su apellido como usuario y contraseña caso contrario mostrar que es incorrecto puede
#    realizarlo con un mensaje o una ventana modal. Si el usuario es correcto mostrar
#    la ventana del ejercicio 2 minimizando o cerrando la primera.

import sys
sys.path.append(".")
from tkinter import *
from tkinter_new_window import new_window
from tkinter_basics import tkinter_basics

## declare exercise 1 and props
ej_1 = tkinter_basics(title='Ingreso de usuario - ')
ej_1.can_resize(False)
ej_1.root.config(background='#594A7D')
# define variables
validUser = 'admin'
validPassword = 'admin'

def login () :
    '''
        Loging validate user and password
    '''
    if (username.get() == validUser and password.get() == validPassword):
        #new window declaration
        ej_1.root.iconify()
        new_window(ej_1.root, type_window='second_exercise' , title='Second exercise goes here - ').execute_window()
    else:
        #new window declaration
        error = new_window(ej_1.root, type_window='error_message', title='Ups an error occurs - ', iconUrl='./icons/j2.ico')
        error.minsize(200,50)
        error.execute_window()



# Get and store data
username = StringVar()
password = StringVar()

# Labels
user_name = Label(ej_1.root, text="User : ", fg='#FFFFFF', background='#594A7D')
user_name.grid(column=1, columnspan=2, sticky=W, row=1, rowspan=1, padx=3, pady=3)

user_password = Label(ej_1.root, text="Password : ", fg='#FFFFFF', background='#594A7D')
user_password.grid(column=1, columnspan=2, sticky=W, row=5, rowspan=1, padx=3, pady=3)

# Entries
username_entry = Entry(textvariable=username)
username_entry.grid(column=1, columnspan=2, sticky=EW, row=2, rowspan=1, padx=3, pady=3)

password_entry = Entry(textvariable=password,  show='*')
password_entry.grid(column=1, columnspan=2, sticky=EW, row=6, rowspan=1, padx=3, pady=3)

# Button
btn = Button (text = 'Login', command=login)
btn.grid (row = 9, column = 8, columnspan=3, padx=3, pady=3)



# Adapt size
ej_1.root.minsize(300, 200)


ej_1.execute_window()
