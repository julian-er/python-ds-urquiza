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
ej_3 = tkinter_basics(title='Travel (third exercise)- ')
ej_3.can_resize(FALSE)
ej_3.root.minsize(1000,800)
ej_3.root.config(background='#594A7D')

# Background photoImage
background = Frame (ej_3.root)
bgImage = PhotoImage (file = "./assets/trip.png")
labelImage = Label (ej_3.root, image = bgImage)
labelImage.place(x=0, y=0, relwidth=1, relheight=1)

# Block LabelFrame Flights
flights_block = LabelFrame (ej_3.root, text = "Flights", fg='white', font =(16))
flights_block.config (bg = "#594A7D")
flights_block.grid(column=9, columnspan=4, sticky=W, row=0, rowspan=5, padx=3, pady=3)

# Row 0 check buttons
round_trip = Checkbutton(flights_block, text = "Round trip", fg='white', bg = "#594A7D")
round_trip.grid (row = 0, column = 0, padx = 7,pady = 15, sticky = EW)

one_way = Checkbutton (flights_block, text = "One Way", fg='white', bg = "#594A7D")
one_way.grid (row = 0, column = 1, padx = 0,pady = 5, sticky = EW)

multi = Checkbutton (flights_block, text = "Multi Destination", fg='white', width = 35, bg = "#594A7D")
multi.grid (row = 0, column = 2, padx = 5,pady = 5, sticky = EW, columnspan = 2)

# Row 1 boarding label
boarding_label = Label (flights_block, text = "- BOARDING -" , fg='white',)
boarding_label.grid (row = 1, column = 0, padx = 5, pady = 20, sticky = EW)
boarding_label.config ( bg = '#594A7D')

# Row 1 boarding entry
boarding_entry = Entry (flights_block, bg = "#594A7D", fg='white',)
boarding_entry.grid (row = 1, column = 1, sticky = EW)

# Row 1 destination label 
destination_label = Label (flights_block, text = "- DESTINATION -" , fg='white')
destination_label.grid (row = 1, column = 2, padx = 5, pady = 20, sticky = EW)
destination_label.config (bg = '#594A7D')

# Row 1 destination entry 
destination_entry = Entry (flights_block, bg = "#594A7D" , fg='white')
destination_entry.grid (row = 1, column = 3, sticky = EW)

# Row 2 passengers label
passengers = Label (flights_block, text = "Passengers", background="#594A7D", fg='white')
passengers.grid (row = 2, column = 0, padx = 5, pady = 5, sticky=E)

# Row 2 passengers combobox 
passengers_box = Combobox (flights_block)
passengers_box.grid (row = 2, column = 1, sticky = W)
passengers_box ['values'] = ('1', '2', '3', '4', '5','6','7','8','9','10')
passengers_box.set ('1')

# Row 4 buttons exit and reserve
exit_btn = Button (flights_block, text = 'Exit')
exit_btn.grid (row = 4, column = 0, pady = 5, columnspan = 2)

reserve_btn = Button (flights_block, text = 'Reserve')
reserve_btn.grid (row = 4, column = 2, pady = 15, columnspan = 2)

ej_3.execute_window()