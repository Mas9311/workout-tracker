from src.widgets.entries.BaseEntryClass import BaseEntryClass


class AlphaIntSpaceEntry(BaseEntryClass):
    def __init__(self, *args, **kwargs):
        BaseEntryClass.__init__(self, *args, **kwargs)

        self.valid_chars = [('a', 'z'), ('A', 'Z'), ('0', '9'), ' ']
