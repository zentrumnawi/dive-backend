from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Slideshow
from .serializers import SlideshowSerializer


class SlideshowEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of all Slideshows including their
    pages and images.
    """
    
    queryset = Slideshow.objects.all()
    serializer_class = SlideshowSerializer
    name = "slideshow"
