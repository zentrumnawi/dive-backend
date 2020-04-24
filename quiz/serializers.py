from rest_framework import serializers
from .models import QuizQuestion, QuizAnswer


class QuizQuestionLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = "__all__"


class QuizAnswerLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = "__all__"


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerLessSerializer(many=True)

    class Meta:
        model = QuizQuestion
        fields = "__all__"


class QuizAnswerSerializer(serializers.ModelSerializer):
    question = QuizQuestionLessSerializer()

    class Meta:
        model = QuizAnswer
        fields = "__all__"
