from importlib import import_module

from django.conf import settings
from rest_framework import serializers

from .models import TreeNode, Plant, Leaf, Sprout, Fruit, Blossom


class LeafSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leaf
        exclude = ["plant"]


class SproutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprout
        exclude = ["plant"]


class FruitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fruit
        exclude = ["plant"]


class BlossomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blossom
        exclude = ["plant"]


class PlantSerializer(serializers.ModelSerializer):

    leaf = LeafSerializer()
    sprout = SproutSerializer()
    fruit = FruitSerializer()
    blossom = BlossomSerializer()

    class Meta:
        model = Plant
        fields = "__all__"
        depth = 1


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
