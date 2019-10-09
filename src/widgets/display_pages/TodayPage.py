from src import *
from src import file_helper, formatter
from src.widgets.display_pages.exercise.ExerciseFrame import ExerciseFrame


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
        self._create_exercise()
        Button(self, text='Save to file', command=self._save_to_file).grid(row=50, column=0)

    def _create_exercise(self):
        self.exercises.append(ExerciseFrame(self, self.exercise_index))
        self.exercise_index += 1

    def _save_to_file(self):
        self.gui.save_workout_to_file(self.exercises)

    def focus(self):
        self.exercises[-1].focus_force()
