from tkinter import *
from tkinter import ttk

from src import file_helper


class TabBar(ttk.Notebook):
    """Creates the Notebook's tabs located at the top-left corner.
    Allows the user to select different tabs.
    Creates all Tabs created, but hidden Tabs are not initially displayed."""
    def __init__(self, parent):
        self.parent = parent
        self._initialize_tab_bar_style()

        ttk.Notebook.__init__(self, parent)
        self.grid(row=0, column=0, sticky=NW, padx=10)

        self.tabs = []

        self._create_page_tab_widgets()

    def _bind_tab_bar_widget(self):
        """Binds the left-click to TabBar's tab_clicked method"""
        self.bind('<ButtonRelease-1>', self.tab_clicked)

    def _create_page_tab_widgets(self):
        """Creates all tabs from parent, but only shows the non-hidden tabs"""
        for p_index, curr_tab in enumerate(self.parent.tab_info):
            # creates 3 tabs
            self.tabs.append(ttk.Frame(self))
            if not curr_tab['hidden']:
                # display 2 tabs
                self.add(self.tabs[p_index], text=curr_tab['name'])

        self._bind_tab_bar_widget()

    def _initialize_tab_bar_style(self):
        """Creates the style used for the Notebook (TabBar) and the Tabs"""
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

    def current_tab_index(self):
        """Returns the integer of the currently selected Tab"""
        return self.index(self.select())

    def manually_select(self, tab_index):
        """Manipulates the selection just as tab_clicked method's behavior """
        if self.current_tab_index() is not tab_index:
            print('Manually selecting tab #', tab_index)
            self.select(tab_index)

    def show_hidden_tab(self):
        """If the user activates a hidden tab to be displayed, display it in the TabBar.
        Manually selects the new hidden Tab."""
        tab_index = self.parent.current_page_number
        curr_tab = self.parent.tab_info[tab_index]
        if curr_tab['hidden']:
            print('Displaying the hidden tab')
            self.add(self.tabs[tab_index], text=curr_tab['name'])
            self.manually_select(tab_index)

            # for attr in dir(event):
            #     print(attr, '=>', getattr(event, attr))

    def tab_clicked(self, event):
        """The binded method for when the user clicks a Tab in the TabBar"""
        if self.parent.current_page_number is 2 and not file_helper.list_of_users():
            print('Must create one user to continue')
            self.manually_select(2)
            self.parent.adjust_focus()
            return

        tab_index = event.widget.index('current')

        print('\nTab', tab_index, 'clicked')
        self.parent.change_page(tab_index)
