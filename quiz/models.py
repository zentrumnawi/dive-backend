from django.db import models
from django.contrib.postgres.fields import ArrayField


class QuizQuestion(models.Model):
    """
    Model for a quesiton in the quiz of the app.
    """
    
    QTYPE_CHOICES = [
         ("SC", "Single Choice"),
         ("MC", "Multiple Choice"),
         ("DD", "Drag and Drop"),
         ("RG", "Ranking"),
         ("HS", "Hotspot")
    ]
    QDIFFICULTY_CHOICES = [
        (1, "Neuling"),
        (2, "Einsteiger"),
        (3, "Fortgeschrittener"),
        (4, "Erfahrener"),
        (5, "Experte")
    ]
    
    type = models.CharField(max_length=2, choices=QTYPE_CHOICES)
    difficulty = models.PositiveSmallIntegerField(choices=QDIFFICULTY_CHOICES)
    text = models.TextField()
    img = models.ImageField(upload_to="quiz/", null=True, blank=True)
    img_alt = models.CharField(max_length=200, default="", blank=True)
    tags = ArrayField(
        base_field=models.CharField(max_length=100),
        default=list,
        blank=True,
        help_text="If you want to add more than one tag, seperate them with commas."
    )
        
    def __str__(self):
        return self.text
