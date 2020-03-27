from rest_framework.routers import SimpleRouter
from .views import QuizQuestionEndpoint, QuizAnswerEndpoint


app_name = "quiz"
router = SimpleRouter()
router.register(r"quizquestion", QuizQuestionEndpoint)
router.register(r"quizanswer", QuizAnswerEndpoint)
urlpatterns = []
urlpatterns += router.urls
