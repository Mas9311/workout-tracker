from tkinter import *
from tkinter import ttk
from src import file_helper


class NewUserFrame(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.gui = self.parent.parent
        Frame.__init__(self, parent.frame, background=self.gui.color('Display_Bg'))
        self.grid(row=1, column=0)

        self.username = StringVar()

        self.__create_new_user_widgets()
        self.adjust_focus()

    def __create_new_user_widgets(self):
        self.left_pad = ttk.Frame(self, width=60, style='Display_Bg.TFrame')
        self.left_pad.grid(row=1, column=0)

        self.name_label = Label(self, height=1, text='Name:',
                                background=self.gui.color('DisplayLabel_Bg'),
                                foreground='#ffffff')
        self.name_label.grid(row=1, column=1, pady=10, ipady=3)

        self.name_entry = Entry(self, textvariable=self.username, width=25,
                                insertbackground='#123456',
                                background=self.gui.color('DisplayLabel_Bg'),
                                foreground='#ffffff')
        self.name_entry.grid(row=1, column=2, padx=5, pady=10, ipady=3)

        self.small_spacing = ttk.Frame(self, width=20, style='Display_Bg.TFrame')
        self.small_spacing.grid(row=1, column=3)

        self.create_button = Button(self, text='Create', command=self.create_button_clicked)
        self.create_button.grid(row=1, column=4)

    def adjust_focus(self):
        self.name_entry.focus()
        self.name_entry.icursor(END)

    def create_button_clicked(self):
        user_input = self.username.get().lower().strip()
        if not user_input:
            print('\nNot a valid username')
            return

        user_name = file_helper.convert_username_to_store(user_input)

        if file_helper.user_exists(user_name):
            print(user_name, 'folder already exists. Username must be unique')
        else:
            file_helper.create_new_user_folder(user_name)

        print('New user created:', self.username.get())
        print(f'User folder stored as ./data/users/{user_name}')

        self.gui.new_user_created(user_name)
