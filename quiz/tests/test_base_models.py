import pytest
from django.db import models
from django.contrib.postgres.fields import ArrayField


class TestQuizQuestionModelExists:
    def test_model_exists(self):
        """
        Test whether an object QuizQuestion can be imported.
        """
        
        from quiz.models import QuizQuestion
        
    def test_model_is_django_model(self):
        """
        Test if the QuizQuestion object is a Django model.
        """
        
        from quiz.models import QuizQuestion
        
        assert issubclass(QuizQuestion, models.Model)


class TestQuizQuestionModelFields:
    """
    Test suite with basic field tests wheater all fields of the QuizQuestion
    object exist and have the correct class instance.
    """
    
    def test_model_has_field_type(self, quiz_question_model_class):
        assert hasattr(quiz_question_model_class, "type")
        
    def test_model_has_field_difficulty(self, quiz_question_model_class):
        assert hasattr(quiz_question_model_class, "difficulty")
        
    def test_model_has_field_text(self, quiz_question_model_class):
        assert hasattr(quiz_question_model_class, "text")
        
    def test_model_has_field_img(self, quiz_question_model_class):
        assert hasattr(quiz_question_model_class, "img")
        
    def test_model_has_field_img_alt(self, quiz_question_model_class):
        assert hasattr(quiz_question_model_class, "img_alt")
        
    def test_model_has_field_tags(self, quiz_question_model_class):
        assert hasattr(quiz_question_model_class, "tags")
        
    def test_field_type_type(self, quiz_question_model_class):
        assert isinstance(
            quiz_question_model_class._meta.get_field("type"), models.CharField
        )
        
    def test_field_type_difficulty(self, quiz_question_model_class):
        assert isinstance(
            quiz_question_model_class._meta.get_field("difficulty"), models.PositiveSmallIntegerField
        )
        
    def test_field_type_text(self, quiz_question_model_class):
        assert isinstance(
            quiz_question_model_class._meta.get_field("text"), models.TextField
        )
        
    def test_field_type_img(self, quiz_question_model_class):
        assert isinstance(
            quiz_question_model_class._meta.get_field("img"), models.ImageField
        )
        
    def test_field_type_img_alt(self, quiz_question_model_class):
        assert isinstance(
            quiz_question_model_class._meta.get_field("img_alt"), models.CharField
        )
        
    def test_field_type_tags(self, quiz_question_model_class):
        assert isinstance(
            quiz_question_model_class._meta.get_field("tags"), ArrayField
        )
