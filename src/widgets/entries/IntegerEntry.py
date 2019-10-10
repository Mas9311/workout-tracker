from src.widgets.entries.BaseEntryClass import BaseEntryClass


class IntegerEntry(BaseEntryClass):
    def __init__(self, *args, **kwargs):
        BaseEntryClass.__init__(self, *args, **kwargs)

        self.valid_chars += [('0', '9')]
