from tkinter import *
from tkinter import ttk


class TodayFrame(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.gui = self.parent.parent
        Frame.__init__(self, self.parent.frame, background=self.gui.color('Display_Bg'))
        self.grid(row=1, column=0)
        self.exercise_index = 1
        self.exercises = []

        self.__create_today_widgets()

    def __create_today_widgets(self):
        ttk.Frame(self, width=20, style='Display_Bg.TFrame').grid(row=0, column=0)
        self.create_exercise()
        self.create_exercise()
        Button(self).grid(row=10, column=1)

    def create_exercise(self):
        print(len(self.exercises), self.exercise_index)
        self.exercises.append(ExerciseFrame(self, self.exercise_index))
        self.exercise_index += 1


class ExerciseFrame(Frame):
    def __init__(self, parent, _row):
        self.parent = parent
        self.gui = self.parent.gui
        Frame.__init__(self, parent, background=self.gui.color('DisplayLabel_Bg'))
        self.grid(row=_row, column=1, pady=4)
        self._row = _row

        self.__create_exercise_widgets()

    def __create_exercise_widgets(self):
        label = ttk.Label(self, text=f'Test workout {self._row}', background=self.gui.color('DisplayLabel_Bg'))
        label.grid(row=0, column=0)
