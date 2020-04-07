from django.db import models


class Slideshow(models.Model):
    """
    Model for a series of pages that can be switched back and forth.
    """
    
    title = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.title
