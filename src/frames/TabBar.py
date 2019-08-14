from tkinter import *
from tkinter import ttk

from src import file_helper


class TabBar(ttk.Notebook):
    """Creates the Notebook's tabs located at the top-left corner.
    Allows the user to click a different tab."""
    def __init__(self, parent):
        self.parent = parent
        self._initialize_tab_bar_style()

        ttk.Notebook.__init__(self, parent)
        self.grid(row=0, column=0, sticky=NW, padx=10)

        self.tabs = []

        self._create_page_tab_widgets()

    def _initialize_tab_bar_style(self):
        # customizes the TabBar widget (exists behind the tabs)
        self.parent.style.configure("TNotebook",
                                    background=self.parent.color('Header_Bg'),
                                    tabmargins=[2, 5, 2, 0])

        # customizes the active tab
        self.parent.style.map("TNotebook.Tab",
                              background=[
                                  ("selected", self.parent.color('TabBar_Active_Bg'))
                              ],
                              foreground=[
                                  ("selected", self.parent.color('TabBar_Active_Fg'))
                              ],
                              expand=[
                                  ('selected', [3, 3, 3, 0])
                              ])

        # customizes the inactive tabs
        self.parent.style.configure('TNotebook.Tab',
                                    padding=[15, 6],
                                    background=self.parent.color('TabBar_Inactive_Bg'),
                                    foreground=self.parent.color('TabBar_Inactive_Fg'))

    def _bind_tab_bar_widget(self):
        self.bind('<ButtonRelease-1>', self.tab_clicked)

    def _create_page_tab_widgets(self):
        for p_index, curr_tab in enumerate(self.parent.tab_info):

            # creates 2 pages in the Notebook tabs
            self.tabs.append(ttk.Frame(self))
            if not curr_tab['hidden']:
                self.add(self.tabs[p_index], text=curr_tab['name'])

        self._bind_tab_bar_widget()

    def tab_clicked(self, event):
        if self.parent.current_page_number is 2 and not file_helper.list_of_users():
            print('Must create one user to continue')
            self.select(self.tabs[len(self.tabs) - 1])
            self.parent.frames['display_window'].adjust_focus()
            return

        page_tab_index = event.widget.index('current')

        # for attr in dir(self.pages[page_tab_index]):
        #     print(attr, '=>', getattr(self.pages[page_tab_index], attr))

        print('\nTab', page_tab_index, 'clicked')
        self.parent.change_page(page_tab_index)

        # for page in self.pages:
        #     print('Tab', page.winfo_rootx(), page.winfo_rooty())

    def reset_tabs(self):
        self.select(self.tabs[0])

    def show_hidden_tab(self):
        tab_index = self.parent.current_page_number
        curr_tab = self.parent.tab_info[tab_index]
        if curr_tab['hidden']:
            print('Displaying the hidden tab')
            self.add(self.tabs[tab_index], text=curr_tab['name'])
            self.select(self.tabs[tab_index])  # manually selects the new hidden tab

            # for attr in dir(event):
            #     print(attr, '=>', getattr(event, attr))
