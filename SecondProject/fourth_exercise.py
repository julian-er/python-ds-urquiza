# 4- Utilizando los widgets Menu y Notebook diseñar una pantalla de Menú/ Solapas de la
#    temática que desees.


import sys
sys.path.append(".")
from tkinter import *
from tkinter.ttk import *
from tkinter_basics import tkinter_basics

## declare exercise 1 and props
ej_4 = tkinter_basics(title='Fourth exercise - ')
ej_4.can_resize(False)
ej_4.root.config(background='#594A7D')

ej_4.execute_window()