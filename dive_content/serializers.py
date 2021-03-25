from rest_framework import serializers
from solid_backend.photograph.serializers import PhotographSerializer

from .choices import *
from .models import Blossom, Fruit, Leaf, Plant, StemRoot, ZeigerNumber


class HumanReadableChoiceField(serializers.ChoiceField):
    def to_representation(self, value):
        if not value:
            return value
        return str(self.grouped_choices[value])


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


class DisplayNameModelSerializer(serializers.ModelSerializer):

    serializer_choice_field = HumanReadableChoiceField

    def to_representation(self, instance):
        ret = super(DisplayNameModelSerializer, self).to_representation(instance)

        return serializers.OrderedDict(filter(lambda x: not x[1] is None, ret.items()))


def concatenate(field, choices, app=""):
    output = ""
    if field:
        if isinstance(field, list):
            output = " bis ".join(f"{dict(choices).get(item)}{app}" for item in field)
        else:
            output = f"{dict(choices).get(field)}{app}"

        if app and ("/" in output):
            output = output.split("/")
            for i, item in enumerate(output[:-1]):
                output[i] = f"{item}{app}"
            output = "/".join(output)

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
        # "[veins]e, [division]e, [succulence]e, [texture]e Blätter mit
        #  [cross_section]em Querschnitt."
        fields = [
            concatenate(obj.veins, VEINS_CHOICES, "e"),
            concatenate(obj.division, DIVISION_CHOICES, "e"),
            concatenate(obj.succulence, SUCCULENCE_CHOICES, "e"),
            concatenate(obj.texture, TEXTURE_CHOICES, "e"),
            concatenate(obj.cross_section, CROSS_SECTION_CHOICES, "em"),
        ]

        text = ", ".join(filter(None, fields[:4]))
        text = f"{f'{text} Blätter' if text else ''}"
        text = f"{f'{text} mit {fields[4]} Querschnitt' if fields[4] else text}"
        text = f"{f'Blätter{text}' if text[:4] == ' mit' else text}"

        return format_sentence(text)

    def get_attachment(self, obj):
        # Generate sentence "Anheftung" according pattern:
        # "Blätter sitzen [attachment], stehen [arrangement]; [rosette]."
        fields = [
            concatenate(obj.attachment, ATTACHMENT_CHOICES),
            concatenate(obj.arrangement, ARRANGMENT_CHOICES),
            concatenate(obj.rosette, ROSETTE_CHOICES),
        ]
        fields[0] = f"{f'sitzen {fields[0]}' if fields[0] else ''}"
        fields[1] = f"{f'stehen {fields[1]}' if fields[1] else ''}"

        text = ", ".join(filter(None, fields[:2]))
        text = f"{f'Blätter {text}' if text else ''}"
        text = "; ".join(filter(None, (text, fields[2])))

        return format_sentence(text)

    def get_leaf_compound(self, obj):
        # Generate sentence "Blattfläche – zusammengesetztes Blatt" according pattern:
        # "[leaf_comp_num] [blade_subdiv_shape]es|e [incision_num]-[incision_depth]es|e
        #  Blatt|Blätter mit [leaflet_incision_num]-[leaflet_incision_add]-[leaflet_
        #  incision_depth]en Blättchen."
        app = {1: "e", 3: "e", 6: "en", 10: "Blätter"}
        if obj.leaf_comp_num == "1":
            app = {1: "es", 3: "es", 6: "en", 10: "Blatt"}

        fields = [
            obj.leaf_comp_num,
            concatenate(obj.blade_subdiv_shape, BLADE_SUBDIV_SHAPE_CHOICES, app[1]),
            obj.incision_num,
            concatenate(obj.incision_depth, INCISION_DEPTH_CHOICES, app[3]),
            obj.leaflet_incision_num,
            obj.leaflet_incision_add,
            concatenate(
                obj.leaflet_incision_depth, LEAFLET_INCISION_DEPTH_CHOICES, app[6]
            ),
        ]
        for i in (2, 4, 5):
            fields[i] = f"{f'{fields[i]}-' if fields[i] else ''}"
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
        text[0] = f"{f'{text[0]} {app[10]}' if text[0] else ''}"
        text = f"{f'{text[0]} mit {text[1]} Blättchen' if text[1] else text[0]}"
        text = f"{f'Blätter{text}' if text[:4] == ' mit' else text}"

        return format_sentence(text)

    def get_leaf_simple(self, obj):
        # Generate sentence "Blattfläche – einfaches Blatt" according pattern:
        # "[leaf_simple_num] [blade_undiv_shape]es|e Blatt|Blätter."
        app = {1: "e", 10: "Blätter"}
        if obj.leaf_simple_num == "1":
            app = {1: "es", 10: "Blatt"}

        fields = [
            obj.leaf_simple_num,
            concatenate(obj.blade_undiv_shape, BLADE_UNDIV_SHAPE_CHOICES, app[1]),
        ]

        text = " ".join(filter(None, fields))
        text = f"{f'{text} {app[10]}' if text else ''}"

        return format_sentence(text)

    def get_leaf_general(self, obj):
        # Generate sentence "Blattfläche – allgemein" according pattern:
        # "Blattränder [edge]; [surface] Blattoberfläche; [stipule_edge]
        #  Nebenblattränder; Spreite am Grund [base], an der Spitze [apex]."

        fields = [
            concatenate(obj.edge, EDGE_CHOICES),
            concatenate(obj.surface, SURFACE_CHOICES, "e"),
            concatenate(obj.stipule_edge, STIPULE_EDGE_CHOICES, "e"),
            concatenate(obj.base, BASE_CHOICES),
            concatenate(obj.apex, APEX_CHOICES),
        ]
        fields[0] = f"{f'Blattränder {fields[0]}' if fields[0] else ''}"
        fields[1] = f"{f'{fields[1]} Blattoberfläche' if fields[1] else ''}"
        fields[2] = f"{f'{fields[2]} Nebenblattränder' if fields[2] else ''}"
        fields[3] = f"{f'am Grund {fields[3]}' if fields[3] else ''}"
        fields[4] = f"{f'an der Spitze {fields[4]}' if fields[4] else ''}"

        text = [
            "; ".join(filter(None, fields[:3])),
            ", ".join(filter(None, fields[3:])),
        ]
        text[1] = f"{f'Spreite {text[1]}' if text[1] else ''}"
        text = "; ".join(filter(None, text))

        return format_sentence(text)

    def get_miscellaneous(self, obj):
        # Generate sentence "Sonstiges" according pattern:
        # "[special_features]; Blattscheide [sheath]."
        fields = [
            obj.special_features,
            obj.sheath,
        ]
        fields[1] = f"{f'Blattscheide {fields[1]}' if fields[1] else ''}"

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
    class Meta:
        model = Blossom
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class FruitSerializer(DisplayNameModelSerializer):
    fruit = serializers.SerializerMethodField(label="Frucht")
    ovule = serializers.SerializerMethodField(label="Samenanlage")
    seed = serializers.SerializerMethodField(label="Samen")

    class Meta:
        model = Fruit
        fields = ["fruit", "ovule", "seed"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_fruit(self, obj):
        # Generate sentence "Fruit" according pattern:
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


class ZeigerNumberSerializer(DisplayNameModelSerializer):

    serializer_choice_field = ZeigerNumberField

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


class PlantSerializer(DisplayNameModelSerializer):
    leaf = LeafSerializer(required=False)
    blossom = BlossomSerializer(required=False)
    fruit = FruitSerializer(required=False)
    stemroot = StemRootSerializer(required=False)
    zeigernumber = ZeigerNumberSerializer(required=False)
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
