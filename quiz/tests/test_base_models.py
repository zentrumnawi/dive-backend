import pytest
from django.db import models


class TestQuizQuestionModelExists:
    def test_model_exists(self):
        """
        This function tests whether an object QuizQuestion can be imported.
        """
        
        from quiz.models import QuizQuestion
        
    def test_model_is_django_model(self):
        """
        This function tests if the QuizQuestion object is a Django model.
        """
        
        from quiz.models import QuizQuestion
        
        assert issubclass(QuizQuestion, models.Model)
