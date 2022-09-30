# import tkinter for all exercises
# All the exercises  will be documented using python self document
from tkinter import *
from tkinter import ttk

# Create tkinter basics class
class tkinter_basics:
    '''
        Define Tkinter class with basics windows and configurations

        Parameter:
        padding_number (int) : padding of window -> has default if value not provided
        title (str) : title of window -> has default if value not provided
        iconUrl (str) : route of window icon -> has default if value not provided

        Return tk window
    '''

    def __init__(self, title='DS Urquiza', padding_number=10, iconUrl = './icons/j1.ico'):

        # define variables
        self.padding_number = padding_number
        self.title = title
        self.iconUrl = iconUrl
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=self.padding_number)

        self.frame.grid()
        self.root.minsize(width=500, height=500)
        self.root.iconbitmap(self.iconUrl)
        self.root.resizable(False, False)
        self.root.title(self.title + 'Second term practice')

    def can_resize(self, resizable_boolean):
        '''
            Allow resize your tk window. By default it's not allowed.

            Parameter:
            resizable_boolean (boolean)
        '''
        self.root.resizable(resizable_boolean, resizable_boolean)

    def change_theme(self, theme):
        '''
            Choose a theme with string, by default theme is light.

            Parameter:
            theme (str) 
        '''
        if theme.lower() == "dark":
            self.root.title(self.title + ' - dark theme')
            self.root.config(background='#000000')
        else:
            self.root.title(self.title + ' - light theme')
            self.root.config(background='#FFFFFF')

    def execute_window(self):
        '''
            Execute mainloop 
        '''
        self.root.mainloop()
