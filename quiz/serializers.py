from rest_framework import serializers
from .models import QuizQuestion


class QuizQuestionSerializer(serializers.Modelserializer):
    qtype = serializers.SerializerMethod()
    
    class Meta:
        model = QuizQuestion
        fields = "__all__"
        ordering = ("pk",)
        
    def get_qtype(self, obj):
        choice_dict = dict(obj.QTYPE_CHOICES)
        return choice_dict.get(obj.qtype)
