from rest_framework import serializers
from operator import itemgetter
from solid_backend.photograph.serializers import PhotographSerializer

from .models import Plant, Leaf, Sprout, Fruit, Blossom


class HumanReadableChoiceField(serializers.ChoiceField):
    def to_representation(self, value):
        if not value:
            return value
        return str(self.grouped_choices[value])


class DisplayNameModelSerializer(serializers.ModelSerializer):

    serializer_choice_field = HumanReadableChoiceField

    def to_representation(self, instance):
        ret = super(DisplayNameModelSerializer, self).to_representation(instance)

        return serializers.OrderedDict(filter(lambda x: not x[1] is None, ret.items()))


class LeafSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Leaf
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class SproutSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Sprout
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class FruitSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Fruit
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class BlossomSerializer(DisplayNameModelSerializer):
    class Meta:
        model = Blossom
        exclude = ["plant"]
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class PlantSerializer(DisplayNameModelSerializer):
    leaf = LeafSerializer()
    sprout = SproutSerializer()
    fruit = FruitSerializer()
    blossom = BlossomSerializer()
    photographs = PhotographSerializer(many=True)

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}
