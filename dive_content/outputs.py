from .choices import *


def add_suffix(term, suffix, separator=None):
    if term:
        if separator:
            splited_term = term.split(separator)
            for i, st in enumerate(splited_term):
                splited_term[i] = f"{st}{suffix}"
            term = separator.join(splited_term)
        else:
            term = f"{term}{suffix}"

    return term


def get_ArrayField_display(field, choices):
    return [f"{dict(choices).get(f)}" for f in field]


def format_enumeration(enumeration, conjunction="und"):
    number = len(enumeration)
    string = ""
    if number == 1:
        string = enumeration[0]
    elif number == 2:
        string = f"{enumeration[0]} {conjunction} {enumeration[1]}"
    elif number > 2:
        string = f"{', '.join(enumeration[:-1])} {conjunction} {enumeration[-1]}"

    return string
