from django.db import models
from datetime import date


class Message(models.Model):
    """
    Model for a message that is displayed to the users when the app starts.
    """
    
    MTYPE_CHOICES = [
         ("CL", "Changlog"),
         ("SE", "Series"),
         ("NO", "Notice")
    ]
    
    type = models.CharField(max_length=2, choices=MTYPE_CHOICES)
    title = models.CharField(max_length=100)
    text = models.TextField(default="", blank=True, verbose_name="text (Markdown)")
    img = models.ImageField(upload_to="message/", null=True, blank=True)
    img_alt = models.CharField(max_length=200, default="", blank=True)
    valid_from = models.DateField(default=date.today)
    valid_to = models.DateField(default=date.today)
    
    def __str__(self):
        return self.title
