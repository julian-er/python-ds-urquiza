# Integrando todos los temas vistos de interfaz gráfica diseñar:
# 1- Una ventana que permita ingresar usuario y contraseña.
import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics


ej_1 = tkinter_basics(iconUrl='./icons/j2.ico')
ej_1.can_resize(False)
ej_1.change_theme('dark')
ej_1.execute_window()
