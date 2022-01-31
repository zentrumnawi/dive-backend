from rest_framework import serializers
from solid_backend.photograph.serializers import PhotographSerializer

from .models import (
    Blossom,
    BlossomPoales,
    Fruit,
    Indicators,
    InterestingFacts,
    Leaf,
    LeafPoales,
    Plant,
    StemRhizomePoales,
    StemRoot,
)
from .outputs import *


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


class ExcludeEmptyFieldsModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)

        for key in [key for key, value in ret.items() if value is (None or "")]:
            del ret[key]

        return ret


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
            add_suffix(obj.get_veins_display(), "e"),
            add_suffix(obj.get_division_display(), "e"),
            add_suffix(obj.get_succulence_display(), "e"),
            add_suffix(obj.get_texture_display(), "e", "/"),
            add_suffix(obj.get_cross_section_display(), "em", "/"),
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
            obj.attachment,
            obj.get_arrangement_display(),
            obj.get_rosette_display(),
        ]
        if fields[0]:
            fields[0] = format_ArrayField(fields[0], ATTACHMENT_CHOICES)

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
            obj.leaf_comp_blade_shape,
            obj.leaf_comp_incision_num,
            obj.leaf_comp_incision_depth,
            obj.leaflet_incision_num,
            obj.leaflet_incision_add,
            obj.leaflet_incision_depth,
        ]
        if fields[1]:
            fields[1] = format_ArrayField(
                fields[1], LEAF_COMP_BLADE_SHAPE_CHOICES, app[1]
            )
        if fields[3]:
            fields[3] = format_ArrayField(
                fields[3], LEAF_COMP_INCISION_DEPTH_CHOICES, app[3], "/"
            )
        if fields[6]:
            fields[6] = format_ArrayField(
                fields[6], LEAFLET_INCISION_DEPTH_CHOICES, app[6], "/"
            )

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
            obj.leaf_simple_blade_shape,
            obj.leaf_simple_incision_num,
            obj.leaf_simple_incision_depth,
        ]
        if fields[1]:
            fields[1] = format_ArrayField(
                fields[1], LEAF_SIMPLE_BLADE_SHAPE_CHOICES, app[1], "/"
            )
        if fields[3]:
            fields[3] = format_ArrayField(
                fields[3], LEAF_SIMPLE_INCISION_DEPTH_CHOICES, app[3], "/"
            )

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
            obj.edge,
            obj.surface,
            obj.stipule_edge,
            obj.get_base_display(),
            obj.get_apex_display(),
        ]
        if fields[0]:
            fields[0] = format_ArrayField(fields[0], EDGE_CHOICES)
        if fields[1]:
            fields[1] = format_ArrayField(fields[1], SURFACE_CHOICES, "e", "/")
        if fields[2]:
            fields[2] = format_ArrayField(fields[2], EDGE_CHOICES, "e")

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


class LeafPoalesSerializer(ExcludeEmptyFieldsModelSerializer):
    overview = serializers.SerializerMethodField(label="Überblick")
    leaf_blade = serializers.SerializerMethodField(label="Blattspreite")
    leaf_base = serializers.SerializerMethodField(label="Blattgrund")
    ligule = serializers.SerializerMethodField(label="Blatthäutchen")
    leaf_sheath = serializers.SerializerMethodField(label="Blattscheide")

    class Meta:
        model = LeafPoales
        fields = ("overview", "leaf_blade", "leaf_base", "ligule", "leaf_sheath")
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_overview(self, obj):
        return LeafPoalesOutput.generate_overview(obj)

    def get_leaf_blade(self, obj):
        return LeafPoalesOutput.generate_leaf_blade(obj)

    def get_leaf_base(self, obj):
        return LeafPoalesOutput.generate_leaf_base(obj)

    def get_ligule(self, obj):
        return LeafPoalesOutput.generate_ligule(obj)

    def get_leaf_sheath(self, obj):
        return LeafPoalesOutput.generate_leaf_sheath(obj)


class BlossomSerializer(ExcludeEmptyFieldsModelSerializer):
    season = serializers.SerializerMethodField(label="Blütezeit")
    inflorescence = serializers.SerializerMethodField(label="Blütenstand")
    general = serializers.SerializerMethodField(label="Allgemeines")
    diameter = serializers.SerializerMethodField(label="Durchmesser")
    sepal = serializers.SerializerMethodField(label="Kelchblatt")
    petal = serializers.SerializerMethodField(label="Kronblatt")
    tepal = serializers.SerializerMethodField(label="Perigonblatt")
    stamen = serializers.SerializerMethodField(label="Staubblatt")
    carpel = serializers.SerializerMethodField(label="Fruchtblatt")

    class Meta:
        model = Blossom
        fields = [
            "season",
            "inflorescence",
            "general",
            "diameter",
            "sepal",
            "petal",
            "tepal",
            "stamen",
            "carpel",
            "specifications",
        ]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_season(self, obj):
        return BlossomOutput.generate_season(obj)

    def get_inflorescence(self, obj):
        return BlossomOutput.generate_inflorescence(obj)

    def get_general(self, obj):
        return BlossomOutput.generate_general(obj)

    def get_diameter(self, obj):
        return BlossomOutput.generate_diameter(obj)

    def get_sepal(self, obj):
        return BlossomOutput.generate_sepal(obj)

    def get_petal(self, obj):
        return BlossomOutput.generate_petal(obj)

    def get_tepal(self, obj):
        return BlossomOutput.generate_tepal(obj)

    def get_stamen(self, obj):
        return BlossomOutput.generate_stamen(obj)

    def get_carpel(self, obj):
        return BlossomOutput.generate_carpel(obj)


class BlossomPoalesSerializer(ExcludeEmptyFieldsModelSerializer):
    season = serializers.SerializerMethodField(label="Blütezeit")
    inflorescence = serializers.SerializerMethodField(label="Blütenstand")
    blossom_perianth = serializers.SerializerMethodField(label="Blüte und Blütenhülle")
    spikelet = serializers.SerializerMethodField(label="Ährchen")
    husks = serializers.SerializerMethodField(label="Spelzen")

    class Meta:
        model = BlossomPoales
        fields = ("season", "inflorescence", "blossom_perianth", "spikelet", "husks")
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_season(self, obj):
        return BlossomPoalesOutput.generate_season(obj)

    def get_inflorescence(self, obj):
        return BlossomPoalesOutput.generate_inflorescence(obj)

    def get_blossom_perianth(self, obj):
        return BlossomPoalesOutput.generate_blossom_perianth(obj)

    def get_spikelet(self, obj):
        return BlossomPoalesOutput.generate_spikelet(obj)

    def get_husks(self, obj):
        return BlossomPoalesOutput.generate_husks(obj)


class FruitSerializer(ExcludeEmptyFieldsModelSerializer):
    fruit = serializers.SerializerMethodField(label="Frucht")
    ovule = serializers.SerializerMethodField(label="Samenanlage")
    seed = serializers.SerializerMethodField(label="Samen")

    class Meta:
        model = Fruit
        fields = ["fruit", "ovule", "seed"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_fruit(self, obj):
        return FruitOutput.generate_fruit(obj)

    def get_ovule(self, obj):
        return FruitOutput.generate_ovule(obj)

    def get_seed(self, obj):
        return FruitOutput.generate_seed(obj)


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
        # "[orientation]er, [appearance]er, [succulence]er, [pith]er Spross; [cross_
        # section]er Querschnitt mit [surface]er Oberfläche."
        app = "er"
        if not obj.cross_section:
            app = "e"
        fields = [
            obj.orientation,
            obj.appearance,
            add_suffix(obj.get_succulence_display(), "er"),
            add_suffix(obj.get_pith_display(), "er"),
            obj.cross_section,
            obj.surface,
        ]
        if fields[0]:
            fields[0] = format_ArrayField(fields[0], ORIENTATION_CHOICES, "er", "/")
        if fields[1]:
            fields[1] = format_ArrayField(fields[1], APPEARANCE_CHOICES, "er")
        if fields[4]:
            fields[4] = format_ArrayField(
                fields[4], SR_CROSS_SECTION_CHOICES, "er", "/"
            )
        if fields[5]:
            fields[5] = format_ArrayField(fields[5], SURFACE_CHOICES, app, "/")

        fields[4] = f"{fields[4]} Querschnitt" if fields[4] else ""
        fields[5] = f"{fields[5]} Oberfläche" if fields[5] else ""

        text = [
            ", ".join(filter(None, fields[:4])),
            " mit ".join(filter(None, fields[4:])),
        ]
        text[0] = f"{text[0]} Spross" if text[0] else ""
        text = "; ".join(filter(None, text))

        return format_sentence(text)

    def get_outgrowths(self, obj):
        # Generate sentence "Auswüchse" according pattern:
        # "[creep_lay_shoots]; [runners]."
        fields = [
            obj.get_creep_lay_shoots_display(),
            obj.get_runners_display(),
        ]

        text = "; ".join(filter(None, fields))

        return format_sentence(text)

    def get_bracts(self, obj):
        # Generate sentence "Beblätterung" according pattern:
        # "[bracts] beblättert."
        fields = obj.get_bracts_display()

        text = f"{fields} beblättert" if fields else ""

        return format_sentence(text)

    def get_milky_sap(self, obj):
        # Generate sentence "Milchsaft" according pattern:
        # "[milky_sap]."
        fields = obj.milky_sap

        text = f"{fields}" if fields else ""

        return format_sentence(text)

    def get_root_morphology(self, obj):
        # Generate sentence "Wurzelmorphologie" according pattern:
        # "[organ_features] [organs]; Primärwurzel [primary_root]."
        fields = [
            obj.organ_features,
            obj.get_organs_display(),
            obj.get_primary_root_display(),
        ]
        fields[2] = f"Primärwurzel {fields[2]}" if fields[2] else ""

        text = " ".join(filter(None, fields[:2]))
        text = "; ".join(filter(None, (text, fields[2])))

        return format_sentence(text)


class StemRhizomePoalesSerializer(ExcludeEmptyFieldsModelSerializer):
    growth_form = serializers.SerializerMethodField(label="Wuchsform")
    stem = serializers.SerializerMethodField(label="Stängel")
    rhizome = serializers.SerializerMethodField(label="Rhizome")

    class Meta:
        model = StemRhizomePoales
        fields = ("growth_form", "stem", "rhizome")
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_growth_form(self, obj):
        return StemRhizomePoalesOutput.generate_growth_form(obj)

    def get_stem(self, obj):
        return StemRhizomePoalesOutput.generate_stem(obj)

    def get_rhizome(self, obj):
        return StemRhizomePoalesOutput.generate_rhizome(obj)


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


class InterestingFactsSerializer(ExcludeEmptyFieldsModelSerializer):
    pollination = serializers.SerializerMethodField(label="Bestäubung")
    dispersal = serializers.SerializerMethodField(label="Ausbreitung")

    class Meta:
        model = InterestingFacts
        fields = ("pollination", "dispersal", "detail_features", "usage", "trivia")
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_pollination(self, obj):
        return InterestingFactsOutput.generate_pollination(obj)

    def get_dispersal(self, obj):
        return InterestingFactsOutput.generate_dispersal(obj)


class PlantSerializer(DisplayNameModelSerializer):
    taxonomy = serializers.CharField(
        label=Plant.taxonomy.short_description, read_only=True
    )
    general = serializers.SerializerMethodField(label="Allgemeines")

    leaf = LeafSerializer(required=False)
    leafpoales = LeafPoalesSerializer(required=False)
    blossom = BlossomSerializer(required=False)
    blossompoales = BlossomPoalesSerializer(required=False)
    fruit = FruitSerializer(required=False)
    stemroot = StemRootSerializer(required=False)
    stemrhizomepoales = StemRhizomePoalesSerializer(required=False)
    indicators = IndicatorsSerializer(required=False)
    interestingfacts = InterestingFactsSerializer(required=False)
    photographs = PhotographSerializer(many=True, required=False)

    class Meta:
        model = Plant
        fields = (
            "id",
            "tree_node",
            "taxonomy",
            "short_description",
            "name",
            "trivial_name",
            "general",
            "leaf",
            "leafpoales",
            "blossom",
            "blossompoales",
            "fruit",
            "stemroot",
            "stemrhizomepoales",
            "indicators",
            "interestingfacts",
            "photographs",
        )
        depth = 1
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_general(self, obj):
        return PlantOutput.generate_general(obj)
