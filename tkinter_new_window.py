from tkinter import *
from tkinter.ttk import Combobox

from SecondProject.second_exercise import validate_docNumber, validate_year




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
            label = Label(self, text ="Your user or password aren't valid")
            label.pack()
        elif self.type == 'second_exercise' :
            self.define_rows_quantity()
            self.define_cols_quantity()
            self.config(background='#594A7D')
            # Title
            title = Label (self, text = 'Please, complete your data !', font =(16), background='#594A7D')
            title.grid (row = 1, column = 2, columnspan = 8, rowspan=1, sticky=EW, padx=3, pady=3)

            # Name label
            name = StringVar()
            name_label = Label (self, text = 'Name', background = '#594A7D')
            name_label.grid (row = 3, column = 1, columnspan = 2, rowspan=1, sticky=SW, padx=3, pady=3)
            name_entry = Entry(self, textvariable = name, width = '30')
            name_entry.grid (row = 4, column = 1, columnspan = 4, rowspan=1, sticky=EW, padx=3, pady=3)

            # Last name 
            last_name = StringVar()
            last_name_label = Label (self, text = 'Last name', background = '#594A7D')
            last_name_label.grid (row = 3, column = 7, columnspan = 2, rowspan=1, sticky=SW, padx=3, pady=3)
            last_name_entry = Entry(self, textvariable = last_name, width = '30')
            last_name_entry.grid (row = 4, column = 7, columnspan = 4, rowspan=1, sticky=EW, padx=3, pady=3)


            # Docs types
                # Combobox
            doc_types_label = Label (self, text = 'Type ID', background = '#594A7D')
            doc_types_label.grid (row = 6, column = 1, columnspan = 2, rowspan=1, sticky=SW, padx=3, pady=3)
            docsType_box = Combobox (self)
            docsType_box.grid (row = 7, column = 1, columnspan = 2, sticky=EW, padx=3, pady=3)
            docsType_box ['values'] = ('DNI', 'LE', 'LC', 'CI', 'PAS')
            docsType_box.set ('DNI')

                # Number
            id_number = Entry (self, validate = "key",width = '30', validatecommand = (self.register (validate_docNumber), "%S", "%P"))
            id_number.grid (row = 7, column = 4, columnspan = 4, sticky = EW, padx=3, pady=3)

            # Birthday
            birthday_label = Label (self, text = 'Birthday date', background = '#594A7D')
            birthday_label.grid (row = 9, column = 1, columnspan = 2, rowspan=1, sticky=SW, padx=3, pady=3)

                # block day box
            day_box = Combobox (self)
            day_box.grid (row = 10, column = 1, columnspan = 2, rowspan=1, sticky=EW, padx=3, pady=3)
            day_box['values'] = ('1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
            day_box.set ('Day')

                # block month box
            month_box = Combobox (self)
            month_box.grid (row = 10, column = 4, columnspan = 4, rowspan=1, sticky=EW, padx=3, pady=3)
            month_box ['values'] = ('January', 'February', 'March', 'April', 'May', "June", "July", "August", "September", "October", "November", "December")
            month_box.set ('Month')

                # block year entry
            year_entry = Entry (self, validate ="key",  validatecommand = (self.register(validate_year), "%S", "%P"))
            year_entry.grid (row = 10, column = 9, columnspan = 2, rowspan=1, sticky=EW, padx=3, pady=3)