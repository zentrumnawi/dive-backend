from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    
    class Meta:
        model = Message
        fields = "__all__"
        
    def get_type(self, obj):
        choice_dict = dict(obj.MTYPE_CHOICES)
        return choice_dict.get(obj.type)
