# 1- Mostrar la alineación de la Selección Argentina del deporte que desees. Para este
# ejercicio lo recomendable es crear una carpeta con el nombre de imágenes en donde
# se colocarán las imágenes descargadas en formato png.
# fondo.png = Simula la cancha del deporte
# jugadores = Foto de los jugadores según su posición en la cancha.

import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics
from tkinter import *


ej_1 = tkinter_basics(title='CABB', iconUrl='./icons/j2.ico', rows=12, cols=24)
ej_1.can_resize(False)

# Add image file
bg = PhotoImage(file = "./assets/basketball-court.png")
facu = PhotoImage(file = "./assets/campazzo.png")
lapro = PhotoImage(file = "./assets/lapro.png")
deck = PhotoImage(file = "./assets/deck.png")
delfino = PhotoImage(file = "./assets/delfino.png")
delia = PhotoImage(file = "./assets/delia.png")
prigioni = PhotoImage(file = "./assets/prigioni.png")
  
# Show image background using label
label1 = Label( ej_1.root, image = bg)
label1.grid(column=0, columnspan=24, sticky=W, row=0, rowspan=12)

# Show image background using label
label_facu = Label( ej_1.root, image = facu)
label_facu.grid(column=9, columnspan=3, sticky=W, row=4, rowspan=4)

# Show image background using label
label_lapro = Label( ej_1.root, image = lapro)
label_lapro.grid(column=5, columnspan=3, sticky=W, row=1, rowspan=4)

# Show image background using label
label_delfino = Label( ej_1.root, image = delfino)
label_delfino.grid(column=5, columnspan=3, sticky=W, row=7, rowspan=4)

# Show image background using label
label_deck = Label( ej_1.root, image = deck)
label_deck.grid(column=1, columnspan=2, sticky=W, row=1, rowspan=4)

# Show image background using label
label_delia = Label( ej_1.root, image = delia)
label_delia.grid(column=1, columnspan=2, sticky=W, row=7, rowspan=4)

#Some title
title = Label(ej_1.root, text='CABB - Initial five', justify=CENTER, font=(20))
title.grid(column=14, columnspan=8, sticky=EW, row=1, rowspan=2, padx=3, pady=3)

#Some title
title = Label(ej_1.root, text='CABB - DT', justify=CENTER, font=(20))
title.grid(column=14, columnspan=8, sticky=EW, row=3, rowspan=2, padx=3, pady=3)

# Show image background using label
label_prigioni = Label( ej_1.root, image = prigioni)
label_prigioni.grid(column=16, columnspan=3, sticky=EW, row=5, rowspan=4)

# Adapt size
ej_1.root.minsize(800,500)



ej_1.execute_window()