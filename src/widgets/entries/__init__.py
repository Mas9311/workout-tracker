"""An import statement of 'from src.widgets.entries import *' will import the following classes.
These ttk.Entry widgets allow for validation of the typed character.
They all inherit from the root class, BaseEntryClass, which contains all relevant methods.
They only differ on the class variable, valid_chars.
 - Alpha only allows for [a-z | A-Z)
 - Integer only allows for [0-9]
 - Double only allows for [0-9 | '.'] (for decimals, like 2.71828)
 - BaseEntryClass does not allow for input of any kind!"""
from src.widgets.entries.AlphaIntSpaceEntry import AlphaIntSpaceEntry
from src.widgets.entries.IntegerEntry import IntegerEntry
from src.widgets.entries.DoubleEntry import DoubleEntry
