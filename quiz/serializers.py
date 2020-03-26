from rest_framework import serializers
from .models import QuizQuestion, QuizAnswer


class QuizQuestionSerializer(serializers.Modelserializer):
    qtype = serializers.SerializerMethod()
    answers = QuizAnswerSerializer(many=True)
    
    class Meta:
        model = QuizQuestion
        fields = "__all__"
        ordering = ("pk",)
        
    def get_qtype(self, obj):
        choice_dict = dict(obj.QTYPE_CHOICES)
        return choice_dict.get(obj.qtype)


class QuizAnswerSerializer(serializers.Modelserializer):
    question = QuizQuestionSerializer
    
    class Meta:
        model = QuizAnswer
        fields = "__all__"
