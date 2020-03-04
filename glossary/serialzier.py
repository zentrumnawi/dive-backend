from .models import GlossaryEntry
from rest_framework import serializers


class GlossaryEntrySerializer(Serializers.Modelserializer):
    class Meta:
        model = GlossaryEntry
        fields = "__all__"
