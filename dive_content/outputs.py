from .choices import *


def add_suffix(term, suffix, separators=None):
    if term:
        if isinstance(separators, str):
            separators = (separators,)
        if separators:
            if not any(separator in term for separator in separators):
                term = f"{term}{suffix}"
            else:
                i = 0
                terms = [term]
                while i < len(separators):
                    sublist = []
                    for j in range(0, len(terms)):
                        sublist.append(terms[j].split(separators[i]))
                    terms = [y for x in sublist for y in x]
                    i += 1
                terms = set(terms)
                for z in terms:
                    term = term.replace(z, f"{z}{suffix}")
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


class PlantOutput:
    def generate_general(obj):
        # Generate output "Allgemeines" according pattern:
        # "[article] [trivial_name] ([name]), auch [alternative_trivial_names] genannt,
        # ist ein/e [growth_form] mit einer Wuchshöhe von [growth_height]. Es handelt
        # sich um eine/n [interaction]e/en [dispersal_form], welche/r auf [ground]em
        # Untergrund in/an/auf [habitats]n sowie an Ruderalstandorten ([ruderal_sites]n)
        # vorkommt. Die Pflanze ist ein [life_form] und gilt als [status].
        # [other_features]
        def adapt_grammar_add_n(words, condition):
            for i, word in enumerate(words):
                if word[-1] in condition:
                    words[i] = f"{word}n"

        fields = [
            obj.article,
            obj.trivial_name,
            obj.name,
            obj.alternative_trivial_names,
            obj.get_growth_form_display(),
            obj.growth_height,
            obj.get_interaction_display(),
            obj.get_dispersal_form_display(),
            obj.get_ground_display(),
            obj.habitats,
            obj.ruderal_sites,
            obj.get_life_form_display(),
            obj.get_status_display(),
            obj.other_features,
        ]
        fields[3] = format_enumeration(fields[3], "oder")
        fields[5] = format_FloatRangeTermCharField(fields[5])
        if fields[7] == "Sporenpflanze":
            article, suffix, relative_pronoun = "eine", "e", "welche"
        else:
            article, suffix, relative_pronoun = "einen", "en", "welcher"
        fields[6] = add_suffix(fields[6], suffix)
        fields[8] = add_suffix(fields[8], "em", (", ", " und ", " bis "))
        if fields[9]:
            sublists = [[]] * 3
            for i, sublist in enumerate(HABITATS_SUBCHOICES):
                sublists[i] = list(filter(lambda x: x in dict(sublist), fields[9]))
                sublists[i] = get_ArrayField_display(sublists[i], HABITATS_CHOICES)
                adapt_grammar_add_n(sublists[i], ("e", "l", "r"))
            fields[9] = sublists
        else:
            fields[9] = [[]] * 3
        fields[10] = get_ArrayField_display(fields[10], RUDERAL_SITES_CHOICES)
        if fields[10]:
            adapt_grammar_add_n(fields[10], ("e", "r"))
        joined_fields = [
            " ".join(filter(None, fields[0:3])),
            " ".join(filter(None, fields[6:8])),
        ]

        text_parts = [
            f" {'' if fields[4] or fields[5] else 'wird '}auch {fields[3]} genannt"
            if fields[3]
            else "",
            f" ist {'eine' if fields[4] in (items[1] for items in GROWTH_FORM_SUBCHOICES[1]) else 'ein'} {fields[4]}"
            if fields[4]
            else "",
            f" {'mit einer' if fields[4] else 'hat eine'} Wuchshöhe von {'' if '–' in fields[5] else 'bis zu '}{fields[5]}"
            if fields[5]
            else "",
            f"Es handelt sich um {article} {joined_fields[1]}"
            if joined_fields[1]
            else "",
            f"auf {fields[8]} Untergrund" if fields[8] else "",
            format_enumeration(
                list(
                    filter(
                        None,
                        (
                            f"an {format_enumeration(fields[9][0])}"
                            if fields[9][0]
                            else "",
                            f"in {format_enumeration(fields[9][1])}"
                            if fields[9][1]
                            else "",
                            f"auf {format_enumeration(fields[9][2])}"
                            if fields[9][2]
                            else "",
                        ),
                    )
                )
            ),
            f"{'sowie ' if any(fields[9]) else ''}an Ruderalstandorten ({', '.join(fields[10])})"
            if fields[10]
            else "",
            f"ist ein {fields[11]}" if fields[11] else "",
            f"gilt als {fields[12]}" if fields[12] else "",
        ]
        if text_parts[0] and (text_parts[1] or text_parts[2]):
            text_parts[0] = f",{text_parts[0]},"

        joined_text_parts = [
            " ".join(filter(None, text_parts[4:7])),
            " und ".join(filter(None, text_parts[7:])),
        ]
        if joined_text_parts[0]:
            joined_text_parts[0] = f"{relative_pronoun} {joined_text_parts[0]} vorkommt"

        texts = [
            "".join(filter(None, [joined_fields[0]] + text_parts[0:3])),
            ", ".join(filter(None, [text_parts[3], joined_text_parts[0]])),
            f"Die Pflanze {joined_text_parts[1]}" if joined_text_parts[1] else "",
            fields[13],
        ]
        texts[0] = format_sentence(texts[0])
        texts[1] = format_sentence(texts[1])
        texts[2] = format_sentence(texts[2])
        joined_texts = " ".join(filter(None, texts))

        return joined_texts


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

    def generate_inflorescence(obj):
        # Generate output "Blütenstand" according pattern:
        # "[inflorescence_blossom_number]-blütige, [inflorescence_density]e,
        # [inflorescence_position]e [inflorescence_type] [inflorescence_features].
        # [inflorescence_bract_length] langes Tragblatt [inflorescence_bract_feature]."
        fields = [
            obj.inflorescence_blossom_number,
            obj.get_inflorescence_density_display(),
            obj.get_inflorescence_position_display(),
            obj.get_inflorescence_type_display(),
            obj.inflorescence_features,
            obj.inflorescence_bract_length,
            obj.inflorescence_bract_feature,
        ]
        fields[1] = add_suffix(fields[1], "e")
        fields[2] = add_suffix(fields[2], "e")
        fields[5] = format_FloatRangeTermCharField(fields[5])

        text_parts = [
            f"{fields[0]}-blütige" if fields[0] else "",
            f"{fields[5]} langes" if fields[5] else "",
        ]
        joined_text_parts = ", ".join(filter(None, [text_parts[0]] + fields[1:3]))

        texts = [
            format_subject_text(joined_text_parts, fields[3], fields[4]),
            format_subject_text(text_parts[1], "Tragblatt", fields[6]),
        ]
        texts[0] = format_sentence(texts[0])
        texts[1] = format_sentence(texts[1])
        joined_texts = " ".join(filter(None, texts))

        return joined_texts

    def generate_blossom_perianth(obj):
        # Generate output "Blüte und Blütenhülle" according pattern:
        # "[blossom_sex]e, [perianth]e Blüte [perianth]. [blossom_description]
        # [perianth_description]"
        fields = [
            obj.get_blossom_sex_display(),
            obj.get_perianth_display(),
            obj.blossom_description,
            obj.perianth_description,
        ]
        fields[0] = add_suffix(fields[0], "e", ", ")

        text_parts = [
            ", ".join(filter(None, [fields[0], "von Spelzen umgebene"]))
            if fields[1] == "Blüte von Spelzen umgeben"
            else fields[0],
            "",
            "",
        ]
        if fields[1] == "mit Blütenhülle":
            text_parts[1] = fields[1]
            text_parts[2] = fields[3]

        texts = [
            format_subject_text(text_parts[0], "Blüten", text_parts[1]),
            fields[2],
            text_parts[2],
        ]
        texts[0] = format_sentence(texts[0])
        joined_texts = " ".join(filter(None, texts))

        return joined_texts

    def generate_spikelet(obj):
        # Generate output "Ährchen" according pattern:
        # "[spikelet_length] lange, [spikelet_shape]e, [spikelet_attachment]e,
        # [spikelet_sex]e Ährchen mit [spikelet_blossom_number] Blüten; Breitenmaximum
        # [spikelet_max_width]; Ährchenachse [spikelet_rachilla]; Ährchenstiel
        # [spikelet_stalk]; Ährchenspindel [spikelet_spindle]. [spikelet_features]"
        fields = [
            obj.spikelet_length,
            obj.get_spikelet_shape_display(),
            obj.get_spikelet_attachment_display(),
            obj.get_spikelet_sex_display(),
            obj.spikelet_blossom_number,
            obj.get_spikelet_max_width_display(),
            obj.get_spikelet_rachilla_display(),
            obj.get_spikelet_stalk_display(),
            obj.get_spikelet_spindle_display(),
            obj.spikelet_features,
        ]
        fields[0] = format_FloatRangeTermCharField(fields[0])
        fields[1] = add_suffix(fields[1], "e")
        fields[2] = add_suffix(fields[2], "e")
        fields[3] = add_suffix(fields[3], "e")

        text_parts = [
            f"{fields[0]} lange" if fields[0] else "",
            f"mit {fields[4]} Blüten" if fields[4] else "",
            f"Breitenmaximum {fields[5]}" if fields[5] else "",
            f"Ährchenache {fields[6]}" if fields[6] else "",
            f"Ährchenstiel {fields[7]}" if fields[7] else "",
            f"Ährchenspindel {fields[8]}" if fields[8] else "",
        ]
        joined_text_parts = [
            ", ".join(filter(None, [text_parts[0]] + fields[1:4])),
            "; ".join(filter(None, text_parts[2:])),
        ]

        texts = [
            format_subject_text(joined_text_parts[0], "Ährchen", text_parts[1]),
            joined_text_parts[1],
            fields[9],
        ]
        texts[1] = format_sentence(texts[1])
        joined_texts = "; ".join(filter(None, texts[:2]))
        joined_texts = " ".join(filter(None, [joined_texts, texts[2]]))

        return joined_texts

    def generate_husks(obj):
        # Generate output "Spelzen" according pattern:
        # "[husks_form]e, [husks_keel]e Spelzen mit [husks_cross_section]em Querschnitt.
        # [husks_description]"
        fields = [
            obj.get_husks_form_display(),
            obj.get_husks_keel_display(),
            obj.husks_cross_section,
            obj.husks_description,
        ]
        fields[0] = add_suffix(fields[0], "e")
        fields[1] = add_suffix(fields[1], "e")
        fields[2] = format_ArrayField(fields[2], HUSKS_CROSS_SECTION_CHOICES, "em")

        text_parts = [
            ", ".join(filter(None, fields[0:2])),
            f"mit {fields[2]} Querschnitt" if fields[2] else "",
        ]

        texts = [
            format_subject_text(text_parts[0], "Spelzen", text_parts[1]),
            fields[3],
        ]
        texts[0] = format_sentence(texts[0])
        joined_texts = " ".join(filter(None, texts))

        return joined_texts


class StemRhizomePoalesOutput:
    def generate_growth_form(obj):
        # Generate output "Wuchsform" according pattern:
        # "Pflanze mit [tuft_stolon]."
        field = obj.tuft_stolon
        field = TUFT_STOLON_EDIT_DICT.get(field)

        text_part = f"mit {field}" if field else ""

        text = format_subject_text("", "Pflanze", text_part)
        text = format_sentence(text)

        return text

    def generate_stem(obj):
        # Generate output "Stängel" according pattern:
        # "[stem_color], [stem_hairiness]er, [stem_cross_section]er, [stem_pith]er
        # Stängel [[stem_nodes_hairiness]en, [stem_pith]en stem_nodes]; im Inneren
        # [stem_transverse_walls]; Oberfläche [stem_surface]. [stem_features]"
        fields = [
            obj.stem_color,
            obj.get_stem_hairiness_display(),
            obj.stem_cross_section,
            obj.get_stem_pith_display(),
            obj.get_stem_nodes_display(),
            obj.get_stem_nodes_hairiness_display(),
            obj.get_stem_transverse_walls_display(),
            obj.stem_surface,
            obj.stem_features,
        ]
        fields[1] = add_suffix(fields[1], "er")
        fields[2] = format_ArrayField(fields[2], STEM_CROSS_SECTION_CHOICES, "er")
        fields[3] = add_suffix(fields[3], "er")
        fields[5] = add_suffix(fields[5], "en")
        if fields[3] == "hohl; nur Knoten markiger":
            fields[3] = "hohler"
            fields[5] = ", ".join(filter(None, (fields[5], "markigen")))
        if fields[4] and fields[5]:
            splited_field = fields[4].split(" ", 1)
            fields[4] = f"{splited_field[0]} {fields[5]} {splited_field[1]}"
        if fields[7]:
            splited_field = fields[7].split(" ", 1)
            splited_field[-1] = f"{STEM_SURFACE_DICT.get(splited_field[-1])}"
            if len(splited_field) == 1:
                fields[7] = splited_field[0]
            else:
                fields[7] = f"{splited_field[0]}-fach {splited_field[1]}"
        joined_fields = ", ".join(filter(None, fields[0:4]))

        text_parts = [
            format_subject_text(joined_fields, "Stängel", fields[4]),
            f"im Inneren {fields[6]}" if fields[6] else "",
            f"Oberfläche {fields[7]}" if fields[7] else "",
        ]
        joined_text_parts = "; ".join(filter(None, text_parts))

        texts = [
            format_sentence(joined_text_parts),
            fields[8],
        ]
        joined_texts = " ".join(filter(None, texts))

        return joined_texts

    def generate_rhizome(obj):
        # Generate output "Rhizom" according pattern:
        # "[rhizome_length]es, [rhizome_branching]es Rhizom."
        fields = [
            obj.get_rhizome_length_display(),
            obj.get_rhizome_branching_display(),
        ]
        fields[0] = add_suffix(fields[0], "es")
        fields[1] = add_suffix(fields[1], "es")
        joined_fields = ", ".join(filter(None, fields))

        text = format_subject_text(joined_fields, "Rhizom", "")
        text = format_sentence(text)

        return text


class InterestingFactsOutput:
    def generate_pollination(obj):
        # Generate output "Bestäubung" according pattern:
        # "[pollination ([insects])]."
        fields = [
            obj.pollination,
            obj.insects,
        ]
        if fields[0]:
            fields[0] = get_ArrayField_display(fields[0], POLLINATION_CHOICES)
            if POLLINATION_CHOICES[0][1] in fields[0] and fields[1]:
                fields[0][0] = f"{fields[0][0]} ({fields[1]})"

        text = format_enumeration(fields[0])
        text = format_sentence(text)

        return text

    def generate_dispersal(obj):
        # Generate output "Ausbreitung" according pattern:
        # "[dispersal]."
        field = obj.dispersal

        text = format_ArrayField(field, DISPERSAL_CHOICES, conjunction="und")
        text = format_sentence(text)

        return text
