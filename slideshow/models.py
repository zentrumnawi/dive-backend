from django.db import models


class Slideshow(models.Model):
    """
    Model for a series of pages that can be switched back and forth.
    """
    
    title = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.title


class SlideshowPage(models.Model):
    """
    Model for a page of the Slideshow model.
    """
    
    show = models.ForeignKey(
        to=Slideshow,
        on_delete=models.PROTECT,
        related_name="pages",
        related_query_name="page",
        db_index=False
    )
    position = models.PositiveSmallIntegerField(
        default=1, #validators=[validate_position_occupied]
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return self.title
