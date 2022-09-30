# 4- Mostrar una ventana y en su interior dos botones y una label. La label muestra
# inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar
# en uno el contenido de la label
import sys
sys.path.append(".")
from tkinter import *
from tkinter_basics import tkinter_basics

ej_4 = tkinter_basics()
ej_4.can_resize(True)
ej_4.root.minsize(200,200)
def set_value (gender_param) :
    '''
        Set new number string
    '''
    if(gender_param.lower() == 'sub'):
        valueCalculated.set(valueCalculated.get() - 1)
    else :
        valueCalculated.set(valueCalculated.get() + 1)


# Get and store data
valueCalculated = IntVar()
valueCalculated.set(0)

# Labels
reveal_title = Label(ej_4.root, text='Increment or decrement the number', justify=CENTER, font=(20))
reveal_title.grid(column=2, columnspan=8, sticky=EW, row=1, rowspan=2, padx=3, pady=3)

reveal_gender = Label(ej_4.root, textvariable=valueCalculated, font=(16), justify=CENTER)
reveal_gender.grid(column=2, columnspan=8 ,row=4, rowspan=3, padx=3, pady=3)

female_gender = Button(ej_4.root, text='SUB', command= lambda: set_value('sub'))
female_gender.grid(column=2, columnspan=3, sticky=EW ,row=10, rowspan=1, padx=3, pady=3)

male_gender = Button(ej_4.root, text='ADD', command=lambda : set_value('add'))
male_gender.grid(column=7, columnspan=3, sticky=EW ,row=10, rowspan=1, padx=3, pady=3)

ej_4.execute_window()