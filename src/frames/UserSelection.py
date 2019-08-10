from tkinter import *
from tkinter import ttk


class UserSelection(ttk.Combobox):
    """A dropbown box located in the top-right corner used for multiple users."""
    def __init__(self, parent):
        self.current_user = StringVar()
        ttk.Combobox.__init__(self, parent, justify=CENTER, textvariable=self.current_user)
        self.grid(row=0, column=1, sticky=NE)
        self.parent = parent

        self.option_values = ['User1', 'User2', 'The name of this User is long for testing']

        self._initialize()

    def _initialize(self):
        self.bind('<<ComboboxSelected>>', self.change_user)
        self['values'] = self.option_values
        self.current(0)  # first user is default
        self.configure(state='readonly')  # user cannot modify the name
        self.adjust_width()

    def adjust_width(self):
        """Adjust the user selection width after a new user is selected.
        New width will be between [7, 30] inclusive."""
        new_width = min(30, max(7, len(self.get_current_user())))
        self.configure(width=new_width)

    def change_user(self, event):
        self.adjust_width()
        self.select_clear()  # clears the highlighted text
        # for attr in dir(event.widget):
        #     print(attr, '=>', getattr(event.widget, attr))
        print('Changed to', self.get().upper())

    def get_current_user(self):
        return self.current_user.get()
