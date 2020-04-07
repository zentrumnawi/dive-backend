from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Slideshow
from .serializers import SlideshowSerializer


class SlideshowEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of all Slideshows.
    """
    
    queryset = Slideshow.objects.all()
    serializer_class = SlideshowSerializer
    name = "slideshow"
