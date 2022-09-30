# 4- Mostrar una ventana y en su interior dos botones y una label. La label muestra
# inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar
# en uno el contenido de la label
import sys
sys.path.append(".")
from tkinter_basics import tkinter_basics

ej_4 = tkinter_basics()
ej_4.can_resize(True)
ej_4.execute_window()