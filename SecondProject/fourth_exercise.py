# 4- Utilizando los widgets Menu y Notebook diseñar una pantalla de Menú/ Solapas de la
#    temática que desees.


from distutils.cmd import Command
import os
import sys
sys.path.append(".")
import webbrowser
from tkinter import filedialog
from tkinter import *
from tkinter_new_window import new_window
from tkinter.ttk import Combobox, Notebook
from tkinter_basics import tkinter_basics

## declare exercise 1 and props
ej_4 = tkinter_basics(title='Fourth exercise - ')
ej_4.can_resize(False)
ej_4.root.config(background='#594A7D')

def close_window () :
    '''
        close window
    '''
    ej_4.root.destroy()

def minimize_window():
    '''
        minimize window
    '''
    ej_4.root.iconify()

def browse_button():
    filename = filedialog.askdirectory()
    print(filename)
    return filename

def open_project(project):
    if project == 'first':
        filedialog.askdirectory(initialdir=os.path.normpath("./FirstProject"), title="FirstProject")
    else:
        filedialog.askopenfilenames(initialdir=os.path.normpath("./SecondProject"), title="SecondProject")

# Create menu bar
exercises_menu = Menu (ej_4.root)
ej_4.root.config (menu = exercises_menu, bg = '#594A7D')

# File menu
projects_menu = Menu (exercises_menu, tearoff = 0) 
exercises_menu.add_cascade (label = "College projects ", menu = projects_menu) 
projects_menu.add_command (label = "Open", command=browse_button) 

# Open Recent
openRecentMenu = Menu (exercises_menu, tearoff = 0)
projects_menu.add_cascade (label = "Open Recent", menu = openRecentMenu)
openRecentMenu.add_command (label = "First Project", command= lambda : open_project('first')) 
openRecentMenu.add_command (label = "Second Project", command= lambda : open_project('second')) 

# separator
projects_menu.add_separator () 

projects_menu.add_command (label = "Close", command=minimize_window)
projects_menu.add_command (label = "Exit", command=close_window) 


# Help menu
helpMenu = Menu (exercises_menu, tearoff = 0)
exercises_menu.add_cascade (label = "Help", menu = helpMenu) 
helpMenu.add_command (label = "Github", command= lambda: webbrowser.open('https://github.com/julian-er/')) 
helpMenu.add_command (label = "LinkedIn", command= lambda: webbrowser.open('https://www.linkedin.com/in/juli%C3%A1n-rosalen/')) 

# Create Notebook panel
notebook = Notebook()
notebook.config(width = 800, height = 500)
notebook.grid(column=0, columnspan=11, sticky=W, row=0, rowspan=11, padx=3, pady=3) 


# Create labels
file_1 = Frame (notebook, bg='#594A7D')
file_2 = Frame (notebook)


# Add labels 
notebook.add (file_1, text = "First exercise" ) 
notebook.add (file_2, text = "Third exercise")


# Content file 1
validUser = 'admin'
validPassword = 'admin'

def login () :
    '''
        Loging validate user and password
    '''
    if (username.get() == validUser and password.get() == validPassword):
        #new window declaration
        ej_4.root.iconify()
        new_window(file_1, type_window='second_exercise' , title='Second exercise goes here - ').execute_window()
    else:
        #new window declaration
        error = new_window(file_1, type_window='error_message', title='Ups an error occurs - ', iconUrl='./icons/j2.ico')
        error.minsize(200,50)
        error.execute_window()

# Get and store data
username = StringVar()
password = StringVar()

# Labels
user_name = Label(file_1, text="User : ", fg='#FFFFFF', background='#594A7D')
user_name.grid(column=1, columnspan=2, sticky=W, row=1, rowspan=1, padx=3, pady=3)

user_password = Label(file_1, text="Password : ", fg='#FFFFFF', background='#594A7D')
user_password.grid(column=1, columnspan=2, sticky=W, row=5, rowspan=1, padx=3, pady=3)

# Entries
username_entry = Entry(file_1, textvariable=username)
username_entry.grid(column=1, columnspan=2, sticky=EW, row=2, rowspan=1, padx=3, pady=3)

password_entry = Entry(file_1, textvariable=password,  show='*')
password_entry.grid(column=1, columnspan=2, sticky=EW, row=6, rowspan=1, padx=3, pady=3)

# Button
btn = Button (file_1, text = 'Login', command=login)
btn.grid (row = 9, column = 8, columnspan=3, padx=3, pady=3)


# Content file 2
# Background photoImage
background = Frame (file_2)
bgImage = PhotoImage (file = "./assets/trip.png")
labelImage = Label (file_2, image = bgImage)
labelImage.place(x=0, y=0, relwidth=1, relheight=1)

# Block LabelFrame Flights
flights_block = LabelFrame (file_2, text = "Flights", fg='white', font =(16))
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



ej_4.execute_window()