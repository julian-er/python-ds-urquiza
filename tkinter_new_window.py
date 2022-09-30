from tkinter import *


class new_window(Toplevel):
    '''
        Define Tkinter Toplevel windows and configurations

        Parameter:
        title (str) : title of window -> has default if value not provided
        iconUrl (str) : route of window icon -> has default if value not provided
        cols (int) : number of columns on your window
        rows (int) : number of rows on your window

        Return tk toplevel , to execute window do new_window(tk.root)
    '''
     
    def __init__(self, master = None, type_window= 'new_window', title='DS Urquiza',  iconUrl='./icons/j1.ico', cols=12, rows=12, ):
        

        # define variables
        super().__init__(master = master)
        self.title(title + ' second term practice')
        self.iconbitmap(iconUrl)
        self.col = cols
        self.row = rows
        self.type = type_window
        self.minsize(500, 500)
        self.resizable(False, False)

    def define_cols_quantity(self):
        '''
            Choose quantity columns for your grid

            Parameter:
            col (int) : default 12
        '''
        for x in range(self.col):
            self.columnconfigure(x, weight=1, uniform="x")

    def define_rows_quantity(self):
        '''
            Choose quantity columns for your grid

            Parameter:
            col (int) : default 12
        '''
        for x in range(self.row):
            self.rowconfigure(x, weight=1, uniform="x")

    def execute_window(self):
        if self.type == 'error_message' :
            label = Label(self, text ="Your user and password aren't valid")
            label.pack()
        elif self.type == 'second_exercise' :
            label = Label(self, text ="This is a new Window")
            label.pack()
    