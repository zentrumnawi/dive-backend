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


class LeafPoalesOutput:
    def generate_overview(obj):
        # Generate output "Überblick" according pattern:
        # "[length] lange, [width] breite, [color], [shape]e, [hairiness]e,
        # streifennervige Blätter mit [cross_section]em Querschnitt. Blätter sitzen
        # [alignment] an [attachment_point]."
        fields = [
            obj.length,
            obj.width,
            obj.color,
            obj.get_shape_display(),
            obj.hairiness,
            obj.cross_section,
            obj.alignment,
            obj.get_attachment_point_display(),
        ]
        fields[0] = format_FloatRangeTermCharField(fields[0])
        fields[3] = add_suffix(fields[3], "e")
        fields[4] = format_ArrayField(fields[4], HAIRINESS_CHOICES, "e")
        fields[5] = format_ArrayField(fields[5], LEAFPOALES_CROSS_SECTION_CHOICES, "em")
        fields[6] = get_NumericPrefixTermField_display(fields[6], ALIGNMENT_CHOICES)

        text_parts = [
            f"{fields[0]} lange" if fields[0] else "",
            f"{fields[1]} breite" if fields[1] else "",
            f"mit {fields[5]} Querschnitt" if fields[5] else "",
            f"an {fields[7]}" if fields[7] else "",
        ]
        joined_text_parts = [
            ", ".join(filter(None, text_parts[:2] + fields[2:5])),
            " ".join(filter(None, [fields[6], text_parts[3]])),
        ]
        joined_text_parts[0] += "," if joined_text_parts[0] else ""

        texts = [
            format_subject_text(
                joined_text_parts[0], "streifennervige Blätter", text_parts[2]
            ),
            format_subject_text("", "Blätter", joined_text_parts[1], " sitzen "),
        ]
        texts[0] = format_sentence(texts[0])
        texts[1] = format_sentence(texts[1])
        joined_texts = " ".join(filter(None, texts))

        return joined_texts

    def generate_leaf_blade(obj):
        # Generate output "Blattspreite" according pattern:
        # "[blade_shape]e Spreite [blade_shape_feature]; Oberseite [blade_corrugation],
        # [blade_double_groove]; Unterseite [blade_shine], [blade_keel]; Blattrand
        # [blade_edge]; Knospenanlage [blade_bud_system]."
        fields = [
            obj.get_blade_shape_display(),
            obj.blade_shape_feature,
            obj.blade_corrugation,
            obj.get_blade_double_groove_display(),
            obj.get_blade_shine_display(),
            obj.get_blade_keel_display(),
            obj.get_blade_edge_display(),
            obj.get_blade_bud_system_display(),
        ]
        fields[0] = add_suffix(fields[0], "e")
        fields[2] = format_ArrayField(fields[2], BLADE_CORRUGATION_CHOICES)
        joined_fields = [
            ", ".join(filter(None, fields[2:4])),
            ", ".join(filter(None, fields[4:6])),
        ]

        text_parts = [
            format_subject_text(fields[0], "Spreite", fields[1]),
            f"Oberseite {joined_fields[0]}" if joined_fields[0] else "",
            f"Unterseite {joined_fields[1]}" if joined_fields[1] else "",
            f"Blattrand {fields[6]}" if fields[6] else "",
            f"Knospenanlage {fields[7]}" if fields[7] else "",
        ]

        text = "; ".join(filter(None, text_parts))
        text = format_sentence(text)

        return text
