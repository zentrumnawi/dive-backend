from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import QuizQuestion
from .serializers import QuizQuestionSerializer


class QuizQuestionEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint provides the database table of all QuizQuestions.
    """
    
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    name = "quizquestion"
