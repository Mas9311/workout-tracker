from src import *
from src import file_helper, formatter


class UserSelection(ttk.Combobox):
    """A dropbown box located in the top-right corner used for multiple users."""
    def __init__(self, parent):
        self.current_user = StringVar()
        ttk.Combobox.__init__(self, parent, justify=CENTER, width=11, textvariable=self.current_user)
        self.grid(row=0, column=1, sticky='NES', pady=7)
        self.parent = parent

        self.option_values = file_helper.list_of_users() + [' ➕ New User ']
        self.last_user_index = 0

        self._initialize()

    def _bind_user_selection(self):
        self.bind('<<ComboboxSelected>>', self.change_user)

    def _initialize(self):
        self._bind_user_selection()
        self['values'] = self.option_values
        self.configure(state='readonly')  # user cannot modify the name

        self.current(0)  # first user is default

    def change_user(self, event=None):
        if self.current() is len(self.option_values) - 1:
            # User clicked the 'Add New User' option
            self.parent.request_tab_change(tab_index=2)
        else:
            self.last_user_index = self.current()
            print('Changed to', self.get().upper())
            self.parent.request_tab_change(tab_index=0)

        self.select_clear()  # clears the highlighted text

    def get_current_user(self):
        return self.current_user.get()

    def select_username(self, username=None):
        if username is not None:
            index = self.option_values.index(formatter.convert_to_capitalize(username))
        else:
            index = 0
        print('Selecting the UserSelection index of', index)

        self.current(index)
