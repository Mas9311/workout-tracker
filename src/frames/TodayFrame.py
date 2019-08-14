from tkinter import *
from tkinter import ttk


class TodayFrame(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.gui = self.parent.parent
        Frame.__init__(self, self.parent.frame, background=self.gui.color('Display_Bg'))
        self.grid(row=1, column=0)

        self.__create_today_widgets()

    def __create_today_widgets(self):
        ExerciseFrame(self)
        Button(self).grid(row=10, column=0)


class ExerciseFrame(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.gui = self.parent.gui
        Frame.__init__(self, parent, background=self.gui.color('DisplayLabel_Bg'))
        self.grid(row=0, column=0)

        self.__create_exercise_widgets()

    def __create_exercise_widgets(self):
        label = ttk.Label(self, text='workout', background=self.gui.color('DisplayLabel_Bg'))
        label.grid(row=0, column=0)
        label = ttk.Label(self, text='workout')
        label.grid(row=0, column=1)
        label = ttk.Label(self, text='workout')
        label.grid(row=0, column=2)
        label = ttk.Label(self, text='workout')
        label.grid(row=0, column=3)
