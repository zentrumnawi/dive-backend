import pytest
from django.db import models


class TestMessageModelExists:
    """
    Test whether an object Message can be imported and is a Django model.
    """
    
    def test_model_exists(self):
        from message.models import Message
        
    def test_model_is_django_model(self):
        from message.models import Message
        
        assert issubclass(Message, models.Model)
