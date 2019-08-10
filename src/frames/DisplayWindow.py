from tkinter import *
from tkinter import ttk


class DisplayWindow(ttk.Labelframe):
    def __init__(self, parent):
        ttk.Labelframe.__init__(self, parent, text=' Initial Label of the Display Window ')
        self.grid(row=1, column=0, columnspan=2, sticky=NW)
        self.parent = parent

        self.display_area_label = None

        self._create_window_widgets()

    def _create_window_widgets(self):
        self._create_label()

    def _create_label(self):
        self.display_area_label = Label(self, text="", height=30, width=60)
        self.display_area_label.grid(column=0, row=0)

    def change_tab(self):
        self.change_display_label()

        if self.parent.current_page_number is 0:
            self.display_progress_window()
        elif self.parent.current_page_number is 1:
            self.display_today_window()

    def change_display_label(self):
        label_description = self.parent.tab_info[self.parent.current_page_number]['label']
        self.configure(text=f' {label_description} ')

    def display_progress_window(self):
        print('Displaying Progress page')

    def display_today_window(self):
        print('Displaying Today page')
