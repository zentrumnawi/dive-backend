from rest_framework import serializers
from solid_backend.photograph.serializers import PhotographSerializer

from .choices import *
from .models import Blossom, Fruit, Indicators, Leaf, Plant, StemRoot


class HumanReadableChoiceField(serializers.ChoiceField):
    def to_representation(self, value):
        if not value:
            return value
        return str(self.grouped_choices[value])


# -------------------------------------- LEGACY -------------------------------------- #
class ZeigerNumberField(serializers.Field):
    """
    This field is designed to be used as 'serializer_choice_field' in the ZeigerNumberSerializer.
    In this Serializer we have pairs of Fields <name>_number and <name>_extra where both fields
    have choices but are meant to be combined. Combination of the field values happens in 'to_representation'.
    """

    def __init__(self, choices, **kwargs):
        """
        Do neccessary init for a choice field
        :param choices:
        :param kwargs:
        """
        self.choices = choices
        super().__init__(**kwargs)

    def bind(self, field_name, parent):
        """
        Construct the extra_field name.
        :param field_name:
        :param parent:
        :return:
        """

        super(ZeigerNumberField, self).bind(field_name, parent)
        self.extra_field = "{}_extra".format(self.field_name.split("_")[0])

    def get_attribute(self, instance):
        return instance

    def to_representation(self, value):
        """
        Combine the <name>_number value with the <name>_extra value.
        :param value:
        :return:
        """
        field_value = getattr(value, self.field_name)
        extra_field_value = getattr(value, self.extra_field)
        if extra_field_value and field_value:
            field_value = f" {extra_field_value} - ".join(field_value.split(" - "))
        return field_value


# ------------------------------------------------------------------------------------ #


class DisplayNameModelSerializer(serializers.ModelSerializer):

    serializer_choice_field = HumanReadableChoiceField

    def to_representation(self, instance):
        ret = super(DisplayNameModelSerializer, self).to_representation(instance)

        return serializers.OrderedDict(filter(lambda x: not x[1] is None, ret.items()))


def concatenate(field, choices=None, app=""):
    output = ""
    if field:
        if choices:
            if isinstance(field, list):
                output = " bis ".join(f"{dict(choices).get(x)}{app}" for x in field)
            else:
                output = f"{dict(choices).get(field)}{app}"

            if app and ("/" in output):
                output = output.split("/")
                for i, x in enumerate(output[:-1]):
                    output[i] = f"{x}{app}"
                output = "/".join(output)
        else:
            output = f"{field}{app}"

    return output


def format_sentence(line):
    return f"{f'{line[0].capitalize()}{line[1:]}.' if line else ''}"


class LeafSerializer(DisplayNameModelSerializer):
    overview = serializers.SerializerMethodField(label="Überblick")
    attachment = serializers.SerializerMethodField(label="Anheftung")
    leaf_compound = serializers.SerializerMethodField(
        label="Blattfläche – zusammengesetztes Blatt"
    )
    leaf_simple = serializers.SerializerMethodField(
        label="Blattfläche – einfaches Blatt"
    )
    leaf_general = serializers.SerializerMethodField(label="Blattfläche – allgemein")
    miscellaneous = serializers.SerializerMethodField(label="Sonstiges")
    seed_leaf = serializers.SerializerMethodField(label="Keimblatt")

    class Meta:
        model = Leaf
        fields = [
            "overview",
            "attachment",
            "leaf_compound",
            "leaf_simple",
            "leaf_general",
            "miscellaneous",
            "seed_leaf",
        ]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_overview(self, obj):
        # Generate sentence "Überblick" according pattern:
        # "[color], [veins]e, [division]e, [succulence]e, [texture]e Blätter mit [cross_
        # section]em Querschnitt."
        fields = [
            obj.color,
            concatenate(obj.veins, VEINS_CHOICES, "e"),
            concatenate(obj.division, DIVISION_CHOICES, "e"),
            concatenate(obj.succulence, SUCCULENCE_CHOICES, "e"),
            concatenate(obj.texture, TEXTURE_CHOICES, "e"),
            concatenate(obj.cross_section, CROSS_SECTION_CHOICES, "em"),
        ]

        text = ", ".join(filter(None, fields[:5]))
        text = f"{text} Blätter" if text else ""
        text = f"{text} mit {fields[5]} Querschnitt" if fields[5] else f"{text}"
        text = f"Blätter{text}" if text[:4] == " mit" else f"{text}"

        return format_sentence(text)

    def get_attachment(self, obj):
        # Generate sentence "Anheftung" according pattern:
        # "Blätter sitzen [attachment], stehen [arrangement]; [rosette]."
        fields = [
            concatenate(obj.attachment, ATTACHMENT_CHOICES),
            concatenate(obj.arrangement, ARRANGMENT_CHOICES),
            concatenate(obj.rosette, ROSETTE_CHOICES),
        ]
        fields[0] = f"sitzen {fields[0]}" if fields[0] else ""
        fields[1] = f"stehen {fields[1]}" if fields[1] else ""

        text = ", ".join(filter(None, fields[:2]))
        text = f"Blätter {text}" if text else ""
        text = "; ".join(filter(None, (text, fields[2])))

        return format_sentence(text)

    def get_leaf_compound(self, obj):
        # Generate sentence "Blattfläche – zusammengesetztes Blatt" according pattern:
        # "[leaf_comp_num] [leaf_comp_blade_shape]es|e [leaf_comp_incision_num]-[leaf_
        # comp_incision_depth]es|e Blatt|Blätter mit [leaflet_incision_num]-[leaflet_
        # incision_add]-[leaflet_incision_depth]en Blättchen."
        app = {1: "e", 3: "e", 6: "en", 10: "Blätter"}
        if obj.leaf_comp_num == "1":
            app = {1: "es", 3: "es", 6: "en", 10: "Blatt"}

        fields = [
            obj.leaf_comp_num,
            concatenate(
                obj.leaf_comp_blade_shape, LEAF_COMP_BLADE_SHAPE_CHOICES, app[1]
            ),
            obj.leaf_comp_incision_num,
            concatenate(
                obj.leaf_comp_incision_depth, LEAF_COMP_INCISION_DEPTH_CHOICES, app[3]
            ),
            obj.leaflet_incision_num,
            obj.leaflet_incision_add,
            concatenate(
                obj.leaflet_incision_depth, LEAFLET_INCISION_DEPTH_CHOICES, app[6]
            ),
        ]
        for i in (2, 4, 5):
            fields[i] = f"{fields[i]}-" if fields[i] else ""
        if fields[2] and " bis " in fields[3]:
            fields[3] = fields[3].split(" bis ", 1)
            fields[3] = f"{fields[3][0]} bis -{fields[3][1]}"
        if (fields[4] or fields[5]) and " bis " in fields[6]:
            fields[6] = fields[6].split(" bis ", 1)
            fields[6] = f"{fields[6][0]} bis -{fields[6][1]}"

        text = [
            " ".join(filter(None, fields[:2])),
            "".join(filter(None, fields[2:4])),
        ]
        text = [
            " ".join(filter(None, text)),
            "".join(filter(None, fields[4:7])),
        ]
        text[0] = f"{text[0]} {app[10]}" if text[0] else ""
        text = f"{text[0]} mit {text[1]} Blättchen" if text[1] else f"{text[0]}"
        text = f"Blätter{text}" if text[:4] == " mit" else f"{text}"

        return format_sentence(text)

    def get_leaf_simple(self, obj):
        # Generate sentence "Blattfläche – einfaches Blatt" according pattern:
        # "[leaf_simple_num] [leaf_simple_blade_shape]es|e [leaf_simple_incision_num]-
        # [leaf_simple_incision_depth]es|e Blatt|Blätter."
        app = {1: "e", 3: "e", 10: "Blätter"}
        if obj.leaf_simple_num == "1":
            app = {1: "es", 3: "es", 10: "Blatt"}

        fields = [
            obj.leaf_simple_num,
            concatenate(
                obj.leaf_simple_blade_shape, LEAF_SIMPLE_BLADE_SHAPE_CHOICES, app[1]
            ),
            obj.leaf_simple_incision_num,
            concatenate(
                obj.leaf_simple_incision_depth,
                LEAF_SIMPLE_INCISION_DEPTH_CHOICES,
                app[3],
            ),
        ]
        fields[2] = f"{fields[2]}-" if fields[2] else ""
        if fields[2] and " bis " in fields[3]:
            fields[3] = fields[3].split(" bis ", 1)
            fields[3] = f"{fields[3][0]} bis -{fields[3][1]}"

        text = [
            " ".join(filter(None, fields[:2])),
            "".join(filter(None, fields[2:])),
        ]
        text = " ".join(filter(None, text))
        text = f"{text} {app[10]}" if text else ""

        return format_sentence(text)

    def get_leaf_general(self, obj):
        # Generate sentence "Blattfläche – allgemein" according pattern:
        # "Blattränder [edge]; [surface] Blattoberfläche; [stipule_edge]
        # Nebenblattränder; Spreite am Grund [base], an der Spitze [apex]."
        fields = [
            concatenate(obj.edge, EDGE_CHOICES),
            concatenate(obj.surface, SURFACE_CHOICES, "e"),
            concatenate(obj.stipule_edge, STIPULE_EDGE_CHOICES, "e"),
            concatenate(obj.base, BASE_CHOICES),
            concatenate(obj.apex, APEX_CHOICES),
        ]
        fields[0] = f"Blattränder {fields[0]}" if fields[0] else ""
        fields[1] = f"{fields[1]} Blattoberfläche" if fields[1] else ""
        fields[2] = f"{fields[2]} Nebenblattränder" if fields[2] else ""
        fields[3] = f"am Grund {fields[3]}" if fields[3] else ""
        fields[4] = f"an der Spitze {fields[4]}" if fields[4] else ""

        text = [
            "; ".join(filter(None, fields[:3])),
            ", ".join(filter(None, fields[3:])),
        ]
        text[1] = f"Spreite {text[1]}" if text[1] else ""
        text = "; ".join(filter(None, text))

        return format_sentence(text)

    def get_miscellaneous(self, obj):
        # Generate sentence "Sonstiges" according pattern:
        # "[special_features]; Blattscheide [sheath]."
        fields = [
            obj.special_features,
            obj.sheath,
        ]
        fields[1] = f"Blattscheide {fields[1]}" if fields[1] else ""

        text = "; ".join(filter(None, fields))

        return format_sentence(text)

    def get_seed_leaf(self, obj):
        # Generate sentence "Keimblatt" according pattern:
        # "[seed_leaf_num] Keimblatt|Keimblätter."
        fields = obj.seed_leaf_num

        text = ""
        if fields:
            text = f"{fields} {'Keimblatt' if fields == 1 else 'Keimblätter'}"

        return format_sentence(text)


class BlossomSerializer(DisplayNameModelSerializer):
    season = serializers.SerializerMethodField(label="Blütezeit")
    inflorescence = serializers.SerializerMethodField(label="Blütenstand")
    overview = serializers.SerializerMethodField(label="Überblick")
    diameter = serializers.SerializerMethodField(label="Durchmesser")
    sepal = serializers.SerializerMethodField(label="Kelchblatt")
    petal = serializers.SerializerMethodField(label="Kronblatt")
    stamen = serializers.SerializerMethodField(label="Staubblatt")
    carpel = serializers.SerializerMethodField(label="Fruchtblatt")

    class Meta:
        model = Blossom
        fields = [
            "season",
            "inflorescence",
            "overview",
            "diameter",
            "sepal",
            "petal",
            "stamen",
            "carpel",
        ]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_season(self, obj):
        # Generate sentence "Blütezeit" according pattern:
        # "([season[0]]) [season[1]] bis [season[2] ([season[3]])."
        fields = obj.season
        if fields:
            fields = [f"{SEASON_DICT.get(x, '')}" for x in fields]
            fields[0] = f"({fields[0]})" if fields[0] else ""
            fields[3] = f"({fields[3]})" if fields[3] else ""

        text = [
            " ".join(filter(None, fields[:2])),
            " ".join(filter(None, fields[2:])),
        ]
        text = " bis ".join(filter(None, text))

        return format_sentence(text)

    def get_inflorescence(self, obj):
        # Generate sentence "Blütenstand" according pattern:
        # "[inflorescence_num] [inflorescence_type] mit [blossom_num] Blüte|Blüten."
        fields = [
            obj.inflorescence_num,
            obj.inflorescence_type,
            obj.blossom_num,
        ]
        if fields[0] not in ("", "1"):
            if fields[1] in dict(INFLORESCENCE_TYPE_CHOICES_2_3).keys():
                fields[1] = concatenate(fields[1], INFLORESCENCE_TYPE_CHOICES_2_3, "n")
            elif fields[1] in dict(INFLORESCENCE_TYPE_CHOICES_3_3).keys():
                fields[1] = f"{INFLORESCENCE_TYPE_DICT_3_3_PLURAL[fields[1]]}"
            else:
                fields[1] = concatenate(fields[1], INFLORESCENCE_TYPE_CHOICES)
        else:
            fields[1] = concatenate(fields[1], INFLORESCENCE_TYPE_CHOICES)

        text = " ".join(filter(None, fields[:2]))
        text = " mit ".join(filter(None, (text, fields[2])))
        if fields[2]:
            text = f"{text} Blüte" if text[-1] == "1" else f"{text} Blüten"

        return format_sentence(text)

    def get_overview(self, obj):
        # Generate sentence "Blütenstand" according pattern:
        # "[merosity]-zählige, [symmetry]e, [perianth]|Blütenhülle; [perianth_form]e
        # Blütenform, [bract_blade]es Tragblatt."
        fields = [
            concatenate(obj.merosity, MEROSITY_CHOICES, "-zählige"),
            concatenate(obj.symmetry, SYMMETRY_CHOICES, "e"),
            concatenate(obj.perianth, PERIANTH_CHOICES),
            concatenate(obj.perianth_form, PERIANTH_FORM_CHOICES, "e"),
            concatenate(obj.bract_blade, BRACT_BLADE_CHOICES, "es"),
        ]

        text = [
            " ".join(filter(None, fields[:3])),
            f"{fields[3]} Blütenform" if fields[3] else "",
            f"{fields[4]} Tragblatt" if fields[4] else "",
        ]
        if text[0] and not fields[2]:
            text[0] = f"{text[0]} Blütenhülle"
        text[1:3] = [", ".join(filter(None, text[1:3]))]
        text = "; ".join(filter(None, text))

        return format_sentence(text)

    def get_diameter(self, obj):
        # Generate sentence "Durchmesser" according pattern:
        # "[diameter] cm."
        fields = ",".join(obj.diameter.split("."))

        text = f"{fields} cm" if fields else ""

        return format_sentence(text)

    def get_sepal(self, obj):
        # Generate sentence "Kelchblatt" according pattern:
        # "[sepal_num] [sepal_color_form] Kelchblatt|Kelchblätter, [sepal_connation_
        # type] [sepal_connation]; [epicalyx]."
        app = "Kelchblätter"
        if obj.sepal_num == "1":
            app = "Kelchblatt"

        fields = [
            obj.sepal_num,
            obj.sepal_color_form,
            obj.sepal_connation_type,
            concatenate(obj.sepal_connation, SEPAL_CONNATION_CHOICES),
            obj.epicalyx,
        ]
        fields[2] = (
            f"{fields[2][0]}{concatenate(fields[2][1:], CONNATION_TYPE_CHOICES)}"
            if fields[2][0:1].isdigit()
            else concatenate(fields[2], CONNATION_TYPE_CHOICES)
        )

        text = [
            " ".join(filter(None, fields[:2])),
            " ".join(filter(None, fields[2:4])),
        ]
        text[0] = f"{text[0]} {app}" if text[0] else ""
        text[1] = f"{app} {text[1]}" if text[1] and not text[0] else f"{text[1]}"
        text = ", ".join(filter(None, text))
        text = "; ".join(filter(None, (text, fields[4])))

        return format_sentence(text)

    def get_petal(self, obj):
        # Generate sentence "Kronblatt" according pattern:
        # "[petal_num] [petal_len] cm lange|-s, [petal_color_form] Kronblätter|-blatt,
        # [petal_connation_type] [petal_connation]; [nectary]."
        app = {1: " cm lange", 10: "Kronblätter"}
        if obj.petal_num == "1":
            app = {1: " cm langes", 10: "Kronblatt"}

        fields = [
            obj.petal_num,
            concatenate(",".join(obj.petal_len.split(".")), app=app[1]),
            obj.petal_color_form,
            obj.petal_connation_type,
            concatenate(obj.petal_connation, PETAL_CONNATION_CHOICES),
            obj.nectary,
        ]
        fields[3] = (
            f"{fields[3][0]}{concatenate(fields[3][1:], CONNATION_TYPE_CHOICES)}"
            if fields[3][0:1].isdigit()
            else concatenate(fields[3], CONNATION_TYPE_CHOICES)
        )

        text = [
            ", ".join(filter(None, fields[1:3])),
            " ".join(filter(None, fields[3:5])),
        ]
        text[0] = " ".join(filter(None, (fields[0], text[0])))
        text[0] = f"{text[0]} {app[10]}" if text[0] else ""
        text[1] = f"{app[10]} {text[1]}" if text[1] and not text[0] else f"{text[1]}"
        text = ", ".join(filter(None, text))
        text = "; ".join(filter(None, (text, fields[5])))

        return format_sentence(text)

    def get_stamen(self, obj):
        # Generate sentence "Staubblatt" according pattern:
        # "[stamen_num] [stamen_len] cm lange|-s, [stamen_color_form]
        # Staubblätter|-blatt, [stamen_connation_type] [stamen_connation]."
        app = {1: " cm lange", 10: "Staubblätter"}
        if obj.stamen_num == "1":
            app = {1: " cm langes", 10: "Staubblatt"}

        fields = [
            obj.stamen_num,
            concatenate(",".join(obj.stamen_len.split(".")), app=app[1]),
            obj.stamen_color_form,
            concatenate(obj.stamen_connation_type, STAMEN_CONNATION_TYPE_CHOICES),
            obj.stamen_connation_type_add,
        ]

        text = [
            ", ".join(filter(None, fields[1:3])),
            " ".join(filter(None, fields[3:5])),
        ]
        text[0] = " ".join(filter(None, (fields[0], text[0])))
        text[0] = f"{text[0]} {app[10]}" if text[0] else ""
        text[1] = f"{app[10]} {text[1]}" if text[1] and not text[0] else f"{text[1]}"
        text = ", ".join(filter(None, text))

        return format_sentence(text)

    def get_carpel(self, obj):
        # Generate sentence "Fruchtblatt" according pattern:
        # "[carpel_num] [carpel_connation_type] verwachsene|-s Fruchtblätter|-blatt,
        # [ovary_pos]er Fruchtkonten, [pistil_pos]er Griffel mit [stigma_num] Narbe|-n;
        # [stylopodium]."

        app = {10: "verwachsene Fruchtblätter", 11: "Narben"}
        if obj.carpel_num == "1":
            app[10] = "verwachsenes Fruchtblatt"
        if obj.stigma_num == "1":
            app[11] = "Narbe"

        fields = [
            obj.carpel_num,
            concatenate(obj.carpel_connation_type, CARPEL_CONNATION_TYPE_CHOICES),
            concatenate(obj.ovary_pos, OVARY_POS_CHOICES, "er"),
            concatenate(obj.pistil_pos, PISTIL_POS_CHOICES, "er"),
            obj.stigma_num,
            obj.stylopodium,
        ]

        text = [
            " ".join(filter(None, fields[:2])),
            f"{fields[2]} Fruchtknoten" if fields[2] else "",
            f"{fields[3]} Griffel" if fields[3] else "",
            f"{fields[4]} {app[11]}" if fields[4] else "",
        ]
        text[0] = f"{text[0]} {app[10]}" if text[0] else ""
        text[2:4] = [" mit ".join(filter(None, text[2:4]))]
        text = ", ".join(filter(None, text))
        text = "; ".join(filter(None, (text, fields[5])))

        return format_sentence(text)


class FruitSerializer(DisplayNameModelSerializer):
    fruit = serializers.SerializerMethodField(label="Frucht")
    ovule = serializers.SerializerMethodField(label="Samenanlage")
    seed = serializers.SerializerMethodField(label="Samen")

    class Meta:
        model = Fruit
        fields = ["fruit", "ovule", "seed"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_fruit(self, obj):
        # Generate sentence "Frucht" according pattern:
        # "[fruit_form] [fruit_type]."
        fields = [
            obj.fruit_form,
            concatenate(obj.fruit_type, FRUIT_TYPE_CHOICES),
        ]

        text = " ".join(filter(None, fields))

        return format_sentence(text)

    def get_ovule(self, obj):
        # Generate sentence "Samenanlage" according pattern:
        # "Samenanlage in [ovule_pos]."
        fields = concatenate(obj.ovule_pos, OVULE_POS_CHOICES)

        text = f"{f'Samenanlage in {fields}' if fields else ''}"

        return format_sentence(text)

    def get_seed(self, obj):
        # Generate sentence "Samen" according pattern:
        # "[seed_num] [seed_form] Samen, [winging] [winging_feature]."
        fields = [
            obj.seed_num,
            obj.seed_form,
            obj.winging,
            obj.winging_feature,
        ]

        text = [
            " ".join(filter(None, fields[:2])),
            " ".join(filter(None, fields[2:])),
        ]
        text[0] = f"{f'{text[0]} Samen' if text[0] else ''}"
        text = ", ".join(filter(None, text))

        return format_sentence(text)


class StemRootSerializer(DisplayNameModelSerializer):
    stem_morphology = serializers.SerializerMethodField(label="Sprossmorphologie")
    outgrowths = serializers.SerializerMethodField(label="Auswüchse")
    bracts = serializers.SerializerMethodField(label="Beblätterung")
    milky_sap = serializers.SerializerMethodField(label="Milchsaft")
    root_morphology = serializers.SerializerMethodField(label="Wurzelmorphologie")

    class Meta:
        model = StemRoot
        fields = [
            "stem_morphology",
            "outgrowths",
            "bracts",
            "milky_sap",
            "root_morphology",
        ]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_stem_morphology(self, obj):
        # Generate sentence "Sprossmorphologie" according pattern:
        # "[orientation]er [appearance]er, [succulence]er Spross; [cross_section]er
        # Querschnitt mit [surface]er Oberfläche."
        app = "er"
        if not obj.cross_section:
            app = "e"
        fields = [
            concatenate(obj.orientation, ORIENTATION_CHOICES, "er"),
            concatenate(obj.appearance, APPEARANCE_CHOICES, "er"),
            concatenate(obj.succulence, SUCCULENCE_CHOICES, "er"),
            concatenate(obj.cross_section, SR_CROSS_SECTION_CHOICES, "er"),
            concatenate(obj.surface, SURFACE_CHOICES, app),
        ]
        fields[3] = f"{f'{fields[3]} Querschnitt' if fields[3] else ''}"
        fields[4] = f"{f'{fields[4]} Oberfläche' if fields[4] else ''}"

        text = [
            ", ".join(filter(None, fields[:3])),
            " mit ".join(filter(None, fields[3:])),
        ]
        text[0] = f"{f'{text[0]} Spross' if text[0] else ''}"
        text = "; ".join(filter(None, text))

        return format_sentence(text)

    def get_outgrowths(self, obj):
        # Generate sentence "Auswüchse" according pattern:
        # "[creep_lay_shoots]; [runners]."
        fields = [
            concatenate(obj.creep_lay_shoots, CREEP_LAY_SHOOTS_CHOICES),
            concatenate(obj.runners, RUNNERS_CHOICES),
        ]

        text = "; ".join(filter(None, fields))

        return format_sentence(text)

    def get_bracts(self, obj):
        # Generate sentence "Beblätterung" according pattern:
        # "[bracts] beblättert."
        fields = concatenate(obj.bracts, BRACTS_CHOICES)

        text = f"{f'{fields} beblättert' if fields else ''}"

        return format_sentence(text)

    def get_milky_sap(self, obj):
        # Generate sentence "Milchsaft" according pattern:
        # "[milky_sap].."
        fields = obj.milky_sap

        text = f"{f'{fields}' if fields else ''}"

        return format_sentence(text)

    def get_root_morphology(self, obj):
        # Generate sentence "Wurzelmorphologie" according pattern:
        # "[organ_features] [organs]; Primärwurzel [primary_root]."
        fields = [
            obj.organ_features,
            concatenate(obj.organs, ORGANS_CHOICES),
            concatenate(obj.primary_root, PRIMARY_ROOT_CHOICES),
        ]
        fields[2] = f"{f'Primärwurzel {fields[2]}' if fields[2] else ''}"

        text = " ".join(filter(None, fields[:2]))
        text = "; ".join(filter(None, (text, fields[2])))

        return format_sentence(text)


class IndicatorsSerializer(serializers.ModelSerializer):
    not_specified = serializers.CharField(label="", read_only=True)
    key = serializers.CharField(source="get_key", label="", read_only=True)

    class Meta:
        model = Indicators
        fields = ["not_specified", *INDICATORS, "key"]
        extra_kwargs = dict.fromkeys(INDICATORS, {"max_length": 100})
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        if ret.get("not_specified") == "True":
            ret.clear()
            ret["not_specified"] = "Keine Angabe"
        else:
            ret.pop("not_specified")
            for key in INDICATORS_DICT:
                value = ret[key]
                # Remove items with empty values.
                if not value:
                    ret.pop(key)
                # Add verbose descriptions to indicator values.
                else:
                    value_key = value[:2]
                    if value[2:3].isdigit():
                        value_key = value[:3]
                    ret[key] = f"{value} – {INDICATORS_DICT[key][value_key]}"
            # Set light value digit in parentheses.
            value = ret.get("light", "")
            if "()" in value:
                ret["light"] = f"{value[0]}({value[1]}){value[4:]}"
            # Remove empty key.
            if not ret.get("key"):
                ret.pop("key")

        return ret


# -------------------------------------- LEGACY -------------------------------------- #
class ZeigerNumberSerializer(DisplayNameModelSerializer):

    serializer_choice_field = ZeigerNumberField


"""
    class Meta:
        model = ZeigerNumber
        exclude = [
            "plant",
            "light_extra",
            "temp_extra",
            "humid_extra",
            "react_extra",
            "nutri_extra",
        ]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}
"""
# ------------------------------------------------------------------------------------ #


class PlantSerializer(DisplayNameModelSerializer):
    leaf = LeafSerializer(required=False)
    blossom = BlossomSerializer(required=False)
    fruit = FruitSerializer(required=False)
    stemroot = StemRootSerializer(required=False)
    indicators = IndicatorsSerializer(required=False)
    photographs = PhotographSerializer(many=True, required=False)

    taxonomy = serializers.CharField(
        label=Plant.taxonomy.short_description, read_only=True
    )
    ground = serializers.CharField(
        source="get_ground_output",
        label=Plant._meta.get_field("ground").base_field.verbose_name,
        read_only=True,
    )

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}
