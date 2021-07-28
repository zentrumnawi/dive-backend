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


def format_ArrayField(field, choices, suffix="", separator=None, conjunction="bis"):
    field = get_ArrayField_display(field, choices)
    if suffix:
        field = [add_suffix(item, suffix, separator) for item in field]
    string = format_enumeration(field, conjunction)

    return string


def convert_decimal_separator(string):
    return string.replace(".", ",")


def remove_empty_decimal_places(string):
    if string:
        numbers = string.split("–", 1)
        if all(float(n).is_integer() for n in numbers):
            string = "–".join(n[: n.index(".")] for n in numbers)

    return string


def get_NumericPrefixTermField_display(field, choices):
    terms = dict(choices)
    if field:
        if field[0].isdigit():
            field = f"{field[0]}{terms[field[1:]]}"
        else:
            field = f"{terms[field]}"

    return field


def format_sentence(text):
    return f"{text[0].capitalize()}{text[1:]}." if text else ""


def format_FloatRangeTermCharField(field):
    string = ""
    if field:
        splited_field = field.split(" ", 1)
        splited_field[0] = remove_empty_decimal_places(splited_field[0])
        splited_field[0] = convert_decimal_separator(splited_field[0])
        string = " ".join(splited_field)

    return string


def format_subject_text(pre_subject_text, subject, post_subject_text, conjunction=" "):
    text = f"{pre_subject_text} {subject}" if pre_subject_text else ""
    text = f"{subject}" if not text and post_subject_text else text
    text = f"{text}{conjunction}{post_subject_text}" if post_subject_text else text

    return text
