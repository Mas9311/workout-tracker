from src import *


class MenuBar(Menu):
    def __init__(self, parent):
        self.parent = parent
        Menu.__init__(self, parent, background=self.parent.color('Menu_Inactive_Bg'),
                      foreground=self.parent.color('Menu_Inactive_Fg'), tearoff=False)

        file = Menu(self, tearoff=False)
        options = Menu(self, tearoff=False)

        self.add_cascade(label="File", activebackground=self.parent.color('Menu_Active_Bg'),
                         activeforeground=self.parent.color('Menu_Active_Fg'), menu=file)
        self.add_cascade(label="Options", activebackground=self.parent.color('Menu_Active_Bg'),
                         activeforeground=self.parent.color('Menu_Active_Fg'), menu=options)
        self.parent.root.config(menu=self)
