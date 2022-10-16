# Una ventana que permita ingresar los siguientes datos:
# Código Artículo
# Descripción
# Precio Unitario
# Stock
# Cantidad Pedida
# Si la cantidad Pedida es menor que el Stock mostrar una advertencia.


from distutils.command.config import config
import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics
from tkinter import *

ej_2 = tkinter_basics(title='Stock', rows=12, cols=6)
ej_2.can_resize(True)
ej_2.change_theme('dark')


# Get and store data
code = StringVar()
description = StringVar()
unit_price = StringVar()
stock = StringVar()
quantity = StringVar()
error = StringVar()

def validate_stock () :
    '''
        Set error Label 
    '''
    if(stock_entry.get() < quantity_entry.get()):
        error.set('Oops! your stock is lower than the quantity requested')
    else :
        error.set('')


def only_number_input(text):
    '''
        Only use numbers, and reset error on change value 
    '''
    error.set('')
    return text.isdecimal()

# Labels
code_article = Label(ej_2.root, text="Cod. : ")
code_article.grid(column=1, columnspan=2, sticky=W, row=0, rowspan=1, padx=3, pady=3)

article_description = Label(ej_2.root, text="Description : ")
article_description.grid(column=1, columnspan=2, sticky=W, row=2, rowspan=1, padx=3, pady=3)

unit_price = Label(ej_2.root, text="Unit price : ")
unit_price.grid(column=1, columnspan=2, sticky=W, row=4, rowspan=1, padx=3, pady=3)

stock = Label(ej_2.root, text="Stock : ")
stock.grid(column=1, columnspan=2, sticky=W, row=6, rowspan=1, padx=3, pady=3)

user_id = Label(ej_2.root, text="Quantity Ord. : ")
user_id.grid(column=1, columnspan=2, sticky=W, row=8, rowspan=1, padx=3, pady=3)

# Entries
code_article_entry = Entry(textvariable=code)
code_article_entry.grid(column=1, columnspan=2, sticky=NW, row=1, rowspan=1, padx=3, pady=3)

article_description_entry = Entry(textvariable=description)
article_description_entry.grid(column=1, columnspan=2, sticky=NW, row=3, rowspan=1, padx=3, pady=3)

unit_price_entry = Entry(textvariable=unit_price, validate="key", validatecommand=(ej_2.root.register(only_number_input), "%S"))
unit_price_entry.grid(column=1, columnspan=2, sticky=NW, row=5, rowspan=1, padx=3, pady=3)

stock_entry = Entry(textvariable=stock, validate="key", validatecommand=(ej_2.root.register(only_number_input), "%S"))
stock_entry.grid(column=1, columnspan=2, sticky=NW, row=7, rowspan=1, padx=3, pady=3)

quantity_entry = Entry(textvariable=quantity, validate="key", validatecommand=(ej_2.root.register(only_number_input), "%S"))
quantity_entry.grid(column=1, columnspan=2, sticky=NW, row=9, rowspan=1, padx=3, pady=3)

error_label = Label(ej_2.root, textvariable=error, background='#000000', font=(16), justify=CENTER, fg='red')
error_label.grid(column=1, columnspan=2 ,row=12, rowspan=1, padx=3, pady=3)

order_btn = Button(ej_2.root, text='Order', command=validate_stock)
order_btn.grid(column=1, columnspan=3, sticky=EW ,row=11, rowspan=1, padx=3, pady=3)

# Adapt size
ej_2.root.minsize(400,400)



ej_2.execute_window()