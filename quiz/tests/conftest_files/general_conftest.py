import pytest
from quiz.models import QuizQuestion, QuizAnswer


@pytest.fixture
def quiz_question_model_class():
    return QuizQuestion


@pytest.fixture
def quiz_answer_model_class():
    return QuizAnswer
