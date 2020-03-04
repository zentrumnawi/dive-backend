from .models import GlossaryEntry
from rest_framework import serializers


class GlossaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GlossaryEntry
        fields = "__all__"
