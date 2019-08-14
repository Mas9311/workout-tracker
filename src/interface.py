from tkinter import *
from tkinter import ttk

from src import file_helper
from src.frames.DisplayWindow import DisplayWindow
from src.frames.MenuBar import MenuBar
from src.frames.TabBar import TabBar
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
        self.root = parent
        self.__initialize_colors()
        self.arg_dict = arg_dict
        self.appearance_mode = 'dark'  # TODO: customizable light mode/dark mode
        Frame.__init__(self, parent, background=self.color('header'))
        self.master.title('Workout Tracker')
        self.pack(expand=True, fill=BOTH)
        self.root.resizable(False, False)

        self.current_page_number = 1
        self.frames = {}
        self.style = ttk.Style()

        self.__initialize_tab_info()
        self.__create_gui_widgets()
        self.root.mainloop()

    def __initialize_colors(self):
        self.colors = {
            'dark': {
                'menu': {
                    'active': {
                        'bg': '114380',
                        'fg': 'ffffff'},
                    'inactive': {
                        'bg': '333333',
                        'fg': 'bbbbbb'}},
                'header': {
                    'bg': '7a00ff'},
                'display': {
                    'bg': '424242'},
                'displaylabel': {
                    'bg': '606060',
                    'fg': 'bbbbbb'
                },
                'tabbar': {
                    'active': {
                        'bg': '424242',
                        'fg': 'bbbbbb'
                    },
                    'inactive': {
                        'bg': '606060',
                        'fg': 'bbbbbb'
                    }
                }
            },
            # 'light': {
            #     'bg': self.root.cget("background"),  # '#d9d9d9' is the default color
            #     'active_bg': '#000000',
            #     'active_fg': '#111111',
            #     'inactive_bg': '#222222',
            #     'inactive_fg': '#333333',
            # },
            'default': self.root.cget("background")
        }

    def __create_gui_widgets(self):
        self.frames['menu_bar'] = MenuBar(self)
        self.reset_tab_bar()
        self.frames['display_window'] = DisplayWindow(self)
        self.frames['user_selection'] = UserSelection(self)
        if not file_helper.list_of_users():
            # if there are no created users, display the new user page
            self.change_page(2)
        else:
            self.reset_gui()  # initially display the first page

        self.resize_frame()

    def __initialize_tab_info(self):
        # assigns each tab's name and label
        self.tab_info = [
            {
                'name': 'Today',
                'label': 'Record Today\'s Workout',
                'hidden': False,
            },
            {
                'name': 'Progress',
                'label': 'Your Progress Over Time',
                'hidden': False,
            },
            {
                'name': 'New User',
                'label': 'Create a New User',
                'hidden': True,
            }
        ]

    def change_page(self, tab_index=0):
        print('Changing to Tab #', tab_index)
        if self.current_page_number is not None:
            if self.current_page_number is tab_index:
                # user clicked the same tab
                return

        if self.tab_info[self.current_page_number]['hidden']:
            if self.current_page_number is 2 and file_helper.list_of_users():
                self.reset_tab_bar(tab_index)
                self.reset_user_selection()

        self.current_page_number = tab_index

        self.frames['display_window'].change_tab()
        if self.tab_info[tab_index]['hidden']:
            # If the tab is hidden, display it
            self.frames['tab_bar'].show_hidden_tab()

    def color(self, area, state=None, layer=None):
        color = '#'

        if area.count('_') is 2:
            area, state, layer = area.split('_')
        elif area.count('_') is 1:
            area, state = area.split('_')

        area = area.lower()
        if state:
            state = state.lower()
        if layer:
            layer = layer.lower()

        if self.appearance_mode not in self.colors.keys():
            self.appearance_mode = 'dark'
        mode_dict = self.colors[self.appearance_mode]

        if area not in mode_dict.keys():
            print('Error:', area, 'is not a valid key in', self.appearance_mode)
            return self.colors['default']
        area_dict = mode_dict[area]
        if len(area_dict.keys()) is 1:
            key = list(area_dict.keys())[0]
            color += area_dict[key]
            return color

        if state not in area_dict.keys():
            print('Error:', state, 'is not a valid key in', self.appearance_mode, area)
            return self.colors['default']
        state_dict = area_dict[state]
        if isinstance(state_dict, dict) and len(state_dict) is 1:
            key = list(state_dict.keys())[0]
            color += state_dict[key]
            return color
        if isinstance(state_dict, str):
            color += state_dict
            return color

        if layer not in state_dict.keys():
            print('Error:', layer, 'is not a valid key in', self.appearance_mode, area, state)
            return self.colors['default']
        if len(state_dict) is 1:
            key = list(state_dict.keys())[0]
            color += state_dict[key]
            return color
        color += state_dict[layer]
        return color

    def get_current_user(self):
        return self.frames['user_selection'].get()

    def new_user_created(self, username=None):
        self.reset_user_selection(username)
        self.reset_gui()

    def reset_gui(self):
        self.current_page_number = 0

        self.reset_tab_bar()
        self.frames['display_window'].reset_display()

    def reset_user_selection(self, username=None):
        widget_key = 'user_selection'
        select_index = None
        if self.frames[widget_key].last_user_index:
            select_index = self.frames[widget_key].last_user_index

        if widget_key in self.frames.keys():
            self.frames[widget_key].grid_forget()
            self.frames[widget_key].destroy()

        self.frames[widget_key] = UserSelection(self)
        if select_index is None:
            self.frames[widget_key].select_username(username)
        else:
            self.frames[widget_key].current(select_index)

    def reset_tab_bar(self, tab_index=0):
        widget_key = 'tab_bar'
        if widget_key in self.frames.keys():
            self.frames[widget_key].grid_forget()
            self.frames[widget_key].destroy()

        self.frames[widget_key] = TabBar(self)
        self.frames[widget_key].select(tab_index)

    def resize_frame(self):
        self.root.update_idletasks()
        x = max(490, self.root.winfo_reqwidth())
        y = max(550, self.root.winfo_reqheight())
        self.root.geometry(f'{x}x{y}')
