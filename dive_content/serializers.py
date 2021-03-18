from rest_framework import serializers
from solid_backend.photograph.serializers import PhotographSerializer

from .choices import *
from .models import Plant, Leaf, Sprout, Fruit, Blossom, ZeigerNumber


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
    if field and type(field) is list:
        output = " bis ".join(str(dict(choices).get(item)) + app for item in field)
    elif field:
        output = str(dict(choices).get(field)) + app
    else:
        output = ""

    if app and ("/" in output):
        output = output.split("/")
        for i, item in enumerate(output[:-1]):
            output[i] = item + app
        output = "/".join(output)

    return output


def format_sentence(line):
    if line:
        line = line.split(" ", 1)
        line[0] = line[0].capitalize()
        line = " ".join(line)
        line += "."
    return line


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
        # Generate "Überblick" line.
        fields = [
            (obj.veins, VEINS_CHOICES),
            (obj.division, DIVISION_CHOICES),
            (obj.succulence, SUCCULENCE_CHOICES),
            (obj.texture, TEXTURE_CHOICES),
            (obj.cross_section, CROSS_SECTION_CHOICES),
        ]

        app = {0: "e", 1: "e", 2: "e", 3: "e", 4: "em"}
        for i, field in enumerate(fields):
            if field[0]:
                fields[i] = concatenate(field[0], field[1], app[i])
            else:
                fields[i] = ""

        text = ", ".join(filter(None, fields[:4]))
        if text:
            text += " Blätter"
        if fields[4]:
            if not text:
                text = "Blätter"
            text += " mit {} Querschnitt".format(fields[4])

        return format_sentence(text)

    def get_attachment(self, obj):
        # Generate "Anheftung" line.
        fields = [
            (obj.attachment, ATTACHMENT_CHOICES),
            (obj.arrangement, ARRANGMENT_CHOICES),
            (obj.rosette, ROSETTE_CHOICES),
        ]

        for i, field in enumerate(fields):
            if field[0]:
                fields[i] = concatenate(field[0], field[1])
            else:
                fields[i] = ""

        text = ["sitzen", "stehen"]
        for i, field in enumerate(fields[:2]):
            if field:
                fields[i] = "{} {}".format(text[i], field)
        fields[1] = ", ".join(filter(None, fields[:2]))
        if fields[1]:
            fields[1] = "Blätter " + fields[1]
        text = "; ".join(filter(None, fields[1:]))

        return format_sentence(text)

    def get_leaf_compound(self, obj):
        # Generate "Blattfläche – zusammengesetztes Blatt" line.
        fields = [
            obj.leaf_comp_num,
            (obj.blade_subdiv_shape, BLADE_SUBDIV_SHAPE_CHOICES),
            obj.incision_num,
            (obj.incision_depth, INCISION_DEPTH_CHOICES),
            obj.leaflet_incision_num,
            obj.leaflet_incision_add,
            (obj.leaflet_incision_depth, LEAFLET_INCISION_DEPTH_CHOICES),
        ]

        app = {1: "", 3: "e", 6: "en"}
        for i, field in enumerate(fields):
            if i in (1, 3, 6):
                if field[0]:
                    fields[i] = concatenate(field[0], field[1], app=app[i])
                else:
                    fields[i] = ""

        text = ""
        if any(fields[:4]):
            text = [
                " ".join(filter(None, fields[:2])),
                "-".join(filter(None, fields[2:4])),
            ]
            text = " ".join(filter(None, text)) + " Blätter"
        if any(fields[4:]):
            if any(fields[:4]):
                text += " mit "
            else:
                text = "Blätter mit "
            text += "-".join(filter(None, fields[4:7])) + " Blättchen"

        return format_sentence(text)

    def get_leaf_simple(self, obj):
        # Generate "Blattfläche – einfaches Blatt" line.
        fields = [
            obj.leaf_simple_num,
            (obj.blade_undiv_shape, BLADE_UNDIV_SHAPE_CHOICES),
        ]

        if fields[0]:
            num = int(fields[0].split("-")[-1])
        else:
            num = 0
        app = {1: "es"}
        if fields[1][0]:
            fields[1] = concatenate(fields[1][0], fields[1][1], app.get(num, "e"))
        else:
            fields[1] = ""

        text = " ".join(filter(None, fields))
        if text:
            if num == 1:
                text += " Blatt"
            else:
                text += " Blätter"

        return format_sentence(text)

    def get_leaf_general(self, obj):
        # Generate "Blattfläche – allgemein" line.
        fields = [
            (obj.edge, EDGE_CHOICES),
            (obj.surface, SURFACE_CHOICES),
            (obj.stipule_edge, STIPULE_EDGE_CHOICES),
            (obj.base, BASE_CHOICES),
            (obj.apex, APEX_CHOICES),
        ]

        app = {0: "", 1: "e", 2: "e", 3: "", 4: ""}
        for i, field in enumerate(fields):
            if field[0]:
                fields[i] = concatenate(field[0], field[1], app[i])
            else:
                fields[i] = ""

        text = [
            "Blattränder",
            "Blattoberfläche",
            "Nebenblattränder",
            "Spreite am Grund",
            "an der Spitze",
        ]
        for i, field in enumerate(fields):
            if field:
                if i in (1, 2):
                    fields[i] = "{} {}".format(field, text[i])
                else:
                    fields[i] = "{} {}".format(text[i], field)
        fields[3] = ", ".join(filter(None, fields[3:]))
        text = "; ".join(filter(None, fields[:4]))

        return format_sentence(text)

    def get_miscellaneous(self, obj):
        # Generate "Sonstiges" line.
        fields = [
            obj.special_features,
            obj.sheath,
        ]

        if fields[1]:
            fields[1] = "Blattscheide {}".format(fields[1])
        text = "; ".join(filter(None, fields))

        return format_sentence(text)

    def get_seed_leaf(self, obj):
        # Generate "Keimblatt" line.
        num = obj.seed_leaf_num
        if not num:
            text = ""
        elif num == 1:
            text = "{} Keimblatt".format(num)
        else:
            text = "{} Keimblätter".format(num)

        return format_sentence(text)


class BlossomSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Blossom
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class FruitSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Fruit
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class SproutSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Sprout
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


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
    sprout = SproutSerializer(required=False)
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
