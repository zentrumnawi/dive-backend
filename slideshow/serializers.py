from rest_framework import serializers
from .models import Slideshow


class SlideshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slideshow
        fields = "__all__"
