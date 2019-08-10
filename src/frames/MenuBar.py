from tkinter import *


class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent, tearoff=False)
        self.parent = parent

        file = Menu(self, tearoff=False)
        options = Menu(self, tearoff=False)

        self.add_cascade(label="File", menu=file)
        self.add_cascade(label="Options", menu=options)
        self.parent.root.config(menu=self)
