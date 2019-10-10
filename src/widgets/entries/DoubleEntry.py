from src.widgets.entries.IntegerEntry import IntegerEntry


class DoubleEntry(IntegerEntry):
    def __init__(self, *args, **kwargs):
        IntegerEntry.__init__(self, *args, **kwargs)

        self.valid_chars += ['.']
