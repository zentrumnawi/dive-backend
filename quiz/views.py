from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import QuizQuestion, QuizAnswer
from .serializers import QuizQuestionSerializer, QuizAnswerSerializer


class QuizQuestionEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of all quiz questions including their answers.
    """

    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    name = "quizquestion"


class QuizAnswerEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of all quiz answers including their related questions.
    """

    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer
    name = "quizanswer"
