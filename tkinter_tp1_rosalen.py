# import tkinter for all exercises
# All the exercises  will be documented using python self document
from tkinter import *
from tkinter import ttk

# Create tkinter basics class
class tkinter_basics:
    '''
        Define Tkinter class with basics windows and configurations

        Parameter:
        padding_number (int) : padding of window -> has default if value not provided
        title (str) : title of window -> has default if value not provided
        iconUrl (str) : route of window icon -> has default if value not provided

        Return tk window
    '''

    def __init__(self, title='DS Urquiza', padding_number=10, iconUrl = './icons/j1.ico'):

        # define variables
        self.padding_number = padding_number
        self.title = title
        self.iconUrl = iconUrl
        self.root = Tk()
        self.top = Toplevel()
        self.frame = ttk.Frame(self.root, padding=self.padding_number)

        self.frame.grid()
        self.root.minsize(width=500, height=500)
        self.root.iconbitmap(self.iconUrl)
        self.root.resizable(False, False)
        self.root.title(self.title + 'Second term practice')

    def can_resize(self, resizable_boolean):
        '''
            Allow resize your tk window. By default it's not allowed.

            Parameter:
            resizable_boolean (boolean)
        '''
        self.root.resizable(resizable_boolean, resizable_boolean)

    def change_theme(self, theme):
        '''
            Choose a theme with string, by default theme is light.

            Parameter:
            theme (str) 
        '''
        if theme.lower() == "dark":
            self.root.title(self.title + ' - dark theme')
            self.root.config(background='#000000')
        else:
            self.root.title(self.title + ' - light theme')
            self.root.config(background='#FFFFFF')

    def execute_window(self):
        '''
            Execute mainloop 
        '''
        self.root.mainloop()


# Integrando todos los temas vistos de interfaz gráfica diseñar:
# 1- Una ventana que permita ingresar usuario y contraseña.
ej_1 = tkinter_basics(iconUrl='./icons/j2.ico')
ej_1.can_resize(False)
ej_1.change_theme('dark')
ej_1.execute_window()

# 2- Una ventana que permita ingresar los siguientes datos:
#    Apellido y Nombre
#    Domicilio
#    Teléfono
#    DNI
ej_2 = tkinter_basics()
ej_2.can_resize(True)
ej_2.execute_window()

# 3- Disponer dos Botones con las etiquetas: "varón" y "mujer", al presionarse mostrar un
# Texto en color según el botón elegido
ej_3 = tkinter_basics(iconUrl='./icons/j2.ico')
ej_3.can_resize(False)
ej_3.change_theme('dark')
ej_3.execute_window()

# 4- Mostrar una ventana y en su interior dos botones y una label. La label muestra
# inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar
# en uno el contenido de la label
ej_4 = tkinter_basics()
ej_4.can_resize(True)
ej_4.execute_window()