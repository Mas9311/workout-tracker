from src import *


class BaseEntryClass(ttk.Entry):
    """This is the base class for other ttk.Entry widgets to inherit from.
    Below, I explain how to pass args and kwargs.
    Allows flexibility, but tkinter style is preferred (first option listed).

    Must be passed its parent as:
     - the first arg (Much like every widget)
     - in the kwargs that explicitly sets parent. Ex: 'parent=self'
    The ttk.Entry's textvariable can be either:
     - Passed it's StringVar in kwargs as (so the higher level can keep it's StringVar local).
     - Else, BaseEntryClass creates an organic str_var"""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kw_args = kwargs
        self.__configure_kwargs()

        ttk.Entry.__init__(self, self.parent, **kwargs)

        # all inherited classes must assign values to valid_chars.
        # i.e.: DoubleEntry.valid_chars = [('0', '9'), '.']
        self.valid_chars = []

        self.__bind_entry()

    def __configure_kwargs(self):
        self.__assign_parent()

        # functional parameters
        self.__assign_textvariable()
        self.__assign_validate()
        self.__assign_validatecommand()

        # cosmetic parameters
        self.__assign_style()
        self.__assign_width()

    def __assign_parent(self):
        """This method """
        if self.args:
            # if args has a length, parent is the first passed argument.
            self.parent = self.args[0]
        elif 'parent' in self.kw_args:
            # else, parent is passed explicitly.
            self.parent = self.kw_args['parent']
            del self.kw_args['parent']  # 'parent=self' doesn't *actually* belong in kwargs
        else:
            print('Quit:', self.__class__.__name__, 'has no parent!')
        self.gui = self.parent.gui

    def __assign_textvariable(self):
        """This method manually manages the StringVar that the ttk.Entry widget uses to save the entry to.
        'textvariable' can passed though kwargs, or one will be created locally.
        Either way, the BaseEntryClass will have a variable to reference to: self.str_var."""
        if 'textvariable' in self.kw_args:
            # If the StringVar instance was passed in through kwargs (dict):
            # assign the class variable, string_var, to point at the instance.
            self.string_var = self.kw_args['textvariable']
        else:
            # else, the inherited class does not wish to keep a variable:
            # instantiate the class variable, string_var.
            self.string_var = StringVar()

        # Now that we manually managed the StringVar instance, assign it to the kwargs (dict),
        # which will emulate: ttk.Entry.__init__(..., textvariable=self.string_var, ...)
        self.kw_args['textvariable'] = self.string_var

    def __assign_validate(self, option='key'):
        """If the validate='' option was not passed in **kwargs,
        assign it to 'key' (press, not release).
        All possible validate options are ['none', 'key', 'focus', 'focusin', 'focusout', 'all']
        The only options that will be permitted are ['key', 'all']:
         - 'key' : entry char is validated prior to being displayed in the Entry box.
         - 'all' : validation is performed for all possible values, but is not necessary.
         - all other options will default to 'all' option. Why else would it be customized?"""
        if 'validate' not in self.kw_args:
            self.kw_args['validate'] = option
        elif self.kw_args['validate'] in ['none', 'focus', 'focusin', 'focusout']:
            self.kw_args['validate'] = 'all'

    def __assign_validatecommand(self):
        """This function should not be overridden by classes that inherit.
        All possible ttk.Entry "percent substitutions" are passed to the self._validate_command method.
        These are ordered from most important to least important:
        %d: action type. 1==insert a char, 0==delete 1+ char(s), -1==entry [focus | focusin | focusout]
        %S: the char to be inserted/deleted (or -1 for focus).
        %i: the index of the char to be inserted/deleted (or -1 for focus).
        %v: the current value of the -validate option.
        %s: the "before" value of the textvariable, StringVar, prior to editing.
        %P: the "after" value of the textvariable (if validatecommand returns True).
        %W: the tk widget name. Ex: .!gui.!displaywindow.!frame3.!newuserpage
        %V: the validation condition that triggered the callback (key, focusin, focusout, or forced)."""
        if 'validatecommand' not in self.kw_args:
            v_cmd = (self.parent.register(self._validate_command),
                     '%d', '%S', '%i', '%v', '%s', '%P', '%W', '%V')
            self.kw_args['validatecommand'] = v_cmd

    def __assign_style(self, style='Base.TEntry'):
        if 'style' not in self.kw_args:
            self.kw_args['style'] = style

    def __assign_width(self, width=25):
        if 'width' not in self.kw_args:
            self.kw_args['width'] = width

    def __bind_entry(self):
        self.bind('<Button-1>', self._click_focus)
        # self.bind('<<Copy>>', lambda *e: 'break')  # User should be allowed to copy at the very least
        self.bind('<<Cut>>', lambda *e: 'break')
        self.bind('<<Paste>>', lambda *e: 'break')
        self.bind('<<Clear>>', lambda *e: 'break')

    def _click_focus(self, event):
        self.focus_force()
        self.icursor(END)

    def _validate_command(self, action_type, char_typed,
                          index, before, after,
                          tk_w_name, condition, val_option):
        if action_type == '1':
            # User typed a single character: before + char == after
            return self._validate_insertion(char_typed)
        # elif action_type is '0':
        #     # User deleted a single character: before - char == after
        #     # TODO: self.validate_deletion(char_typed)?
        # elif action_type is '-1':
        #     # changed focus focused
        #     # TODO: self.validate_revalidate(char_typed)?
        return True

    def _validate_insertion(self, char_typed):
        if self.valid_chars:
            for curr_valid in self.valid_chars:
                if isinstance(curr_valid, tuple):
                    # if curr_valid is a range. i.e.: ('0', '9') | ('a', 'z') | ('A', 'Z')
                    if curr_valid[0] <= char_typed <= curr_valid[1]:
                        # char lies within valid range
                        return True
                elif isinstance(curr_valid, str):
                    # else curr_valid is a single character. i.e.: '.' | ' '
                    if char_typed == curr_valid:
                        # char matches the valid character
                        return True
                else:
                    print(curr_valid, 'is not in the correct format.\n'
                                      'Correct formats include: (min_char, max_char) tuple or a single char.\n'
                                      '\ti.e.: (\'0\', \'9\') or \'.\'')
                # continue checking the rest of the elements in the self.valid_chars list

        # char did not pass any validity checks || is a meta key, ∴ char is invalid
        print(f'  - Invalid: Failed to insert char: \'{char_typed}\'.\n\tValid characters: {self.valid_chars}.')
        return False

    def get_value(self):
        """Redundant method to retrieve the StringVar's string."""
        return self.string_var.get()

    def get_string_var(self):
        """In case we want an instance of the textvariable (StringVar type) elsewhere."""
        return self.string_var
