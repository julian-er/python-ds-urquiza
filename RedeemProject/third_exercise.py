# Disponer dos Botones con las etiquetas: "Inglés" y "Francés" Si elige Inglés
# ese botón debe colorearse de Rojo y el de Francés quedar en gris y si elige
# Francés este debe poner Azul y el otro gris. En una Label mostrar cualquier
# palabra en la traducción según el idioma elegido.
import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics
from tkinter import *


ej_3 = tkinter_basics(title='Hello, Bonjour!', iconUrl='./icons/j2.ico')
ej_3.can_resize(False)
ej_3.change_theme('dark')

def set_translation (language_param) :
    '''
        Set language Label from param received
        To pass params in button use lambda
    '''
    if(language_param.lower() == 'english'):
        language.set('Hello! c\'est "bonjour" en anglais')
        translated_label.config(fg='#FFFFFF')
        french.config(bg='gray')
        english.config(bg='red')
    else :
        language.set('Bonjour! Is "Hello" in french')
        translated_label.config(fg='#FFFFFF')
        french.config(bg='blue')
        english.config(bg='gray')

# Get and store data
language = StringVar()

# Labels
translation_title = Label(ej_3.root, text='Choose your language !', fg="white", background='#000000', justify=CENTER, font=(20))
translation_title.grid(column=2, columnspan=8, sticky=EW, row=1, rowspan=2, padx=3, pady=3)

translated_label = Label(ej_3.root, textvariable=language, background='#000000', font=(16), justify=CENTER)
translated_label.grid(column=2, columnspan=8 ,row=4, rowspan=3, padx=3, pady=3)

english = Button(ej_3.root, text='English', command= lambda: set_translation('english'))
english.grid(column=2, columnspan=3, sticky=EW ,row=10, rowspan=1, padx=3, pady=3)

french = Button(ej_3.root, text='Français', command=lambda : set_translation('français'))
french.grid(column=7, columnspan=3, sticky=EW ,row=10, rowspan=1, padx=3, pady=3)

ej_3.execute_window()
