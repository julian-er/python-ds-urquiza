# 3- Diseñar una pantalla similar a la de la imagen. Usar otra imagen e ícono. También
#    puedes cambiar el diseño y temática. Pero, DEBES utilizar los widgets que se ven en
#    la imagen. Puede también utilizar ventanas Modales
import sys
from tkinter.ttk import Combobox
sys.path.append(".")
from tkinter import *
from tkinter_new_window import new_window
from tkinter_basics import tkinter_basics

## declare exercise 3 and props
ej_3 = tkinter_basics(title='Travel - ')
ej_3.can_resize(FALSE)
ej_3.root.minsize(1000,800)
ej_3.root.config(background='#594A7D')

# Block 1 background photoImage
block1 = Frame (ej_3.root)
bgImage = PhotoImage (file = "./assets/trip.png")
labelImage = Label (ej_3.root, image = bgImage)
labelImage.place(x=0, y=0, relwidth=1, relheight=1)

# Block 3 labelFrame Flights
block3 = LabelFrame (ej_3.root, text = "Flights", font =(16))
block3.config (bg = "#594A7D")
block3.grid(column=8, columnspan=4, sticky=EW, row=0, rowspan=7, padx=3, pady=3)

# Row 0 check buttons
round_trip = Checkbutton(block3, text = "Round trip", bg = "#594A7D")
round_trip.grid (row = 0, column = 0, padx = 7,pady = 15, sticky = EW)

one_way = Checkbutton (block3, text = "One Way", bg = "#594A7D")
one_way.grid (row = 0, column = 1, padx = 0,pady = 5, sticky = EW)

multi = Checkbutton (block3, text = "Multi Destination", width = 35, bg = "#594A7D")
multi.grid (row = 0, column = 2, padx = 5,pady = 5, sticky = EW, columnspan = 2)

# Row 1 boarding label
boarding_label = Label (block3, text = "- BOARDING -")
boarding_label.grid (row = 1, column = 0, padx = 5, pady = 20, sticky = EW)
boarding_label.config ( bg = '#594A7D')

# Row 1 boarding entry
boarding_entry = Entry (block3, bg = "#594A7D",)
boarding_entry.grid (row = 1, column = 1, sticky = EW)

# Row 1 destination label 
destination_label = Label (block3, text = "- DESTINATION -")
destination_label.grid (row = 1, column = 2, padx = 5, pady = 20, sticky = EW)
destination_label.config (bg = '#594A7D')

# Row 1 destination entry 
destination_entry = Entry (block3, bg = "#594A7D")
destination_entry.grid (row = 1, column = 3, sticky = EW)

# Row 2 passengers label
passengers = Label (block3, text = "Passengers")
passengers.grid (row = 2, column = 0, padx = 5, pady = 5, sticky=E)

# Row 2 passengers combobox 
passengers_box = Combobox (block3)
passengers_box.grid (row = 2, column = 1, sticky = W)
passengers_box ['values'] = ('1', '2', '3', '4', '5','6','7','8','9','10')
passengers_box.set ('1')

# Row 3 div (separator)
div_separator = Frame (block3)
div_separator.grid (row = 3, column = 0, columnspan = 2)
div_separator.config (bg = '#594A7D')

# Row 4 buttons exit and reserve
exit_btn = Button (block3, text = 'Exit')
exit_btn.grid (row = 4, column = 0, pady = 5, columnspan = 2)

reserve_btn = Button (block3, text = 'Reserve')
reserve_btn.grid (row = 4, column = 2, pady = 15, columnspan = 2)

ej_3.execute_window()