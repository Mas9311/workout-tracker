from tkinter import *
from tkinter import ttk


class PageTabBar(ttk.Notebook):
    """Creates the Notebook's tabs located at the top-left corner.
    Allows the user to click a different tab."""
    def __init__(self, parent):
        ttk.Notebook.__init__(self, parent)
        self.grid(row=0, column=0, sticky=NW, padx=10)
        self.parent = parent

        self.pages = []

        self._create_page_tab_widgets()

    def _bind_tabs(self):
        self.bind('<ButtonRelease-1>', self.page_tab_clicked)

    def _create_page_tab_widgets(self):
        for p_index, curr_tab in enumerate(self.parent.tab_info):

            # creates 2 pages in the Notebook tabs
            self.pages.append(ttk.Frame(self))
            if not curr_tab['hidden']:
                self.add(self.pages[p_index], text=curr_tab['name'])

        self._bind_tabs()

    def page_tab_clicked(self, event):
        page_tab_index = event.widget.index('current')
        print('Tab', page_tab_index, 'clicked')
        self.parent.change_page(page_tab_index)

        # for attr in dir(event):
        #     print(attr, '=>', getattr(event, attr))
