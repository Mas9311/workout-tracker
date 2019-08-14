from tkinter import *
from tkinter import ttk

from src.frames.NewUserFrame import NewUserFrame
from src.frames.TodayFrame import TodayFrame


class DisplayWindow(ttk.Labelframe):
    def __init__(self, parent):
        self.parent = parent
        self.__initialize_display_window_style()
        ttk.Labelframe.__init__(self, self.parent, text=' Initial Label of the Display Window ')
        self.grid(row=1, column=0, columnspan=2, sticky=N+E+S+W)

        self.display_area_label = None
        self.frame = None
        self.current_page = None

        self._create_window_widgets()

    def __initialize_display_window_style(self):
        # creates the Padding ttk.Frame style
        self.parent.style.configure('Display_Bg.TFrame',
                                    background=self.parent.color('Display_Bg'))

        # customizes the DisplayWindow widget
        self.parent.style.configure('TLabelframe',
                                    background=self.parent.color('Display_Bg'),
                                    borderwidth=3)

    def _create_window_widgets(self):
        self._create_label()

    def _create_label(self):
        self.display_area_label = Label(self, height=30, width=60)
        self.display_area_label.grid(column=0, row=0)

    def adjust_focus(self):
        self.current_page.adjust_focus()

    def change_tab(self):
        self.change_display_label()
        self.clear_display()

        self.frame = ttk.Frame(self, style='Display_Bg.TFrame')
        self.frame.grid(row=0, column=0, sticky='NESW')

        # add a 'spacer' frame at the top
        spacer = ttk.Frame(self.frame, height=30, style='Display_Bg.TFrame')
        spacer.grid(row=0, column=0)

        if self.parent.current_page_number is 0:
            self.display_today_page()
        elif self.parent.current_page_number is 1:
            self.display_progress_page()
        elif self.parent.current_page_number is 2:
            self.display_new_user_page()

    def change_display_label(self):
        label_description = self.parent.tab_info[self.parent.current_page_number]['label']
        self.configure(text=f' {label_description} ')

    def clear_display(self):
        if self.frame is not None:
            for widget in self.frame.winfo_children():
                if str(widget).count('label') is 0:
                    widget.forget()
                    widget.destroy()

    def display_today_page(self):
        self.current_page = TodayFrame(self)

    def display_progress_page(self):
        print('Displaying Progress page')

    def display_new_user_page(self):
        self.current_page = NewUserFrame(self)

    def reset_display(self):
        self.clear_display()
        self.change_tab()

