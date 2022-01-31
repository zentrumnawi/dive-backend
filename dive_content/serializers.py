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


class LeafSerializer(ExcludeEmptyFieldsModelSerializer):
    general = serializers.SerializerMethodField(label="Allgemeines")
    attachment = serializers.SerializerMethodField(label="Anheftung")
    lamina_compound_leaf = serializers.SerializerMethodField(
        label="Blattfläche (zusammengesetztes Blatt)"
    )
    lamina_simple_leaf = serializers.SerializerMethodField(
        label="Blattfläche (einfaches Blatt)"
    )
    lamina_general = serializers.SerializerMethodField(label="Blattfläche (allgemein)")
    miscellaneous = serializers.SerializerMethodField(label="Sonstiges")

    class Meta:
        model = Leaf
        fields = [
            "general",
            "attachment",
            "lamina_compound_leaf",
            "lamina_simple_leaf",
            "lamina_general",
            "stipule",
            "miscellaneous",
        ]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_general(self, obj):
        return LeafOutput.generate_general(obj)

    def get_attachment(self, obj):
        return LeafOutput.generate_attachment(obj)

    def get_lamina_compound_leaf(self, obj):
        return LeafOutput.generate_lamina_compound_leaf(obj)

    def get_lamina_simple_leaf(self, obj):
        return LeafOutput.generate_lamina_simple_leaf(obj)

    def get_lamina_general(self, obj):
        return LeafOutput.generate_lamina_general(obj)

    def get_miscellaneous(self, obj):
        return LeafOutput.generate_miscellaneous(obj)


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


class StemRootSerializer(ExcludeEmptyFieldsModelSerializer):
    stem_morphology = serializers.SerializerMethodField(label="Sprossmorphologie")
    outgrowths = serializers.SerializerMethodField(label="Auswüchse")
    root_morphology = serializers.SerializerMethodField(label="Wurzelmorphologie")

    class Meta:
        model = StemRoot
        fields = [
            "trunk_features",
            "stem_morphology",
            "outgrowths",
            "milky_sap",
            "root_morphology",
        ]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}

    def get_stem_morphology(self, obj):
        return StemRootOutput.generate_stem_morphology(obj)

    def get_outgrowths(self, obj):
        return StemRootOutput.generate_outgrowths(obj)

    def get_root_morphology(self, obj):
        return StemRootOutput.generate_root_morphology(obj)


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
