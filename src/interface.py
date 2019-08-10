from tkinter import *
from src.frames.DisplayWindow import DisplayWindow
from src.frames.MenuBar import MenuBar
from src.frames.PageTabBar import PageTabBar
from src.frames.UserSelection import UserSelection


def run():
    arg_dict = {'interface': True}  # parameters.retrieve_parameters()
    if arg_dict['interface']:
        GUI(Tk(), arg_dict)
    else:
        CLI(arg_dict)


class CLI:
    def __init__(self, arg_dict):
        self.arg_dict = arg_dict


class GUI(Frame):
    def __init__(self, parent, arg_dict):
        Frame.__init__(self, parent)
        self.master.title('Workout Tracker')
        self.pack(fill=X, expand=False)
        self.root = parent
        self.root.resizable(False, False)

        self.arg_dict = arg_dict
        self.current_page_number = None
        self.tab_info = None
        self.frames = {}

        self._initialize_tab_info_dict()
        self._create_gui_widgets()
        self.root.mainloop()

    def _create_gui_widgets(self):
        self.frames['menu_bar'] = MenuBar(self)
        self.frames['page_tab_bar'] = PageTabBar(self)
        self.frames['user_selection'] = UserSelection(self)
        self.frames['display_window'] = DisplayWindow(self)

        self.change_page(0)  # initially display the first page

        self.resize_frame()

    def _initialize_tab_info_dict(self):
        # assigns each tab's name and label
        self.tab_info = [
            {
                'name': 'Progress',
                'label': 'Your Progress over Time'
            },
            {
                'name': 'Today',
                'label': 'Record Today\'s Workout'
            }
        ]

    def change_page(self, page_tab_index: int):
        if self.current_page_number is page_tab_index:
            # user clicked the same tab
            return

        self.current_page_number = page_tab_index

        self.frames['display_window'].change_tab()

    def get_current_user(self):
        return self.frames['user_selection'].get()

    def resize_frame(self):
        self.root.update_idletasks()
        self.root.geometry(f'{self.root.winfo_reqwidth()}x{self.root.winfo_reqheight()}')
