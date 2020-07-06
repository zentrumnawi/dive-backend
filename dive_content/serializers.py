from importlib import import_module

from django.conf import settings
from django.db import models
from rest_framework import serializers

from .models import TreeNode, Plant, Leaf, Sprout, Fruit, Blossom


class HumanReadableChoiceField(serializers.ChoiceField):
    def to_representation(self, value):
        if not value:
            return value
        return str(self.grouped_choices[value])


class DisplayNameModelSerializer(serializers.ModelSerializer):

    serializer_choice_field = HumanReadableChoiceField


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

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1
        swagger_schema_fields = {"title": str(model._meta.verbose_name)}


class TreeNodeSerializer(serializers.ModelSerializer):

    profiles = getattr(
        import_module(settings.PROFILES_SERIALIZER_MODULE), settings.PROFILES_SERIALIZER
    )(many=True)
    leaf_nodes = serializers.SerializerMethodField()

    class Meta:
        depth = 1
        model = TreeNode
        fields = ("node_name", "profiles", "leaf_nodes", "info_text")

    def get_leaf_nodes(self, obj):
        return TreeNodeSerializer(obj.get_children(), many=True).data
