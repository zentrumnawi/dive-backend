from rest_framework import serializers
from .models import Slideshow, SlideshowPage, SlideshowImage


class SlideshowImageLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideshowImage
        fields = ["id", "position", "title", "img", "img_alt", "caption"]


class SlideshowPageLessSerializer(serializers.ModelSerializer):
    images = SlideshowImageLessSerializer(many=True)
    
    class Meta:
        model = SlideshowPage
        fields = ["id", "position", "title", "text", "images"]


class SlideshowSerializer(serializers.ModelSerializer):
    pages = SlideshowPageLessSerializer(many=True)

    class Meta:
        model = Slideshow
        fields = "__all__"


class SlideshowPageSerializer(serializers.ModelSerializer):
    images = SlideshowImageLessSerializer(many=True)

    class Meta:
        model = SlideshowPage
        fields = "__all__"


class SlideshowImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideshowImage
        fields = "__all__"
