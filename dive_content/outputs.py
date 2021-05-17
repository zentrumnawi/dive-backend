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
