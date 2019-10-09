from src import *


class DisplayWindow(ttk.Labelframe):
    def __init__(self, parent):
        self.parent = parent
        self.__initialize_display_window_style()
        ttk.Labelframe.__init__(self, self.parent, text=' Initial Label of the Display Window ')
        self.grid(row=1, column=0, columnspan=2, sticky='nesw')

        self.display_area_label = None
        self.frame = None

        self._create_window_widgets()

    def __initialize_display_window_style(self):
        # creates a custom ttk.Frame "Padding Frame template" style
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

    def change_page_displayed(self):
        self.clear_display()

        self.frame = ttk.Frame(self, style='Display_Bg.TFrame')
        self.frame.grid(row=0, column=0, sticky='NESW')

        # creates a padding frame for row=0 with a height of 30 pixels
        ttk.Frame(self.frame, height=30, style='Display_Bg.TFrame').grid(row=0, column=0)

        if self.parent.curr_display['page']:
            # The current 'page' is initialized:
            # change the top-left label description
            self.change_display_label()
            # invoke the currently displayed 'page' Frame class.
            self.parent.curr_display['page'](self)

    def change_display_label(self):
        label_description = self.parent.display_info[self.parent.curr_display['page']]['label']
        self.configure(text=f' {label_description} ')

    def clear_display(self):
        if self.frame is not None:
            for widget in self.frame.winfo_children():
                if str(widget).count('label') is 0:
                    widget.forget()
                    widget.destroy()

    def reset_display(self):
        self.clear_display()
        self.change_page_displayed()
