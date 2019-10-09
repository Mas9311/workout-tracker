from src import *
from src import file_helper


class TabBar(ttk.Notebook):
    """Creates the Notebook's tabs located at the top-left corner.
    Allows the user to select different tabs.
    Creates all Tabs created, but hidden Tabs are not initially displayed."""
    def __init__(self, parent):
        self.parent = parent
        self._initialize_tab_bar_style()

        ttk.Notebook.__init__(self, parent)
        self.enable_traversal()
        self.grid(row=0, column=0, sticky=NW, padx=10)

        self._create_page_tab_widgets()

    def _create_page_tab_widgets(self):
        """Creates all tabs from parent, but only shows the non-hidden tabs"""
        for frame in self.parent.display_info.keys():
            curr_display = self.parent.display_info[frame]
            curr_state = ('normal', 'hidden')[curr_display['hidden']]
            self.add(ttk.Frame(self), text=curr_display['name'], state=curr_state)

        # self._bind_tab_bar_widget()

    def _initialize_tab_bar_style(self):
        """Creates the style used for the Notebook (TabBar) and the Tabs"""
        # print("TNotebook :".format(self.parent.style('TNotebook.Tab')))
        # customizes the TabBar widget (exists behind the tabs)
        self.parent.style.configure("TNotebook",
                                    background=self.parent.color('Gui_Bg'),
                                    borderwidth=0,
                                    tabmargins=[2, 5, 2, 0])

        # customizes the active tab
        self.parent.style.map("TNotebook.Tab",
                              background=[
                                  ('selected', self.parent.color('TabBar_Active_Bg')),
                                  ('active', self.parent.color('TabBar_Inactive_Bg')),
                              ],
                              foreground=[
                                  ('selected', self.parent.color('TabBar_Active_Fg')),
                                  ('active', self.parent.color('TabBar_Inactive_Fg'))
                              ],
                              expand=[
                                  ('selected', [3, 3, 3, 0])
                              ],
                              focuscolor=[
                                  ('selected', self.parent.color('TabBar_Active_Bg')),
                              ])

        # customizes the inactive tabs
        self.parent.style.configure('TNotebook.Tab',
                                    background=self.parent.color('TabBar_Inactive_Bg'),
                                    foreground=self.parent.color('TabBar_Inactive_Fg'),
                                    padding=[15, 6],
                                    borderwidth=1)

    def current_tab_index(self):
        """Returns the integer of the currently selected Tab"""
        print(self.select())
        return self.index(self.select())

    def override_select(self, tab_index=None):
        """Manipulates the selection to emulate <<NotebookTabChanged>> virtual event"""
        if self.current_tab_index() is not tab_index:
            print('Manually selecting tab #', tab_index)
            self.show_tab()
            self.select(tab_index)

    # def tab_clicked(self, event):
    #     """The binded method for when the user clicks a Tab in the TabBar"""
    #     if self.parent.page_tab_index is 2 and not file_helper.list_of_users():
    #         print('Must create one user to continue')
    #         self.override_select(2)
    #         # self.parent.adjust_focus()
    #         return
    #
    #     tab_index = event.widget.index('current')
    #
    #     print('\nTab', tab_index, 'clicked')
    #     self.parent.change_page(tab_index)

    def disable_tabs(self, active_index):
        # disable all displayed tabs, and force the tab at active_index to be selected
        for curr_index, curr_info in enumerate(self.parent.display_info.values()):
            if curr_index is not active_index:
                if not curr_info['hidden']:
                    self.tab(curr_index, state='disabled')
        self.show_tab()
        self.select(active_index)

    def hide_tab(self, index=None):
        if self.parent.curr_display['tab'] is None:
            return
        elif index is None:
            # if no index is provided, retrieve the currently displayed tab index
            index = self.parent.curr_display['tab']

        if self.parent.display_info[self.parent.convert_index_to_key(index)]['hidden']:
            # if it is suppose to be hidden, hide it
            self.tab(index, state='hidden')

    def show_tab(self):
        """Updates a currently displayed tab's state to be visible."""
        self.tab(self.parent.curr_display['tab'], state='normal')

    def reset(self):
        for curr_tab_index in range(len(self.parent.display_info.keys())):
            self.hide_tab(curr_tab_index)
