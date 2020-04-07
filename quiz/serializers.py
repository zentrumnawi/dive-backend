from rest_framework import serializers
from .models import QuizQuestion, QuizAnswer


class QuizQuestionLessSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    
    class Meta:
        model = QuizQuestion
        fields = "__all__"
        
    def get_type(self, obj):
        choice_dict = dict(obj.QTYPE_CHOICES)
        return choice_dict.get(obj.type)


class QuizAnswerLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = "__all__"


class QuizQuestionSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    answers = QuizAnswerLessSerializer(many=True)
    
    class Meta:
        model = QuizQuestion
        fields = "__all__"
        
    def get_type(self, obj):
        choice_dict = dict(obj.QTYPE_CHOICES)
        return choice_dict.get(obj.type)


class QuizAnswerSerializer(serializers.ModelSerializer):
    question = QuizQuestionLessSerializer()
    
    class Meta:
        model = QuizAnswer
        fields = "__all__"
