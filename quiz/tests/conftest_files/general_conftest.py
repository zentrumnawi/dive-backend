import pytest
from quiz.models import QuizQuestion


@pytest.fixture
def quiz_question_model_class():
    return QuizQuestion


@pytest.fixture
def quizanswer_model_class():
    pass
