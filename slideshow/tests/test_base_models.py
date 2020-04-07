import pytest
from django.db import models


class TestSlideshowModelExists:
    """
    Test whether an object Slideshow can be imported and is a Django model.
    """
    
    def test_model_exists(self):
        from slideshow.models import Slideshow
        
    def test_model_is_django_model(self):
        from slideshow.models import Slideshow
        
        assert issubclass(Slideshow, models.Model)
