from rest_framework import serializers
from solid_backend.photograph.serializers import PhotographSerializer

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


class LeafSerializer(DisplayNameModelSerializer):
    att_axis = serializers.CharField(
        source="get_att_axis_output",
        label=Leaf._meta.get_field("att_axis").base_field.verbose_name,
        read_only=True,
    )
    dep_cuts = serializers.CharField(
        source="get_dep_cuts_output",
        label=Leaf._meta.get_field("dep_cuts").base_field.verbose_name,
        read_only=True,
    )
    blade_div = serializers.CharField(
        source="get_blade_div_output",
        label=Leaf._meta.get_field("blade_div").base_field.verbose_name,
        read_only=True,
    )
    blade_undiv = serializers.CharField(
        source="get_blade_undiv_output",
        label=Leaf._meta.get_field("blade_undiv").base_field.verbose_name,
        read_only=True,
    )

    class Meta:
        model = Leaf
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


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
