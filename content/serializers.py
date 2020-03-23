from django.apps import apps as django_apps
from rest_framework import serializers

from .models import TreeNode


class TreeNodeSerializer(serializers.ModelSerializer):

    profiles = django_apps.get_app_config("content").profiles_serializer
    leaf_nodes = serializers.SerializerMethodField()

    class Meta:
        depth = 1
        model = TreeNode
        fields = ("node_name", "profiles", "leaf_nodes", "info_text")

    def get_leaf_nodes(self, obj):
        return TreeNodeSerializer(obj.get_children(), many=True).data
