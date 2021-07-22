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

    def generate_leaf_base(obj):
        # Generate output "Blattgrund" according pattern:
        # "[base_edge] Blattgrund [[base_auricle_feature] base_auricle]."
        fields = [
            obj.get_base_edge_display(),
            obj.get_base_auricle_display(),
            obj.base_auricle_feature,
        ]
        if fields[0] == "behaart (< 3 mm)":
            fields[0] = "behaarter (< 3 mm)"
        else:
            fields[0] = add_suffix(fields[0], "er")
        if fields[1] == "mit Öhrchen" and fields[2]:
            splited_field = fields[1].split(" ", 1)
            fields[1] = f"{splited_field[0]} {fields[2]} {splited_field[1]}"

        text = format_subject_text(fields[0], "Blattgrund", fields[1])
        text = format_sentence(text)

        return text

    def generate_ligule(obj):
        # Generate output "Blatthäutchen" according pattern:
        # "[ligule_length]e, [ligule_color], [ligule_shape]e, [ligule_consistency]e,
        # Blatthäutchen. [ligule_features]"
        fields = [
            obj.get_ligule_length_display(),
            obj.ligule_color,
            obj.get_ligule_shape_display(),
            obj.get_ligule_consistency_display(),
            obj.ligule_features,
        ]
        fields[0] = add_suffix(fields[0], "e")
        fields[2] = add_suffix(fields[2], "e")
        fields[3] = add_suffix(fields[3], "e")
        joined_fields = ", ".join(filter(None, fields[0:4]))
        if fields[2] == "fehlende":
            joined_fields = "fehlende"

        texts = [
            format_subject_text(joined_fields, "Blatthäutchen", ""),
            fields[4],
        ]
        texts[0] = format_sentence(texts[0])
        joined_texts = " ".join(filter(None, texts))

        return joined_texts

    def generate_leaf_sheath(obj):
        # Generate output "Blattscheide" according pattern:
        # "[sheath_coloring], [sheath_connation]e Blattscheide. [sheath_features]"
        fields = [
            obj.sheath_coloring,
            obj.get_sheath_connation_display(),
            obj.sheath_features,
        ]
        fields[1] = add_suffix(fields[1], "e")
        joined_fields = ", ".join(filter(None, fields[0:2]))

        texts = [
            format_subject_text(joined_fields, "Blattscheide", ""),
            fields[2],
        ]
        texts[0] = format_sentence(texts[0])
        joined_texts = " ".join(filter(None, texts))

        return joined_texts


class BlossomPoalesOutput:
    def generate_season(obj):
        # Generate output "Blütezeit" according pattern:
        # "([season[0]]) [season[1]] bis [season[2] ([season[3]])."
        field = obj.season

        months = [None] * 4
        months = [f"{SEASON_DICT.get(month)}" for month in field] if field else months
        months[0] = f"({months[0]})" if months[0] else None
        months[3] = f"({months[3]})" if months[3] else None
        joined_months = [
            " ".join(filter(None, months[:2])),
            " ".join(filter(None, months[2:])),
        ]

        text = " bis ".join(filter(None, joined_months))
        text = format_sentence(text)

        return text
