import re


def convert_to_capitalize(input_str, all_words=True):
    """This function is called when displaying a string to the user.
    Takes a string containing [0, many] spaces, strips extra spaces between words, and capitalizes the first letter.
    When all_words is set to False, only capitalizes the first word. Subsequent words are all lowercase.
    Ex:
        ' my   name is:  ', False   =>  'My name is:'
        'mike smith'                =>  'Mike Smith'
    Note: when writing to file, all characters should be/are assumed to be lowercase."""
    output_list = []
    data = re.split('[_ ]', input_str.strip().lower())

    for index, word in enumerate(data):
        word = word.strip()
        if word:
            # if the word has any remaining characters after stripping whitespace
            if index is 0 or all_words:
                # First word is capitalized regardless. Subsequent word are only capitalized if all_words is set to True
                new_word = word[0].upper()  # capitalize the first character
                if len(word) > 1:
                    # if the current word is longer than one character
                    new_word += word[1:]    # lowercase letters
            else:
                new_word = word
            output_list.append(new_word)

    output_str = ' '.join(output_list)
    return output_str


def convert_to_underscore(input_str):
    """This function is called when writing a string to file.
    Takes a string containing [0, many] spaces, strips extra spaces between words, and places underscores between words.
    Ex:
        'Mike Smith'    =>  'mike_smith'
        'Push Ups'      =>  'push_ups'
    """
    output_list = []
    data = re.split('[_ ]', input_str.lower())

    for word in data:
        word = word.strip()
        if word:
            # if the word has any remaining characters after stripping whitespace
            output_list.append(word)

    output_str = '_'.join(output_list)
    return output_str
