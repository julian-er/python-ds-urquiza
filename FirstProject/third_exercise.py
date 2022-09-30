# 3- Disponer dos Botones con las etiquetas: "varón" y "mujer", al presionarse mostrar un
# Texto en color según el botón elegido
import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics
from tkinter import *


ej_3 = tkinter_basics(iconUrl='./icons/j2.ico')
ej_3.can_resize(False)
ej_3.change_theme('dark')

def set_gender (gender_param) :
    '''
        Set gender Label from param received
        To pass params in button use lambda
    '''
    if(gender_param.lower() == 'female'):
        gender.set('It`s a girl!')
        reveal_gender.config(fg='#fdc1da')
    else :
        gender.set('It`s a boy!')
        reveal_gender.config(fg='#b9eeff')

# Get and store data
gender = StringVar()

# Labels
reveal_title = Label(ej_3.root, text='Choose gender to reveal text !', fg="white", background='#000000', justify=CENTER, font=(20))
reveal_title.grid(column=2, columnspan=8, sticky=EW, row=1, rowspan=2, padx=3, pady=3)

reveal_gender = Label(ej_3.root, textvariable=gender, background='#000000', font=(16), justify=CENTER)
reveal_gender.grid(column=2, columnspan=8 ,row=4, rowspan=3, padx=3, pady=3)

female_gender = Button(ej_3.root, text='Female', command= lambda: set_gender('female'))
female_gender.grid(column=2, columnspan=3, sticky=EW ,row=10, rowspan=1, padx=3, pady=3)

male_gender = Button(ej_3.root, text='Male', command=lambda : set_gender('male'))
male_gender.grid(column=7, columnspan=3, sticky=EW ,row=10, rowspan=1, padx=3, pady=3)

ej_3.execute_window()
