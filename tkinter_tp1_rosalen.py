# import tkinter for all exercises
# All the exercises  will be documented using python self document
from tkinter import *
from tkinter import ttk


class tkinter_basics:
    '''
        Define Tkinter class with basics windows and configurations

        Parameter:
        padding_number (int) : padding of window -> has default if value not provided
        title (str) : title of window -> has default if value not provided

        Return tk window
    '''

    def __init__(self, padding_number=10, title='DS Urquiza tkinter practice'):
        
        # define variables 
        self.padding_number = padding_number
        self.title = title
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=self.padding_number)

        # define padding on initialization variable
        self.frame.grid()
        self.root.resizable(False, False)
        ttk.Label(self.frame, text=self.title).grid(column=0, row=0)
        ttk.Button(self.frame, text="Quit", command=self.root.destroy).grid(column=1, row=0)

    def can_resize(self, resizable_boolean):  # To Do resize
        '''
            Allow resize your tk window. By default it's not allowed.

            Parameter:
            argument1 (boolean)
        '''
        self.root.resizable(resizable_boolean, resizable_boolean)

    def execute_window(self):
        '''
            Execute mainloop 
        '''
        self.root.mainloop()



window = tkinter_basics()
window.can_resize(True)
window.execute_window()

# Integrando todos los temas vistos de interfaz gráfica diseñar:
# 1- Una ventana que permita ingresar usuario y contraseña.


# 2- Una ventana que permita ingresar los siguientes datos:
#    Apellido y Nombre
#    Domicilio
#    Teléfono
#    DNI

# 3- Disponer dos Botones con las etiquetas: "varón" y "mujer", al presionarse mostrar un
# Texto en color según el botón elegido

# 4- Mostrar una ventana y en su interior dos botones y una label. La label muestra
# inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar
# en uno el contenido de la label
