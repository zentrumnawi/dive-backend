from rest_framework import serializers
from .models import QuizQuestion, QuizAnswer


class QuizQuestionSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    
    class Meta:
        model = QuizQuestion
        fields = "__all__"
        ordering = ("pk")
        
    def get_type(self, obj):
        choice_dict = dict(obj.QTYPE_CHOICES)
        return choice_dict.get(obj.type)


class QuizAnswerSerializer(serializers.ModelSerializer):
    question = QuizQuestionSerializer()
    
    class Meta:
        model = QuizAnswer
        fields = "__all__"
