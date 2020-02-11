from django.db import models


class GlossaryEntry(models.Model):
    """Defines a model for an entry in the glossary that is displayed in the app."""

    term = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField(upload_to="glossary/images/", null=True, blank=True)
    img_alt = models.CharField(max_length=200, blank=True, default="")
    links = models.ManyToManyField("self", symmetrical=False, blank=True)
