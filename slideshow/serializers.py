from rest_framework import serializers
from .models import Slideshow, SlideshowPage


class SlideshowPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideshowPage
        fields = ["id", "position", "title", "text"]


class SlideshowSerializer(serializers.ModelSerializer):
    pages = SlideshowPageSerializer(many=True)

    class Meta:
        model = Slideshow
        fields = "__all__"
